# MEMORY.md

## Quimbot (github.com/milwrite/quimbot) — current local setup

- Repo remote: `https://github.com/milwrite/quimbot.git` (branch: `main`).
- Project: **Two-stage LoRA fine-tuning pipeline** for a pedagogically-aware language-learning assistant (Stage 1 “Core Linguist” → Stage 2 language/learner variants). See `README.md` for architecture + workflow.

### Local datasets currently present in this workspace (git-tracked location)

**Note:** The repo’s README describes a gitignored `datasets/` directory, but **there is no `datasets/` folder on disk right now**. The locally-available training corpora are stored under `fine-tuning/data/` (plus a few small JSONLs in `fine-tuning/`).

#### `fine-tuning/data/`
- `stage1_train.jsonl` (~445M) — mixed Stage 1 training set.
- `ultrachat_200k_train_sft.jsonl` (~500M) — UltraChat 200K SFT (pilot / general SFT substrate).
- `ultrachat_200k_train_sft_cuny_es.jsonl` (~1.3G) — UltraChat 200K SFT (CUNY ES variant).
- `toefl_synth_followups_100part1_20260211_2301.jsonl` (~28K) — TOEFL-style synthetic followups (batch).
- `toefl_synth_followups_10_part1..45_kimi-k2-0905_20260212_*.jsonl` (~4–8K each) — TOEFL-style synthetic followups split into 45 small parts.
- Archive folder: `fine-tuning/data/_archive_20260212_000042/`
  - `toefl_synth_followups_500_20260211_2235.jsonl` (~24K)
  - `toefl_synth_followups_25_part1_kimi-k2-0905_20260211_234713.jsonl` (~16K)
  - `toefl_synth_followups_25_part2_kimi-k2-0905_20260211_234737.jsonl` (~8K)
  - `toefl_synth_followups_10_part1_kimi-k2-0905_20260212_000019.jsonl` (~4K)

#### `fine-tuning/` (small local JSONLs)
- `fine-tuning/scaffolding_1000.jsonl` (~20K) — small scaffolding dataset.
- `fine-tuning/test_scaffolding.jsonl` (~4K) — tiny test set.
- `fine-tuning/proof_of_concept_10.jsonl` (~8K) — minimal POC.
- `fine-tuning/scaffolding_kimi_k2.5_50.jsonl` (0 bytes) — placeholder/empty.

## Discord Server: Gibbs Street (guild `930250199157334036`)

### Categories & Channels
- **🎭| Gibbs Street** (category `930254435605696522`)
  - `🛝sandbox` (`930250199157334039`) — general chat, open to all
  - `🌐web-search` (`930252691886719017`) — web search results
  - `🎶orchestra` (`1467738838846799953`) — bot coordination, gallery drops, stand-ups. Access: milwrite, Cen, Chopppa, Petrarch, Quimbot, user `1436782482967101491`
  - `🪈agent-log` (`1453422546874798192`) — automated agent output, cron job targets
- **🎱 | Basement Billiards** (category `930391357854470185`)
  - `🦑moltorum` (`1470162786582663200`) — forum channel
  - `🌃backroom` (`1474924288938213417`) — private: Cen, Petrarch, Quimbot
  - `🧭improv` (`930392115601637408`)
- **Voice:** `68 jefferson st.` (`1453543208901411019`)

### Bot IDs
- **Quimbot** (this bot): `1467736354766196829`
- **Petrarch** (Clawdbot, PI): `1464098720340508776`
- Unknown bot/user: `1436782482967101491` (has orchestra access)

## GitHub Pages
- Repo: `https://github.com/milwrite/quimbot.git` (branch: `main`)
- Pages URL: `https://milwrite.github.io/quimbot/`
- `docs/index.html` — Orchestra Project Showcase (landing page)
- `docs/gallery/` — 25 HTML canvas visualizations (self-contained, dark theme)
- `docs/cail-docs/` — CUNY AI Lab documentation (Starter Kit, Design Kit, Instructional Kit)
- `docs/cail-docs/cail-logo.png` — CAIL logo asset

## Discord protocol: communicating with Petrarch (Clawdbot, PI)

**Who is Petrarch (in Discord):**
- Petrarch appears as a bot user: **Clawdbot, PI**
- Discord user/app id: **1464098720340508776**

### Reliable mention / attribution (don’t use plain @handles)
Discord mentions must use the ID form to reliably ping the right entity:
- Mention Petrarch: `<@1464098720340508776>`
- Mention this OpenClaw bot (Quimbot): `<@1467736354766196829>`

(Plain text like `@Petrarch` may not create a real Discord mention and won’t reliably trigger notifications or automation.)

### Bot-to-bot caveat (likely cause of “handle attribution fails”)
Because Petrarch is a bot, **bot-authored messages may be ignored** by default on either side:
- OpenClaw Discord channel config has an `allowBots` flag (if false/omitted, Petrarch’s messages might not trigger OpenClaw).
- Petrarch may also ignore messages authored by bots unless explicitly designed otherwise.

**Practical workaround:**
- Prefer a human to “bridge” by mentioning the other bot with the ID mention, or
- Enable/confirm `channels.discord.allowBots=true` if you want OpenClaw to respond to Petrarch’s bot messages.

### Stand-up / sync message format
When pinging Petrarch for stand-ups (KANBAN sync):
1. Start with an ID mention: `<@1464098720340508776>`
2. State the task explicitly: “sync KANBAN.md”
3. Include the app id for traceability: `app id: 1464098720340508776`
4. Ask for structured output:
   - “Commitment / Blocker / No” or “Done / Next / Blockers”

### Preferred location
- Keep Petrarch coordination inside the relevant Discord thread/channel so both bots can see the same context.

## Gallery Rules
- Every gallery artifact must have a "back to gallery" button
- The button and all controls/labels must be hidden when loaded inside an iframe
- Detection: `if (window.self !== window.top)` hides UI overlays so iframe previews stay clean

## People (Discord interactions)

- **milwrite** (aneventperhaps) `<@aneventperhaps>`: Project owner. Directs both bots. Runs the server.
- **Cen** (cenliu) `<@756158144660635648>`: Working on a dissertation (topic undisclosed). Brief friendly exchange in #sandbox, Feb 16.
- **Chopppa** (chopppa32) `<@822471451399159819>`: Banter in #sandbox, Feb 16. Asked me to relay a dinner invite to St. Louis. Called me a prick when I was smug about it, we squashed it. Vibe: playful trash talk.

## Weekly Site Curation (Saturday 10 PM ET)
- Every Saturday at 10 PM ET: Petrarch and Quimbot meet in #orchestra to discuss updates to milwrite.github.io/quimbot/
- Quimbot implements changes, Petrarch reviews and verifies
- Goal: curate and showcase the week's contributions, add new categories as projects grow
- Standing meeting, started Feb 21 2026
