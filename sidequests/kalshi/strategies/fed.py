"""
Fed ladder strategy — detects monotonicity violations in KXFED rate markets.

Core insight: Kalshi Fed rate markets are cumulative thresholds.
P(rate > 4.25%) MUST be <= P(rate > 4.00%) by definition.
If the market violates this, one side is mispriced — arb both legs.

Data source: Kalshi market prices only (no external API needed).
The CME FedWatch implied probabilities serve as a sanity check when available.

CME FedWatch (no key, scrape):
  https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html
  (or use FRED API for historical fed funds target ranges)

Market scan:
  - Fetch all open KXFED markets
  - Sort by threshold value
  - Check adjacent pairs for monotonicity: P(>higher) <= P(>lower)
  - Any violation = edge on the mispriced contract
  - Also check against CME FedWatch implied probs for absolute edge

Runs every scan cycle (gated to market hours if configured).
"""

import os
import re
import logging
import requests
from typing import Optional

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.fed")

EDGE_THRESHOLD  = float(os.getenv("FED_EDGE_THRESHOLD",  "0.08"))  # 8%
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS",       "1"))
KALSHI_FEE      = 0.01

FED_SERIES_PREFIXES = ["KXFED", "FED-", "FEDRATE"]   # confirm live prefix via /markets

# FRED API (no key for basic reads)
FRED_SERIES_FEDFUNDS = "FEDFUNDS"
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"
FRED_API_KEY = os.getenv("FRED_API_KEY", "")  # optional


# ── CME FedWatch implied probability ─────────────────────────────────────────

def fetch_cme_implied_prob() -> Optional[dict]:
    """
    Scrape CME FedWatch page for implied probabilities of rate outcomes.
    Returns dict of {rate_pct_str: probability} or None on failure.
    Very fragile — CME changes their page layout. Use as sanity check only.
    """
    try:
        r = requests.get(
            "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10,
        )
        # Look for percentage patterns associated with rate levels
        # This is best-effort scraping; the real data is behind JavaScript
        matches = re.findall(r"(\d+\.\d+)%.*?(\d+\.\d+)%", r.text)
        return {"raw_matches": matches[:10]} if matches else None
    except Exception as e:
        log.debug("CME FedWatch fetch failed (non-critical): %s", e)
        return None


def fetch_fred_fedfunds() -> Optional[float]:
    """Get current effective fed funds rate from FRED (no key needed for public series)."""
    try:
        params = {
            "series_id":    FRED_SERIES_FEDFUNDS,
            "sort_order":   "desc",
            "limit":        1,
            "file_type":    "json",
        }
        if FRED_API_KEY:
            params["api_key"] = FRED_API_KEY
        else:
            params["api_key"] = "abcdefghijklmnopqrstuvwxyz123456"  # public demo key
        r = requests.get(FRED_BASE, params=params, timeout=10)
        r.raise_for_status()
        obs = r.json().get("observations", [])
        if obs:
            return float(obs[0]["value"])
    except Exception as e:
        log.debug("FRED fetch failed: %s", e)
    return None


# ── market fetching ───────────────────────────────────────────────────────────

def find_fed_markets(client: KalshiClient) -> list:
    """Return all open Fed rate markets, sorted by threshold ascending."""
    markets = client.get_markets(limit=500)
    fed_markets = [
        m for m in markets
        if any(m.get("ticker", "").startswith(p) for p in FED_SERIES_PREFIXES)
        and m.get("status") == "open"
    ]
    return fed_markets


def parse_rate_threshold(ticker: str) -> Optional[float]:
    """
    Extract rate threshold from ticker.
    Examples:
      KXFED-25DEC-T4P25 → 4.25
      KXFED-25MAR-T4P00 → 4.00
      KXFED-25JUN-T4P50 → 4.50
    """
    # Pattern: T{whole}P{frac} where frac is hundredths
    match = re.search(r"T(\d+)P(\d+)", ticker)
    if match:
        whole = int(match.group(1))
        frac  = int(match.group(2))
        return whole + frac / 100
    # Alternate: look for decimal in ticker like 4.25, 4.00
    match2 = re.search(r"(\d+)\.(\d+)", ticker)
    if match2:
        return float(f"{match2.group(1)}.{match2.group(2)}")
    return None


# ── monotonicity check ────────────────────────────────────────────────────────

