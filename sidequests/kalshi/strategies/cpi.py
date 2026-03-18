"""
CPI strategy — BLS CPI release vs Kalshi "CPI MoM > X%" markets.

Data flow:
  1. Fetch latest CPI data from BLS public API (no key for basic use)
  2. Use Cleveland Fed Inflation Nowcasting for forward estimate
     https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting
  3. Compare nowcast to market-implied probability
  4. If edge > threshold: place maker order

BLS API (no key, limited):  https://api.bls.gov/publicAPI/v2/timeseries/data/
  Series CUUR0000SA0 = CPI-U, All items, not seasonally adjusted
  Series CUSR0000SA0 = CPI-U, All items, seasonally adjusted

Cleveland Fed Nowcast (JSON):
  https://www.clevelandfed.org/api/simple/GetInflationChartData
  (monthly updated, day-of release morning update is key signal window)

Release calendar from BLS:
  https://www.bls.gov/schedule/news_release/cpi.htm
  (scraped: next release date, release time = 8:30 AM ET)

Market window:  8:00–8:30 AM ET on BLS release day (pre-announcement)
"""

import os
import re
import json
import logging
import requests
from datetime import date, datetime, timezone, timedelta
from typing import Optional

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.cpi")

# ── config ────────────────────────────────────────────────────────────────────
EDGE_THRESHOLD  = float(os.getenv("CPI_EDGE_THRESHOLD", "0.07"))
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "5"))
KALSHI_FEE      = 0.01

BLS_API         = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
BLS_API_KEY     = os.getenv("BLS_API_KEY", "")   # optional — doubles rate limit
CPI_SERIES_SA   = "CUSR0000SA0"   # seasonally adjusted all-items
CPI_SERIES_NSA  = "CUUR0000SA0"   # not seasonally adjusted

CLEVELAND_URL   = "https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting"

# Kalshi CPI market series prefix (confirm exact prefix via /markets endpoint)
CPI_SERIES_PREFIX = "KXCPI"


# ── BLS data ──────────────────────────────────────────────────────────────────

def fetch_bls_cpi(series_id: str = CPI_SERIES_SA, n_months: int = 3) -> list:
    """
    Return last n months of CPI index values from BLS.
    Returns list of dicts: [{year, period, value}, ...]
    """
    payload = {
        "seriesid":  [series_id],
        "startyear": str(date.today().year - 1),
        "endyear":   str(date.today().year),
    }
    if BLS_API_KEY:
        payload["registrationkey"] = BLS_API_KEY

    r = requests.post(BLS_API, json=payload, timeout=15)
    r.raise_for_status()
    data = r.json()

    series = data.get("Results", {}).get("series", [])
    if not series:
        return []

    items = series[0].get("data", [])
    # BLS returns newest first
    return items[:n_months]


def cpi_mom_from_bls(items: list) -> Optional[float]:
    """Calculate month-over-month % change from two most recent readings."""
    if len(items) < 2:
        return None
    try:
        curr = float(items[0]["value"])
        prev = float(items[1]["value"])
        return (curr - prev) / prev * 100
    except Exception:
        return None


# ── Cleveland Fed nowcast ──────────────────────────────────────────────────────

def fetch_cleveland_nowcast() -> Optional[float]:
    """
    Scrape Cleveland Fed inflation nowcasting page for CPI MoM estimate.
    No official API — parse visible percentage figures from the page.
    Returns monthly % change or None.
    """
    try:
        r = requests.get(
            CLEVELAND_URL,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0 (compatible; kalshi-bot/1.0)"},
        )
        r.raise_for_status()
        # Look for CPI MoM nowcast figure — typically shows as "X.X%" near "CPI"
        # Pattern: CPI followed shortly by a decimal percentage
        matches = re.findall(
            r"CPI[^0-9]{0,60}?([-]?\d+\.\d+)\s*%", r.text, re.IGNORECASE
        )
        if matches:
            # Convert annual rate to monthly if value looks annualized (>1.5 typical)
            val = float(matches[0])
            if val > 2.0:
                val = val / 12   # rough annualized → monthly
            log.info("Cleveland nowcast scraped: %.3f%% MoM", val)
            return val
        return None
    except Exception as e:
        log.warning("Cleveland nowcast fetch failed: %s", e)
        return None


def fetch_nowcast_fallback() -> Optional[float]:
    """Unused — kept for future alternative source."""
    return None


def get_best_cpi_estimate() -> Optional[float]:
    """Return best available forward CPI MoM estimate (%)."""
    estimate = fetch_cleveland_nowcast()
    if estimate is None:
        estimate = fetch_nowcast_fallback()
    if estimate is None:
        # Fall back to last known BLS reading
        items = fetch_bls_cpi()
        estimate = cpi_mom_from_bls(items)
        if estimate:
            log.info("Using trailing BLS MoM as estimate: %.3f%%", estimate)
    return estimate


# ── BLS release schedule ──────────────────────────────────────────────────────

