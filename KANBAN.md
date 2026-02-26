# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-26 07:05 ET (morning stand-up)_

## ✅ Done
- Overnight local Ollama generation completed: +156 rows total (`92 + 51 + 13` across new outputs)
- Latest clean batch validated: `toefl_ollama_batch_20260224_2130_clean.jsonl` is 21/21 valid
- 07:00 ET stand-up logged in `agents/KANBAN.md` with updated handoff context
- Nightly stocktake artifact created: `reports/nightly/stocktake-2026-02-25.md`

## 🔨 In Progress
- Merge the three fresh Ollama outputs into one staging JSONL
- Dedup merged staging data against existing superset and run integrity checks
- Prepare immediate eval launch path for Run 4 checkpoints once weights arrive

### 👇 Waiting on Petrarch
- Stage 1 Run 4 eval blocker: local path or transfer for adapter weights (step 350 + final)
- Stage 2 direction call: continue local generation push vs pause after merge+dedup

## 📋 Backlog
- Stage 2 language/learner variant fine-tuning (Spanish SFT datasets scouted: ~1.1M rows from latam-gpt)
- Evaluation framework build-out (`evaluation/` dir exists, needs populating)
- A2A cross-machine delegation (Petrarch ↔ Quimbot task passing)
- Dataset quality metrics / automated filtering (length histograms, role-order checks, near-dup)

## 🚫 Blocked
- Stage 1 Run 4 checkpoint evaluation: adapter weights not on local disk
- OpenRouter scale-out generation: **HTTP 402 Payment Required** (billing/account state)

## 📝 Notes
- Morning stand-up check completed 2026-02-26 07:05 ET.
- Attempted Quimbot session sync via `sessions_send`, but received provider billing error (insufficient credits), so no fresh cross-agent deltas were available at stand-up time.
- No new git commits landed today in this workspace after morning review; progress was coordination + artifacting.
- Core priority remains unchanged: unblock checkpoint eval first; dataset prep runs in parallel.
