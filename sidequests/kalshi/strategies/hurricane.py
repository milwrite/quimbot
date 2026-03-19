"""
Hurricane / Storm strategy — NHC forecast vs Kalshi storm/hurricane contracts.

Edge source: NHC publishes cone-of-uncertainty forecasts every 6 hours.
Kalshi markets on landfall location, intensity, and timing often lag the NHC
updates by hours — especially on strengthening/weakening trends.

Data sources (all free, no key):
  - NHC active storms GeoJSON:
      https://www.nhc.noaa.gov/CurrentStorms.json
  - NHC storm forecast/advisory:
      https://www.nhc.noaa.gov/nhc_at{N}.xml  (Atlantic track {N})
  - NOAA storm GeoJSON:
      https://www.nhc.noaa.gov/gis/forecast/archive/{name}{year}_5day_latest.zip
  - Open-Meteo extended: can also fetch hurricane track from their API

Kalshi market patterns:
  - KXHURR-{year}{name}-LAND: will storm make landfall? (YES/NO)
  - KXHURR-{year}{name}-CAT{N}: will storm reach Category N?
  - KXHURR-{year}{name}-{STATE}: will storm hit named state?

Model: Use NHC official forecast probabilities directly from the XML advisory.
NHC publishes wind speed probabilities for US coastline — these are the ground truth.
"""

import os
import re
import logging
import requests
import xml.etree.ElementTree as ET
from typing import Optional

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.hurricane")

EDGE_THRESHOLD  = float(os.getenv("HURR_EDGE_THRESHOLD", "0.08"))
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "1"))
KALSHI_FEE      = 0.01

HURR_SERIES_PREFIXES = ["KXHURR", "KXTROP", "HURR-", "STORM-", "KXSTORM"]

NHC_CURRENT_URL = "https://www.nhc.noaa.gov/CurrentStorms.json"
NHC_RSS_BASE    = "https://www.nhc.noaa.gov/rss_feeds_at.xml"


# ── NHC data ───────────────────────────────────────────────────────────────────

def fetch_active_storms() -> list:
    """
    Returns list of active storm dicts from NHC.
    Each: {id, name, basin, intensity_kt, category, lat, lon, landfall_prob}
    """
    try:
        r = requests.get(NHC_CURRENT_URL, timeout=10)
        r.raise_for_status()
        data = r.json()
        storms = []
        for storm in data.get("activeStorms", []):
            cat    = saffir_simpson(int(storm.get("intensity", 0)))
            storms.append({
                "id":            storm.get("id"),
                "name":          storm.get("name"),
                "basin":         storm.get("basin"),
                "intensity_kt":  int(storm.get("intensity", 0)),
                "category":      cat,
                "lat":           float(storm.get("latitude", 0)),
                "lon":           float(storm.get("longitude", 0)),
                "movement":      storm.get("movement", ""),
                "headline":      storm.get("headline", ""),
            })
        return storms
    except Exception as e:
        log.debug("NHC active storms fetch failed: %s", e)
    return []


def saffir_simpson(wind_kt: int) -> int:
    """Map max sustained wind (knots) to Saffir-Simpson category."""
    if wind_kt < 64:
        return 0   # tropical storm or below
    elif wind_kt < 83:
        return 1
    elif wind_kt < 96:
        return 2
    elif wind_kt < 113:
        return 3
    elif wind_kt < 137:
        return 4
    else:
        return 5


def fetch_nhc_probabilities(storm_id: str) -> Optional[dict]:
    """
    Fetch NHC wind speed probability XML for a storm.
    Returns dict of {'landfall_any': float, 'cat3plus': float} or None.

    NHC provides probabilistic wind speed forecasts at:
    https://www.nhc.noaa.gov/text/refresh/{storm_id}prb/
    This parses the raw text advisory for key probability statements.
    """
    try:
        url = f"https://www.nhc.noaa.gov/text/refresh/{storm_id}prb/"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        text = r.text.lower()

        probs = {}

        # Look for patterns like "probability of tropical storm force winds...X PERCENT"
        m = re.search(r"(\d+)\s*percent\s*(?:chance|probability).*?landfall", text)
        if m:
            probs["landfall_any"] = int(m.group(1)) / 100

        m = re.search(r"(\d+)\s*percent.*?hurricane", text)
        if m:
            probs["landfall_hurricane"] = int(m.group(1)) / 100

        return probs if probs else None
    except Exception as e:
        log.debug("NHC probabilities for %s failed: %s", storm_id, e)
    return None


# ── intensity-based model ──────────────────────────────────────────────────────

def estimate_landfall_prob(storm: dict) -> float:
    """
    Simple heuristic based on:
    - Storm category (higher = more likely to be tracked/named)
    - Hemisphere/basin (Atlantic in season vs Pacific off-season)
    - Movement heading (from NHC headline)
    Returns a rough P(landfall) for a US coastline hit.
    """
    cat = storm.get("category", 0)
    headline = storm.get("headline", "").lower()
    lat = storm.get("lat", 0)
    lon = storm.get("lon", 0)

    base_prob = 0.3   # baseline for any named Atlantic storm

    # Category boost
    if cat >= 3:
        base_prob += 0.20
    elif cat >= 1:
        base_prob += 0.10

    # Geographic: if lat > 20N and lon between -100 and -60 → Gulf/Atlantic threat
    if 15 < lat < 40 and -100 < lon < -60:
        base_prob += 0.15

    # Headline keywords
    if any(kw in headline for kw in ["florida", "gulf coast", "gulf of mexico", "texas", "louisiana"]):
        base_prob += 0.20
    if "weakening" in headline or "dissipat" in headline:
        base_prob -= 0.15
    if "strengthening" in headline or "intensif" in headline:
        base_prob += 0.10

    return max(0.01, min(0.97, base_prob))


