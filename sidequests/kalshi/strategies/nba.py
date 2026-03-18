"""
NBA strategy — live win probability vs Kalshi in-game / pre-game markets.

Data sources (all free, no key):
  - ESPN scoreboard API (unofficial, stable):
      http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard
  - ESPN game summary (win probability series):
      http://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event={game_id}
  - The-Sports-DB (pre-game odds/context, no key):
      https://www.thesportsdb.com/api/v1/json/3/eventsnextleague.php?id=4387

Win probability source:
  ESPN embeds a real-time win probability series in the game summary endpoint
  (`winProbability` array with `homeWinPercentage` at each game moment).
  This is the same model powering their broadcast graphics.

Market matching:
  Kalshi NBA markets follow patterns like:
    KXNBA-{YYMMDD}-{AWAYTEAM}   (team wins today)
    KXNBA-SPREAD-{GAMEID}        (spread markets)
  We match by team name/abbreviation against ESPN game data.

Edge sources:
  1. Pre-game: ESPN pre-game win% vs Kalshi opening price
  2. In-game: live ESPN win% vs current Kalshi price (biggest opportunity —
     Kalshi reprices slowly vs ESPN's near-real-time model)

Rate of scan: every full cycle (60s default). Most edge appears:
  - 10-20 min before tip (ESPN has pregame model, Kalshi hasn't adjusted)
  - After a big swing (lead change, key foul, late-game 3-pointer)
  - Final 2 minutes with Kalshi still showing 50/50 on a 10-point game
"""

import os
import re
import logging
import requests
from datetime import date, datetime, timezone
from typing import Optional

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.nba")

EDGE_THRESHOLD  = float(os.getenv("NBA_EDGE_THRESHOLD",  "0.07"))  # 7%
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS",       "1"))
KALSHI_FEE      = 0.01

ESPN_SCOREBOARD = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
ESPN_SUMMARY    = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary"

NBA_SERIES_PREFIXES = ["KXNBA", "NBA-"]


# ── ESPN data ─────────────────────────────────────────────────────────────────

