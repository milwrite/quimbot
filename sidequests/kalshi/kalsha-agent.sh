#!/usr/bin/env bash
# kalsha-agent.sh — Claude Code trading agent
#
# Runs Claude Code against the kalshi toolset with full file access.
# Claude reads live signals/trades/strategies, identifies edges, and
# autonomously improves the toolset over time.
#
# Usage:
#   ./kalsha-agent.sh [task_name] [extra_context]
#
# Task names: morning | cpi_window | oil_window | learn | eod
# If no task given, defaults to a general scan+learn pass.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [[ -f venv/bin/activate ]]; then
    source venv/bin/activate
fi

# ~/kalshi/.env is the canonical credentials file
if [[ -f "$HOME/kalshi/.env" ]]; then
    set -a; source "$HOME/kalshi/.env"; set +a
fi

# Local sidequests/kalshi/.env can override individual vars if needed
if [[ -f .env ]]; then
    set -a; source .env; set +a
fi

TASK="${1:-learn}"
EXTRA="${2:-}"
LOG="logs/claude-agent.log"
mkdir -p logs

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S %Z')
echo "" >> "$LOG"
echo "================================================================" >> "$LOG"
echo "[$TIMESTAMP] kalsha-agent TASK=$TASK" >> "$LOG"
echo "================================================================" >> "$LOG"

# ── Build context for Claude ────────────────────────────────────────────────
RECENT_SIGNALS=""
if [[ -f logs/signals.jsonl ]]; then
    RECENT_SIGNALS=$(tail -30 logs/signals.jsonl 2>/dev/null || echo "(none)")
fi

RECENT_TRADES=""
if [[ -f logs/trades.jsonl ]]; then
    RECENT_TRADES=$(tail -20 logs/trades.jsonl 2>/dev/null || echo "(none)")
fi

