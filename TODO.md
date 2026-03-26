# TODO

**Last Updated:** 2026-03-25 21:00 ET

## High Priority
- [ ] Unblock Run 4 eval: obtain adapter weights locally (step 350 + final)
- [ ] Run checkpoint eval pass (perplexity + inference samples) immediately after weights arrive
- [x] Merge fresh Ollama outputs into one staging JSONL and dedup against current superset → superset3 (5,560 unique) ✅ 2/27
- [ ] Fix `fine-tuning/prospects` Discord notifier path (`openclaw` binary missing in cron runtime)
- [x] Spot-check superset3 quality (5,560 rows, 0 parse errors, 10 short replies flagged) ✅ 2/27
- [x] Review 10 flagged short assistant replies in superset3 — all degenerate (2-38 chars) ✅ 3/7
- [x] Write removal script for 10 degenerate replies (`0e9d57bc`) ✅ 3/7
- [x] Run removal script → superset3 cleaned to 5550 rows (`0faa7767`) ✅ 3/10

## Medium Priority
- [x] Merge toefl_batch_20260323 (11,240 rows) into superset pipeline → superset10 (59,509) ✅ 3/24
- [ ] Fix superset3_cleaned system prompt gap (rows start with `user`, no system message)
- [ ] Spot-check superset10 quality (59,509 rows — verify dedup integrity, role structure)
- [x] Kalshi NO-only strategy pivot per milwrite voice note (`adfcd1b`) ✅ 3/24
- [x] Cloze reader editor PAT restore (GitHub blocked hardcoded token) ✅ 3/24
- [x] Refresh `fine-tuning/data/INVENTORY.md` after merge/dedup and recount totals ✅ 3/17
- [x] Cloze reader paper: citation chain upgrades (words 1000-2000) ✅ 3/18
- [x] Cloze reader paper: v15-v29 revision marathon (Gutenberg, stochasticity, Figure 1, closing, Gitelman, inference-engine) ✅ 3/18
- [x] Create shared JOURNAL.md for cloze-reader paper ✅ 3/18
- [x] Add Kalshi trading bot (weather + CPI strategies) ✅ 3/18
- [x] Cloze reader paper: colon audit pass (6 hidden connectors surfaced) ✅ 3/19
- [x] Cloze reader paper: OB1/Rego + context window paragraph rewrites ✅ 3/19
- [x] Cloze reader paper: title finalized ("Fill in the Blank: Cloze Reader and the Twin Histories of Occlusion") ✅ 3/19
- [ ] Cloze reader paper: sharpen thesis paragraph for body section inheritance
- [ ] Cloze reader paper: obtain formal S1→S2 approval from milwrite
- [ ] Log dedup delta (kept vs removed rows) in `STATUS.md` and `KANBAN.md`
- [ ] Verify superset7 dedup integrity (39,133 rows — confirm no duplicates slipped through)
- [ ] Cloze reader paper: draft Section IV
- [ ] Validate `generate_toefl_ollama_10k.py` with a small reproducible smoke command in docs
- [ ] Decide Stage 2 dataset composition (Spanish SFT candidates from latam-gpt)
- [ ] Fix OpenRouter 402 on milwrite account (DAY 28, 4 weeks)
- [x] Merge toefl_batch_20260319 into superset8 (46,943 rows landed) ✅ 3/20
- [ ] Verify superset8 dedup integrity (46,943 rows — confirm no duplicates)
- [x] Complete cloze reader draft_v32 → v33 → v34 → v35 (narrator, prepositions, genealogy) ✅ 3/21
- [x] Cloze reader paper v36→v39 (paragraph bridging, colon sweep, verb audit, genealogy condensed) ✅ 3/22
- [ ] Cloze reader paper: continue past v39 (body sections, Section IV)
- [ ] Kalshi: v2 graduated rollout design (budget caps, risk tiers)

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
