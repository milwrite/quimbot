"""
Kalshi runner — continuous high-frequency scanning across all strategies.

Risk controls (configured via .env):
  MAX_DAILY_TRADES     hard ceiling on orders per calendar day (default: 200)
  MAX_OPEN_POSITIONS   max concurrent open contracts (default: 50)
  MAX_DAILY_LOSS_CENTS maximum daily drawdown before halt (default: 5000 = $50)
  ORDER_CONTRACTS      contracts per order (default: 1 — small while dialing in)
  SCAN_INTERVAL_SEC    seconds between full scans (default: 60)

Schedule:
  All strategies run on every scan cycle.
  CPI is gated internally to the 8:00–8:30 AM ET window on release days
  (override with FORCE_CPI_RUN=1).

Usage:
  python runner.py               # live continuous mode
  python runner.py --dry-run     # signals only, no real orders
  python runner.py --now         # single scan pass then exit
  python runner.py --strategy weather --now
  python runner.py --strategy cpi --now --force-cpi
  python runner.py --status      # print today's P&L + open positions

Strategies: weather + CPI only.
Fed and NBA strategies exist as files but are not loaded by this runner.
"""

import os
import sys
import json
import time
import logging
import argparse
import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

from core.client import KalshiClient
from core import log_signal, log_trade, log_close, manage_positions
import strategies.weather as weather_strat
import strategies.cpi as cpi_strat

# ── logging setup ──────────────────────────────────────────────────────────────
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/runner.log"),
    ],
)
log = logging.getLogger("kalshi.runner")

ET = ZoneInfo("America/New_York")

# ── risk config ───────────────────────────────────────────────────────────────
MAX_DAILY_TRADES    = int(os.getenv("MAX_DAILY_TRADES",      "200"))
MAX_OPEN_POSITIONS  = int(os.getenv("MAX_OPEN_POSITIONS",    "50"))
MAX_DAILY_LOSS_C    = int(os.getenv("MAX_DAILY_LOSS_CENTS",  "5000"))  # $50
SCAN_INTERVAL       = int(os.getenv("SCAN_INTERVAL_SEC",     "60"))

ALL_STRATEGIES      = ["weather", "cpi"]


# ── state helpers ─────────────────────────────────────────────────────────────

def _today() -> str:
    return datetime.date.today().isoformat()


def _read_trades_today() -> list:
    path = Path("logs/trades.jsonl")
    if not path.exists():
        return []
    today = _today()
    out = []
    with open(path) as f:
        for line in f:
            try:
                rec = json.loads(line)
                if rec.get("ts", "").startswith(today):
                    out.append(rec)
            except Exception:
                pass
    return out


def trades_placed_today() -> int:
    return sum(1 for r in _read_trades_today() if r.get("status") == "placed")


def daily_pnl_cents() -> int:
    """Rough P&L from today's closed trades. Negative = loss."""
    total = 0
    for r in _read_trades_today():
        if r.get("event") == "close" and r.get("pnl_c") is not None:
            total += int(r["pnl_c"])
    return total


def open_positions(client: KalshiClient) -> list:
    try:
        return client.get_positions()
    except Exception as e:
        log.warning("Could not fetch positions: %s", e)
        return []


# ── risk gate ─────────────────────────────────────────────────────────────────

def risk_ok(client: KalshiClient) -> bool:
    """Return False and log reason if any risk limit is breached."""
    placed = trades_placed_today()
    if placed >= MAX_DAILY_TRADES:
        log.warning("RISK HALT: daily trade limit %d reached", MAX_DAILY_TRADES)
        return False

    pnl = daily_pnl_cents()
    if pnl <= -MAX_DAILY_LOSS_C:
        log.warning("RISK HALT: daily loss limit hit (%.2f)", pnl / 100)
        return False

    positions = open_positions(client)
    total_open = sum(abs(p.get("position", 0)) for p in positions)
    if total_open >= MAX_OPEN_POSITIONS:
        log.warning("RISK HALT: open position limit %d reached (%d open)",
                    MAX_OPEN_POSITIONS, total_open)
        return False

    return True


# ── single scan pass ──────────────────────────────────────────────────────────

