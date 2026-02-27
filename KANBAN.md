# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-26 19:00 ET (evening stand-up)_

## ✅ Done
- Overnight local Ollama generation completed: +156 rows total (`92 + 51 + 13` across new outputs)
- Latest clean batch validated: `toefl_ollama_batch_20260224_2130_clean.jsonl` is 21/21 valid
- 07:00 ET stand-up logged in `agents/KANBAN.md` with updated handoff context
- Nightly stocktake artifact created: `reports/nightly/stocktake-2026-02-25.md`
- **2026-02-26 Gallery/Docs Day**: Added kaleidoscope + audiomountain artifacts, microblog entry-5, devlog cleanup
  - Commits: `d14cb71`, `f15d71a`, `6299dab`, `756fa10`

## 🔨 In Progress
**Training pipeline STALLED — Quimbot session blocked by billing error**

### 👇 Waiting on Petrarch
- **URGENT**: Quimbot session funding fix (execute config.patch from morning stand-up)
- Stage 1 Run 4 eval blocker: local path or transfer for adapter weights (step 350 + final)
- Stage 2 direction call: continue local generation push vs pause after merge+dedup

## 📋 Backlog
- Merge the three fresh Ollama outputs into one staging JSONL
- Dedup merged staging data against existing superset and run integrity checks
- Prepare immediate eval launch path for Run 4 checkpoints once weights arrive
- Stage 2 language/learner variant fine-tuning (Spanish SFT datasets scouted: ~1.1M rows from latam-gpt)
- Evaluation framework build-out (`evaluation/` dir exists, needs populating)
- A2A cross-machine delegation (Petrarch ↔ Quimbot task passing)
- Dataset quality metrics / automated filtering (length histograms, role-order checks, near-dup)

## 🚫 Blocked
- **CRITICAL**: Quimbot agent session billing error — cannot execute dataset pipeline work
- Stage 1 Run 4 checkpoint evaluation: adapter weights not on local disk
- OpenRouter scale-out generation: **HTTP 402 Payment Required** (billing/account state)

## 📝 Notes
- **Evening stand-up completed 2026-02-26 19:00 ET**
- Training pipeline completely stalled today due to Quimbot session billing block
- Zero dataset/training commits landed; only gallery/docs work progressed
- **Action required**: Execute funding fix from morning stand-up before training work can resume
- Merge/dedup/eval prep tasks moved to Backlog until session unblocked
- Morning stand-up config.patch options (2 & 3) ready to execute on Quimbot host
