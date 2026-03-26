#!/usr/bin/env bash
# daily_skill_learn.sh
# Picks one skill from awesome-openclaw-skills relevant to active projects
# and installs it via clawhub. Posts a summary to #orchestra.
# Run: every other day at 11 AM ET via cron.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="$HOME/Quimbot"
LOG="$WORKSPACE/memory/skill-learns.log"
STATE="$WORKSPACE/memory/skill-learn-state.json"
CHANNEL="1467738838846799953"  # #orchestra

mkdir -p "$WORKSPACE/memory"

# Active project context — skills relevant to these themes get priority
THEMES=(
  "data analytics jsonl training"
  "creative coding canvas visualization"
  "github git workflow"
  "transcription speech audio"
  "web frontend html"
  "search research"
  "pdf documents"
  "notes pkm memory"
)

# Curated candidate list from awesome-openclaw-skills, relevant to active projects
# Format: "slug|name|category|why"
CANDIDATES=(
  "session-wrap-up|Session Wrap-Up|productivity|Auto-commits unpushed work + extracts learnings per session"
  "github|Github|git|gh CLI integration — PR/issue/actions automation for quimbot + creative-clawing repos"
  "github-trending|Github Trending|research|Daily trending repos — useful for creative coding inspiration sourcing"
  "whisper-audio-transcription|Whisper Audio Transcription|speech|Local Whisper transcription skill — directly relevant to audio transcription work"
  "vibe-coding|Vibe Coding|creative|Prompts-as-prototypes workflow skill — directly relevant to ITP lab deck"
  "session-memory-workspace|Session Memory Workspace|productivity|Persist context across sessions — better continuity"
  "session-watchdog|Session Watchdog|productivity|Monitor session health and detect stalls"
  "github-workflow|Github Workflow|git|GitHub Actions workflow generation and management"
  "github-ops|Github Ops|git|Advanced GitHub operations — PRs, branch management, releases"
  "transcription|Transcription|speech|General transcription skill — pairs with Whisper for audio work"
  "obsidian|Obsidian|notes|Vault/markdown automation — bridge to research notes and dissertation context"
  "gog|Gog|productivity|Google Workspace — Gmail + Calendar + Drive integration"
  "gemini|Gemini|ai|Gemini one-shot Q&A — alternative model for summarization and generation tasks"
  "weather|Weather|utility|Current weather + forecasts — supports Kalshi weather trading bot"
  "1password|1password|security|Secret injection via op CLI — credential management"
  "healthcheck|Healthcheck|security|Host security audit — periodic hygiene for this machine"
  "skill-creator|Skill-creator|meta|Design + package new skills — build custom tools for active projects"
  "blogwatcher|Blogwatcher|research|RSS/Atom feed monitoring — creative coding and AI news sourcing"
  "mcporter|Mcporter|tools|Configure and call MCP servers — expand tooling surface"
  "gifgrep|Gifgrep|media|GIF search and download — useful for Discord posts and reactions"
)

# Load state (which skills already installed)
if [[ -f "$STATE" ]]; then
  INSTALLED=$(python3 -c "import json,sys; d=json.load(open('$STATE')); print(' '.join(d.get('installed',[])))" 2>/dev/null || echo "")
else
  echo '{"installed":[],"last_run":""}' > "$STATE"
  INSTALLED=""
fi

# Pick next uninstalled candidate
CHOSEN=""
CHOSEN_NAME=""
CHOSEN_WHY=""
CHOSEN_CAT=""

for entry in "${CANDIDATES[@]}"; do
  IFS='|' read -r slug name cat why <<< "$entry"
  if ! echo "$INSTALLED" | grep -qw "$slug"; then
    CHOSEN="$slug"
    CHOSEN_NAME="$name"
    CHOSEN_WHY="$why"
    CHOSEN_CAT="$cat"
    break
  fi
done

if [[ -z "$CHOSEN" ]]; then
  echo "[$(date)] All candidates already installed. No new skill today." | tee -a "$LOG"
  exit 0
fi

echo "[$(date)] Installing skill: $CHOSEN ($CHOSEN_NAME)" | tee -a "$LOG"

# Install via clawhub
INSTALL_OUTPUT=$(clawhub install "$CHOSEN" 2>&1) || {
  echo "[$(date)] Install failed: $INSTALL_OUTPUT" | tee -a "$LOG"
  # Post failure to orchestra
  openclaw message --channel "$CHANNEL" \
    "🔧 📚 Daily skill learn: attempted **$CHOSEN_NAME** — install failed. Manual install: \`clawhub install $CHOSEN\`" 2>/dev/null || true
  exit 1
}

echo "[$(date)] Install output: $INSTALL_OUTPUT" | tee -a "$LOG"

# Update state
python3 - <<PYEOF
import json, datetime
state = json.load(open('$STATE'))
if '$CHOSEN' not in state['installed']:
    state['installed'].append('$CHOSEN')
state['last_run'] = datetime.datetime.now().isoformat()
json.dump(state, open('$STATE', 'w'), indent=2)
PYEOF

# Post to #orchestra
MSG="📚 🆕 **Daily skill learned:** \`$CHOSEN\` — **$CHOSEN_NAME** [$CHOSEN_CAT]
$CHOSEN_WHY
Install: \`clawhub install $CHOSEN\`"

openclaw message --channel "$CHANNEL" "$MSG" 2>/dev/null || \
  echo "[$(date)] Could not post to #orchestra" | tee -a "$LOG"

echo "[$(date)] Done." | tee -a "$LOG"
