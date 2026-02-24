# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-23 19:46 ET (evening stand-up)_

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
- Gallery expanded to 26 artifacts (incl. Rubik's cube, Mitosis, Pendulum Wave); homepage showcase updated
- Mobile optimization pass on gallery artifacts (touch targets, readability)
- CAIL docs: scaffold + AI Toolkit integration attempted, reverted to original Sandbox docs

## 🔨 In Progress
- **Evaluate Stage 1 Run 4 checkpoints** — step 350 looks optimal per early perplexity; need full eval pass (TOP PRIORITY)
- **Evaluate Stage 1 Run 4 checkpoints** — BLOCKED: adapter weights not on local disk, need to locate/download

### 👇 Waiting on Petrarch
- Stage 1 Run 4 eval: need location of adapter weights (not on local disk) to begin eval pass

## 📋 Backlog
- Stage 2 language/learner variant fine-tuning (Spanish SFT datasets scouted: ~1.1M rows from latam-gpt)
- Evaluation framework build-out (`evaluation/` dir exists, needs populating)
- A2A cross-machine delegation (Petrarch ↔ Quimbot task passing)
- Dataset quality metrics / automated filtering (length histograms, role-order checks, near-dup)

## 🚫 Blocked
- OpenRouter scale-out generation: **HTTP 402 Payment Required** (billing/account state)

## 📝 Notes
- Latest detailed work log lives in `agents/KANBAN.md` (stand-ups) + `memory/` daily notes.
- Sidequests have active work (microlearning pipeline scripts + data artifacts under `sidequests/microlearning/`), but core priority remains unblocking Stage 1 mix + training.
- Current coordination asks are parked in `TODO.md` + the top of `agents/KANBAN.md`. 