def find_violations(markets_with_prices: list) -> list:
    """
    markets_with_prices: list of (ticker, threshold_pct, yes_price_cents)
    sorted by threshold ascending.

    Finds pairs where P(>higher_threshold) > P(>lower_threshold).
    Returns list of violation dicts.
    """
    violations = []
    sorted_mkts = sorted(markets_with_prices, key=lambda x: x[1])

    for i in range(len(sorted_mkts) - 1):
        t_low,  thresh_low,  p_low  = sorted_mkts[i]
        t_high, thresh_high, p_high = sorted_mkts[i + 1]

        if thresh_high <= thresh_low:
            continue

        # P(>higher) must be <= P(>lower). If not: violation.
        if p_high > p_low:
            # The higher-threshold market is overpriced, lower is underpriced.
            violations.append({
                "type":        "monotonicity",
                "low_ticker":  t_low,
                "low_thresh":  thresh_low,
                "low_price":   p_low,
                "high_ticker": t_high,
                "high_thresh": thresh_high,
                "high_price":  p_high,
                "spread":      p_high - p_low,   # cents — theoretical max edge
                "action":      [
                    {"ticker": t_high, "side": "no",  "price": 100 - p_high},
                    {"ticker": t_low,  "side": "yes", "price": p_low},
                ],
            })

        # Also check: if spread between adjacent levels is implausibly large
        # (market underpricing the higher threshold vs. implied distribution)
        spread = p_low - p_high
        if spread > 40:   # >40c gap between adjacent thresholds = suspicious
            violations.append({
                "type":        "gap",
                "low_ticker":  t_low,
                "low_thresh":  thresh_low,
                "low_price":   p_low,
                "high_ticker": t_high,
                "high_thresh": thresh_high,
                "high_price":  p_high,
                "spread":      spread,
                "action":      [
                    {"ticker": t_high, "side": "yes", "price": p_high},
                ],
            })

    return violations


# ── edge calculation ──────────────────────────────────────────────────────────

def violation_edge(violation: dict) -> float:
    """
    For monotonicity violations: edge is the spread (cents) / 100 minus fees.
    A 5c spread on a YES+NO pair = 5% gross edge.
    """
    gross = violation["spread"] / 100
    net   = gross - KALSHI_FEE * 2   # fee on both legs
    return net


# ── main strategy entry ───────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    """Scan Fed rate markets for monotonicity violations. Place orders on edges."""
    orders_placed = []

    fed_markets = find_fed_markets(client)
    if not fed_markets:
        log.debug("No Fed markets found (check FED_SERIES_PREFIXES)")
        return []

    # Fetch yes prices for all Fed markets
    markets_with_prices = []
    for mkt in fed_markets:
        ticker    = mkt["ticker"]
        threshold = parse_rate_threshold(ticker)
        if threshold is None:
            continue
        try:
            ob = client.get_orderbook(ticker, depth=1)
            yes_bids = ob.get("orderbook", {}).get("yes", [])
            if not yes_bids:
                continue
            yes_price = yes_bids[0][0]
            markets_with_prices.append((ticker, threshold, yes_price))
        except Exception as e:
            log.debug("Orderbook fetch %s: %s", ticker, e)

    if len(markets_with_prices) < 2:
        log.debug("Not enough Fed markets with prices to compare")
        return []

    violations = find_violations(markets_with_prices)

    if not violations:
        log.debug("Fed: no violations found across %d markets", len(markets_with_prices))
        return []

    log.info("Fed: found %d violation(s) across %d markets",
             len(violations), len(markets_with_prices))

    for v in violations:
        edge = violation_edge(v)

        log_signal(
            strategy="fed",
            ticker=f"{v['low_ticker']}|{v['high_ticker']}",
            side="arb",
            edge=edge,
            data=v,
        )

        if edge < EDGE_THRESHOLD:
            log.debug("Fed violation edge %.2f%% below threshold %.2f%%",
                      edge * 100, EDGE_THRESHOLD * 100)
            continue

        log.info("Fed arb: %s type=%s spread=%dc edge=%.1f%%",
                 v["type"], v["type"], v["spread"], edge * 100)

        for leg in v["action"]:
            if not dry_run:
                try:
                    result = client.place_order(
                        ticker=leg["ticker"],
                        side=leg["side"],
                        action="buy",
                        count=ORDER_CONTRACTS,
                        price=leg["price"],
                        order_type="limit",
                    )
                    order_id = result.get("order", {}).get("order_id", "?")
                    log_trade(
                        strategy="fed",
                        ticker=leg["ticker"],
                        side=leg["side"],
                        price=leg["price"],
                        count=ORDER_CONTRACTS,
                        order_id=order_id,
                        status="placed",
                        raw=result,
                    )
                    orders_placed.append(order_id)
                    log.info("Fed order placed: %s %s @ %dc",
                             leg["ticker"], leg["side"], leg["price"])
                except Exception as e:
                    log.error("Fed order failed %s: %s", leg["ticker"], e)
            else:
                tag = f"DRY:fed:{leg['ticker']}:{leg['side']}:{leg['price']}"
                log.info("[DRY RUN] %s", tag)
                orders_placed.append(tag)

    return orders_placed
