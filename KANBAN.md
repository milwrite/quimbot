# Orchestra Kanban Board
**Last Updated:** 2026-02-22 19:00 EST by Quimbot (Evening Stand-up)

## Current State

### Stage 1 LoRA Training — COMPLETE ✅
- **Run 4** (Feb 21): 671 steps, 14 checkpoints, Qwen3-8B, rank 16, batch 64, lr 1e-4
- Dataset: `stage1_mix_v3` — 43,170 records (LMSYS 40.8% / Magpie 25.5% / TOEFL 20.4% / Prosocial 10.2% / Pilot 3.2%)
- Final checkpoint: `tinker://1409ede0-689d-53a9-af07-a2426cf4f218:train:0/sampler_weights/final`
- Log: `fine-tuning/data/stage1_run4_v3.log`

### Repo Reorganized (Feb 22)
- Commit `9fed895`: flattened `agents/` → root, moved scripts into `fine-tuning/scripts/` and `tools/`
- Workspace migrated from `~/.openclaw/workspace` to `~/Quimbot`

### Gallery / Site
- 25 gallery visualizations built (HTML pages)
- Site redesigned as 3-tab hub: Creative Coding / Workflows / Dev Docs
- README updated with gallery, models, side quests

---

## 🎯 Active Sprint

### To Do
- [ ] **[Quimbot]** Evaluate Run 4 checkpoints — compare step 350 vs final perplexity, run inference samples
- [ ] **[Quimbot]** Reorganize `fine-tuning/prospects/` — integrate useful parts, archive rest
- [ ] **[Both]** Design Stage 2 dataset (Spanish SFT candidates: 5 from latam-gpt, ~1.1M rows)
- [ ] **[Both]** Register Saturday 10PM cron for weekly site curation meeting (blocked on gateway restart)

### In Progress
- [ ] **[Quimbot]** Run 4 eval — perplexity analysis started, cloud eval stalled on final step

### Done (Recent)
- [x] Stage 1 Run 4 complete — 671 steps, 14 checkpoints (Feb 21)
- [x] Repo reorganization by file type (Feb 22)
- [x] Workspace migration to ~/Quimbot (Feb 22)
- [x] Discord ecosystem audit (Feb 22)
- [x] README + site hub redesign (Feb 21)
- [x] Gallery: 25 visualizations (heat diffusion, Turing patterns, harmonograph, etc.)
- [x] Stage 1 mix v3: filtered 5 overlong samples from v2 (Feb 20)

---

## 🚧 Blockers
1. **Gateway token mismatch** — cron, browser tools unavailable until `openclaw gateway restart`
2. **OpenRouter 402** — milwrite account, status unknown
3. **Run 4 eval** — cloud eval stalled at final checkpoint, need retry or local alternative

---

## 📋 Next Milestones
1. Evaluate Run 4 → pick best checkpoint
2. Stage 2 dataset design (multilingual + domain expansion)
3. Stage 2 training run
