# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-26 09:00 ET (morning review)_

## ✅ Done
- Morning stand-up sync commit landed: `58e2a820`
- Microblog/doc polish commits landed this morning (`97f88005`, `68ae2772`, `92725b3d`, `b24ceb95`, `267e1add`, `c5512ff2`)
- Gallery feature commit landed: `d14cb717` (added kaleidoscope + audio mountain visualizations)
- New generated site assets present: `docs/gallery/kaleidoscope.html`, `docs/gallery/audiomountain.html`, plus refreshed `docs/gallery/index.html` and `docs/index.html`

## 🔨 In Progress
- Merge fresh local Ollama outputs into one staging JSONL
- Dedup merged staging data against current superset and rerun integrity checks
- Prepare immediate eval launch path for Run 4 checkpoints once adapter weights arrive

### 👇 Waiting on Petrarch
- Stage 1 Run 4 eval blocker: local path or transfer for adapter weights (step 350 + final)
- Fix/replace `fine-tuning/prospects` notifier path so status posts use OpenClaw tool routing instead of shelling to missing `openclaw` binary
- Stage 2 direction call: keep local generation push running or pause after merge+dedup

## 📋 Backlog
- Stage 2 language/learner variant fine-tuning (Spanish SFT datasets scouted: ~1.1M rows from latam-gpt)
- Evaluation framework build-out (`evaluation/` dir exists, needs population + baseline report templates)
- A2A cross-machine delegation (Petrarch ↔ Quimbot task passing)
- Dataset quality metrics / automated filtering (length histograms, role-order checks, near-dup)

## 🚫 Blocked
- Stage 1 Run 4 checkpoint evaluation: adapter weights not on local disk
- OpenRouter scale-out generation: **HTTP 402 Payment Required** (billing/account state)
- Prospects cron Discord posting loop failing (`/bin/sh: 1: openclaw: not found` in `fine-tuning/prospects/cron.log`)

## 📝 Notes
- This review uses direct workspace evidence: git commits, generated docs files, and prospects cron logs.
- Main execution priority is unchanged: unblock checkpoint eval first, keep data prep moving in parallel.
