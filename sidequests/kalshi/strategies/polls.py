"""
Polls strategy — aggregate polling data vs Kalshi political markets.

Edge source: Kalshi political markets often price off pundit consensus or
older polls. Fresh aggregate data (538, RCP, Polymarket) can diverge by 5-15%.

Data sources (all free):
  - 538 forecast JSON (GitHub):
      https://projects.fivethirtyeight.com/polls/data/
  - RealClearPolitics (scraped headlines only — unreliable, use as fallback)
  - Polymarket public API (for cross-market calibration):
      https://gamma-api.polymarket.com/markets

Strategy:
  1. Fetch current polling averages for open political markets
  2. Convert polling average to win probability (via logistic model or
     direct if already expressed as probability)
  3. Compare against Kalshi YES price
  4. Trade when edge > threshold

Cross-market calibration (Polymarket):
  If a matching Polymarket contract exists, use its price as a second signal.
  Kalshi vs Polymarket spread alone can generate arb when it exceeds fees.
"""

import os
import re
import json
import logging
import requests
from typing import Optional

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.polls")

EDGE_THRESHOLD  = float(os.getenv("POLLS_EDGE_THRESHOLD", "0.06"))
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "1"))
KALSHI_FEE      = 0.01

POLITICS_PREFIXES = ["KXPRES", "KXSEN", "KXGOV", "KXHOUSE", "PRES-", "SEN-", "GOV-", "KXELEC"]

POLYMARKET_API = "https://gamma-api.polymarket.com/markets"
FTE_POLLS_URL  = "https://projects.fivethirtyeight.com/polls/data/president_polls.csv"


# ── Polymarket prices ─────────────────────────────────────────────────────────

