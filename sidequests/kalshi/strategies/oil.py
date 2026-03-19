"""
Oil / Energy strategy — EIA weekly inventory report vs Kalshi energy contracts.

EIA releases weekly petroleum supply data every Wednesday at 10:30 AM ET.
Kalshi energy markets often price on stale consensus. When the inventory
draw/build exceeds consensus by enough, the market is mispriced.

Data sources (all free):
  - EIA Open Data API (no key for public series):
      https://api.eia.gov/v2/petroleum/stoc/wstk/data/
  - Bloomberg consensus (via scraping energy news headlines — low quality)
  - Brent/WTI spot price fallback via Yahoo Finance or Open-Meteo commodity feed

Market series:
  - KXOIL: WTI price threshold contracts
  - KXBRENT: Brent price threshold contracts
  - KXENERGY: general energy contracts

Edge types:
  1. Inventory surprise: actual draw > consensus → price spike → YES on higher tiers
  2. Spot-vs-threshold: same log-normal model as crypto, applied to crude futures
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

log = logging.getLogger("kalshi.oil")

ET = ZoneInfo("America/New_York")

EDGE_THRESHOLD  = float(os.getenv("OIL_EDGE_THRESHOLD", "0.07"))
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "1"))
KALSHI_FEE      = 0.01
FORCE_RUN       = os.getenv("FORCE_OIL_RUN", "0") == "1"

OIL_SERIES_PREFIXES = ["KXWTI", "KXOIL", "KXBRENT", "KXENERGY", "OIL-", "ENERGY-"]

EIA_API_BASE = "https://api.eia.gov/v2"
EIA_API_KEY  = os.getenv("EIA_API_KEY", "")   # optional — public tier works without

# Historical annual vol for WTI (crude is ~35-45% annualized)
OIL_ANNUAL_VOL = float(os.getenv("OIL_ANNUAL_VOL", "0.40"))


# ── EIA data ───────────────────────────────────────────────────────────────────

def fetch_eia_crude_stocks() -> Optional[dict]:
    """
    Fetch latest weekly crude oil stocks from EIA.
    Returns {'value': float_mbbl, 'period': 'YYYY-MM-DD'} or None.
    """
    try:
        url = f"{EIA_API_BASE}/petroleum/stoc/wstk/data/"
        params = {
            "frequency":  "weekly",
            "data[]":     "value",
            "facets[product][]": "EPC0",   # crude oil
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "length": 4,
            "offset": 0,
        }
        if EIA_API_KEY:
            params["api_key"] = EIA_API_KEY

        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        recs = data.get("response", {}).get("data", [])
        if recs:
            latest = recs[0]
            prior  = recs[1] if len(recs) > 1 else None
            change = None
            if prior:
                try:
                    change = float(latest["value"]) - float(prior["value"])
                except Exception:
                    pass
            return {
                "value":  float(latest["value"]),
                "period": latest["period"],
                "change": change,   # positive = build, negative = draw
            }
    except Exception as e:
        log.debug("EIA crude stocks fetch failed: %s", e)
    return None


def fetch_wti_spot() -> Optional[float]:
    """
    Fetch WTI spot price. Tries EIA first, falls back to Yahoo Finance.
    """
    # Try EIA WTI spot price series RWTC
    try:
        url = f"{EIA_API_BASE}/petroleum/pri/spt/data/"
        params = {
            "frequency": "daily",
            "data[]":    "value",
            "facets[product][]": "EPCWTI",
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "length": 1,
        }
        if EIA_API_KEY:
            params["api_key"] = EIA_API_KEY
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        recs = data.get("response", {}).get("data", [])
        if recs:
            return float(recs[0]["value"])
    except Exception as e:
        log.debug("EIA WTI spot failed: %s", e)

    # Fallback: Yahoo Finance CL=F (crude futures)
    try:
        r = requests.get(
            "https://query1.finance.yahoo.com/v8/finance/chart/CL=F",
            params={"interval": "1m", "range": "1d"},
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=8,
        )
        r.raise_for_status()
        meta = r.json()["chart"]["result"][0]["meta"]
        return float(meta.get("regularMarketPrice") or meta.get("previousClose"))
    except Exception as e:
        log.debug("Yahoo WTI fallback failed: %s", e)

    return None


# ── EIA release timing ─────────────────────────────────────────────────────────

def is_eia_window() -> bool:
    """True if current ET time is 10:25–11:00 AM on a Wednesday."""
    if FORCE_RUN:
        return True
    now = datetime.datetime.now(ET)
    if now.weekday() != 2:   # Wednesday
        return False
    return datetime.time(10, 25) <= now.time() <= datetime.time(11, 0)


# ── probability model ──────────────────────────────────────────────────────────

def prob_above_threshold(spot: float, threshold: float, hours_to_close: float) -> float:
    if hours_to_close <= 0:
        return 1.0 if spot > threshold else 0.0
    T = hours_to_close / 8760
    sigma = OIL_ANNUAL_VOL
    log_ratio = math.log(spot / threshold)
    d = log_ratio / (sigma * math.sqrt(T))
    return NormalDist().cdf(d)


def hours_until_close(market: dict) -> float:
    close_time = market.get("close_time") or market.get("expiration_time")
    if not close_time:
        return 24
    try:
        if isinstance(close_time, str):
            if close_time.endswith("Z"):
                close_time = close_time.replace("Z", "+00:00")
            close_dt = datetime.datetime.fromisoformat(close_time)
        else:
            return 24
        now = datetime.datetime.now(datetime.timezone.utc)
        delta = (close_dt - now).total_seconds() / 3600
        return max(0.0, delta)
    except Exception:
        return 24


# ── market parsing ─────────────────────────────────────────────────────────────

def find_oil_markets(client: KalshiClient) -> list:
    markets = client.get_markets(limit=500)
    return [
        m for m in markets
        if any(m.get("ticker", "").startswith(p) for p in OIL_SERIES_PREFIXES)
        and m.get("status") == "open"
    ]


def parse_oil_threshold(ticker: str) -> Optional[float]:
    """E.g. KXOIL-25MAR-T80 → 80.0, KXOIL-25MAR-T72P50 → 72.50"""
    m = re.search(r"T(\d+)P(\d+)", ticker.upper())
    if m:
        return float(f"{m.group(1)}.{m.group(2)}")
    m = re.search(r"T(\d+)", ticker.upper())
    if m:
        return float(m.group(1))
    return None


# ── inventory-surprise signal ──────────────────────────────────────────────────

def inventory_surprise_direction(change_mbbl: Optional[float]) -> Optional[str]:
    """
    Returns 'bullish' (draw larger than expected), 'bearish' (build), or None.
    Threshold: ±3 million barrels is historically significant.
    """
    if change_mbbl is None:
        return None
    if change_mbbl < -3.0:
        return "bullish"   # large draw → price up → favor YES on higher thresholds
    if change_mbbl > 3.0:
        return "bearish"
    return None


# ── main strategy entry ────────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    orders_placed = []

    markets = find_oil_markets(client)
    if not markets:
        log.debug("Oil: no Kalshi energy markets found")
        return []

    log.info("Oil: scanning %d energy market(s)", len(markets))

    wti_spot    = fetch_wti_spot()
    eia_stocks  = fetch_eia_crude_stocks() if is_eia_window() else None
    inv_signal  = inventory_surprise_direction(
        eia_stocks.get("change") if eia_stocks else None
    )

    if wti_spot:
        log.info("Oil: WTI spot=%.2f | EIA stocks=%s | inv_signal=%s",
                 wti_spot, eia_stocks, inv_signal)
    else:
        log.warning("Oil: no WTI spot price — will skip log-normal model")

    for mkt in markets:
        ticker    = mkt["ticker"]
        threshold = parse_oil_threshold(ticker)

        if threshold is None or wti_spot is None:
            continue

        try:
            ob = client.get_orderbook(ticker, depth=1)
            yes_bids = ob.get("orderbook", {}).get("yes", [])
            if not yes_bids:
                continue
            market_yes = yes_bids[0][0]
        except Exception as e:
            log.debug("Oil orderbook %s: %s", ticker, e)
            continue

        hours_left  = hours_until_close(mkt)
        our_prob    = prob_above_threshold(wti_spot, threshold, hours_left)

        # Adjust for inventory surprise signal
        if inv_signal == "bullish":
            our_prob = min(0.98, our_prob * 1.05)   # slight upward nudge
        elif inv_signal == "bearish":
            our_prob = max(0.02, our_prob * 0.95)

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
            strategy="oil",
            ticker=ticker,
            side=side or "none",
            edge=edge,
            data={
                "wti_spot":   wti_spot,
                "threshold":  threshold,
                "hours_left": hours_left,
                "our_prob":   our_prob,
                "market_yes": market_yes,
                "inv_signal": inv_signal,
            },
        )

        if side and edge >= EDGE_THRESHOLD:
            log.info("OIL EDGE: %s side=%s edge=%.1f%% | spot=%.2f thr=%.2f h=%.1f",
                     ticker, side, edge * 100, wti_spot, threshold, hours_left)
            if not dry_run:
                try:
                    result = client.place_order(
                        ticker=ticker, side=side, action="buy",
                        count=ORDER_CONTRACTS, price=price, order_type="limit",
                    )
                    order_id = result.get("order", {}).get("order_id", "?")
                    log_trade(
                        strategy="oil", ticker=ticker, side=side,
                        price=price, count=ORDER_CONTRACTS,
                        order_id=order_id, status="placed", raw=result,
                    )
                    orders_placed.append(order_id)
                    log.info("Oil order placed: %s", order_id)
                except Exception as e:
                    log.error("Oil order failed %s: %s", ticker, e)
            else:
                tag = f"DRY:oil:{ticker}:{side}:{price}"
                log.info("[DRY RUN] %s", tag)
                orders_placed.append(tag)

    return orders_placed
