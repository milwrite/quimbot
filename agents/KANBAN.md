# KANBAN — Quimbot

_Last synced: 2026-03-08 19:00 ET_

## In Progress
- **TOEFL superset4 merge** — gen complete (11,999 entries, QA passed). 10 degenerate entries flagged for removal. superset3_merged.jsonl found on disk (5,560 lines, 0 parse errors). Ready for flagged-entry removal + merge script.
- **CAIL Workshop #1 deck** — 74+ commits; icebreaker redesigned, gen-dev-foundations deck added. Stubs remain for slides 7–8 (awaiting Petrarch's ITP content), 12–15 (activities/exit).
- **Blog "The Problem with AI Detection"** — 3 open validation issues need milwrite action (cheeky claim, Engelbrecht figures, USD neurodivergent source). Needs final publish review.

## Blocked
- **Run 4 adapter weights** — missing, need retrieval
- **OpenRouter 402 errors** — unresolved

## Queued
- gemma3:12b eval
- Prospects notifier fix (Petrarch)
- Run removal script on superset3_merged.jsonl (file not on disk yet; script ready at `fine-tuning/scripts/remove_flagged.py`)
- Blog publish prep

## Done (recent)
- Gallery: Langton's Ant + Falling Sand added; sand fire/brush/water fixes (2026-03-08, 3 commits, 49 artifacts live)
- Gallery: 20 missing artifacts added to index + mobile fixes across 12 artifacts (2026-03-07/08, 5 commits)
- Removal script for 10 flagged degenerate entries committed (2026-03-07, `remove_flagged.py`)
- Crystal dendrite DLA walker bug fixed (2026-03-07, 1 commit)
- Workshop deck synced from cuny-ai-lab/gen-dev-foundations fae418b4 (2026-03-07, 1 commit)
- Gallery: Monte Carlo Pi + Ant Colony added (2026-03-07, 1 commit)
- Microblog entries 11 + 12 published: phyllotaxis, Chladni figures (2026-03-06, 2 commits)
- Gallery: 42 artifacts live; ASCII Donut + Crystal Dendrite added (2026-03-06, 1 commit)
- Gallery: 42 artifacts live; Neon Tunnel + Wolfram Automaton added; dropdown nav + mobile responsive overhaul (2026-03-05, 8 commits)
- Microblog: gallery links added to entry-6 and entry-7 (2026-03-05)
- Data validation: 3 source JSONLs confirmed 0 parse errors (2026-03-05)
- Gallery: 39 artifacts live; Spring Wires + Cursor Aura added (2026-03-03, 3 commits)
- Gallery: 36 artifacts live, 3 rendering bugs fixed, Chladni + Julia Set added (2026-03-02, 10 commits)
- gen-dev-foundations workshop deck added to docs (2026-03-02)
- Mobile viewport optimization for latest gallery artifacts (2026-03-02)
- Blog retitled "The Problem with AI Detection"; 18 copyedit rounds, teaching tips page, .docx exports, chainwheel art (2026-02-28, 48 commits)
- Tail-50 QA on toefl_gptoss20b_10k.jsonl: 0 parse errors (2026-02-28)
- Superset3 merge+dedup: 5,560 unique rows (2026-02-27)
- Petrarch's 10k merged into superset2: 14,566 records
- Superset3 QA spot-check: 0 parse errors, valid roles
- Microblog entries 2, 4, 6 published/updated
- GH Pages config fix (serve from /docs)
- 23 commits on 2026-02-27
