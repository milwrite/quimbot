# TODO

**Last Updated:** 2026-03-09 21:00 ET

## High Priority
- [ ] Unblock Run 4 eval: obtain adapter weights locally (step 350 + final)
- [ ] Run checkpoint eval pass (perplexity + inference samples) immediately after weights arrive
- [x] Merge fresh Ollama outputs into one staging JSONL and dedup against current superset → superset3 (5,560 unique) ✅ 2/27
- [ ] Fix `fine-tuning/prospects` Discord notifier path (`openclaw` binary missing in cron runtime)
- [x] Spot-check superset3 quality (5,560 rows, 0 parse errors, 10 short replies flagged) ✅ 2/27
- [x] Review 10 flagged short assistant replies in superset3 — all degenerate (2-38 chars) ✅ 3/7
- [x] Write removal script for 10 degenerate replies (`0e9d57bc`) ✅ 3/7
- [ ] Run removal script → produce superset4

## Medium Priority
- [ ] Refresh `fine-tuning/data/INVENTORY.md` after merge/dedup and recount totals
- [ ] Log dedup delta (kept vs removed rows) in `STATUS.md` and `KANBAN.md`
- [ ] Validate `generate_toefl_ollama_10k.py` with a small reproducible smoke command in docs
- [ ] Decide Stage 2 dataset composition (Spanish SFT candidates from latam-gpt)
- [ ] Fix OpenRouter 402 on milwrite account

## Workshop / CAIL Deck
- [ ] Unpack VSC-IDE setup steps more concretely (slide 9):
  - Step 1: Download + install VS Code — add download link, OS variants (macOS/Windows/Linux)
  - Step 2: Sign in with your GitHub profile — clarify where in VS Code (accounts menu, bottom-left)
  - Step 3: Add the GitHub extension — name the exact extension (GitHub Pull Requests / GitHub Repositories), show what "start tracking" means in practice
  - Step 4: Open the integrated terminal — show the keyboard shortcut (Ctrl+` / Cmd+`), explain this is where CLI + Git commands run

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
