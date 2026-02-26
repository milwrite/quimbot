# TODO

**Last Updated:** 2026-02-25 21:00 EST

## High Priority
- [ ] Unblock Run 4 eval: obtain adapter weights locally (step 350 + final)
- [ ] Run checkpoint eval pass (perplexity + inference samples) immediately after weights arrive
- [ ] Merge overnight Ollama outputs into one staging JSONL and dedup against current superset

## Medium Priority
- [ ] Refresh `fine-tuning/data/INVENTORY.md` after merge/dedup and recount totals
- [ ] Log dedup delta (kept vs removed rows) in `STATUS.md` and `KANBAN.md`
- [ ] Validate `generate_toefl_ollama_10k.py` with a small reproducible smoke command in docs
- [ ] Decide Stage 2 dataset composition (Spanish SFT candidates from latam-gpt)
- [ ] Fix OpenRouter 402 on milwrite account

## Low Priority
- [ ] Reorganize `fine-tuning/prospects/` into main `fine-tuning/` workflow layout
- [ ] Review and prune gallery visualizations (26 pages, stale check)
- [ ] Document Slidev ConfigPanel integration patterns

## Done (Feb 25)
- [x] Logged 07:00 ET stand-up update in `agents/KANBAN.md`
- [x] Ran three local Ollama generation passes overnight (+156 rows total)
- [x] Validated clean batch slice (`toefl_ollama_batch_20260224_2130_clean.jsonl`: 21/21 valid)
- [x] Added nightly stocktake artifact (`reports/nightly/stocktake-2026-02-25.md`)

## Done (Feb 24)
- [x] Nightly stocktake commit: added `fine-tuning/data/INVENTORY.md` (`4efefe28`)
- [x] Re-verified dataset integrity snapshot (33,834 rows across 7 files)
- [x] Syntax-check completed for eval scripts (`qwen-eval.py`, `qwen-eval-v2.py`)
- [x] Added generation scaffold `fine-tuning/scripts/generation/generate_toefl_ollama_10k.py`
