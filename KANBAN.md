# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-21 21:00 ET (nightly review)_

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
- Creative coding gallery expansion: 27 commits on 2/20 — 5 new artifacts (Lorenz, Sospiri, Nake, Noll, Harmonograph), full UX overhaul, iframe embed support
- Gallery day 2 (2/21): +4 artifacts (Heat Diffusion, Turing Patterns, Truchet Tiles, Voronoi), ~18 total pages
- README overhaul: GitHub Pages showcase, gallery, scraper, models, side quests sections
- Stage 1 LoRA Run 3: 83% complete before crash; superseded by Run 4
- **Stage 1 LoRA Run 4 COMPLETE** — 671 steps, 14 checkpoints, v3 mix (43,170 records), Qwen3-8B rank 16
- Gallery expanded to 22 artifacts; homepage showcase updated
- CAIL docs: scaffold + AI Toolkit integration attempted, reverted to original Sandbox docs

## 🔨 In Progress
- **Evaluate Stage 1 checkpoints** — step 350 looks optimal per early perplexity; need full eval
- Decide synth followups **dedup policy** (hard dedup vs keep duplicates as weighting) — dedup passes done, policy confirmation still needed
- Build a training-ready Stage 1 mix JSONL with pinned ratios/seeds (reproducible) — **script done** (`build_stage1_mix.py`, 43175 records), awaiting policy sign-off

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
