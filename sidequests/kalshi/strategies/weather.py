"""
Weather strategy — HRRR model + live NWS station obs vs Kalshi "high temp > X°F" markets.

Signal pipeline per city:
  1. HRRR hourly forecast (via Open-Meteo, model=hrrr_conus, updates every ~1h)
  2. Live station observation (NWS observations/latest, actual current temp)
  3. Blended probability: obs-informed true_prob that tightens as the day progresses
  4. Compare to Kalshi orderbook YES price
  5. Place maker YES or NO order if edge > threshold

Data sources (all free, no key):
  Open-Meteo HRRR: https://api.open-meteo.com/v1/forecast?models=hrrr_conus
  NWS station obs:  https://api.weather.gov/stations/{STATION}/observations/latest
  NWS gridpoint:    https://api.weather.gov/points/{lat},{lon}  (forecast fallback)
"""

import os
import math
import requests
import logging
from datetime import date, datetime, timezone, timedelta
from typing import Optional

from core.client import KalshiClient
from core.logger import log_signal, log_trade

log = logging.getLogger("kalshi.weather")

# ── config ─────────────────────────────────────────────────────────────────────
EDGE_THRESHOLD  = float(os.getenv("WEATHER_EDGE_THRESHOLD", "0.06"))   # 6%
ORDER_CONTRACTS = int(os.getenv("ORDER_CONTRACTS", "1"))
KALSHI_FEE      = 0.01

# Cities: lat/lon for HRRR model pull, ICAO station for live obs,
# Kalshi series prefix (confirm against live /markets endpoint before trading).
CITIES = [
    {"name": "NYC",     "lat": 40.7128, "lon": -74.0060,  "station": "KNYC",  "series": "KXHIGHNY"},
    {"name": "CHI",     "lat": 41.8781, "lon": -87.6298,  "station": "KORD",  "series": "KXHIGHCHI"},
    {"name": "LA",      "lat": 33.9425, "lon": -118.4081, "station": "KLAX",  "series": "KXHIGHLAX"},
    {"name": "MIA",     "lat": 25.7959, "lon": -80.2870,  "station": "KMIA",  "series": "KXHIGHMIA"},   # Miami
    {"name": "DAL",     "lat": 32.8998, "lon": -97.0403,  "station": "KDFW",  "series": "KXHIGHTDAL"},  # Dallas
    {"name": "ATL",     "lat": 33.6407, "lon": -84.4277,  "station": "KATL",  "series": "KXHIGHTATL"},  # Atlanta
    {"name": "HOU",     "lat": 29.9902, "lon": -95.3368,  "station": "KIAH",  "series": "KXHIGHTHOU"},  # Houston
    {"name": "PHX",     "lat": 33.4373, "lon": -112.0078, "station": "KPHX",  "series": "KXHIGHTPHX"},  # Phoenix
    {"name": "SEA",     "lat": 47.4502, "lon": -122.3088, "station": "KSEA",  "series": "KXHIGHTSEA"},  # Seattle
    {"name": "BOS",     "lat": 42.3656, "lon": -71.0096,  "station": "KBOS",  "series": "KXHIGHTBOS"},  # Boston
]

_NWS_HEADERS = {"User-Agent": "kalshi-weather-bot/2.0 (contact@example.com)"}


# ── HRRR forecast (Open-Meteo, hourly updates) ─────────────────────────────────

