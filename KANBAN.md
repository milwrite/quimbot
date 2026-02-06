# Orchestra Kanban Board
**Last Updated:** 2026-02-05 19:00 EST by Petrarch (Evening Stand-up)  
**Update Frequency:** Minimum 2x daily (unless no changes)

## 🌅 Morning Progress (2026-02-05)
**Petrarch:** 
- ✅ Morning sync attempt with Quimbot (timed out, but Quimbot updated KANBAN independently)
- 🔍 Training crash analysis: Stopped at step 16/100, no checkpoints, empty losses array
- 💡 **Recommendation:** Retry with batch_size=32 (was 64), add more verbose error handling, consider max_steps=50 for first successful run
- 📥 **PRIMARY FOCUS:** Starting Tier 1 dataset downloads (OpenHermes-2.5, WAXAL, Magpie priority)
- 📚 Will research handwriting datasets for Movement 2 in parallel

**Quimbot:** Updated KANBAN, awaiting training retry decision  
**Next:** Petrarch begins dataset downloads (07:30 EST start target), Quimbot decides on training retry timing/params

## 🌆 Evening Progress (2026-02-05)
**Petrarch:**
- ✅ Handwriting dataset research completed (07:06) — IAM Database recommended via HuggingFace, MNIST for validation
- ✅ OpenHermes-2.5 downloaded (1.6GB, first Tier 1 dataset complete)
- ✅ Fixed checkpoint path extraction bug (18:01) — tinker:// paths now properly extracted from futures
- ⏸️ WAXAL & Magpie downloads postponed (assisting with training debugging priority)
- 📝 Updated .gitignore to exclude datasets/ directory

**Quimbot:**
- ✅ Fixed checkpoint saving in run_tinker_lora.py (15:00) — added save_weights_for_sampler() calls
- ✅ Training run IN PROGRESS: 12/62 steps (19%) as of 18:55 EST
- ✅ First production checkpoint saved: `tinker://.../step_0010` (verified working)
- 📊 Next checkpoint due at step 20

**Next:** Petrarch resumes Tier 1 downloads (WAXAL, Magpie) tomorrow morning; Quimbot monitors training completion + shares final checkpoint

---

## 🎯 Active Sprint: Linguist Track Fine-Tuning

### Backlog
- [ ] Set up unified ChatML preprocessing pipeline
- [ ] Confirm Qwen3-8B-Base training environment
- [ ] Plan deduplication strategy across datasets
- [ ] Design evaluation metrics for base + secondary fine-tuning

### To Do
- [ ] **[Petrarch]** Debug training crash (analyze logs, check batch size limits, add error handling)
- [ ] **[Petrarch]** Retry training with safer params (batch=32, max-steps=50)
- [ ] **[Petrarch]** Download Tier 1 datasets in parallel (OpenHermes-2.5, Magpie, WAXAL) — 3 priority
- [ ] **[Petrarch]** Research handwriting datasets for Movement 2 (IAM, MNIST, synthetic options)
- [ ] **[Petrarch]** Verify TBD licenses (DialogSum, CS-Dialogue, Prosocial-Dialog, AfriQA, Swahili Parallel) — 5 datasets
- [ ] **[Quimbot]** Review training crash + advise on Tinker API limits/timeouts
- [ ] **[Petrarch]** Submit LMSYS access form (Chat-1M, Arena conversations) — gated but high value
- [ ] **[Petrarch]** Submit SwitchLingua access form — gated multilingual code-switching dataset
- [ ] **[Both]** Design dataset mixing ratios (initial + secondary) — after Tier 1 downloads complete
- [ ] **[Quimbot]** Add QuAC/CoQA + Wizard of Wikipedia to Linguist dataset plan (responsive Q&A)

### In Progress
- [ ] **[Petrarch]** 100-step LoRA training run (ultrachat_train.jsonl) — running overnight, share checkpoints when complete
- [x] **[Petrarch]** Research conversational datasets (10 found) - COMPLETED 2026-02-04 17:56
- [x] **[Petrarch]** Research multilingual/dialect datasets (10 found) - COMPLETED 2026-02-04 18:13

### Review/Blocked
- ⏸️ **[Quimbot]** Movement 2 (Scribe) - Waiting on handwriting dataset source (IAM or alternative)
- ⏸️ **[Quimbot]** Movement 3 (Gamer) - Tinker API resolved, ready to proceed after Movement 1

### Done
- [x] **[Petrarch]** Test GitHub push to milwrite/quimbot repo (2026-02-04 13:56)
- [x] **[Petrarch]** Conversational dataset research + documentation (2026-02-04 17:56)
- [x] **[Petrarch]** Multilingual/dialect dataset research + documentation (2026-02-04 18:13)
- [x] **[Petrarch]** License verification phase 1 (9/20 confirmed, 11 pending - see LICENSE-VERIFICATION.md) (2026-02-04 18:36)
- [x] **[Petrarch]** Created complete LoRA training pipeline with checkpoint saving (train_and_save_lora.py) (2026-02-04 23:30)
- [x] **[Petrarch]** Created inference/comparison script (test_lora_model.py) (2026-02-04 23:30)
- [x] **[Petrarch]** Documented full training workflow (WORKFLOW.md) (2026-02-04 23:30)
- [x] **[Petrarch]** Created formal collaboration protocol (COLLABORATION.md) (2026-02-04 23:40)
- [x] **[Petrarch]** Validated 2-step training run successfully (2026-02-04 21:30)
- [x] **[Quimbot]** Dataset ingestion for Movement 1 (roskoN/dailydialog)
- [x] **[Quimbot]** ChatML preprocessing (train/val/test)

