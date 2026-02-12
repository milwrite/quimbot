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
