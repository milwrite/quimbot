# agents/KANBAN.md — Stand-up Log

## 2026-02-24 (Tue) — 7:00 PM ET

**Top goal:** Unblock Stage 1 Run 4 eval (adapter weights still missing — day 2).

**Since last stand-up (noon):**
- Syntax-validated both eval scripts (`qwen-eval.py`, `qwen-eval-v2.py`) — clean, ready to run
- Re-confirmed dataset integrity: 33,834 total JSONL records across 7 files, 0 errors
- No new commits today; blocked on weights

**Next actions:**
- Weights land → run smoke-test checkpoint load → kick off eval
- Draft Stage 2 dataset spec once Petrarch confirms design direction

**Ask for Petrarch:**
- Run 4 adapter weights (step 350 checkpoint) — sole blocker, now day 2. Any ETA?
- Stage 2 dataset design: ready to discuss when you are

## 2026-02-25 (Wed) — 7:00 AM ET

**Top goal:** Keep Stage 1 pipeline moving by consolidating fresh local TOEFL generation while Run 4 weights are still blocked.

**Since last stand-up (7:00 PM):**
- Added dataset inventory doc (`fine-tuning/data/INVENTORY.md`) and committed (`4efefe28`)
- Ran three local Ollama generation passes overnight; net +156 samples produced (92 + 51 + 13)
- Validated/cleaned latest batch slice: `toefl_ollama_batch_20260224_2130_clean.jsonl` has 21/21 valid, 0 dropped
- Recounted dataset totals this morning: 34,011 JSONL rows across current data files

**Next actions:**
- Merge the three new Ollama output files into one staging JSONL and dedup against superset
- Run a quick schema/integrity pass on merged staging set and refresh `INVENTORY.md`
- If Run 4 weights arrive, immediately smoke-load checkpoint and launch eval

**Ask for Petrarch:**
- Can you share ETA or path for Run 4 adapter weights (step 350) so I can switch from data prep to eval?
- Do you want me to keep pushing local generation today or pause at merge+dedup until Stage 2 direction is finalized?

## 2026-02-25 (Wed) — 7:00 PM ET

**Top goal:** Keep momentum under the Run 4 weights block by shipping one concrete data maintenance step tonight.

**Since last stand-up (7:00 AM):**
- Refreshed `fine-tuning/data/INVENTORY.md` with a full recount across all local JSONL files (11 files, 34,011 rows)
- Ran JSON parse validation during inventory refresh: 0 JSON errors across the scanned dataset files
- Confirmed blocker status unchanged: no local Run 4 adapter checkpoint available yet for eval start

**Next actions:**
- When weights land, immediately smoke-load checkpoint and launch Stage 1 Run 4 eval
- If weights stay blocked tonight, prep merged staging file list for dedup run first thing tomorrow

**Ask for Petrarch:**
- Can you share ETA and expected path for Run 4 adapter weights (step 350) so eval can start tonight/tomorrow AM?

