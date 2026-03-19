"""
analyze.py — Bet record keeper + methodology reviewer.

Does three things:
  1. Builds/updates ledger.jsonl — enriched trade record with logic snapshot
  2. Fetches resolved positions from Kalshi and records outcomes
  3. Runs methodology analysis: per-strategy edge accuracy, calibration,
     and generates actionable improvements as patches to .env thresholds

Run:
  python analyze.py               # update ledger + print summary
  python analyze.py --patch       # also write threshold patches to .env
  python analyze.py --report      # full markdown report to logs/reports/
  python analyze.py --discord     # post summary to Discord

Cron: every 6 hours (see crontab).
"""

import os
import sys
import json
import re
import logging
import argparse
import datetime
import subprocess
from pathlib import Path
from collections import defaultdict
from statistics import mean, stdev

# ── setup ─────────────────────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
from dotenv import load_dotenv
load_dotenv(Path.home() / "kalshi" / ".env")
load_dotenv(Path(__file__).parent / ".env")

from core.client import KalshiClient
from core.auth import get_base_url

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
log = logging.getLogger("kalshi.analyze")

KALSHI_FEE = 0.01
DISCORD_CHANNEL = "1483986889328562307"

# ── file paths ────────────────────────────────────────────────────────────────
LOGS_DIR    = Path(__file__).parent / "logs"
TRADES_FILE = LOGS_DIR / "trades.jsonl"
SIGNALS_FILE= LOGS_DIR / "signals.jsonl"
LEDGER_FILE = LOGS_DIR / "ledger.jsonl"
REPORTS_DIR = LOGS_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# ── strategy methodology registry ─────────────────────────────────────────────
# Codified logic for each strategy so we can compare outcome vs expectation
METHODOLOGY = {
    "weather": {
        "description": "NWS forecast high vs Kalshi temperature threshold markets",
        "data_sources": ["NWS gridpoint forecast (fallback from HRRR)", "NWS station observations"],
        "model": "Step function on (forecast - threshold) distance; obs blended by time-to-close weight",
        "edge_threshold_env": "WEATHER_EDGE_THRESHOLD",
        "default_threshold": 0.06,
        "expected_calibration": "forecast within 3°F of actual ~70% of time; edge>8% should win ~80%",
        "known_weaknesses": [
            "HRRR returning 400s — using NWS gridpoint only (less accurate for afternoon highs)",
            "Obs weight model untested — may overweight stale obs",
            "B-bracket markets use same Gaussian as threshold — may underestimate tails",
        ],
        "improvement_candidates": [
            "Integrate Open-Meteo without HRRR model param for better forecast",
            "Calibrate obs_weight curve against historical data",
            "Add persistence check: if obs already above threshold, boost YES prob",
        ],
    },
    "fed": {
        "description": "Monotonicity arb across Kalshi Fed rate ladder markets",
        "data_sources": ["Kalshi orderbook only (pure internal arb)"],
        "model": "P(rate>higher) must be <= P(rate>lower); gap>threshold = edge",
        "edge_threshold_env": "FED_EDGE_THRESHOLD",
        "default_threshold": 0.08,
        "expected_calibration": "Cross-date gaps may reflect genuine term structure differences, not mispricing",
        "known_weaknesses": [
            "Gap detection compares different meeting dates — most 'violations' are cross-date",
            "True monotonicity arb only valid within same meeting date",
            "Low liquidity on far-dated contracts — limit orders may not fill",
        ],
        "improvement_candidates": [
            "Filter to same-meeting-date comparisons only",
            "Add CME FedWatch probability as external calibration",
            "Weight edge by liquidity depth (only trade when 2+ contracts available)",
        ],
    },
    "shortterm": {
        "description": "Short-dated (<7d) weather bracket + econ ladder gaps",
        "data_sources": ["NWS observations as forecast proxy", "Kalshi orderbook for ladder gaps"],
        "model": "Gaussian bracket probability + ladder gap detection on short-dated contracts",
        "edge_threshold_env": "SHORTTERM_EDGE_THRESHOLD",
        "default_threshold": 0.08,
        "expected_calibration": "Using current obs temp as forecast — crude but fast to resolve",
        "known_weaknesses": [
            "Uses current obs as forecast rather than tomorrow's forecast high",
            "Gaussian std (5°F) not calibrated to actual forecast error distribution",
            "May double-count positions already placed by weather strategy",
        ],
        "improvement_candidates": [
            "Use NWS point forecast high instead of current obs",
            "Calibrate std from historical NWS forecast vs actual data",
            "Add dedup check against existing open positions before placing",
        ],
    },
    "mlb_gdp": {
        "description": "MLB season win totals vs FanGraphs projections; GDP ladder gaps",
        "data_sources": ["FanGraphs win projections (hardcoded estimates)", "Kalshi orderbook"],
        "model": "Gaussian with mu=proj_wins, sigma=7 wins; GDP ladder monotonicity",
        "edge_threshold_env": None,
        "default_threshold": 0.08,
        "expected_calibration": "Season-long bets; high variance. Edge should compound across multiple teams.",
        "known_weaknesses": [
            "Projections are hardcoded estimates — not live FanGraphs data",
            "7-win sigma is a guess — actual MLB outcome variance may differ",
            "These bets close in October 2026 — long hold time",
        ],
        "improvement_candidates": [
            "Scrape live FanGraphs depth chart projections or use Baseball Reference",
            "Calibrate sigma from past season win total prediction accuracy",
            "Add injury adjustment: if star player hurt, reduce projection",
        ],
    },
    "cpi": {
        "description": "Cleveland Fed nowcast vs Kalshi CPI release contracts",
        "data_sources": ["BLS API (trailing MoM)", "Cleveland Fed Inflation Nowcast"],
        "model": "Step function on (estimate - threshold) diff",
        "edge_threshold_env": "CPI_EDGE_THRESHOLD",
        "default_threshold": 0.07,
        "expected_calibration": "Gate to 8:00-8:30 AM ET on release days; not yet tested on a live release",
        "known_weaknesses": ["No live releases yet — strategy untested"],
        "improvement_candidates": ["Confirm CPI ticker format on next release day"],
    },
}