STRATEGY_FILES=$(ls strategies/*.py 2>/dev/null | grep -v __pycache__ | tr '\n' ' ')

# ── Task-specific prompts ────────────────────────────────────────────────────
case "$TASK" in

  morning)
    PROMPT="You are an autonomous Kalshi trading agent with full code access.

Working directory: $SCRIPT_DIR
Available strategies: $STRATEGY_FILES
CLI wrapper: ./kalsha

YOUR TASK — Morning open (run every weekday at 6 AM ET):
1. Run './kalsha scan --dry-run' and capture the output
2. Review logs/signals.jsonl (last 30 entries) for any overnight signals that fired
3. Check which markets are currently open by examining the strategies' market-fetch logic
4. If any strategy's dry-run output shows 'no markets found', inspect the ticker PREFIX constants
   and search Kalshi's /markets endpoint for the real prefixes — update the strategy file
5. Review weather.py CITIES list — confirm cities are still active on Kalshi
6. Commit any fixes you make with message 'morning-agent: [what you fixed]'
7. Post a brief status to the Discord channel via:
   openclaw send --channel discord --target 1483986889328562307 --message '[your status]'

Recent signals:
$RECENT_SIGNALS

Recent trades:
$RECENT_TRADES

$EXTRA

Fix what's broken. Improve what's weak. Note what you learned."
    ;;

  cpi_window)
    PROMPT="You are an autonomous Kalshi trading agent. It is 8:25 AM ET — the CPI/NFP release window.

Working directory: $SCRIPT_DIR

YOUR TASK:
1. Check if today is a BLS CPI release day OR an NFP first-Friday release day
   - BLS CPI schedule: https://www.bls.gov/schedule/news_release/cpi.htm (scrape or check date)
   - NFP: first Friday of each month
2. If CPI day: run 'FORCE_CPI_RUN=1 ./kalsha test cpi' and review output
3. If NFP day: run 'FORCE_NFP_RUN=1 ./kalsha test nfp' and review output
4. If KALSHI_API_KEY_ID is set and valid, run the live scan (not dry-run) for the relevant strategy
5. After the release (if data is live), check if the strategy's estimate was close to the actual
   - If not: examine the data source, identify why, patch the estimation logic
6. Log your findings to logs/cpi-nfp-review.md with today's date and actual vs estimated
7. Notify Discord: openclaw send --channel discord --target 1483986889328562307 --message '[result]'

$EXTRA"
    ;;

  oil_window)
    PROMPT="You are an autonomous Kalshi trading agent. It is 10:25 AM ET on a Wednesday — EIA release window.

Working directory: $SCRIPT_DIR

YOUR TASK:
1. Fetch the EIA crude inventory data by running: python3 -c \"
import sys; sys.path.insert(0, '.'); from strategies.oil import fetch_eia_crude_stocks; import json; print(json.dumps(fetch_eia_crude_stocks(), indent=2))
\"
2. Run 'FORCE_OIL_RUN=1 ./kalsha test oil' to see the signal output
3. If KALSHI_API_KEY_ID is set, run the live oil scan
4. Compare the inventory change to consensus (search web or check Reuters/Bloomberg headlines)
5. If the estimate model is off by >30% from consensus, examine oil.py and improve the
   consensus estimation logic (e.g., add a Reuters scraper or Bloomberg API call)
6. Log findings to logs/oil-review.md
7. Notify Discord: openclaw send --channel discord --target 1483986889328562307 --message '[result]'

$EXTRA"
    ;;

  learn)
    PROMPT="You are an autonomous Kalshi trading agent with full code access.

Working directory: $SCRIPT_DIR
Available strategies: $STRATEGY_FILES

YOUR TASK — Continuous learning pass:
1. Review the last 30 signal log entries (logs/signals.jsonl). Look for:
   - Signals that fired but market had no match (ticker prefix wrong)
   - Strategies returning zero signals repeatedly (data source broken?)
   - Edge calculations that seem off (our_prob way above/below market)
2. For any strategy that hasn't fired in >24h: run its dry-test and diagnose
3. Identify ONE new data source or market type Kalshi might offer that we don't have yet
   - Ideas: unemployment claims, FOMC minutes date, mortgage rates, GDP, Senate votes
   - Search the Kalshi API: python3 -c \"
import sys; sys.path.insert(0, '.'); from core.client import KalshiClient
c = KalshiClient(); mkts = c.get_markets(limit=500)
tickers = set(m['ticker'][:8] for m in mkts)
print(sorted(tickers))
\"
   - If you find a promising market type, write a new strategy file following the pattern
     in strategies/weather.py and register it in __init__.py and runner.py
4. Run 'python3 -c \"import runner\"' to confirm imports still work after any changes
5. Commit any improvements with 'learn-agent: [description]'
6. Post to Discord: openclaw send --channel discord --target 1483986889328562307 --message '[what you found/built]'

Recent signals:
$RECENT_SIGNALS

$EXTRA"
    ;;

  eod)
    PROMPT="You are an autonomous Kalshi trading agent. It is end of day.

Working directory: $SCRIPT_DIR

YOUR TASK — End-of-day review and improvement:
1. Run './kalsha status' to get today's P&L and trade count
2. Read logs/trades.jsonl — identify any trades placed today and their outcomes
3. Read logs/signals.jsonl — scan all of today's signals:
   - What was our hit rate? (signals that passed edge threshold / total signals)
   - Which strategies generated the most signals? The most trades?
   - Which had the highest average edge?
4. Write a concise daily debrief to logs/eod/$(date +%Y-%m-%d).md with:
   - Trade count, P&L, best/worst signal
   - One concrete improvement to make tomorrow
5. Implement that improvement now if it's a code change
6. Review edge thresholds — if no trades fired all day but signals existed just below threshold,
   consider whether thresholds are too conservative (check .env or strategy defaults)
7. Commit everything: 'eod-agent: daily review $(date +%Y-%m-%d)'
8. Post to Discord: openclaw send --channel discord --target 1483986889328562307 \
   --message '**EOD $TIMESTAMP** [summary]'

Recent trades:
$RECENT_TRADES

$EXTRA"
    ;;

  *)
    PROMPT="You are an autonomous Kalshi trading agent.

Working directory: $SCRIPT_DIR
Task: $TASK

$EXTRA

Explore, diagnose, fix, and improve the kalshi toolset as needed.
Commit any changes you make. Post results to Discord channel 1483986889328562307."
    ;;
esac

echo "[kalsha-agent] Running Claude Code for task: $TASK" | tee -a "$LOG"

# Run Claude Code with full permissions in the kalshi directory
claude \
  --permission-mode bypassPermissions \
  --print \
  "$PROMPT" 2>&1 | tee -a "$LOG"

echo "" >> "$LOG"
echo "[kalsha-agent] Task $TASK complete: $(date)" >> "$LOG"
