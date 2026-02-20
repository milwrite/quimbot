# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-19 19:00 ET (evening standup)_

---

## 📋 2026-02-19 Evening Standup

**Quimbot session status:** Still unavailable for direct sync (session not found).

**Observed repo state since morning:**
- Latest commit `ed657b4`: Gallery work (merge duplicate flow fields, add fractal tag, live iframe previews)
- Training artifacts **remain uncommitted**: logs, merged_model/, lora_weights.tar/, new scripts
- **Superset builds NOT completed**: `fine-tuning/data/supersets/` directory does not exist
- Only one dataset file in data/: `final_combined_train.jsonl`
- Untracked work files: `scaffolding_combined.jsonl`, `scaffolding_gpt120b_500.jsonl`, `scaffolding_v2_completion.jsonl`, `stage1_eval.json`

**Status assessment:**
- ❌ Superset 2 (TOEFL) — **NOT built**
- ❌ Superset 3 (Pilot+Scaffold) — **NOT built**
- ❓ ITP presentation status — **unknown** (no confirmation available)
- ⚠️ Training work in progress but not committed to git

**Action items for next standup:**
- Sync with Quimbot to understand blockers on superset builds
- Decide whether to commit training artifacts or wait for Quimbot's direction
- Clarify ITP presentation outcome
- Re-confirm priorities for Feb 20

---

## 📋 2026-02-19 Morning Standup

**Quimbot session status:** Not available for direct sync (session not found).

**Observed repo state:**
- New untracked files indicate active work:
  - `training_run_stage1.log`, `training_run_stage1_v2.log`, `training_run_ultrachat.log`
  - `merged_model/` directory (3 GB merged Qwen3-8B model)
  - `lora_weights.tar/` 
  - New scripts: `merge_lora.py`, `train_reward_model.py`, `sample_on_policy.py`, `annotate_samples.py`, `export_to_ollama.py`
  - New data: `scaffolding_combined.jsonl`, `scaffolding_gpt120b_500.jsonl`, `scaffolding_v2_completion.jsonl`, `stage1_eval.json`
- Deleted files: cleanup of failed/test scaffolding files
- Modified: `.DS_Store` files (filesystem metadata)

**Inferred activity:** Training runs executed, model merging complete, new dataset variants generated. The "In Progress" tasks from yesterday appear to have work artifacts, but no git commits to confirm completion.

**Action items for next sync:**
- Reach Quimbot for status confirmation on Superset 2/3 completion
- Review uncommitted scripts for git inclusion
- Confirm ITP presentation readiness (scheduled for today, Feb 19)

**Status:** Superset builds remain **unconfirmed** pending Quimbot sync.

---

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
