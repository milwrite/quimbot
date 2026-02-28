# KANBAN.md — Quimbot Project Board

_Last synced: 2026-02-27 19:00 ET (evening stand-up)_

## ✅ Done
- **Evening stand-up sync (2/27 19:00):** Reviewed full day progress with Quimbot
- **Data pipeline (2/27 AM):** Superset3 merge complete — 5,560 unique records (commit `b67bbf4`)
- **Gallery expansion:** Wave Interference + Clifford Attractor visualizations added
- **Gallery fixes:** clifford.html variable redeclaration bug fixed
- **Blog post:** "Writing Under Surveillance" draft v1 + copyedit published
- **Microblog updates:** Entry-2 (Rubik walkthrough) added, entry-4 (Fourier) live iframe, cleanup passes
- **Repo maintenance:** GitHub Pages fixes, OpenClaw cleanup, gitignore updates
- **Prior:** Morning stand-up (2/27 07:00), gallery mobile optimization, microblog entry-6

## 🔨 In Progress
- **Training eval prep:** QA superset3 dataset (5,560 records), verify integrity
- **Gallery/docs iteration:** Ongoing polish and expansion
- **Billing status:** Partially resolved (functional at 7:02 AM), current state unclear

### 👇 Waiting on milwrite
- **🟡 OpenRouter billing:** Partially resolved (merge worked at 7:02 AM), full status unclear
- **🔴 Stage 1 Run 4 eval:** Provide adapter weights location/transfer path (step 350 + final checkpoint)
- **Stage 2 direction call:** Keep local generation push or pause after merge+dedup complete

## 📋 Backlog
- **Prospects cron fix:** Replace shell `openclaw` call with proper tool routing (assigned to Petrarch)
- **Superset3 QA:** Verify integrity of 5,560-record merged dataset
- **Evaluation framework:** Build-out `evaluation/` dir (baseline report templates, metrics)
- Stage 2 language/learner variants (Spanish SFT: ~1.1M rows from latam-gpt)
- A2A cross-machine delegation (Petrarch ↔ Quimbot task passing)
- Dataset quality metrics / automated filtering (length histograms, role-order checks, near-dup)

## 🚫 Blocked
- **Stage 1 Run 4 eval:** Adapter weights not on local disk (waiting on milwrite for source path)
- **Training runs:** No active training (waiting on weights + eval results)
- **Prospects cron:** Discord posting loop failing (`/bin/sh: 1: openclaw: not found`)

## 📝 Notes
- **Evening stand-up 2/27 19:00:** Reviewed day's work — superset3 merge shipped early, gallery/blog updates throughout day, training eval still blocked on adapter weights.
- **Billing partial resolution:** Superset3 merge completed at 7:02 AM suggests Quimbot session was functional, but no further training activity detected afterward.
- **Tomorrow's priority:** QA superset3, fix prospects cron, coordinate adapter weight transfer.
- **Data pipeline:** 5,560 unique records in superset3, ready for training once eval unblocked.
- Gallery/docs work continues unblocked (static generation, no API dependencies).
