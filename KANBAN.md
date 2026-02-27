# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-27 07:00 ET (morning stand-up)_

## ✅ Done
- Morning stand-up sync (2/27 07:00): Coordinated with Quimbot, identified billing block as root cause
- Gallery mobile optimization: Turing/voronoi HTML fixes for responsive display
- Microblog entry-6 published: New content in `docs/microblog/entry-6.html`
- Prior work: Gallery features (kaleidoscope + audio mountain, commit `d14cb717`), microblog polish passes

## 🔨 In Progress
- ⚠️ **Training pipeline stalled** — No merge/dedup/eval work overnight due to Quimbot session billing block
- Gallery/docs iteration continues (mobile optimization, microblog updates)
- Awaiting billing fix to resume: merge local Ollama outputs, dedup against superset, eval prep

### 👇 Waiting on milwrite
- **🔴 CRITICAL: Execute OpenRouter billing fix** — Quimbot session blocked (HTTP 402) since 2/26 morning, blocking all training work
  - Option 1: Top up OpenRouter account
  - Option 2: Execute config.patch to rotate to funded API key (command ready from 2/26 AM stand-up)
- Stage 1 Run 4 eval blocker: Provide adapter weights location/transfer path (step 350 + final checkpoint)
- Stage 2 direction call: Keep local generation push running or pause after merge+dedup completes

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
- **Morning stand-up 2/27 07:00:** Coordinated with Quimbot via sessions_send. Confirmed zero training pipeline activity overnight.
- **Root cause identified:** Quimbot session billing block (HTTP 402 since 2/26 AM) prevents all model-dependent work.
- **Critical path:** Execute billing fix → resume merge/dedup → fix prospects cron → prepare eval launch when weights arrive.
- Gallery/docs work continues unblocked (static generation, no API calls required).