# ── ledger enrichment ─────────────────────────────────────────────────────────

def load_jsonl(path: Path) -> list:
    if not path.exists():
        return []
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
    return out


def build_ledger(client: KalshiClient) -> list:
    """
    Merge trades.jsonl with live position/order status from Kalshi.
    Each ledger entry: trade record + outcome fields.
    """
    trades = load_jsonl(TRADES_FILE)
    existing_ledger = {r["order_id"]: r for r in load_jsonl(LEDGER_FILE)}

    # Fetch all orders from Kalshi for status updates
    try:
        all_orders = client.get_orders()
        order_map = {o["order_id"]: o for o in all_orders}
    except Exception as e:
        log.warning("Could not fetch orders: %s", e)
        order_map = {}

    # Fetch settled positions for P&L
    try:
        positions = client.get_positions()
        pos_map = {p["ticker"]: p for p in positions}
    except Exception as e:
        log.warning("Could not fetch positions: %s", e)
        pos_map = {}

    ledger = []
    for t in trades:
        oid = t.get("order_id", "")
        entry = existing_ledger.get(oid, {}).copy()

        # Base fields from trade log
        entry.update({
            "order_id":   oid,
            "ticker":     t.get("ticker"),
            "strategy":   t.get("strategy"),
            "side":       t.get("side"),
            "price_c":    t.get("price_c"),
            "count":      t.get("count", 1),
            "placed_ts":  t.get("ts"),
        })

        # Methodology snapshot
        strat = t.get("strategy", "")
        entry["methodology"] = METHODOLOGY.get(strat, {}).get("description", "unknown")
        entry["model_summary"] = METHODOLOGY.get(strat, {}).get("model", "")

        # Live order status from Kalshi
        live = order_map.get(oid, {})
        if live:
            entry["kalshi_status"] = live.get("status")
            entry["fill_count"]    = float(live.get("fill_count_fp", 0) or 0)
            entry["remaining"]     = float(live.get("remaining_count_fp", 0) or 0)
            entry["maker_fees"]    = live.get("maker_fees_dollars")
            entry["taker_fees"]    = live.get("taker_fees_dollars")
        else:
            # Try from raw trade record
            raw_order = t.get("raw", {}).get("order", {})
            entry["kalshi_status"] = raw_order.get("status")
            entry["fill_count"]    = float(raw_order.get("fill_count_fp", 0) or 0)
            entry["remaining"]     = float(raw_order.get("remaining_count_fp", 0) or 0)

        # Position data (for resolved markets)
        pos = pos_map.get(t.get("ticker", ""))
        if pos:
            entry["position"]          = pos.get("position")
            entry["market_exposure"]   = pos.get("market_exposure")
            entry["realized_pnl"]      = pos.get("realized_pnl")
            entry["unrealized_pnl"]    = pos.get("unrealized_pnl")
            entry["current_price"]     = pos.get("last_price")

        ledger.append(entry)

    # Write updated ledger
    with open(LEDGER_FILE, "w") as f:
        for entry in ledger:
            f.write(json.dumps(entry) + "\n")

    log.info("Ledger updated: %d entries", len(ledger))
    return ledger


