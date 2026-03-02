# TODO

**Last Updated:** 2026-02-28 21:00 EST

## High Priority
- [ ] Unblock Run 4 eval: obtain adapter weights locally (step 350 + final)
- [ ] Run checkpoint eval pass (perplexity + inference samples) immediately after weights arrive
- [x] Merge fresh Ollama outputs into one staging JSONL and dedup against current superset → superset3 (5,560 unique) ✅ 2/27
- [ ] Fix `fine-tuning/prospects` Discord notifier path (`openclaw` binary missing in cron runtime)
- [x] Spot-check superset3 quality (5,560 rows, 0 parse errors, 10 short replies flagged) ✅ 2/27
- [ ] Review 10 flagged short assistant replies in superset3

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

## Done (Feb 26)
- [x] Morning review completed from live evidence (git, generated docs files, cron logs)
- [x] Updated `KANBAN.md`, `CLAUDE.md`, and `STATUS.md` for 09:00 review cycle
- [x] Identified recurring cron notifier failure signature in `fine-tuning/prospects/cron.log`

## Done (Feb 25)
- [x] Added nightly stocktake artifact (`reports/nightly/stocktake-2026-02-25.md`)
- [x] Logged evening sync and refreshed coordination state files
