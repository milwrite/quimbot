# KANBAN.md — Quimbot Project Board

_Last synced: 2026-03-01 07:00 ET (morning stand-up)_

## ✅ Done
- Merge+dedup all sources → superset3 (5,560 unique rows) (`b67bbf4c`) ✅ 2/27
- Morning stand-up sync (2/27 07:00): Coordinated with Quimbot, identified billing block as root cause
- Gallery: Wave Interference + Clifford Attractor (`a20be098`) ✅ 2/27
- Gallery mobile optimization: Turing/voronoi HTML fixes for responsive display
- Microblog entry-6 published: New content in `docs/microblog/entry-6.html`
- Blog post "Writing Under Surveillance" drafted + copyedited through v3.2 (`ed5a581a`)
- TOEFL superset2 merged: 14,566 unique records (Petrarch's gemma3:27b batch deduped + merged)
- Microblog entry-2 (Rubik) + entry-4 (Fourier iframe) published; entry-5 removed
- Gallery bugfix: Clifford attractor var redeclaration (`0b4cf9de`)
- Site cleanup: OpenClaw files removed from repo, .gitignore updated, GH Pages source fixed

## 🔨 In Progress
- **TOEFL gen at 2,834/10,000 — process still stalled** (no active PID found at 07:00 stand-up)
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
- **Morning stand-up 3/1 07:00:** Pulled latest `main` and reviewed board + local runtime/log state.
- **Quimbot sync attempt:** `sessions_send` to label `Quimbot` returned "No session found with label: Quimbot" from this host.
- **Runtime check:** No active TOEFL generation process found (`pgrep`), while Ollama daemon is still running.
- **Log check:** `fine-tuning/generation_qwen72b.log` still ends in OpenRouter HTTP 402 credits error.
- **Cron check:** `fine-tuning/prospects/cron.log` is currently missing on this checkout (previous board note referenced `/bin/sh: 1: openclaw: not found`).
- **Critical path:** Execute billing fix → resume generation/merge pipeline → restore prospects cron visibility/fix → prepare eval launch when adapter weights arrive.
- Gallery/docs work continues unblocked (static generation, no API calls required).