# ── analysis ──────────────────────────────────────────────────────────────────

def analyze(ledger: list) -> dict:
    """Run per-strategy analysis against methodology."""
    by_strategy = defaultdict(list)
    for entry in ledger:
        by_strategy[entry.get("strategy", "unknown")].append(entry)

    results = {}
    for strat, entries in by_strategy.items():
        total    = len(entries)
        filled   = [e for e in entries if float(e.get("fill_count", 0) or 0) > 0]
        resting  = [e for e in entries if e.get("kalshi_status") == "resting"]
        resolved = [e for e in entries if e.get("realized_pnl") is not None]
        won      = [e for e in resolved if float(e.get("realized_pnl", 0) or 0) > 0]

        # Avg entry price
        prices = [e["price_c"] for e in entries if e.get("price_c")]
        avg_price = mean(prices) if prices else None

        # Total deployed (cents)
        deployed_c = sum(e.get("price_c", 0) * e.get("count", 1)
                         for e in filled)

        # Realized P&L
        realized = sum(float(e.get("realized_pnl", 0) or 0) for e in resolved)

        # Calibration: expected win rate from avg price
        # If avg_price is the cost of a NO contract at 80c, we expect to win 80% of the time
        # For YES at 40c, we expect 40% win rate — check against methodology edge claim
        methodology = METHODOLOGY.get(strat, {})
        edge_env    = methodology.get("edge_threshold_env") or ""
        live_threshold = float(os.getenv(edge_env, str(methodology.get("default_threshold", 0.06))) if edge_env else str(methodology.get("default_threshold", 0.06)))

        results[strat] = {
            "total_orders":         total,
            "filled":               len(filled),
            "resting":              len(resting),
            "resolved":             len(resolved),
            "won":                  len(won),
            "win_rate":             len(won) / len(resolved) if resolved else None,
            "avg_entry_price_c":    round(avg_price, 1) if avg_price else None,
            "deployed_dollars":     round(deployed_c / 100, 2),
            "realized_pnl_dollars": round(realized / 100, 2),
            "edge_threshold":       live_threshold,
            "methodology":          methodology.get("description", ""),
            "weaknesses":           methodology.get("known_weaknesses", []),
            "improvements":         methodology.get("improvement_candidates", []),
        }

    return results


