#!/usr/bin/env bash
# Cloze Reader paper session runner
# Checks date parity from anchor date, runs session task if it's a session day.

ANCHOR="2026-03-10"
ANCHOR_EPOCH=$(date -d "$ANCHOR" +%s)
TODAY_EPOCH=$(date -d "$(date +%Y-%m-%d)" +%s)
DIFF_DAYS=$(( (TODAY_EPOCH - ANCHOR_EPOCH) / 86400 ))

if (( DIFF_DAYS % 2 != 0 )); then
  echo "Not a session day (day offset: $DIFF_DAYS). Skipping."
  exit 0
fi

SESSION_NUM=$(( DIFF_DAYS / 2 + 1 ))
echo "SESSION DAY — Session $SESSION_NUM (day offset: $DIFF_DAYS)"
echo "Session state: /home/milwrite/Quimbot/writing/cloze-reader-paper/SESSION_STATE.md"
