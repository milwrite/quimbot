#!/bin/bash
# Cloze Paper Every-Other-Day Session Runner (Petrarch)
# SCOPE DIRECTIVE (2026-04-04): Second half only — Cloze Reader + Continuity and Asymmetry

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

cat << SESSIONMSG
**Cloze Paper — Session $CURRENT_SESSION**
**Phase:** $SESSION_PHASE
**Focus:** $SESSION_FOCUS

---

**SCOPE DIRECTIVE (2026-04-04 — milwrite instruction):**
All cron sessions now focus exclusively on the second half of the draft:

- Cloze Reader section (critical game design, architecture, prompt engineering, word selection)
- Continuity and Asymmetry section (how game design enacts the twin-histories argument)
- Gutenberg rationale (historicity of primary sources, flattening, call stack argument)

The core framing: Cloze Reader encourages deep, slow reading with texts otherwise subsumed
by large language models, which flatten primary sources into vacuous tertiary forms without
the historicity of the source as its complement.

**OFF LIMITS in cron sessions:**
- First-half lit review (Taylor, BERT genealogy, educational psychology)
- New citation chains for the Introduction
- ML genealogy sections

---

**Division of labor:**
- Petrarch: historicity argument, flattening/foreclosure framing, style enforcement, citation check
- Quimbot: critical game design analysis, architecture-as-argument, asymmetry paragraph development

**Key open items:**
- EX-05 (asymmetry paragraph) — pending milwrite approval
- EX-06 ("decentered" vs "does not perform") — pending milwrite review
- Simplified comparisons to remove per milwrite (2026-04-04)

**Resources:**
- Draft: /Users/milwright/clawd/quimbot/writing/cloze-reader-paper/draft.md
- Live: https://milwrite.github.io/quimbot/cloze-reader-draft/
- Style guide: /Users/milwright/clawd/quimbot/writing/cloze-reader-paper/JOURNAL.md
- Excerpts: /Users/milwright/clawd/quimbot/writing/cloze-reader-paper/EXCERPTS.md

Deliver session memo to #writing. Await milwrite approval before committing prose.
SESSIONMSG
