# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-19 21:00 ET (evening review)_

## ✅ Done
- Two-stage LoRA fine-tuning pipeline architecture (README)
- Stage 1 "Core Linguist" dataset assembly (`stage1_train.jsonl` ~445M)
- UltraChat 200K SFT variants (base + CUNY ES)
- TOEFL-style synthetic followup generation script (`fine-tuning/generate_toefl_followups_openrouter.py`)
- Followups QA + consolidation scripts (`fine-tuning/qa_followups_jsonl.py`, `fine-tuning/consolidate_followups.py`)
- JSONL audit tooling + audit snapshot captured (TOEFL concat issues isolated to empty-assistant + role alternation; parse errors=0)
- HF dataset mixing utility + consolidated dataset notes (`fine-tuning/prepare_stage1_mix_hf.py`, `fine-tuning/CONSOLIDATED_DATASETS.md`)
- Superset 2 (TOEFL): 9227 records, cross-source deduped
- Superset 3 (Pilot): 1366 records, clean
- Microlearning sidequest: generated 10x 60s scripts + 60 Veo scene prompts (commit `da0a599`; see `sidequests/microlearning/docs/GENERATION_SUMMARY.md`)
- ITP Lab deck: 19 commits — full layout overhaul, GitHub Pages deployment, mobile UX, creative-coding visualizations, content polish

## 🔨 In Progress
- **Clean** TOEFL synth concat — ✅ verified clean in both supersets (0 empty-asst, 0 alt-violations)
- Decide synth followups **dedup policy** (hard dedup vs keep duplicates as weighting) — dedup passes done, policy confirmation still needed
- Build a training-ready Stage 1 mix JSONL with pinned ratios/seeds (reproducible)

### 👇 Waiting on Petrarch decisions
- Confirm policy: drop the 30 empty-assistant + 2 alternation-violation rows (vs reconstruct)
- Confirm dedup: full `messages` hash hard-dedup vs keep dupes as weighting
- Propose Stage 1 mixing ratios once above is settled

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
