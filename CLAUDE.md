# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Protocol

- Follow **COLLABORATION.md** protocol for multi-agent coordination
- Update **KANBAN.md**, **STATUS.md**, **DEVLOG.md**, **RUNLOG.md** after each significant action
- **Update `dataset_review.md` after every training or evaluation run** — document dataset composition changes, new/removed datasets, and data quality observations
- Always include commit hash **and** direct GitHub file link in Discord updates
- Never commit datasets or large artifacts to Git

## Key Decisions Log (2026-03-27)
- **Evening review 3/27 21:00**: 36 commits full day (10 Quimbot, 26 creative-clawing). Data: off-day generation produced 10,413 new TOEFL entries across 7 iterative scripts (17 new error categories: BU-BZ, CD-CN; new domains: medical, legal, business, tech, school-age); superset12 at 76,419. Quimbot: CUNY Commons featured sites (20 candidates, 10 confirmed live), CALI script rewrites finalized, cloze paper genealogy pass. creative-clawing: technical debt sweep day (100dvh on 73 files, manifest agent casing normalization with hard validation gate, IFS artifact untracked fix, sand.html iframe deferred init, iframe load listener restore, SW cache bust to cc-v2, mobile audit pass, thomas attractor scale correction, back button href sweep, submit-artifact.yml YAML repair, CSS semicolon repair on 14 files). Dataset generation saturation noted: 7 iterative passes needed to clear 10k; future off-days will need new grammatical structures and domains.
- **Morning review 3/27 09:00**: 2 commits overnight (CALI script rewrites — three length variants 250/500/750w, AmigAI arc reframe per milwrite brief). Writing lane active; data/training lane static. OpenRouter 402 day 30. Superset11 at 66,006.

## Key Decisions Log (2026-03-26)
- **Evening review 3/26 21:00**: 17 commits full day (10 Quimbot, 7 creative-clawing). Writing: cloze paper genealogy framing pass + narrator line restore + Veldre et al. cut per milwrite ruling + v38 closing rejection. Pages build: 3 commits fixing nested-repo dirs, dangling submodule, knowledge-collections-repo. creative-clawing: homepage perf (shared rAF, iframe cap 32, unified lifecycle), dadras mobile scope fix, astar iframe timing + service worker offline cache. OpenRouter 402 day 29. Superset11 at 66,006.
- **Morning review 3/26 09:00**: 5 commits overnight. creative-clawing: PageRank (power iteration + random surfer) + Snowflake (Reiter hex CA) artifacts, static thumbnail placeholders for homepage/gallery cards, rossler/schelling 100dvh normalize. Quimbot: gyro parallax starfield smoothing + flowfield fade fix. OpenRouter 402 day 29. Superset11 at 66,006.

## Key Decisions Log (2026-03-25)
- **Night review 3/25 21:00**: ~23 commits full day. Writing: cloze paper v37→v38 + STYLE_GUIDE LLM-as-judge gate. creative-clawing: 3 new artifacts (Dadras, Sprott, KH instability) + mobile fixes on 25 files + iframe black-card bug fixes. Kalshi config v2. Data: 8,177/10k clean from toefl_batch_20260325. OpenRouter 402 day 28.
- **Morning review 3/25**: ~18 commits overnight across 3 repos
- **creative-clawing iframe + mobile sweep**: 19 artifacts had .panel/.controls hidden for clean iframe embeds; hatmonotile/gradient/astar got mobile responsive fixes; astar auto-demo loop added; nav submenu overflow:hidden removed; lotkavolterra mobile layout fixed
- **Microblogs #30 + #31**: Lotka-Volterra (phase orbits, Adriatic fish) + Mandelbrot (smooth coloring, Julia/Fatou/Mandelbrot history)
- **Kalshi config finalized**: $5 fixed bets, 10 trades/run, 10% edge threshold (`a655047`)
- **OpenRouter 402 day 28**

## Key Decisions Log (2026-03-24)
- **Superset10 merged (59,509 rows)**: new high-water mark; 8 new error categories from batch_20260323 (subjunctive, cleft sentences, ellipsis/substitution)
- **Kalshi NO-only pivot**: milwrite clarified via voice note: trade NO when threshold is absurdly out of reach; removed YES branch from `evaluate_signal()`; added `price_tracker.py` + historical CSV export (`adfcd1b`)
- **Cloze reader editor PAT restore**: GitHub blocked hardcoded token; now prompts once, caches in localStorage (`c3f2b172`)
- **Cloze paper citation fix**: replaced generic PMC/arXiv refs with proper author citations (Veldre et al., Jacobs et al.) (`f140cba0`)
- **creative-clawing iframe fix**: CSS-first control hiding on 9 artifacts; stops flash in homepage card previews (`55c64b3`)
- **Microblog #29**: Truchet tiles published (`394a6e5`)
- **OpenRouter 402 day 27**

