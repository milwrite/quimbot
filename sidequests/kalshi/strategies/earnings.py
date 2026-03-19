"""
Earnings strategy — analyst EPS estimates vs Kalshi earnings-beat markets.

Edge source: Kalshi markets on "Will AAPL beat EPS estimates?" often price
off consensus at time of listing. When a company pre-announces or when
analyst revisions cluster before earnings, the market can lag.

Data sources (all free):
  - FinancialModelingPrep public API (basic tier, no key for some endpoints):
      https://financialmodelingprep.com/api/v3/
  - Alpha Vantage (free tier, 25 req/day with key):
      https://www.alphavantage.co/
  - Open FMP calendar endpoint:
      https://financialmodelingprep.com/api/v3/earning_calendar

Signals:
  1. Analyst revision momentum: if >70% of recent revisions are UP before earnings
     → higher probability of beat
  2. Whisper vs consensus spread: wide gap → higher uncertainty → fade consensus
  3. Surprise rate: company's historical beat rate (FMP earnings surprises endpoint)
     → regression to mean
"""

import os
import re
import logging
import datetime
import requests
from typing import Optional

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.earnings")

EDGE_THRESHOLD  = float(os.getenv("EARN_EDGE_THRESHOLD",  "0.08"))
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "1"))
KALSHI_FEE      = 0.01

EARN_SERIES_PREFIXES = ["KXEARNINGS", "KXEPS", "EARN-", "EPS-"]

FMP_BASE    = "https://financialmodelingprep.com/api/v3"
FMP_API_KEY = os.getenv("FMP_API_KEY", "demo")   # "demo" gives limited access

AV_BASE     = "https://www.alphavantage.co/query"
AV_API_KEY  = os.getenv("ALPHA_VANTAGE_KEY", "")


# ── FMP data ───────────────────────────────────────────────────────────────────