def is_release_window() -> bool:
    """
    True if we're within the pre-release trading window:
    8:00–8:30 AM ET on a BLS CPI release day.
    BLS releases CPI on a known schedule; we check against the BLS calendar RSS
    or simply allow the operator to set BLS_RELEASE_DATE env var.
    """
    release_date_str = os.getenv("BLS_RELEASE_DATE", "")
    if release_date_str:
        try:
            release_date = date.fromisoformat(release_date_str)
            if date.today() != release_date:
                return False
        except ValueError:
            pass

    now_et = datetime.now(tz=timezone(timedelta(hours=-4)))  # EDT
    return now_et.hour == 8 and now_et.minute < 30


# ── market matching ───────────────────────────────────────────────────────────

def find_cpi_markets(client: KalshiClient) -> list:
    markets = client.get_markets(limit=200)
    return [
        m for m in markets
        if m.get("ticker", "").startswith(CPI_SERIES_PREFIX)
        and m.get("status") == "open"
    ]


def parse_cpi_threshold(ticker: str) -> Optional[float]:
    """
    Extract threshold from ticker like KXCPI-25MAR-T0P3 → 0.3
    Kalshi CPI tickers vary — adjust regex to actual live ticker format.
    """
    match = re.search(r"T(\d+)P(\d+)", ticker)
    if match:
        whole = int(match.group(1))
        frac  = int(match.group(2))
        return whole + frac / 10
    # Alternate format: T0P2 → 0.2
    match2 = re.search(r"(\d+)P(\d+)", ticker)
    if match2:
        return int(match2.group(1)) + int(match2.group(2)) / 10
    return None


# ── edge calculation ──────────────────────────────────────────────────────────

def compute_cpi_edge(estimate: float, threshold: float, market_yes_price: int) -> tuple:
    """
    estimate: nowcast MoM CPI % (e.g. 0.3)
    threshold: Kalshi market threshold (e.g. 0.3 = "CPI above 0.3%")
    Returns (side, edge_fraction).
    """
    diff = estimate - threshold   # positive = estimate above threshold

    if diff >= 0.15:
        true_prob = 0.90
    elif diff >= 0.08:
        true_prob = 0.75
    elif diff >= 0.03:
        true_prob = 0.60
    elif diff <= -0.15:
        true_prob = 0.10
    elif diff <= -0.08:
        true_prob = 0.25
    elif diff <= -0.03:
        true_prob = 0.40
    else:
        true_prob = 0.50

    market_prob = market_yes_price / 100
    edge_yes = true_prob - market_prob - KALSHI_FEE
    edge_no  = (1 - true_prob) - (1 - market_prob) - KALSHI_FEE

    if edge_yes > edge_no and edge_yes > 0:
        return "yes", edge_yes
    elif edge_no > 0:
        return "no", edge_no
    else:
        return None, max(edge_yes, edge_no)


# ── main strategy entry ───────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False, force: bool = False) -> list:
    """
    Run CPI strategy. By default only executes in the pre-release window.
    Set force=True or FORCE_CPI_RUN=1 to ignore timing gate.
    """
    orders_placed = []

    if not force and not bool(os.getenv("FORCE_CPI_RUN")):
        if not is_release_window():
            log.info("CPI: outside release window, skipping")
            return []

    estimate = get_best_cpi_estimate()
    if estimate is None:
        log.warning("CPI: no estimate available, skipping")
        return []

    log.info("CPI estimate (MoM): %.3f%%", estimate)
    markets = find_cpi_markets(client)

    for mkt in markets:
        ticker = mkt["ticker"]
        threshold = parse_cpi_threshold(ticker)
        if threshold is None:
            log.debug("Could not parse threshold from %s", ticker)
            continue

        try:
            ob = client.get_orderbook(ticker, depth=1)
            yes_bids = ob.get("orderbook", {}).get("yes", [])
            if not yes_bids:
                continue
            market_yes_price = yes_bids[0][0]
        except Exception as e:
            log.warning("Orderbook fetch failed %s: %s", ticker, e)
            continue

        side, edge = compute_cpi_edge(estimate, threshold, market_yes_price)

        log_signal(
            strategy="cpi",
            ticker=ticker,
            side=side or "none",
            edge=edge,
            data={
                "estimate":    estimate,
                "threshold":   threshold,
                "market_yes":  market_yes_price,
            },
        )

        if side and edge >= EDGE_THRESHOLD:
            price = market_yes_price if side == "yes" else (100 - market_yes_price)
            log.info("EDGE FOUND %s side=%s edge=%.2f%% price=%dc",
                     ticker, side, edge * 100, price)

            if not dry_run:
                try:
                    result = client.place_order(
                        ticker=ticker,
                        side=side,
                        action="buy",
                        count=ORDER_CONTRACTS,
                        price=price,
                        order_type="limit",
                    )
                    order_id = result.get("order", {}).get("order_id", "?")
                    log_trade(
                        strategy="cpi",
                        ticker=ticker,
                        side=side,
                        price=price,
                        count=ORDER_CONTRACTS,
                        order_id=order_id,
                        status="placed",
                        raw=result,
                    )
                    orders_placed.append(order_id)
                    log.info("Order placed: %s", order_id)
                except Exception as e:
                    log.error("Order failed %s: %s", ticker, e)
            else:
                log.info("[DRY RUN] Would place %s %s @ %dc", side, ticker, price)
                orders_placed.append(f"DRY:{ticker}:{side}:{price}")

    return orders_placed