## Key Decisions Log (2026-03-23)
- **toefl_batch_20260323 generated**: 11,240 rows via 3 local generation scripts (gen_20260323.py, v2, supplement)
- **Data audit**: superset3_cleaned.jsonl rows lack system prompts (all start with `user` role); needs fix before merge
- **Superset9 (45,555 rows) confirmed missing from local disk** — only superset3_cleaned + today's batch on Legion
- **Microblog #22 shipped**: Schotter (Georg Nees, 1968) — gravel and the gradient of chaos (`e58a17a6`)
- **Cloze paper prose fix**: overcommitted divergence paragraph replaced with review-frame sentence (`3ffa2f2a`)
- **OpenRouter 402 day 26** — still blocking cloud generation

## Key Decisions Log (2026-03-28–29)
- **Cloze paper draft at v42**: PASSAGE A (occlusion/closure, Kanizsa 1979) added; intro closing restored to v37 (v38 close rejected by milwrite — "violates basically every rule in the style guide"); dangling referent fix (para 4: "All three researchers" → "Both accounts"); expansion paragraph (Continuity and Asymmetry) added at v41; Sunday synthesis logged, roadmap updated.
- **New style rules (milwrite rulings)**: vacuous openers banned; stacked punctuation (colon + semicolon same clause) banned; earned assertion gate added; lazy punctuation cue rule added.
- **Veldre et al. cut**: milwrite ruled CUT on 2026-03-26; revisit at Session 7 when body has its proper form.
- **creative-clawing.com major bug fix sweep** (2026-03-28): short-lane dup bug (pad groups <8); Recently Added grid columns; upper-left tiny canvas (rAF defer); blank iframe previews (Turing, Sand, Stable Fluids, PageRank); gallery MAX_LIVE cap raised to 60 with pending queue. `tests/lint_gallery.py` + CI workflow added.
- **TOEFL master file built** (2026-03-28): `toefl_master_20260328.jsonl` at 52,164 unique records (superset8 base + synth_10k + superset3_cleaned deduped). Superset12 at 76,419 per Quimbot.
- **Invalid GH_TOKEN removed** from `openclaw.json`; milwrite keyring OAuth handles `gh` auth going forward.
- **OpenRouter 402 day 30+** — cloud generation still blocked.

## Key Decisions Log (2026-03-22)
- **Cloze paper post-v39 fixes** — 'cannot read slowly' contrast restored (with humans, not total absence); hanging Firth quote fixed; bad style rule reverted; 2 new style rules added (`03df4b73`, `ac987799`)
- **Site synced to v37** with cross-links between site deployment and draft.md (`1d5773a2`, `25e84602`)
- **Overnight v36→v39** — paragraph bridging, colon sweep (11 eliminated), verb audit, genealogy condensed
- **Writing system expanded** — CHECKLIST_COPY, CHECKLIST_REVISE, PROCESS_GUIDE added for phase-decomposed style with conditional routing
- **Single draft.md canonical** — versioned filenames eliminated, git handles history; writing/ directory reorganized with subdirectories

## Agent Documentation

Agent coordination files are in the project root:

- **COLLABORATION.md** - Multi-agent workflow protocol
- **KANBAN.md** - Project board and stand-up notes
- **STATUS.md** - Real-time status updates
- **DEVLOG.md** - Timestamped work log
- **RUNLOG.md** - Training run history
- **NEXT-ACTIONS.md** - Prioritized action items

## Project Structure

```
molt/
├── README.md              # Project overview
├── CLAUDE.md              # This file (agent instructions)
├── dataset_review.md      # Dataset review notes (UPDATE AFTER EVERY RUN)
├── COLLABORATION.md       # Multi-agent workflow protocol
├── KANBAN.md              # Project board
├── STATUS.md              # Real-time status
├── DEVLOG.md              # Timestamped work log
├── RUNLOG.md              # Training run history
├── NEXT-ACTIONS.md        # Prioritized action items
├── LoRA-ROADMAP.md        # LoRA training roadmap
├── evaluation/            # Model evaluation framework
├── fine-tuning/           # Training scripts, workflows, and working JSONL data
├── datasets/              # Training data JSONL files (not committed)
├── checkpoints/           # Model checkpoints (not committed)
└── research/              # Research notes and plans
```

