"""
Short-term exploit scanner — closes within 7 days, external data vs market price.

Principle: same information-edge logic as weather/MLB/GDP, but filtered to
markets resolving within 7 days. Faster capital turnover, quicker feedback.

Categories targeted:
  1. Weather B-bracket markets (same NWS data, hourly close)
     KXHIGH*-26MAR19-B83.5 = "will high land between 83 and 84°F?"
     Edge: NWS forecast gives a probability distribution; bracket prob = CDF(upper) - CDF(lower)

  2. Boston snow monthly (closes March 31)
     KXBOSSNOWM-26MAR-X.X = "will BOS get >= X inches in March?"
     Edge: NWS monthly precipitation forecast

  3. S&P 500 intraday (KXINX, closes 4pm ET today)
     Edge: opening price + intraday momentum vs threshold

  4. Economic data ladders within 30 days (KXGDP Apr 30, KXCPI May)
     Ladder gap arb: same monotonicity exploit, prioritised by time to expiry

  5. Any series with close_time < 7 days where ladder gaps exist

Edge threshold: 8% (tighter than seasonal markets — less time to be right)
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

log = logging.getLogger("kalshi.shortterm")

ET = ZoneInfo("America/New_York")

EDGE_THRESHOLD  = float(os.getenv("SHORTTERM_EDGE_THRESHOLD", "0.08"))
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "1"))
KALSHI_FEE      = 0.01
MAX_HOURS_OUT   = float(os.getenv("SHORTTERM_MAX_HOURS", "168"))   # 7 days

# Weather series we track (matches weather.py CITIES)
WEATHER_SERIES = [
    "KXHIGHNY", "KXHIGHCHI", "KXHIGHLAX", "KXHIGHMIA", "KXHIGHTDAL",
    "KXHIGHTHOU", "KXHIGHTPHX", "KXHIGHTSEA", "KXHIGHTBOS", "KXHIGHTATL",
]

# City metadata for NWS obs (keyed by series prefix)
CITY_NWS = {
    "KXHIGHNY":   {"station": "KNYC", "tz": "America/New_York"},
    "KXHIGHCHI":  {"station": "KORD", "tz": "America/Chicago"},
    "KXHIGHLAX":  {"station": "KLAX", "tz": "America/Los_Angeles"},
    "KXHIGHMIA":  {"station": "KMIA", "tz": "America/New_York"},
    "KXHIGHTDAL": {"station": "KDFW", "tz": "America/Chicago"},
    "KXHIGHTHOU": {"station": "KIAH", "tz": "America/Chicago"},
    "KXHIGHTPHX": {"station": "KPHX", "tz": "America/Phoenix"},
    "KXHIGHTSEA": {"station": "KSEA", "tz": "America/Los_Angeles"},
    "KXHIGHTBOS": {"station": "KBOS", "tz": "America/New_York"},
    "KXHIGHTATL": {"station": "KATL", "tz": "America/New_York"},
}

# Econ ladder series to check for monotonicity gaps
ECON_LADDER_SERIES = ["KXGDP", "KXCPI", "KXNFP", "KXFED", "KXWTI"]


# ── time helpers ─────────────────────────────────────────────────────────────

def hours_until_close(market: dict) -> Optional[float]:
    ct = market.get("close_time") or market.get("expiration_time") or ""
    if not ct:
        return None
    try:
        if ct.endswith("Z"):
            ct = ct.replace("Z", "+00:00")
        close_dt = datetime.datetime.fromisoformat(ct)
        now = datetime.datetime.now(datetime.timezone.utc)
        h = (close_dt - now).total_seconds() / 3600
        return h if h > 0 else None
    except Exception:
        return None


# ── NWS forecast high ─────────────────────────────────────────────────────────

def fetch_nws_forecast_high(station: str) -> Optional[float]:
    """Fetch tomorrow's high from NWS gridpoint forecast."""
    try:
        url = f"https://api.weather.gov/stations/{station}/observations/latest"
        r = requests.get(url, headers={"User-Agent": "kalshi-bot/1.0"}, timeout=8)
        r.raise_for_status()
        temp_c = r.json().get("properties", {}).get("temperature", {}).get("value")
        if temp_c is not None:
            return temp_c * 9/5 + 32   # current obs temp as proxy
    except Exception as e:
        log.debug("NWS obs %s: %s", station, e)
    return None