def fetch_earnings_calendar(days_ahead: int = 7) -> list:
    """
    Fetch upcoming earnings from FMP.
    Returns list of {symbol, date, eps_estimated, revenue_estimated}.
    """
    today = datetime.date.today()
    to_dt = today + datetime.timedelta(days=days_ahead)
    try:
        r = requests.get(
            f"{FMP_BASE}/earning_calendar",
            params={
                "from":    today.isoformat(),
                "to":      to_dt.isoformat(),
                "apikey":  FMP_API_KEY,
            },
            timeout=10,
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        log.debug("FMP earnings calendar failed: %s", e)
    return []


def fetch_earnings_surprises(symbol: str, limit: int = 8) -> Optional[list]:
    """
    Historical earnings surprises for a company.
    Returns list of {date, actualEarningResult, estimatedEarning}.
    """
    try:
        r = requests.get(
            f"{FMP_BASE}/earnings-surprises/{symbol}",
            params={"apikey": FMP_API_KEY},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()[:limit]
    except Exception as e:
        log.debug("FMP earnings surprises %s failed: %s", symbol, e)
    return None


def historical_beat_rate(surprises: list) -> float:
    """
    Fraction of quarters where actual > estimated.
    Returns float 0-1.
    """
    if not surprises:
        return 0.5
    beats = sum(
        1 for s in surprises
        if s.get("actualEarningResult", 0) > s.get("estimatedEarning", 0)
    )
    return beats / len(surprises)


def fetch_analyst_estimates(symbol: str) -> Optional[dict]:
    """
    Fetch analyst EPS estimates from FMP.
    Returns {eps_avg, eps_high, eps_low, revision_up_pct} or None.
    """
    try:
        r = requests.get(
            f"{FMP_BASE}/analyst-estimates/{symbol}",
            params={"apikey": FMP_API_KEY, "limit": 4},
            timeout=10,
        )
        r.raise_for_status()
        data = r.json()
        if not data:
            return None
        latest = data[0]
        eps_avg  = float(latest.get("estimatedEpsAvg", 0) or 0)
        eps_high = float(latest.get("estimatedEpsHigh", 0) or 0)
        eps_low  = float(latest.get("estimatedEpsLow", 0) or 0)
        return {
            "eps_avg":   eps_avg,
            "eps_high":  eps_high,
            "eps_low":   eps_low,
            "spread_pct": (eps_high - eps_low) / abs(eps_avg) if eps_avg != 0 else 0,
        }
    except Exception as e:
        log.debug("FMP analyst estimates %s failed: %s", symbol, e)
    return None


# ── beat probability model ────────────────────────────────────────────────────

def estimate_beat_prob(symbol: str) -> float:
    """
    Blend historical beat rate + analyst estimate spread.
    Wide spread = more uncertainty = regress to 50%.
    """
    surprises  = fetch_earnings_surprises(symbol) or []
    base_rate  = historical_beat_rate(surprises)
    estimates  = fetch_analyst_estimates(symbol)

    prob = base_rate

    if estimates:
        spread = estimates.get("spread_pct", 0)
        # Wide analyst spread → regress toward 50%
        regression_weight = min(0.5, spread)
        prob = prob * (1 - regression_weight) + 0.5 * regression_weight

    return max(0.05, min(0.95, prob))


# ── market matching ────────────────────────────────────────────────────────────

def find_earnings_markets(client: KalshiClient) -> list:
    markets = client.get_markets(limit=500)
    return [
        m for m in markets
        if any(m.get("ticker", "").startswith(p) for p in EARN_SERIES_PREFIXES)
        and m.get("status") == "open"
    ]


KNOWN_TICKERS = {
    "AAPL": "AAPL", "MSFT": "MSFT", "GOOGL": "GOOGL", "AMZN": "AMZN",
    "NVDA": "NVDA", "META": "META", "TSLA": "TSLA", "AMD": "AMD",
    "NFLX": "NFLX", "JPM": "JPM", "GS": "GS", "BAC": "BAC",
}


def parse_symbol_from_market(mkt: dict) -> Optional[str]:
    """Extract stock ticker from Kalshi market ticker or title."""
    ticker = mkt.get("ticker", "").upper()
    title  = (mkt.get("title") or "").upper()

    for sym in KNOWN_TICKERS:
        if sym in ticker or sym in title:
            return sym

    # Try regex: 1-5 capital letters in the Kalshi ticker
    m = re.search(r"([A-Z]{2,5})", ticker.replace("KXEARNINGS", "").replace("KXEPS", ""))
    if m:
        return m.group(1)

    return None


# ── main strategy entry ────────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    orders_placed = []

    markets = find_earnings_markets(client)
    if not markets:
        log.debug("Earnings: no Kalshi earnings markets found")
        return []

    # Upcoming earnings for context
    upcoming = fetch_earnings_calendar(days_ahead=7)
    upcoming_syms = {e.get("symbol") for e in upcoming}
    log.info("Earnings: %d markets, %d upcoming in 7d", len(markets), len(upcoming_syms))

    for mkt in markets:
        ticker = mkt["ticker"]
        symbol = parse_symbol_from_market(mkt)

        if not symbol:
            continue

        our_prob = estimate_beat_prob(symbol)

        try:
            ob = client.get_orderbook(ticker, depth=1)
            yes_bids = ob.get("orderbook", {}).get("yes", [])
            if not yes_bids:
                continue
            market_yes = yes_bids[0][0]
        except Exception as e:
            log.debug("Earnings orderbook %s: %s", ticker, e)
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
            strategy="earnings",
            ticker=ticker,
            side=side or "none",
            edge=edge,
            data={
                "symbol":       symbol,
                "our_prob":     our_prob,
                "market_yes":   market_yes,
                "in_upcoming":  symbol in upcoming_syms,
            },
        )

        if side and edge >= EDGE_THRESHOLD:
            log.info("EARN EDGE: %s %s side=%s edge=%.1f%% | ours=%.2f mkt=%.2f",
                     ticker, symbol, side, edge * 100, our_prob, market_prob)
            if not dry_run:
                try:
                    result = client.place_order(
                        ticker=ticker, side=side, action="buy",
                        count=ORDER_CONTRACTS, price=price, order_type="limit",
                    )
                    order_id = result.get("order", {}).get("order_id", "?")
                    log_trade(
                        strategy="earnings", ticker=ticker, side=side,
                        price=price, count=ORDER_CONTRACTS,
                        order_id=order_id, status="placed", raw=result,
                    )
                    orders_placed.append(order_id)
                    log.info("Earnings order placed: %s", order_id)
                except Exception as e:
                    log.error("Earnings order failed %s: %s", ticker, e)
            else:
                tag = f"DRY:earnings:{ticker}:{side}:{price}"
                log.info("[DRY RUN] %s", tag)
                orders_placed.append(tag)

    return orders_placed