## Commands

### Evaluation (recommended: v2)
```bash
pip3 install -r evaluation/requirements-eval.txt
python3 evaluation/qwen-eval-v2.py --models qwen2.5:8b --verbose
python3 evaluation/qwen-eval-v2.py --config evaluation/eval-config-example.yaml --workers 8 --cache
```

### Fine-tuning (requires Python 3.11+)
```bash
python3.11 -m pip install -r fine-tuning/requirements.txt --user
python3.11 fine-tuning/prepare_stage1.py
python3.11 fine-tuning/run_tinker_lora.py --data datasets/stage1_mix_200k.jsonl --batch 64 --rank 16 --save-every 50
python3.11 fine-tuning/test_lora_model.py --lora-weights checkpoints/lora_*/final_lora_weights --compare-base
```

### A2A Bridge (Node.js, zero dependencies)
```bash
node a2a-bridge.mjs                    # listens on 0.0.0.0:18800
A2A_PORT=9000 node a2a-bridge.mjs      # custom port
```

## Architecture

- **fine-tuning/run_tinker_lora.py** — primary training script; uses `tinker.ServiceClient`, converts JSONL ChatML → token streams with loss masking on assistant tokens only, saves checkpoints to `tinker://` URIs
- **evaluation/qwen_eval/** — evaluation package: `core.py` (engine + parallel workers + caching), `metrics.py` (15+ metrics), `test_suites.py` (4 built-in suites), `reporters.py` (JSON/Markdown/Comparison)
- **a2a-bridge.mjs** — standalone HTTP server exposing OpenClaw via Google A2A protocol (JSON-RPC: `tasks/send`, `tasks/get`, `tasks/cancel`), proxies to `http://127.0.0.1:18789/v1/chat/completions`

## Data & Environment

- Training data is JSONL in ChatML format (OpenAI-style messages). Datasets (*.jsonl, ~4.5GB) and model files (*.gguf) are gitignored.
- **Synth followups (concatenated outputs):**
  - `fine-tuning/data/toefl_synth_followups_concat_20260212.jsonl` (5742 lines)
  - `fine-tuning/data/pilot_concat_20260212.jsonl` (1610 lines)
  - These are convenience concat files under gitignored `fine-tuning/data/`.
- **QA/Audit helpers (reproducible):**
  - `fine-tuning/qa_followups_jsonl.py` (fast schema/sanity scan)
  - `fine-tuning/consolidate_followups.py` (merge/normalize multiple followups JSONLs)
  - `fine-tuning/audit_toefl_followups.py` (deeper audit; issue + dupe counts)
- Required env vars for training: `TINKER_API_KEY`, `TINKER_API_BASE`, `HF_TOKEN`

---

## Archived Decisions (pre-2026-03-22)

### Key Decisions (2026-03-19 through 2026-03-21)
- **Paper title finalized** (3/19): "Fill in the Blank: Cloze Reader and the Twin Histories of Occlusion"
- **Colon/semicolon audit rule** added to STYLE_GUIDE (3/19); 3 more rules: trailing participle ban, anaphora abuse ban, tricolon abuse ban
- **Style system disaggregated** (3/21): monolithic STYLE_GUIDE.md split into 6 modular files with SKILL.md router in `style/`
- **Superset9 merged** (3/21) at 45,555 rows; Pages build fix (broken a11y-checker submodule removed)
- **Superset8 merged** (3/20) at 46,943 rows; writing hub page shipped; cloze reader browser editor added (password-gated, commit to GitHub)
- **Cloze reader live draft is additive-only** (3/18): never rewrite existing v14 prose without milwrite approval
- **JOURNAL.md is the canonical shared record** for cloze-reader paper; both bots maintain it
- **Kalshi sidequest** trimmed to weather + CPI only (3/18)

### Notes (2026-02 through 2026-03-18)
- OpenRouter HTTP 402 blocked cloud generation from day 21 (3/18) onward; do not assume generation scripts run until billing resolved.
- `fine-tuning/prospects/cron.log` shows Discord notifier failures from missing `openclaw` binary — use OpenClaw-native messaging (message tool / API path) in cron environments, not local CLI.
- Run 4 adapter weights (step 350 + final) remain missing from local disk; eval blocked until they arrive.
- Petrarch push auth still blocked (zmuhls lacks write on milwrite/quimbot) as of 3/18.
- Synth followups audit: 30 rows empty assistant content, 2 role alternation violations, 0 JSON parse errors.
- Stage 1 mix decision pending: hard-dedup vs. implicit weighting via duplicates.