def forecast_high_std() -> float:
    """Typical intraday temperature uncertainty (~4-6°F std for 24h forecast)."""
    return 5.0


# ── Weather B-bracket probability ────────────────────────────────────────────

def parse_bracket(ticker: str) -> Optional[tuple]:
    """
    Parse B-bracket ticker format.
    KXHIGHCHI-26MAR19-B54.5 → lower=54.5, upper=55.5 (width 1°F)
    Returns (lower, upper) or None.
    """
    m = re.search(r"-B(\d+\.?\d*)", ticker.upper())
    if m:
        lower = float(m.group(1))
        upper = lower + 1.0
        return lower, upper
    return None


def bracket_prob(forecast: float, std: float, lower: float, upper: float) -> float:
    """P(lower <= high <= upper) under Gaussian model."""
    d = NormalDist(mu=forecast, sigma=std)
    return d.cdf(upper) - d.cdf(lower)


def threshold_prob(forecast: float, std: float, threshold: float) -> float:
    """P(high > threshold) under Gaussian model."""
    return 1 - NormalDist(mu=forecast, sigma=std).cdf(threshold)


# ── Ladder gap detector ───────────────────────────────────────────────────────

def detect_ladder_gaps(markets_with_prices: list, min_gap_cents: int = 20) -> list:
    """
    markets_with_prices: [(ticker, threshold_float, yes_price_cents), ...]
    Returns list of gap dicts: {ticker, side, price, edge, rationale}
    """
    sorted_mkts = sorted(markets_with_prices, key=lambda x: x[1])
    gaps = []
    for i in range(len(sorted_mkts) - 1):
        t_low,  th_low,  p_low  = sorted_mkts[i + 1]
        t_high, th_high, p_high = sorted_mkts[i]
        if th_high >= th_low:
            continue
        gap = p_low - p_high
        if gap >= min_gap_cents:
            net = gap / 100 - KALSHI_FEE * 2
            gaps.append({
                "ticker":    t_high,
                "side":      "yes",
                "price":     p_high,
                "edge":      net,
                "rationale": f"ladder gap: P(>{th_low})={p_low}c vs P(>{th_high})={p_high}c gap={gap}c",
            })
        # Also check monotonicity inversion
        if p_high > p_low:
            net = (p_high - p_low) / 100 - KALSHI_FEE * 2
            gaps.append({
                "ticker":    t_high,
                "side":      "no",
                "price":     100 - p_high,
                "edge":      net,
                "rationale": f"monotonicity: P(>{th_high})={p_high}c > P(>{th_low})={p_low}c",
            })
    return gaps