def generate_improvements(results: dict) -> list:
    """
    Produce concrete improvement suggestions based on actual results vs methodology.
    Returns list of (strategy, suggestion, severity) tuples.
    """
    improvements = []

    for strat, r in results.items():
        meth = METHODOLOGY.get(strat, {})

        # Check: if many resting orders → liquidity problem
        if r["resting"] > r["filled"] and r["total_orders"] > 3:
            improvements.append((
                strat,
                f"{r['resting']} of {r['total_orders']} orders still resting — "
                "consider reducing limit price aggressiveness or skipping illiquid contracts",
                "medium"
            ))

        # Check: win rate below implied probability
        if r["win_rate"] is not None and r["avg_entry_price_c"]:
            implied = r["avg_entry_price_c"] / 100
            actual  = r["win_rate"]
            if actual < implied - 0.15:
                improvements.append((
                    strat,
                    f"Win rate {actual:.0%} below implied {implied:.0%} — "
                    "edge model may be overconfident; raise {meth.get('edge_threshold_env','threshold')} by 2%",
                    "high"
                ))
            elif actual > implied + 0.15:
                improvements.append((
                    strat,
                    f"Win rate {actual:.0%} above implied {implied:.0%} — "
                    "edge model may be conservative; could lower threshold or increase size",
                    "low"
                ))

        # Add methodology-coded improvements
        for imp in meth.get("improvement_candidates", [])[:2]:
            improvements.append((strat, imp, "planned"))

    return improvements