def fetch_espn_games() -> list:
    """
    Return list of today's NBA games from ESPN.
    Each item: {game_id, home_team, away_team, status, home_score, away_score,
                home_win_pct, period, clock}
    """
    try:
        r = requests.get(ESPN_SCOREBOARD, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        log.warning("ESPN scoreboard fetch failed: %s", e)
        return []

    games = []
    for event in data.get("events", []):
        try:
            game_id    = event["id"]
            status     = event["status"]["type"]["name"]   # e.g. STATUS_IN_PROGRESS
            competitors = event["competitions"][0]["competitors"]

            home = next(c for c in competitors if c["homeAway"] == "home")
            away = next(c for c in competitors if c["homeAway"] == "away")

            home_team  = home["team"]["abbreviation"]
            away_team  = away["team"]["abbreviation"]
            home_score = int(home.get("score", 0) or 0)
            away_score = int(away.get("score", 0) or 0)

            period = event["status"].get("period", 0)
            clock  = event["status"].get("displayClock", "")

            # Win probability from ESPN (in-game)
            home_win_pct = fetch_espn_win_prob(game_id, home_team)

            games.append({
                "game_id":      game_id,
                "home_team":    home_team,
                "away_team":    away_team,
                "home_score":   home_score,
                "away_score":   away_score,
                "status":       status,
                "period":       period,
                "clock":        clock,
                "home_win_pct": home_win_pct,
            })
        except Exception as e:
            log.debug("Error parsing ESPN event: %s", e)

    return games


def fetch_espn_win_prob(game_id: str, home_abbr: str) -> Optional[float]:
    """
    Fetch current win probability for the home team from ESPN game summary.
    Returns float 0.0–1.0 or None.
    """
    try:
        r = requests.get(ESPN_SUMMARY, params={"event": game_id}, timeout=10)
        r.raise_for_status()
        data = r.json()

        # winProbability is a time-series; last entry = current
        wp_series = data.get("winProbability", [])
        if not wp_series:
            # Try pickcenter (pre-game)
            pc = data.get("pickcenter", [])
            for p in pc:
                if "homeTeamOdds" in p:
                    win_pct = p["homeTeamOdds"].get("winPercentage")
                    if win_pct is not None:
                        return float(win_pct) / 100
            return None

        last = wp_series[-1]
        return float(last.get("homeWinPercentage", 50)) / 100

    except Exception as e:
        log.debug("ESPN win prob fetch %s: %s", game_id, e)
        return None


# ── market matching ───────────────────────────────────────────────────────────

def find_nba_markets(client: KalshiClient) -> list:
    markets = client.get_markets(limit=500)
    return [
        m for m in markets
        if any(m.get("ticker", "").startswith(p) for p in NBA_SERIES_PREFIXES)
        and m.get("status") == "open"
    ]


def match_game_to_market(game: dict, markets: list) -> Optional[dict]:
    """
    Match an ESPN game to a Kalshi market by team abbreviation.
    Returns the market dict or None.
    """
    home = game["home_team"].upper()
    away = game["away_team"].upper()
    today = date.today().strftime("%y%m%d")

    for mkt in markets:
        ticker = mkt["ticker"].upper()
        # Try to match home or away team in ticker
        if home in ticker or away in ticker:
            return mkt

    return None


# ── edge calculation ──────────────────────────────────────────────────────────

def compute_nba_edge(
    espn_home_win_pct: float,
    market_yes_price: int,
    game: dict,
    market_is_home: bool = True,
) -> tuple:
    """
    espn_home_win_pct: 0.0–1.0
    market_yes_price: cents (1–99) for the market's YES outcome
    market_is_home: True if market YES = home team wins

    Returns (side, edge_fraction).
    """
    true_prob = espn_home_win_pct if market_is_home else (1 - espn_home_win_pct)
    market_prob = market_yes_price / 100

    # Confidence discount for pre-game (less certain than in-game)
    status = game.get("status", "")
    if "PRE" in status or game.get("period", 0) == 0:
        # Pre-game: ESPN model less reliable, widen required edge
        confidence = 0.85
    elif game.get("period", 0) >= 4:
        # Late game: ESPN model very reliable
        confidence = 1.0
    else:
        confidence = 0.92

    adjusted_prob = true_prob * confidence + 0.5 * (1 - confidence)

    edge_yes = adjusted_prob - market_prob - KALSHI_FEE
    edge_no  = (1 - adjusted_prob) - (1 - market_prob) - KALSHI_FEE

    if edge_yes > edge_no and edge_yes > 0:
        return "yes", edge_yes
    elif edge_no > 0:
        return "no", edge_no
    else:
        return None, max(edge_yes, edge_no)


# ── late-game filter ──────────────────────────────────────────────────────────

def is_interesting_game_state(game: dict) -> bool:
    """
    Filter out uninteresting game states where ESPN model is weakest.
    Skip: early Q1 (market hasn't moved much yet),
    Skip: pre-game when teams are roughly equal
    """
    status = game.get("status", "")
    period = game.get("period", 0)
    home_wp = game.get("home_win_pct", 0.5)

    # Pre-game: only if there's a clear favorite (espn shows >65%)
    if "PRE" in status or period == 0:
        return home_wp is not None and (home_wp > 0.65 or home_wp < 0.35)

    # In-game: always interesting (live repricing opportunity)
    return True


# ── main strategy entry ───────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    """Scan NBA games for ESPN win% vs Kalshi price divergence."""
    orders_placed = []

    games = fetch_espn_games()
    if not games:
        log.debug("NBA: no ESPN games today or fetch failed")
        return []

    log.info("NBA: %d game(s) found", len(games))
    markets = find_nba_markets(client)

    if not markets:
        log.debug("NBA: no Kalshi NBA markets found")
        return []

    for game in games:
        if not is_interesting_game_state(game):
            continue

        home_wp = game.get("home_win_pct")
        if home_wp is None:
            log.debug("NBA: no win prob for %s vs %s", game["away_team"], game["home_team"])
            continue

        mkt = match_game_to_market(game, markets)
        if not mkt:
            log.debug("NBA: no Kalshi market matched for %s vs %s",
                      game["away_team"], game["home_team"])
            continue

        ticker = mkt["ticker"]

        try:
            ob = client.get_orderbook(ticker, depth=1)
            yes_bids = ob.get("orderbook", {}).get("yes", [])
            if not yes_bids:
                continue
            market_yes_price = yes_bids[0][0]
        except Exception as e:
            log.warning("NBA orderbook fetch %s: %s", ticker, e)
            continue

        # Assume market YES = home team wins (common Kalshi convention)
        side, edge = compute_nba_edge(home_wp, market_yes_price, game, market_is_home=True)

        log_signal(
            strategy="nba",
            ticker=ticker,
            side=side or "none",
            edge=edge,
            data={
                "home":        game["home_team"],
                "away":        game["away_team"],
                "score":       f"{game['away_score']}-{game['home_score']}",
                "period":      game["period"],
                "clock":       game["clock"],
                "espn_home_wp": home_wp,
                "market_yes":  market_yes_price,
            },
        )

        if side and edge >= EDGE_THRESHOLD:
            price = market_yes_price if side == "yes" else (100 - market_yes_price)
            log.info("NBA EDGE: %s side=%s edge=%.1f%% price=%dc | %s@%s P%s %s",
                     ticker, side, edge * 100, price,
                     game["away_team"], game["home_team"],
                     game["period"], game["clock"])

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
                        strategy="nba",
                        ticker=ticker,
                        side=side,
                        price=price,
                        count=ORDER_CONTRACTS,
                        order_id=order_id,
                        status="placed",
                        raw=result,
                    )
                    orders_placed.append(order_id)
                    log.info("NBA order placed: %s", order_id)
                except Exception as e:
                    log.error("NBA order failed %s: %s", ticker, e)
            else:
                tag = f"DRY:nba:{ticker}:{side}:{price}"
                log.info("[DRY RUN] %s", tag)
                orders_placed.append(tag)

    return orders_placed
