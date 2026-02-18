# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-17 19:00 ET (evening standup)_

## ✅ Done
- Two-stage LoRA fine-tuning pipeline architecture (README)
- Stage 1 "Core Linguist" dataset assembly (`stage1_train.jsonl` ~445M)
- UltraChat 200K SFT variants (base + CUNY ES)
- TOEFL-style synthetic followup generation script (`fine-tuning/generate_toefl_followups_openrouter.py`)
- Followups QA + consolidation scripts (`fine-tuning/qa_followups_jsonl.py`, `fine-tuning/consolidate_followups.py`)
- JSONL audit tooling + audit snapshot captured (TOEFL concat issues isolated to empty-assistant + role alternation; parse errors=0)
- HF dataset mixing utility + consolidated dataset notes (`fine-tuning/prepare_stage1_mix_hf.py`, `fine-tuning/CONSOLIDATED_DATASETS.md`)
- Microlearning sidequest: generated 10x 60s scripts + 60 Veo scene prompts (commit `da0a599`; see `sidequests/microlearning/docs/GENERATION_SUMMARY.md`)

## 🔨 In Progress
- **Write build recipe** (concrete input paths + expected counts for all 3 supersets) — Quimbot
- **Execute Superset 2** (TOEFL clean concat → re-audit before/after) — Quimbot
- **Execute Superset 3** (Pilot+Scaffold superset, clean+dedup) — Quimbot

### ✅ Decisions resolved (2026-02-17 morning standup)
- ✅ Drop 30 empty-assistant + 2 alternation-violation rows (confirmed)
- ✅ Dedup policy: hard dedup by full `messages` hash, within-source only (HF datasets), cross-source for TOEFL+Pilot arm
- ✅ Stage 1 mixing ratios: LMSYS 40% / Magpie 25% / TOEFL synth 20% / Prosocial 10% / Pilot 5%
- ✅ Taxonomy endorsed: three-tier naming (sources / combined / mixes), folder conventions, three canonical supersets
- ✅ `stage1_train.jsonl` is a legacy mixed output → archive as `_redundant_stage1_train_legacy.jsonl`

## 📋 Backlog
- Run Stage 1 LoRA training on validated dataset mix
- Stage 2 language/learner variant fine-tuning
- Evaluation framework build-out (`evaluation/` dir exists, needs populating)
- A2A cross-machine delegation (Petrarch ↔ Quimbot task passing)
- Dataset quality metrics / automated filtering (length histograms, role-order checks, near-dup)

## 🚫 Blocked
- OpenRouter scale-out generation: **HTTP 402 Payment Required** (billing/account state)

## 📝 Notes
- Latest detailed work log lives in `agents/KANBAN.md` (stand-ups) + `memory/` daily notes.
- Sidequests have active work (microlearning pipeline scripts + data artifacts under `sidequests/microlearning/`), but core priority remains unblocking Stage 1 mix + training.
- Current coordination asks are parked in `TODO.md` + the top of `agents/KANBAN.md`. 