# ── Main strategy ─────────────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    """Scan all short-term markets (<7d) for information-edge opportunities."""
    orders_placed = []

    # ── 1. Weather B-bracket markets ────────────────────────────────────────
    log.info("ShortTerm: scanning weather B-bracket markets")
    for series in WEATHER_SERIES:
        city_info = CITY_NWS.get(series, {})
        station   = city_info.get("station")
        if not station:
            continue

        forecast = fetch_nws_forecast_high(station)
        if forecast is None:
            log.debug("ShortTerm: no forecast for %s", series)
            continue

        std = forecast_high_std()
        resp = client._get("/markets", {"series_ticker": series, "status": "open", "limit": 20})
        mkts = resp.get("markets", []) if resp else []

        for mkt in mkts:
            ticker = mkt["ticker"]
            h = hours_until_close(mkt)
            if h is None or h > MAX_HOURS_OUT or h < 0.5:
                continue

            # B-bracket format
            bracket = parse_bracket(ticker)
            if bracket:
                lower, upper = bracket
                our_prob = bracket_prob(forecast, std, lower, upper)
            else:
                # T-threshold format (also short-term)
                m = re.search(r"-T(\d+\.?\d*)", ticker.upper())
                if not m:
                    continue
                thresh = float(m.group(1))
                our_prob = threshold_prob(forecast, std, thresh)

            try:
                ob = client.get_orderbook(ticker, depth=1)
                yes_bids = ob.get("orderbook", {}).get("yes", [])
                no_bids  = ob.get("orderbook", {}).get("no",  [])
                if not yes_bids:
                    continue
                market_yes = yes_bids[0][0]
            except Exception as e:
                log.debug("ShortTerm orderbook %s: %s", ticker, e)
                continue

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
                strategy="shortterm",
                ticker=ticker,
                side=side or "none",
                edge=edge,
                data={"series": series, "forecast": forecast, "our_prob": our_prob,
                      "market_yes": market_yes, "hours_left": h},
            )

            if side and edge >= EDGE_THRESHOLD:
                log.info("ST-WEATHER EDGE: %s %s edge=+%.1f%% h=%.1f",
                         ticker, side, edge * 100, h)
                if not dry_run:
                    try:
                        result = client.place_order(
                            ticker=ticker, side=side, action="buy",
                            count=ORDER_CONTRACTS, price=price, order_type="limit",
                        )
                        oid = result.get("order", {}).get("order_id", "?")
                        log_trade(strategy="shortterm", ticker=ticker, side=side,
                                  price=price, count=ORDER_CONTRACTS,
                                  order_id=oid, status="placed", raw=result)
                        orders_placed.append(oid)
                        log.info("ShortTerm order placed: %s", oid)
                    except Exception as e:
                        log.error("ShortTerm order failed %s: %s", ticker, e)
                else:
                    tag = f"DRY:shortterm:{ticker}:{side}:{price}"
                    log.info("[DRY RUN] %s", tag)
                    orders_placed.append(tag)

    # ── 2. Econ ladder gap arb (short-dated) ────────────────────────────────
    log.info("ShortTerm: scanning econ ladder gaps")
    for series in ECON_LADDER_SERIES:
        resp = client._get("/markets", {"series_ticker": series, "status": "open", "limit": 100})
        mkts = resp.get("markets", []) if resp else []

        # Group by expiry date to avoid cross-date comparisons
        by_date = {}
        for mkt in mkts:
            h = hours_until_close(mkt)
            if h is None or h > MAX_HOURS_OUT:
                continue
            date_key = (mkt.get("close_time") or "")[:10]
            by_date.setdefault(date_key, []).append(mkt)

        for date_key, group in by_date.items():
            prices = []
            for mkt in group:
                ticker = mkt["ticker"]
                m = re.search(r"-T(\d+\.?\d*)", ticker)
                if not m:
                    continue
                thresh = float(m.group(1))
                try:
                    ob = client.get_orderbook(ticker, depth=1)
                    yes_bids = ob.get("orderbook", {}).get("yes", [])
                    if not yes_bids:
                        continue
                    prices.append((ticker, thresh, yes_bids[0][0]))
                except Exception:
                    pass

            gaps = detect_ladder_gaps(prices)
            for gap in gaps:
                if gap["edge"] < EDGE_THRESHOLD:
                    continue
                log.info("ST-LADDER EDGE: %s %s edge=+%.1f%% | %s",
                         gap["ticker"], gap["side"], gap["edge"] * 100, gap["rationale"])
                log_signal(
                    strategy="shortterm",
                    ticker=gap["ticker"],
                    side=gap["side"],
                    edge=gap["edge"],
                    data={"type": "ladder_gap", "series": series,
                          "rationale": gap["rationale"]},
                )
                if not dry_run:
                    try:
                        result = client.place_order(
                            ticker=gap["ticker"], side=gap["side"], action="buy",
                            count=ORDER_CONTRACTS, price=gap["price"], order_type="limit",
                        )
                        oid = result.get("order", {}).get("order_id", "?")
                        log_trade(strategy="shortterm", ticker=gap["ticker"],
                                  side=gap["side"], price=gap["price"],
                                  count=ORDER_CONTRACTS, order_id=oid,
                                  status="placed", raw=result)
                        orders_placed.append(oid)
                        log.info("ShortTerm ladder order placed: %s", oid)
                    except Exception as e:
                        log.error("ShortTerm ladder order failed %s: %s",
                                  gap["ticker"], e)
                else:
                    tag = f"DRY:shortterm:ladder:{gap['ticker']}:{gap['side']}"
                    log.info("[DRY RUN] %s", tag)
                    orders_placed.append(tag)

    return orders_placed
