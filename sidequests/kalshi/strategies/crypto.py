"""
Crypto strategy — spot price vs Kalshi price-threshold contracts.

Edge source: Kalshi "Will BTC/ETH close above $X?" markets often lag spot by
minutes. Real-time Kraken + Coinbase prices give a tight probability estimate
using historical intraday volatility.

Data sources (all free, no key):
  - Kraken public ticker: https://api.kraken.com/0/public/Ticker
  - Coinbase public ticker: https://api.coinbase.com/v2/exchange-rates
  - CoinGecko fallback: https://api.coingecko.com/api/v3/simple/price

Model: Black-Scholes style log-normal distribution. Given current spot S,
target threshold K, time to market close T (hours), and historical vol σ,
compute P(S_T > K).

Historical daily vol (annualized):
  BTC: ~60%  ETH: ~75%  SOL: ~90%
These are conservative estimates; use as baseline.
"""

import os
import re
import math
import logging
import datetime
import requests
from typing import Optional
from statistics import NormalDist
from zoneinfo import ZoneInfo

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.crypto")

ET = ZoneInfo("America/New_York")

EDGE_THRESHOLD  = float(os.getenv("CRYPTO_EDGE_THRESHOLD", "0.07"))
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "1"))
KALSHI_FEE      = 0.01

CRYPTO_SERIES_PREFIXES = ["KXBTC", "KXETH", "KXSOL", "BTC-", "ETH-", "CRYPTO-"]

# Historical annualized vol by asset (conservative)
ANNUAL_VOL = {"BTC": 0.60, "ETH": 0.75, "SOL": 0.90, "DEFAULT": 0.70}


# ── spot price fetching ────────────────────────────────────────────────────────

def fetch_kraken(symbol: str) -> Optional[float]:
    """Fetch spot price from Kraken. symbol: 'XBTUSD', 'ETHUSD', 'SOLUSD'."""
    try:
        r = requests.get(
            "https://api.kraken.com/0/public/Ticker",
            params={"pair": symbol},
            timeout=5,
        )
        r.raise_for_status()
        data = r.json()
        result = data.get("result", {})
        for k, v in result.items():
            return float(v["c"][0])   # last trade price
    except Exception as e:
        log.debug("Kraken %s fetch failed: %s", symbol, e)
    return None


def fetch_coingecko(coin_id: str) -> Optional[float]:
    """Fallback: CoinGecko simple price."""
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin_id, "vs_currencies": "usd"},
            timeout=5,
        )
        r.raise_for_status()
        data = r.json()
        return float(data.get(coin_id, {}).get("usd", 0) or 0) or None
    except Exception as e:
        log.debug("CoinGecko %s fetch failed: %s", coin_id, e)
    return None


KRAKEN_SYMBOLS = {"BTC": "XBTUSD", "ETH": "ETHUSD", "SOL": "SOLUSD"}
COINGECKO_IDS  = {"BTC": "bitcoin",  "ETH": "ethereum", "SOL": "solana"}


def get_spot_price(asset: str) -> Optional[float]:
    """Get spot price for asset (BTC/ETH/SOL). Tries Kraken, falls back to CoinGecko."""
    kraken_sym = KRAKEN_SYMBOLS.get(asset)
    if kraken_sym:
        price = fetch_kraken(kraken_sym)
        if price:
            return price
    cg_id = COINGECKO_IDS.get(asset)
    if cg_id:
        return fetch_coingecko(cg_id)
    return None


# ── probability model ──────────────────────────────────────────────────────────

def prob_above_threshold(spot: float, threshold: float, hours_to_close: float, annual_vol: float) -> float:
    """
    P(S_T > threshold) under log-normal model.
    spot: current price
    threshold: contract strike
    hours_to_close: time remaining until market close
    annual_vol: annualized volatility (e.g. 0.60 for 60%)
    """
    if hours_to_close <= 0:
        return 1.0 if spot > threshold else 0.0

    T = hours_to_close / 8760   # convert hours to years
    sigma = annual_vol
    mu    = 0   # risk-neutral drift (zero for prediction market, not option pricing)

    log_ratio = math.log(spot / threshold)
    d = (log_ratio + mu * T) / (sigma * math.sqrt(T))
    return NormalDist().cdf(d)


def hours_until_close(market: dict) -> float:
    """Estimate hours until market closes from market data."""
    close_time = market.get("close_time") or market.get("expiration_time")
    if not close_time:
        return 12   # default assumption

    try:
        if isinstance(close_time, str):
            # ISO format
            if close_time.endswith("Z"):
                close_time = close_time.replace("Z", "+00:00")
            close_dt = datetime.datetime.fromisoformat(close_time)
        else:
            return 12
        now = datetime.datetime.now(datetime.timezone.utc)
        delta = (close_dt - now).total_seconds() / 3600
        return max(0.0, delta)
    except Exception:
        return 12


