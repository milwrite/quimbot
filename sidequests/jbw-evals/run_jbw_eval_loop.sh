#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/milwrite/Quimbot/sidequests/jbw-evals"
LOGDIR="$ROOT/logs"
REPORTDIR="$ROOT/reports"
mkdir -p "$LOGDIR" "$REPORTDIR"

STAMP="$(date +%F_%H%M%S)"
LOGFILE="$LOGDIR/run_$STAMP.log"
REPORTFILE="$REPORTDIR/summary_$STAMP.md"
JBW_ROOT="${JBW_ROOT:-$HOME/Desktop/JBW}"

{
  echo "# JBW Eval Loop"
  echo
  echo "- timestamp: $(date -Is)"
  echo "- jbw_root: $JBW_ROOT"
  echo
  if [[ ! -d "$JBW_ROOT" ]]; then
    echo "JBW corpus path not found on this machine."
    echo "Expected: $JBW_ROOT"
    exit 0
  fi

  echo "## Inventory"
  find "$JBW_ROOT" -maxdepth 2 -type f | sed -n '1,400p'
  echo
  echo "## Next step"
  echo "Hook inventory + eval scripts here once corpus-specific paths are confirmed."
} | tee "$LOGFILE" > "$REPORTFILE"
