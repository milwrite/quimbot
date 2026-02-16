# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-16 09:00 ET (daily review + Petrarch tasking)_

## ✅ Done
- Two-stage LoRA fine-tuning pipeline architecture (README)
- Stage 1 "Core Linguist" dataset assembly (`stage1_train.jsonl` ~445M)
- UltraChat 200K SFT variants (base + CUNY ES)
- TOEFL-style synthetic followup generation script (`fine-tuning/generate_toefl_followups_openrouter.py`)
- Followups QA + consolidation scripts (`fine-tuning/qa_followups_jsonl.py`, `fine-tuning/consolidate_followups.py`)
- JSONL audit tooling + audit snapshot captured (TOEFL concat issues isolated to empty-assistant + role alternation; parse errors=0)
- HF dataset mixing utility + consolidated dataset notes (`fine-tuning/prepare_stage1_mix_hf.py`, `fine-tuning/CONSOLIDATED_DATASETS.md`)

## 🔨 In Progress
- **Clean** TOEFL synth concat by filtering/dropping:
  - empty `assistant` content rows (30)
  - role alternation violations (2)
- Decide synth followups **dedup policy** (hard dedup vs keep duplicates as weighting)
- Build a training-ready Stage 1 mix JSONL with pinned ratios/seeds (reproducible)

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