def fetch_polymarket_markets(limit: int = 200) -> list:
    """Fetch open Polymarket markets. Returns list of market dicts."""
    try:
        r = requests.get(
            POLYMARKET_API,
            params={"closed": "false", "limit": limit},
            timeout=10,
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        log.debug("Polymarket fetch failed: %s", e)
        return []


def find_polymarket_match(kalshi_mkt: dict, poly_markets: list) -> Optional[float]:
    """
    Find matching Polymarket contract and return its YES price (0-1).
    Matches on title keywords.
    """
    title = (kalshi_mkt.get("title") or kalshi_mkt.get("subtitle") or "").lower()
    if not title:
        return None

    # Extract key entities from Kalshi title
    words = set(re.findall(r"[a-z]{4,}", title))

    best_match = None
    best_score = 0

    for pm in poly_markets:
        pm_title = (pm.get("question") or pm.get("description") or "").lower()
        pm_words = set(re.findall(r"[a-z]{4,}", pm_title))
        overlap = len(words & pm_words) / max(len(words), 1)
        if overlap > best_score and overlap > 0.4:
            best_score = overlap
            best_match = pm

    if best_match:
        # Polymarket prices are in the `outcomePrices` field or `tokens[].price`
        try:
            tokens = best_match.get("tokens", [])
            for t in tokens:
                if t.get("outcome", "").lower() in ("yes", "true"):
                    return float(t["price"])
            # Fallback: outcomes field
            prices = json.loads(best_match.get("outcomePrices", "[]"))
            if prices:
                return float(prices[0])
        except Exception:
            pass

    return None


# ── polling averages ──────────────────────────────────────────────────────────

def fetch_fte_latest_polls(candidate_name: str) -> Optional[float]:
    """
    Fetch 538 polling CSV and extract the latest rolling average for a candidate.
    Returns a float 0-100 (percentage) or None.
    Very rough — CSV column names change across cycles.
    """
    try:
        r = requests.get(FTE_POLLS_URL, timeout=10)
        r.raise_for_status()
        lines = r.text.splitlines()
        if not lines:
            return None
        headers = [h.strip('"').lower() for h in lines[0].split(",")]
        pct_col = headers.index("pct") if "pct" in headers else None
        name_col = headers.index("candidate_name") if "candidate_name" in headers else None
        if pct_col is None or name_col is None:
            return None

        candidate_upper = candidate_name.upper()
        values = []
        for line in lines[1:20]:   # last 20 polls
            parts = line.split(",")
            if len(parts) <= max(pct_col, name_col):
                continue
            name = parts[name_col].strip('"').upper()
            if candidate_upper in name:
                try:
                    values.append(float(parts[pct_col].strip('"')))
                except ValueError:
                    pass
        if values:
            return sum(values) / len(values)
    except Exception as e:
        log.debug("538 polls fetch failed: %s", e)
    return None


def polls_to_win_prob(avg_pct: float, opponent_pct: float = None) -> float:
    """
    Convert a polling average to a win probability.
    If we have both candidates: win_prob = avg / (avg + opponent)
    If only one: use logistic transform centered at 50%.
    """
    if opponent_pct and opponent_pct > 0:
        total = avg_pct + opponent_pct
        return avg_pct / total if total > 0 else 0.5

    # Logistic: steeper than linear, but a simple approximation
    z = (avg_pct - 50) / 10
    return 1 / (1 + pow(2.718, -z))


# ── market matching ────────────────────────────────────────────────────────────

def find_political_markets(client: KalshiClient) -> list:
    markets = client.get_markets(limit=500)
    return [
        m for m in markets
        if any(m.get("ticker", "").startswith(p) for p in POLITICS_PREFIXES)
        and m.get("status") == "open"
    ]


def extract_candidate(market: dict) -> Optional[str]:
    """Best-effort candidate extraction from market title."""
    title = market.get("title") or market.get("subtitle") or ""
    # Look for capitalized words (names)
    names = re.findall(r"\b[A-Z][a-z]+\b", title)
    if names:
        return names[0]
    return None


# ── main strategy entry ────────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    """Scan political markets for poll-vs-market edge."""
    orders_placed = []

    markets = find_political_markets(client)
    if not markets:
        log.debug("Polls: no open political markets found")
        return []

    log.info("Polls: scanning %d political market(s)", len(markets))

    # Pre-fetch Polymarket for cross-market calibration
    poly_markets = fetch_polymarket_markets()
    log.info("Polls: fetched %d Polymarket contracts for calibration", len(poly_markets))

    for mkt in markets:
        ticker    = mkt["ticker"]
        candidate = extract_candidate(mkt)

        # Source 1: Polymarket cross-calibration
        poly_prob = find_polymarket_match(mkt, poly_markets)

        # Source 2: 538 polling (if candidate identifiable)
        poll_prob = None
        if candidate:
            avg_pct = fetch_fte_latest_polls(candidate)
            if avg_pct:
                poll_prob = polls_to_win_prob(avg_pct)

        # Blend signals (weight Polymarket more — it's also a prediction market)
        if poly_prob is not None and poll_prob is not None:
            our_prob = 0.6 * poly_prob + 0.4 * poll_prob
        elif poly_prob is not None:
            our_prob = poly_prob
        elif poll_prob is not None:
            our_prob = poll_prob
        else:
            log.debug("Polls: no signal for %s, skipping", ticker)
            continue

        try:
            ob = client.get_orderbook(ticker, depth=1)
            yes_bids = ob.get("orderbook", {}).get("yes", [])
            if not yes_bids:
                continue
            market_yes = yes_bids[0][0]
        except Exception as e:
            log.debug("Polls orderbook %s: %s", ticker, e)
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
            strategy="polls",
            ticker=ticker,
            side=side or "none",
            edge=edge,
            data={
                "candidate":    candidate,
                "our_prob":     our_prob,
                "poly_prob":    poly_prob,
                "poll_prob":    poll_prob,
                "market_yes":   market_yes,
            },
        )

        if side and edge >= EDGE_THRESHOLD:
            log.info("POLLS EDGE: %s %s side=%s edge=%.1f%% | ours=%.2f mkt=%.2f",
                     ticker, candidate, side, edge * 100, our_prob, market_prob)
            if not dry_run:
                try:
                    result = client.place_order(
                        ticker=ticker, side=side, action="buy",
                        count=ORDER_CONTRACTS, price=price, order_type="limit",
                    )
                    order_id = result.get("order", {}).get("order_id", "?")
                    log_trade(
                        strategy="polls", ticker=ticker, side=side,
                        price=price, count=ORDER_CONTRACTS,
                        order_id=order_id, status="placed", raw=result,
                    )
                    orders_placed.append(order_id)
                    log.info("Polls order placed: %s", order_id)
                except Exception as e:
                    log.error("Polls order failed %s: %s", ticker, e)
            else:
                tag = f"DRY:polls:{ticker}:{side}:{price}"
                log.info("[DRY RUN] %s", tag)
                orders_placed.append(tag)

    return orders_placed