def fetch_hrrr_high(lat: float, lon: float) -> Optional[float]:
    """Return today's forecast high in °F from HRRR via Open-Meteo."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":         lat,
        "longitude":        lon,
        "hourly":           "temperature_2m",
        "temperature_unit": "fahrenheit",
        "forecast_days":    1,
        "timezone":         "auto",
        "models":           "hrrr_conus",   # hourly-updating HRRR model
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        temps = r.json().get("hourly", {}).get("temperature_2m", [])
        return max(temps) if temps else None
    except Exception as e:
        log.warning("HRRR fetch failed (%.4f, %.4f): %s", lat, lon, e)
        return None


def fetch_nws_gridpoint_high(lat: float, lon: float) -> Optional[float]:
    """Fallback: NWS gridpoint hourly forecast max temp for today."""
    try:
        pt = requests.get(
            f"https://api.weather.gov/points/{lat},{lon}",
            headers=_NWS_HEADERS, timeout=10
        ).json()
        forecast_url = pt["properties"]["forecastHourly"]
        periods = requests.get(forecast_url, headers=_NWS_HEADERS, timeout=10).json()
        periods = periods["properties"]["periods"]
        today = date.today().isoformat()
        temps = [
            p["temperature"] for p in periods
            if p["startTime"].startswith(today) and p["temperatureUnit"] == "F"
        ]
        return max(temps) if temps else None
    except Exception as e:
        log.warning("NWS gridpoint fallback failed: %s", e)
        return None


def get_forecast_high(lat: float, lon: float) -> Optional[float]:
    """HRRR preferred, NWS gridpoint fallback."""
    t = fetch_hrrr_high(lat, lon)
    if t is None:
        log.info("HRRR unavailable, falling back to NWS gridpoint")
        t = fetch_nws_gridpoint_high(lat, lon)
    return t


# ── Live station observations ──────────────────────────────────────────────────

def fetch_station_obs(station: str) -> Optional[dict]:
    """
    Fetch the latest observation from an NWS ICAO station.
    Returns dict with 'temp_f' (float) and 'obs_time' (datetime) or None.
    """
    try:
        url = f"https://api.weather.gov/stations/{station}/observations/latest"
        r = requests.get(url, headers=_NWS_HEADERS, timeout=10)
        r.raise_for_status()
        props = r.json().get("properties", {})
        temp_c = props.get("temperature", {}).get("value")
        obs_time_str = props.get("timestamp")
        if temp_c is None or obs_time_str is None:
            return None
        temp_f = temp_c * 9 / 5 + 32
        obs_time = datetime.fromisoformat(obs_time_str.replace("Z", "+00:00"))
        return {"temp_f": temp_f, "obs_time": obs_time}
    except Exception as e:
        log.warning("Station obs fetch failed (%s): %s", station, e)
        return None


# ── Blended probability model ──────────────────────────────────────────────────

def hours_until_market_close() -> float:
    """
    Rough estimate of hours left in the trading day for weather contracts.
    Kalshi high-temp contracts typically resolve at end of day (local midnight).
    Uses UTC with an 18h offset as a conservative end-of-day proxy.
    """
    now_utc = datetime.now(timezone.utc)
    eod_utc = now_utc.replace(hour=23, minute=59, second=0, microsecond=0)
    delta = (eod_utc - now_utc).total_seconds() / 3600
    return max(0.0, delta)


def compute_edge(
    forecast: float,
    threshold: int,
    market_yes_price: int,
    obs: Optional[dict] = None,
) -> tuple:
    """
    Returns (side, edge_fraction).

    Signal blending:
    - Base probability from HRRR forecast vs threshold distance
    - If live obs available: weight obs-informed bound more heavily as
      the day progresses (obs matters more when close to resolution)
    - edge = |true_prob - market_prob| - fee_drag

    Obs logic: if current temp is already above threshold, YES probability
    gets a strong boost; if already far below, NO probability gets a boost.
    The weight of obs increases as hours_until_close decreases.
    """
    hours_left = hours_until_market_close()

    # Base true_prob from HRRR forecast distance to threshold
    diff = forecast - threshold
    if diff >= 5:
        base_prob = 0.93
    elif diff >= 3:
        base_prob = 0.82
    elif diff >= 1:
        base_prob = 0.65
    elif diff <= -5:
        base_prob = 0.07
    elif diff <= -3:
        base_prob = 0.18
    elif diff <= -1:
        base_prob = 0.35
    else:
        base_prob = 0.50

    true_prob = base_prob

    # Blend in live obs if available
    if obs is not None:
        current_temp = obs["temp_f"]
        obs_age_h = (datetime.now(timezone.utc) - obs["obs_time"]).total_seconds() / 3600

        if obs_age_h < 2:  # only trust obs less than 2 hours old
            # How far is current obs from threshold?
            obs_diff = current_temp - threshold

            # Obs-informed probability (similar step function)
            if obs_diff >= 3:
                obs_prob = 0.95   # already near threshold, trending up
            elif obs_diff >= 0:
                obs_prob = 0.80   # at or above, still hours to go
            elif obs_diff >= -3:
                obs_prob = 0.55   # slightly below but reachable
            elif obs_diff >= -6:
                obs_prob = 0.30
            else:
                obs_prob = 0.08   # well below, very unlikely to reach

            # Weight obs more heavily closer to market close
            # At 12h out: obs_weight = 0.2; at 2h out: obs_weight = 0.7
            obs_weight = max(0.1, min(0.75, 1.0 - (hours_left / 14)))
            true_prob = (1 - obs_weight) * base_prob + obs_weight * obs_prob

            log.debug(
                "Blended prob: base=%.2f obs=%.2f weight=%.2f → true=%.2f "
                "(obs_temp=%.1f°F, hours_left=%.1f)",
                base_prob, obs_prob, obs_weight, true_prob, current_temp, hours_left
            )

    market_prob = market_yes_price / 100
    edge_yes = true_prob - market_prob - KALSHI_FEE
    edge_no  = (1 - true_prob) - (1 - market_prob) - KALSHI_FEE

    if edge_yes > edge_no and edge_yes > 0:
        return "yes", edge_yes
    elif edge_no > 0:
        return "no", edge_no
    else:
        return None, max(edge_yes, edge_no)


# ── Market matching ────────────────────────────────────────────────────────────

def find_weather_markets(client: KalshiClient, series: str) -> list:
    """Return open Kalshi markets for the given series (uses series_ticker API param)."""
    resp = client._get("/markets", {"series_ticker": series, "limit": 100, "status": "open"})
    return resp.get("markets", []) if isinstance(resp, dict) else []


def parse_threshold(ticker: str, series: str) -> Optional[int]:
    """
    Extract numeric threshold from ticker.
    Live format: KXHIGHNY-26MAR19-T50 → 50  (T = above/below threshold)
                 KXHIGHNY-26MAR19-B49.5 → None (B = between, skip)
    """
    try:
        parts = ticker.split("-")
        for part in reversed(parts):
            if part.startswith("T") and part[1:].replace(".", "").isdigit():
                return int(float(part[1:]))
        return None  # B (between) markets or unrecognised format
    except Exception:
        return None


# ── Main strategy entry ────────────────────────────────────────────────────────

def run(client: KalshiClient, dry_run: bool = False) -> list:
    """
    Scan all configured cities, pull HRRR forecast + live obs, log signals,
    place orders where edge > threshold.
    """
    orders_placed = []

    for city in CITIES:
        log.info("--- %s ---", city["name"])

        # HRRR forecast high
        forecast = get_forecast_high(city["lat"], city["lon"])
        if forecast is None:
            log.warning("%s: no forecast available, skipping", city["name"])
            continue
        log.info("%s HRRR forecast high: %.1f°F", city["name"], forecast)

        # Live station obs
        obs = fetch_station_obs(city["station"])
        if obs:
            age_min = (datetime.now(timezone.utc) - obs["obs_time"]).total_seconds() / 60
            log.info("%s live obs: %.1f°F (%.0f min ago)", city["name"], obs["temp_f"], age_min)
        else:
            log.info("%s: no live obs available", city["name"])

        # Scan matching Kalshi markets
        markets = find_weather_markets(client, city["series"])
        if not markets:
            log.info("%s: no open markets found for series %s", city["name"], city["series"])

        for mkt in markets:
            ticker = mkt["ticker"]
            threshold = parse_threshold(ticker, city["series"])
            if threshold is None:
                log.debug("Could not parse threshold from %s", ticker)
                continue

            # Get current best YES price from orderbook
            try:
                ob = client.get_orderbook(ticker, depth=1)
                yes_bids = ob.get("orderbook", {}).get("yes", [])
                if not yes_bids:
                    log.debug("%s: empty orderbook", ticker)
                    continue
                market_yes_price = yes_bids[0][0]
            except Exception as e:
                log.warning("Orderbook fetch failed %s: %s", ticker, e)
                continue

            side, edge = compute_edge(forecast, threshold, market_yes_price, obs)

            log_signal(
                strategy="weather",
                ticker=ticker,
                side=side or "none",
                edge=edge,
                data={
                    "city":        city["name"],
                    "forecast":    forecast,
                    "threshold":   threshold,
                    "market_yes":  market_yes_price,
                    "obs_temp":    obs["temp_f"] if obs else None,
                    "obs_age_min": round((datetime.now(timezone.utc) - obs["obs_time"]).total_seconds() / 60) if obs else None,
                    "hours_left":  round(hours_until_market_close(), 1),
                },
            )

            if side and edge >= EDGE_THRESHOLD:
                price = market_yes_price if side == "yes" else (100 - market_yes_price)
                log.info(
                    "EDGE %-6s side=%-3s edge=%+.1f%% price=%dc obs=%s",
                    ticker, side, edge * 100, price,
                    f"{obs['temp_f']:.1f}°F" if obs else "none"
                )

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
                            strategy="weather",
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