# ── market matching ────────────────────────────────────────────────────────────

def find_crypto_markets(client: KalshiClient) -> list:
    markets = client.get_markets(limit=500)
    return [
        m for m in markets
        if any(m.get("ticker", "").startswith(p) for p in CRYPTO_SERIES_PREFIXES)
        and m.get("status") == "open"
    ]


def parse_crypto_market(ticker: str) -> tuple:
    """
    Returns (asset, threshold).
    E.g. KXBTC-25MAR-T95000 → ('BTC', 95000)
         KXETH-25MAR-T3500  → ('ETH', 3500)
    """
    upper = ticker.upper()
    asset = "DEFAULT"
    for a in ("BTC", "ETH", "SOL"):
        if a in upper:
            asset = a
            break

    # Threshold can be T followed by digits, possibly with P for decimal
    m = re.search(r"T(\d+)P(\d+)", upper)
    if m:
        threshold = float(f"{m.group(1)}.{m.group(2)}")
        return asset, threshold

    m = re.search(r"T(\d+)", upper)
    if m:
        return asset, float(m.group(1))

    return asset, None


# ── main strategy entry ────────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    """Scan crypto price-threshold markets for spot vs. implied probability edges."""
    orders_placed = []

    markets = find_crypto_markets(client)
    if not markets:
        log.debug("Crypto: no Kalshi crypto markets found")
        return []

    # Cache spot prices
    spot_cache = {}

    log.info("Crypto: scanning %d market(s)", len(markets))

    for mkt in markets:
        ticker = mkt["ticker"]
        asset, threshold = parse_crypto_market(ticker)

        if threshold is None:
            continue

        if asset not in spot_cache:
            spot_cache[asset] = get_spot_price(asset)

        spot = spot_cache.get(asset)
        if spot is None:
            log.debug("Crypto: no spot price for %s", asset)
            continue

        try:
            ob = client.get_orderbook(ticker, depth=1)
            yes_bids = ob.get("orderbook", {}).get("yes", [])
            if not yes_bids:
                continue
            market_yes = yes_bids[0][0]
        except Exception as e:
            log.debug("Crypto orderbook %s: %s", ticker, e)
            continue

        hours_left  = hours_until_close(mkt)
        annual_vol  = ANNUAL_VOL.get(asset, ANNUAL_VOL["DEFAULT"])
        our_prob    = prob_above_threshold(spot, threshold, hours_left, annual_vol)
        market_prob = market_yes / 100

        edge_yes = our_prob - market_prob - KALSHI_FEE
        edge_no  = (1 - our_prob) - (1 - market_prob) - KALSHI_FEE

        if edge_yes >= edge_no and edge_yes > 0:
            side, edge, price = "yes", edge_yes, market_yes
        elif edge_no > 0:
            side, edge, price = "no", edge_no, 100 - market_yes
        else:
            side, edge, price = None, max(edge_yes, edge_no), market_yes

        log_signal(
            strategy="crypto",
            ticker=ticker,
            side=side or "none",
            edge=edge,
            data={
                "asset":       asset,
                "spot":        spot,
                "threshold":   threshold,
                "hours_left":  hours_left,
                "our_prob":    our_prob,
                "market_yes":  market_yes,
            },
        )

        if side and edge >= EDGE_THRESHOLD:
            log.info("CRYPTO EDGE: %s %s side=%s edge=%.1f%% | spot=%.0f thr=%.0f h=%.1f",
                     ticker, asset, side, edge * 100, spot, threshold, hours_left)
            if not dry_run:
                try:
                    result = client.place_order(
                        ticker=ticker, side=side, action="buy",
                        count=ORDER_CONTRACTS, price=price, order_type="limit",
                    )
                    order_id = result.get("order", {}).get("order_id", "?")
                    log_trade(
                        strategy="crypto", ticker=ticker, side=side,
                        price=price, count=ORDER_CONTRACTS,
                        order_id=order_id, status="placed", raw=result,
                    )
                    orders_placed.append(order_id)
                    log.info("Crypto order placed: %s", order_id)
                except Exception as e:
                    log.error("Crypto order failed %s: %s", ticker, e)
            else:
                tag = f"DRY:crypto:{ticker}:{side}:{price}"
                log.info("[DRY RUN] %s", tag)
                orders_placed.append(tag)

    return orders_placed
