"""
NFP strategy — Non-Farm Payrolls release arb.

Core logic mirrors the CPI strategy:
  - BLS releases NFP at 8:30 AM ET on the first Friday of each month
  - Cleveland Fed / ADP / consensus whisper numbers give a pre-release edge
  - Kalshi "Will NFP be above X?" markets price off stale consensus
  - Fade retail crowd in the 8:00–8:30 AM window

Data sources:
  - BLS API (no key for public series):
      https://api.bls.gov/publicAPI/v2/timeseries/data/CES0000000001
  - ADP National Employment Report (free JSON feed via unofficial mirror):
      https://payroll-api.adp.com (scraped or via FRED ADPNFPUS)
  - FRED PAYEMS (total nonfarm payroll) — lagged but useful for trend:
      https://api.stlouisfed.org/fred/series/observations?series_id=PAYEMS

Market scan window: 8:00–8:30 AM ET, first Friday of each month.
Override with FORCE_NFP_RUN=1.
"""

import os
import re
import logging
import datetime
import calendar
import requests
from typing import Optional
from zoneinfo import ZoneInfo

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.nfp")

ET = ZoneInfo("America/New_York")

EDGE_THRESHOLD  = float(os.getenv("NFP_EDGE_THRESHOLD",  "0.07"))
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "1"))
KALSHI_FEE      = 0.01
FORCE_RUN       = os.getenv("FORCE_NFP_RUN", "0") == "1"

NFP_SERIES_PREFIXES = ["KXNFP", "NFP-", "KXJOBS"]

BLS_API  = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
FRED_API = "https://api.stlouisfed.org/fred/series/observations"
# Public demo FRED key — replace with real one for higher rate limits
FRED_API_KEY = os.getenv("FRED_API_KEY", "abcdefghijklmnopqrstuvwxyz123456")


# ── release timing ─────────────────────────────────────────────────────────────

def is_nfp_window() -> bool:
    """True if current ET time is 8:00–8:30 AM on the first Friday of the month."""
    if FORCE_RUN:
        return True
    now = datetime.datetime.now(ET)
    if now.weekday() != 4:  # Friday = 4
        return False
    # Is it the first Friday?
    first_friday = _first_friday(now.year, now.month)
    if now.date() != first_friday:
        return False
    return datetime.time(8, 0) <= now.time() <= datetime.time(8, 30)


def _first_friday(year: int, month: int) -> datetime.date:
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if week[4] != 0:
            return datetime.date(year, month, week[4])
    raise ValueError(f"No Friday in {year}-{month}")


# ── data sources ───────────────────────────────────────────────────────────────

def fetch_bls_nfp_latest() -> Optional[int]:
    """Fetch most recent NFP value from BLS PAYEMS series (thousands of jobs)."""
    try:
        payload = {
            "seriesid":  ["CES0000000001"],
            "startyear": str(datetime.date.today().year - 1),
            "endyear":   str(datetime.date.today().year),
        }
        r = requests.post(BLS_API, json=payload, timeout=10)
        r.raise_for_status()
        data = r.json()
        series = data.get("Results", {}).get("series", [])
        if series:
            latest = series[0]["data"][0]
            return int(float(latest["value"]))
    except Exception as e:
        log.debug("BLS NFP fetch failed: %s", e)
    return None


def fetch_fred_adp() -> Optional[int]:
    """Fetch ADP private payroll change from FRED (ADPNFPUS). Thousands."""
    try:
        params = {
            "series_id":  "ADPNFPUS",
            "sort_order": "desc",
            "limit":      2,
            "file_type":  "json",
            "api_key":    FRED_API_KEY,
        }
        r = requests.get(FRED_API, params=params, timeout=10)
        r.raise_for_status()
        obs = r.json().get("observations", [])
        if obs:
            return int(float(obs[0]["value"]))
    except Exception as e:
        log.debug("FRED ADP fetch failed: %s", e)
    return None