def format_report(results: dict, improvements: list) -> str:
    """Generate a markdown report."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M ET")
    lines = [
        f"# Kalshi Bet Ledger — {now}",
        "",
        "## Portfolio Summary",
    ]

    total_deployed = sum(r["deployed_dollars"] for r in results.values())
    total_realized = sum(r["realized_pnl_dollars"] for r in results.values())
    total_orders   = sum(r["total_orders"] for r in results.values())
    total_filled   = sum(r["filled"] for r in results.values())
    total_resting  = sum(r["resting"] for r in results.values())

    lines += [
        f"- Total orders: {total_orders} ({total_filled} filled, {total_resting} resting)",
        f"- Total deployed: ${total_deployed:.2f}",
        f"- Realized P&L: ${total_realized:+.2f}",
        "",
        "## Per-Strategy Results",
        "",
    ]

    for strat, r in sorted(results.items()):
        wr = f"{r['win_rate']:.0%}" if r["win_rate"] is not None else "pending"
        lines += [
            f"### {strat}",
            f"**Methodology:** {r['methodology']}",
            f"- Orders: {r['total_orders']} | Filled: {r['filled']} | Resting: {r['resting']}",
            f"- Resolved: {r['resolved']} | Won: {r['won']} | Win rate: {wr}",
            f"- Avg entry: {r['avg_entry_price_c']}c | Deployed: ${r['deployed_dollars']:.2f} | P&L: ${r['realized_pnl_dollars']:+.2f}",
            f"- Edge threshold: {r['edge_threshold']:.0%}",
            "",
            "**Weaknesses:**",
        ]
        for w in r["weaknesses"]:
            lines.append(f"  - {w}")
        lines += ["", "**Improvement candidates:**"]
        for imp in r["improvements"]:
            lines.append(f"  - {imp}")
        lines.append("")

    lines += ["## Action Items", ""]
    for strat, suggestion, severity in improvements:
        emoji = {"high": "🔴", "medium": "🟡", "low": "🟢", "planned": "📋"}.get(severity, "•")
        lines.append(f"{emoji} **[{strat}]** {suggestion}")

    return "\n".join(lines)


def patch_env(results: dict) -> list:
    """
    Update .env thresholds based on performance data.
    Returns list of changes made.
    """
    env_path = Path(__file__).parent / ".env"
    changes = []

    for strat, r in results.items():
        meth = METHODOLOGY.get(strat, {})
        env_key = meth.get("edge_threshold_env")
        if not env_key or r["win_rate"] is None:
            continue

        implied = (r["avg_entry_price_c"] or 50) / 100
        actual  = r["win_rate"]

        if actual < implied - 0.15 and r["resolved"] >= 5:
            # Losing more than expected — raise bar
            old = r["edge_threshold"]
            new = min(old + 0.02, 0.20)
            changes.append((env_key, old, new, f"win rate {actual:.0%} < implied {implied:.0%}"))

    if changes:
        # Read current .env
        env_content = env_path.read_text() if env_path.exists() else ""
        for key, old, new, reason in changes:
            old_line = f"{key}={old}"
            new_line = f"{key}={new}"
            if old_line in env_content:
                env_content = env_content.replace(old_line, new_line)
            else:
                env_content += f"\n{key}={new}   # auto-patched: {reason}\n"
        env_path.write_text(env_content)
        log.info("Patched .env: %s", changes)

    return changes


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--patch",   action="store_true", help="auto-patch .env thresholds")
    parser.add_argument("--report",  action="store_true", help="write full markdown report")
    parser.add_argument("--discord", action="store_true", help="post summary to Discord")
    args = parser.parse_args()

    client = KalshiClient(base_url=get_base_url())

    # 1. Build / update ledger
    ledger = build_ledger(client)

    # 2. Analyse
    results = analyze(ledger)
    improvements = generate_improvements(results)

    # 3. Report
    report = format_report(results, improvements)

    if args.report:
        today = datetime.date.today().isoformat()
        report_path = REPORTS_DIR / f"report-{today}.md"
        report_path.write_text(report)
        log.info("Report written: %s", report_path)
        print(report)
    else:
        # Print compact summary
        print(f"\n{'='*60}")
        print(f"  Kalshi Analysis — {datetime.datetime.now():%Y-%m-%d %H:%M}")
        print(f"{'='*60}")
        for strat, r in sorted(results.items()):
            wr = f"{r['win_rate']:.0%}" if r["win_rate"] is not None else "pending"
            print(f"  {strat:<15} {r['total_orders']:>3} orders | "
                  f"${r['deployed_dollars']:>6.2f} deployed | "
                  f"P&L ${r['realized_pnl_dollars']:>+6.2f} | "
                  f"win {wr}")
        print(f"{'='*60}")
        print(f"\nTop action items:")
        for strat, suggestion, severity in improvements[:5]:
            print(f"  [{severity.upper():<8}] {strat}: {suggestion[:70]}")

    # 4. Patch thresholds if requested
    if args.patch:
        changes = patch_env(results)
        if changes:
            print(f"\nPatched .env: {changes}")
        else:
            print("\nNo threshold patches needed (insufficient resolved data)")

    # 5. Discord post
    if args.discord:
        # Compact Discord summary
        total_orders = sum(r["total_orders"] for r in results.values())
        total_filled = sum(r["filled"] for r in results.values())
        total_deployed = sum(r["deployed_dollars"] for r in results.values())
        total_pnl = sum(r["realized_pnl_dollars"] for r in results.values())

        try:
            bal = client.get_balance()
            portfolio_val = bal.get("portfolio_value", 0)
            balance = bal.get("balance", 0)
        except Exception:
            portfolio_val = 0
            balance = 0

        msg_lines = [
            f"**Kalshi ledger update — {datetime.datetime.now():%H:%M ET}**",
            f"",
            f"Orders: {total_orders} total | {total_filled} filled",
            f"Deployed: ${total_deployed:.2f} | Realized P&L: ${total_pnl:+.2f}",
            f"Balance: ${balance/100:.2f} | Portfolio: ${portfolio_val/100:.2f}",
            f"",
            "**Strategy breakdown:**",
        ]
        for strat, r in sorted(results.items()):
            wr = f"{r['win_rate']:.0%}" if r["win_rate"] is not None else "—"
            msg_lines.append(
                f"- `{strat}` {r['total_orders']} orders | "
                f"${r['deployed_dollars']:.2f} | win {wr}"
            )

        if improvements:
            msg_lines += ["", "**Top improvement:**",
                          f"> [{improvements[0][2].upper()}] {improvements[0][0]}: {improvements[0][1][:100]}"]

        msg = "\n".join(msg_lines)
        subprocess.run([
            "/home/milwrite/.npm-global/bin/openclaw",
            "send", "--channel", "discord",
            "--target", DISCORD_CHANNEL,
            "--message", msg,
        ], capture_output=True)
        log.info("Discord update posted")

    return results


if __name__ == "__main__":
    main()