def run_scan(strategies: list, client: KalshiClient, dry_run: bool) -> int:
    """Run one full pass of the given strategies. Returns total orders placed."""
    total = 0

    for strat_name in strategies:
        if not dry_run and not risk_ok(client):
            break

        log.debug("Scanning: %s", strat_name)
        try:
            if strat_name == "weather":
                orders = weather_strat.run(client, dry_run=dry_run)
            elif strat_name == "cpi":
                orders = cpi_strat.run(client, dry_run=dry_run)
            else:
                log.warning("Unknown strategy: %s", strat_name)
                orders = []

            if orders:
                log.info("%s: %d order(s) placed this scan: %s",
                         strat_name, len(orders), orders)
            total += len(orders)

        except Exception as e:
            log.error("Strategy %s error: %s", strat_name, e, exc_info=True)

    return total


# ── status report ─────────────────────────────────────────────────────────────

def print_status(client: KalshiClient):
    placed = trades_placed_today()
    pnl    = daily_pnl_cents()
    try:
        bal = client.get_balance()
    except Exception:
        bal = {}

    positions = open_positions(client)
    open_count = sum(abs(p.get("position", 0)) for p in positions)

    print(f"\n{'='*50}")
    print(f"  Kalshi Bot Status — {_today()}")
    print(f"{'='*50}")
    print(f"  Trades today:    {placed} / {MAX_DAILY_TRADES}")
    print(f"  Open contracts:  {open_count} / {MAX_OPEN_POSITIONS}")
    print(f"  Realized P&L:    ${pnl/100:+.2f} (limit: -${MAX_DAILY_LOSS_C/100:.2f})")
    print(f"  Balance:         {bal}")
    print(f"{'='*50}\n")


# ── main loops ────────────────────────────────────────────────────────────────

def continuous_loop(strategies: list, client: KalshiClient, dry_run: bool):
    log.info(
        "Starting continuous scan (dry=%s, interval=%ds, max_trades=%d, "
        "max_open=%d, max_loss=$%.2f)",
        dry_run, SCAN_INTERVAL, MAX_DAILY_TRADES,
        MAX_OPEN_POSITIONS, MAX_DAILY_LOSS_C / 100,
    )

    scan_count  = 0
    total_today = 0
    last_day    = _today()

    while True:
        today = _today()
        if today != last_day:
            log.info("New day %s — counters reset", today)
            total_today = 0
            last_day = today

        scan_count += 1
        log.debug("Scan #%d | trades today: %d", scan_count, trades_placed_today())

        # Manage open positions every scan (take-profit / stop-loss / expiry)
        try:
            manage_positions(client, dry_run=dry_run)
        except Exception as e:
            log.error("Position manager error: %s", e)

        placed = run_scan(strategies, client, dry_run)
        total_today += placed

        if scan_count % 10 == 0:
            log.info("Heartbeat | scan #%d | trades today: %d | P&L: $%.2f",
                     scan_count, trades_placed_today(), daily_pnl_cents() / 100)

        time.sleep(SCAN_INTERVAL)


def main():
    parser = argparse.ArgumentParser(description="Kalshi strategy runner")
    parser.add_argument("--dry-run",   action="store_true",
                        help="signals only, no real orders")
    parser.add_argument("--now",       action="store_true",
                        help="single scan pass then exit")
    parser.add_argument("--strategy",  default=None,
                        help="limit to one strategy: weather|cpi")
    parser.add_argument("--force-cpi", action="store_true",
                        help="ignore CPI timing gate")
    parser.add_argument("--status",    action="store_true",
                        help="print today's status and exit")
    args = parser.parse_args()

    if args.force_cpi:
        os.environ["FORCE_CPI_RUN"] = "1"

    strats = [args.strategy] if args.strategy else ALL_STRATEGIES
    client = KalshiClient()

    # Connectivity check
    try:
        bal = client.get_balance()
        log.info("Connected. Balance: %s", bal)
    except Exception as e:
        log.warning("Balance check failed (expected without creds): %s", e)

    if args.status:
        print_status(client)
        return

    if args.now:
        run_scan(strats, client, dry_run=args.dry_run)
    else:
        continuous_loop(strats, client, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