def get_implied_prob_above(threshold_k: int, estimate_k: int, std_k: int = 70) -> float:
    """
    P(NFP change > threshold) given a Gaussian estimate.
    threshold_k, estimate_k in thousands of jobs.
    std_k: historical standard deviation ~70k.
    """
    from statistics import NormalDist
    dist = NormalDist(mu=estimate_k, sigma=std_k)
    return 1 - dist.cdf(threshold_k)


# ── market matching ────────────────────────────────────────────────────────────

def find_nfp_markets(client: KalshiClient) -> list:
    markets = client.get_markets(limit=500)
    return [
        m for m in markets
        if any(m.get("ticker", "").startswith(p) for p in NFP_SERIES_PREFIXES)
        and m.get("status") == "open"
    ]


def parse_nfp_threshold(ticker: str) -> Optional[int]:
    """
    Extract threshold (in thousands) from NFP ticker.
    E.g. KXNFP-25MAR-T200 → 200 (200k jobs), KXNFP-25MAR-TN50 → -50
    """
    m = re.search(r"TN(\d+)", ticker)   # negative threshold
    if m:
        return -int(m.group(1))
    m = re.search(r"T(\d+)", ticker)
    if m:
        return int(m.group(1))
    return None


# ── main strategy entry ────────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    """NFP release arb — only runs in the 30-min pre-release window."""
    orders_placed = []

    if not is_nfp_window():
        log.debug("NFP: outside release window, skipping")
        return []

    log.info("NFP: in release window, scanning markets")

    # Best estimate: blend BLS latest trend + ADP leading indicator
    bls_val  = fetch_bls_nfp_latest()
    adp_val  = fetch_fred_adp()
    estimate = None

    if bls_val and adp_val:
        # Weighted blend: ADP leads by ~1 month, weight it more
        estimate = int(0.4 * bls_val + 0.6 * adp_val)
    elif adp_val:
        estimate = adp_val
    elif bls_val:
        estimate = bls_val

    if estimate is None:
        log.warning("NFP: could not build estimate, skipping")
        return []

    log.info("NFP estimate: %dk jobs (bls=%s, adp=%s)", estimate, bls_val, adp_val)

    markets = find_nfp_markets(client)
    if not markets:
        log.debug("NFP: no Kalshi NFP markets found")
        return []

    for mkt in markets:
        ticker    = mkt["ticker"]
        threshold = parse_nfp_threshold(ticker)
        if threshold is None:
            continue

        try:
            ob = client.get_orderbook(ticker, depth=1)
            yes_bids = ob.get("orderbook", {}).get("yes", [])
            if not yes_bids:
                continue
            market_yes = yes_bids[0][0]
        except Exception as e:
            log.debug("NFP orderbook %s: %s", ticker, e)
            continue

        our_prob    = get_implied_prob_above(threshold, estimate)
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
            strategy="nfp",
            ticker=ticker,
            side=side or "none",
            edge=edge,
            data={
                "threshold_k":  threshold,
                "estimate_k":   estimate,
                "our_prob":     our_prob,
                "market_yes":   market_yes,
            },
        )

        if side and edge >= EDGE_THRESHOLD:
            log.info("NFP EDGE: %s side=%s edge=%.1f%% price=%dc | threshold=%dk est=%dk",
                     ticker, side, edge * 100, price, threshold, estimate)
            if not dry_run:
                try:
                    result = client.place_order(
                        ticker=ticker, side=side, action="buy",
                        count=ORDER_CONTRACTS, price=price, order_type="limit",
                    )
                    order_id = result.get("order", {}).get("order_id", "?")
                    log_trade(
                        strategy="nfp", ticker=ticker, side=side,
                        price=price, count=ORDER_CONTRACTS,
                        order_id=order_id, status="placed", raw=result,
                    )
                    orders_placed.append(order_id)
                    log.info("NFP order placed: %s", order_id)
                except Exception as e:
                    log.error("NFP order failed %s: %s", ticker, e)
            else:
                tag = f"DRY:nfp:{ticker}:{side}:{price}"
                log.info("[DRY RUN] %s", tag)
                orders_placed.append(tag)

    return orders_placed