def estimate_cat_prob(storm: dict, target_cat: int) -> float:
    """Estimate P(storm reaches category target_cat) from current intensity."""
    current_cat = storm.get("category", 0)
    headline    = storm.get("headline", "").lower()

    if current_cat >= target_cat:
        return 0.80   # already there, likely to stay

    gap = target_cat - current_cat
    base = max(0.05, 0.55 - gap * 0.15)

    if "strengthening" in headline or "rapid intensif" in headline:
        base += 0.15
    if "weakening" in headline:
        base -= 0.20

    return max(0.02, min(0.95, base))


# ── market matching ────────────────────────────────────────────────────────────

def find_hurricane_markets(client: KalshiClient) -> list:
    markets = client.get_markets(limit=500)
    return [
        m for m in markets
        if any(m.get("ticker", "").startswith(p) for p in HURR_SERIES_PREFIXES)
        and m.get("status") == "open"
    ]


def match_storm_to_market(storm: dict, mkt: dict) -> Optional[str]:
    """
    Determine what the market is asking about this storm.
    Returns 'landfall', 'cat3', 'cat4', 'cat5', 'state:FL', etc. or None.
    """
    storm_name = storm.get("name", "").upper()
    ticker     = mkt.get("ticker", "").upper()
    title      = (mkt.get("title") or "").upper()

    if storm_name not in ticker and storm_name not in title:
        return None

    # Category markets
    m = re.search(r"CAT(\d)", ticker)
    if m:
        return f"cat{m.group(1)}"

    # Landfall market
    if "LAND" in ticker or "LANDFALL" in title:
        return "landfall"

    # State market
    state_match = re.search(r"(FL|TX|LA|NC|SC|GA|AL|MS|VA|MD)", ticker)
    if state_match:
        return f"state:{state_match.group(1)}"

    return "generic"


# ── main strategy entry ────────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    orders_placed = []

    active_storms = fetch_active_storms()
    if not active_storms:
        log.debug("Hurricane: no active storms from NHC")
        return []

    log.info("Hurricane: %d active storm(s)", len(active_storms))

    markets = find_hurricane_markets(client)
    if not markets:
        log.debug("Hurricane: no Kalshi storm markets found")
        return []

    for storm in active_storms:
        storm_id = storm.get("id", "")

        # Try to get NHC official probabilities; fall back to heuristic
        nhc_probs  = fetch_nhc_probabilities(storm_id) or {}
        landfall_p = nhc_probs.get("landfall_any") or estimate_landfall_prob(storm)

        for mkt in markets:
            ticker   = mkt["ticker"]
            ask_type = match_storm_to_market(storm, mkt)

            if ask_type is None:
                continue

            # Map market type to our probability estimate
            if ask_type == "landfall":
                our_prob = landfall_p
            elif ask_type.startswith("cat"):
                target = int(ask_type[3:])
                our_prob = estimate_cat_prob(storm, target)
                if target <= 3:
                    our_prob *= landfall_p   # must make landfall to count
            elif ask_type.startswith("state:"):
                # State-specific: ~30-40% of landfall prob is concentrated in one state
                our_prob = landfall_p * 0.35
            else:
                our_prob = landfall_p

            try:
                ob = client.get_orderbook(ticker, depth=1)
                yes_bids = ob.get("orderbook", {}).get("yes", [])
                if not yes_bids:
                    continue
                market_yes = yes_bids[0][0]
            except Exception as e:
                log.debug("Hurricane orderbook %s: %s", ticker, e)
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
                strategy="hurricane",
                ticker=ticker,
                side=side or "none",
                edge=edge,
                data={
                    "storm":      storm.get("name"),
                    "category":   storm.get("category"),
                    "ask_type":   ask_type,
                    "our_prob":   our_prob,
                    "market_yes": market_yes,
                },
            )

            if side and edge >= EDGE_THRESHOLD:
                log.info("HURR EDGE: %s %s ask=%s side=%s edge=%.1f%% | ours=%.2f mkt=%.2f",
                         ticker, storm.get("name"), ask_type, side, edge * 100,
                         our_prob, market_prob)
                if not dry_run:
                    try:
                        result = client.place_order(
                            ticker=ticker, side=side, action="buy",
                            count=ORDER_CONTRACTS, price=price, order_type="limit",
                        )
                        order_id = result.get("order", {}).get("order_id", "?")
                        log_trade(
                            strategy="hurricane", ticker=ticker, side=side,
                            price=price, count=ORDER_CONTRACTS,
                            order_id=order_id, status="placed", raw=result,
                        )
                        orders_placed.append(order_id)
                        log.info("Hurricane order placed: %s", order_id)
                    except Exception as e:
                        log.error("Hurricane order failed %s: %s", ticker, e)
                else:
                    tag = f"DRY:hurricane:{ticker}:{side}:{price}"
                    log.info("[DRY RUN] %s", tag)
                    orders_placed.append(tag)

    return orders_placed