---

## 📋 Task Assignments

### Petrarch's Responsibilities
**Machine:** Zach's Mac Studio (local)  
**Focus:** Dataset research, curation, documentation, file management

**Current Tasks:**
1. ✅ Dataset research (initial conversational + multilingual/dialect) — COMPLETE
2. ✅ License verification phase 1 (17/20 verified) — COMPLETE
3. **NEXT:** Download Tier 1 datasets (6 commercial-OK, ready now)
4. **NEXT:** Verify TBD licenses (5 datasets remaining)
5. Submit gated dataset access forms (LMSYS, SwitchLingua)
6. Pre-processing pipeline design (after downloads)
7. Documentation maintenance (ongoing)

**Daily Commits:**
- Morning: Status update + downloads/verification
- Evening: Progress report + next steps

---

### Quimbot's Responsibilities
**Machine:** Remote (separate instance)  
**Focus:** Model training, Tinker API integration, RL loops

**Current Tasks:**
1. Movement 1 (Linguist): Train on dailydialog with Qwen3‑8B‑Base
   - **Status needed:** Training running? Metrics/logs available?
   - **Blocker check:** jinja2 issue resolved?
2. Movement 2 (Scribe): Source handwriting dataset → train
   - **Blocker:** Handwriting dataset source unclear — handoff to Petrarch for research?
3. Movement 3 (Gamer): Wire RL loop after Tinker API fix
   - **Status:** Ready to proceed after Movement 1

**Daily Commits:**
- Morning: Training progress + metrics
- Evening: Checkpoints + blockers + status report

---

## 🔄 Handoff Protocol

### Petrarch → Quimbot
**When:** Dataset curation complete (preprocessed, deduplicated, ChatML format)  
**Deliverable:** Dataset files + mixing config + training script template  
**Location:** `quimbot/datasets/` (to be created)

### Quimbot → Petrarch
**When:** Model training checkpoint ready  
**Deliverable:** LoRA weights + training logs + evaluation metrics  
**Location:** `quimbot/checkpoints/` (to be created)

---

## 🕐 Live Timer Schedule

### Petrarch Check-ins
- **Morning (10:00 EST):** Review overnight progress, plan day
- **Afternoon (14:00 EST):** Mid-day status update
- **Evening (18:00 EST):** Commit findings, update Kanban

### Quimbot Check-ins
- **Morning (10:15 EST)**
- **Evening (18:05 EST)**

### Coordination Points
- **Daily sync:** Review Kanban, assign new tasks, resolve blockers
- **Handoff events:** Explicit notification in Discord #orchestra channel

---

## 📊 Progress Metrics

### Datasets
- **Conversational:** 10 identified, 0 downloaded, 8/10 licenses verified (2 pending TBD)
- **Multilingual/Dialect:** 10 identified, 0 downloaded, 9/10 licenses verified (1 pending TBD)
- **Total unique languages:** ~80+ (52 XTREME-S, 19 African WAXAL, 31 Fun-ASR, overlapping coverage)
- **Commercial-OK datasets:** 9 ready for immediate download (Tier 1: 6 priority, Tier 2: 3 verify-first)
- **Gated datasets:** 7 requiring form submission (high value: LMSYS Chat-1M/Arena, SwitchLingua, DialogStudio, MultiDialog)
- **Non-commercial:** 1 dataset (CS-FLEURS — evaluate for research use)

### Training
- **Movement 1 (Linguist):** Dataset ready, training TBD
- **Movement 2 (Scribe):** Blocked on dataset sourcing
- **Movement 3 (Gamer):** Ready after Movement 1

---

## 🚧 Blockers

1. ~~**Dataset licenses:** Need verification before download~~ — **RESOLVED** (17/20 verified, 9 commercial-OK ready)
2. **Scribe dataset:** Handwriting dataset source unclear (Quimbot - handoff to Petrarch for research?)
3. ~~**Training environment:** Gemma 3 14B setup~~ — **RESOLVED** (switched to Qwen3-8B-Base)
4. **Movement 1 status:** Training progress unknown — awaiting Quimbot update (running? logs? metrics?)

---

## ✅ Quimbot Training Plan (Movement 1)
- **Backend:** Tinker LoRA
- **Base model:** Qwen/Qwen3-8B-Base
- **Data:** dailydialog (roskoN), ChatML processed
- **Hyperparams:** LR 2e-4, batch 64, epochs 3 (full pass)
- **Output:** qwen3-8b-dialog-lora-v1
- **Status:** Running / logging pending (jinja2 installed; retrying)

## 📝 Notes

- **GitHub workflow:** Both agents push to `milwrite/quimbot` main branch
- **Commit convention:** `[Agent] Action: Description` (e.g., `[Petrarch] Docs: Add multilingual datasets`)
- **Conflict resolution:** Petrarch handles `/research/`, Quimbot handles `/fine-tuning/`, both update `KANBAN.md`
- **Communication:** Discord #orchestra for handoffs, Kanban for async status

---

**Next Update Due:** 2026-02-05 10:00 EST (Petrarch) | TBD (Quimbot)
