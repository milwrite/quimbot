# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-27 19:00 ET (evening stand-up)_

## ✅ Done
- Merge+dedup all sources → superset3 (5,560 unique rows) (`b67bbf4c`) ✅ 2/27
- Morning stand-up sync (2/27 07:00): Coordinated with Quimbot, identified billing block as root cause
- Gallery: Wave Interference + Clifford Attractor (`a20be098`) ✅ 2/27
- Gallery mobile optimization: Turing/voronoi HTML fixes for responsive display
- Microblog entry-6 published: New content in `docs/microblog/entry-6.html`

## 🔨 In Progress
- **TOEFL generation running** — gpt-oss:20b via local Ollama, 1,814/10,000 entries (~78/hr). ETA ~March 2–3.
- Gallery/docs iteration continues
- Superset3 quality validation needed (spot-check)

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
