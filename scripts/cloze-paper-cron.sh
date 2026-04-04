#!/bin/bash
# Cloze Paper Every-Other-Day Session Runner (Petrarch)

ANCHOR_DATE="2026-03-10"
STATE_FILE="/Users/milwright/clawd/quimbot/cloze-paper-sessions.json"

# Calculate days since anchor
TODAY=$(date -u +%Y-%m-%d)
ANCHOR_EPOCH=$(date -j -f "%Y-%m-%d" "$ANCHOR_DATE" "+%s" 2>/dev/null || echo 0)
TODAY_EPOCH=$(date -j -f "%Y-%m-%d" "$TODAY" "+%s" 2>/dev/null || echo 0)
DAYS_DIFF=$(( (TODAY_EPOCH - ANCHOR_EPOCH) / 86400 ))

# Check if today is an "on" day (every other day from anchor)
if [ $((DAYS_DIFF % 2)) -ne 0 ]; then
  echo "[Petrarch] Skipping: Not a scheduled session day (anchor: $ANCHOR_DATE, today: $TODAY, diff: $DAYS_DIFF days)"
  exit 0
fi

# Read current session from state file
CURRENT_SESSION=$(jq -r '.current_session' "$STATE_FILE")
SESSION_FOCUS=$(jq -r ".sessions.\"$CURRENT_SESSION\".focus" "$STATE_FILE")
SESSION_PHASE=$(jq -r ".sessions.\"$CURRENT_SESSION\".phase" "$STATE_FILE")

echo "[Petrarch] Cloze Paper Session $CURRENT_SESSION (Phase $SESSION_PHASE)"
echo "[Petrarch] Focus: $SESSION_FOCUS"
echo ""
echo "Draft: /Users/milwright/clawd/quimbot/writing/cloze-reader-paper/draft.md"
echo "Live: https://milwrite.github.io/quimbot/cloze-reader-draft/"
echo "Style guide: /Users/milwright/clawd/quimbot/writing/cloze-reader-paper/JOURNAL.md"
echo ""
echo "Current emphasis (milwrite, 2026-04-04): second half — Cloze Reader section and Continuity and Asymmetry."
echo "Deliver session memo to #writing and await approval before committing prose."
