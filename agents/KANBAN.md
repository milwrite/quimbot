# Orchestra Kanban Board
**Last Updated:** 2026-02-10 07:00 EST by Petrarch (Morning Stand-up)  
**Update Frequency:** Minimum 2x daily (unless no changes)

## 🌅 Morning Stand-up (2026-02-10)
**Petrarch:**
- ✅ Repo synced (already up to date)
- ✅ Reviewed KANBAN status — evening update shows `dataset-review.md` deliverable (2026-02-09)
- ⚠️ Quimbot session not active at morning standup
- 📊 **Current state**: Dataset curation complete (4.5GB), evaluation framework v2 ready, on-policy training scripts status unknown
- 🔍 **Awaiting**: Quimbot session activation to coordinate next phase

**Quimbot:**
- ⚠️ Session not active at standup time
- 📋 Last known deliverable: `dataset-review.md` (pedagogical justification for Stage 1 dataset mix)
- ❓ Status unknown: on-policy sampling/scoring scripts, Stage 1 retraining timeline

**Next:**
- Petrarch: Monitor for Quimbot session activation
- Quimbot (when active): Share progress on LoRA-ROADMAP.md implementation and Stage 1 retraining plans
- Both: Coordinate on-policy training workflow implementation

---

## 🌆 Evening Stand-up (2026-02-09)
**Petrarch:**
- ✅ Evening sync completed (Quimbot session not active)
- ✅ Reviewed new commit: `dataset-review.md` added to repo (by OpenClaw Agent, 5 hours ago)
- 📝 Dataset review provides rationale for Stage 1 dataset choices (LMSYS, Magpie, Prosocial, UltraChat, TOEFL scaffolding)
- 🔍 No other progress since morning standup
- ⏸️ Awaiting Quimbot session activation to coordinate on-policy training implementation

**Quimbot:**
- ⚠️ Session not active at evening standup
- ✅ Deliverable: dataset-review.md (pedagogical justification for dataset mix)
- 📊 Status unknown: on-policy sampling/scoring scripts, Stage 1 retraining plans

**Next:**
- Petrarch: Continue monitoring for Quimbot session activation
- Quimbot (when active): Share progress on on-policy training scripts + Stage 1 retraining timeline
- Both: Coordinate implementation of LoRA-ROADMAP.md workflow

---

## 🌅 Morning Stand-up (2026-02-09)
**Petrarch:**
- ✅ Repo synced (pulled latest: LoRA-ROADMAP.md, SCAFFOLDING_TAXONOMY.md, DEVLOG updates)
- ✅ Reviewed Stage 1 eval results (`stage1_eval.json`): LoRA model shows more concise responses vs base
- ✅ Reviewed new deliverables: scaffolding taxonomy (10 pedagogical patterns), on-policy fine-tuning roadmap
- 🔍 Quimbot session not active; proceeding with documentation review and next steps planning
- 📊 Key finding: LoRA model removes verbose thinking patterns, responds more directly

**Quimbot:**
- ⚠️ Session not active at standup time
- 📝 Recent deliverables (overnight): LoRA-ROADMAP.md (on-policy training workflow), SCAFFOLDING_TAXONOMY.md (adaptive scaffolding patterns)
- ✅ Prior work: evaluation framework v2, repo reorganization, model testing complete

**Next:**
- Petrarch: Review TOEFL11 extraction requirements, plan dataset mixing based on scaffolding taxonomy
- Petrarch: Assess on-policy training pipeline requirements per LoRA-ROADMAP.md
- Quimbot (when active): Share status on Stage 1 retraining and next checkpoint plans
- Both: Coordinate on implementing on-policy sampling/scoring/training scripts

---

## 🌅 Morning Stand-up (2026-02-08)
**Petrarch:**
- ⏳ No new deliverables reported overnight
- 🔍 Continuing TOEFL11 extraction + dataset mixing design
- 🧠 Ready to proceed once Quimbot shares eval metrics from final checkpoint

**Quimbot:**
- ✅ Fixed `test_lora_model.py` sampling API (SampleResponse.sequences)
- ✅ Reran evaluation on final checkpoint; outputs saved to `lora_test_results.json`
- ✅ Synced repo status updates to STATUS + RUNLOG

**Next:**
- Quimbot: Share eval metrics summary with Petrarch
- Petrarch: Begin TOEFL11 scaffolding pattern extraction + mixing ratios once metrics reviewed
- Both: Coordinate Stage 1 retraining parameters

---

## 🌙 Evening Stand-up (2026-02-07)
**Petrarch:**
- ⏳ No new deliverables reported since morning update
- 🔍 Still prioritizing TOEFL11 extraction + data mixing design

**Quimbot:**
- ⏳ No new deliverables since morning update
- 🧪 Still need to run `test_lora_model.py` on final checkpoint

**Next:**
- Petrarch: Begin TOEFL11 scaffolding pattern extraction after checkpoint metrics arrive
- Petrarch: Design dataset mixing ratios for Stage 1
- Quimbot: Share evaluation metrics from final checkpoint
- Both: Coordinate on Stage 1 retraining parameters

---

## 🌅 Morning Stand-up (2026-02-07)
**Petrarch:**
- 📋 KANBAN synced (repo up to date)
- ⏳ Awaiting Quimbot's checkpoint evaluation results
- 📝 Ready to proceed with dataset work once test metrics available
- 🔍 Priority today: TOEFL11 extraction + data mixing design

**Quimbot:**
- ⏳ No new deliverables to report overnight
- 🧪 Still need to run `test_lora_model.py` on final checkpoint

**Next:**
- Petrarch: Begin TOEFL11 scaffolding pattern extraction if Quimbot reports checkpoint success
- Petrarch: Design dataset mixing ratios for Stage 1
- Quimbot: Share evaluation metrics from final checkpoint
- Both: Coordinate on Stage 1 retraining parameters

---

## 🌆 Evening Progress (2026-02-06)
**Petrarch:**
- ⏳ No new deliverables reported since morning update
- 🔎 Awaiting next steps on dataset mixing + preprocessing plan

**Quimbot:**
- ✅ Training confirmed complete (63 steps, all checkpoints saved)
- 🧪 Pending: run `test_lora_model.py` with final checkpoint

**Next:** Petrarch proceeds with TOEFL11 extraction + mixing script + ChatML preprocessing; Quimbot runs `test_lora_model.py` and reports metrics

## 🌅 Morning Stand-up (2026-02-06)
**Petrarch:**
- ✅ Training run COMPLETED overnight (63 steps, 18:44 EST Feb 5)
- ✅ All checkpoints saved: step_0010 through step_0060 + final
- ✅ Base path: `tinker://1d70c787-fc09-5de9-9922-4fcf062f7c80:train:0/sampler_weights/`
- ✅ Datasets downloaded overnight (4.5GB total for Stage 1):
  - LMSYS Chat-1M (2.4GB, 1M conversations, 154 languages)
  - Magpie (2.0GB, 300K filtered examples)
  - Prosocial Dialog (91MB, 120K safety-focused dialogues)
  - TOEFL11 error annotations (6K+ learner errors)
  - *(WAXAL 1.3GB archived in stage2-variants/ for future use)*
- ✅ Two-stage architecture designed (CUNY Language Learning approach)
- ✅ Shifted pedagogy from "error correction" to "adaptive scaffolding"
- ✅ All documentation committed to GitHub

**Quimbot:**
- ✅ Training confirmed complete (63 steps, all checkpoints saved)
- 🧪 Ready to run `test_lora_model.py` with final checkpoint

**Next:**
- Petrarch: Extract TOEFL11 error patterns → Generate scaffolding dialogues
- Petrarch: Design data mixing script (combine all datasets per ratios)
- Petrarch: Preprocess to ChatML format
- Petrarch: Prep for Stage 1 retraining (500-1000 steps)
- Quimbot: Test/evaluate final checkpoint with test_lora_model.py

---

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

## 🌆 Evening Progress (2026-02-04)
**Petrarch:** Dataset research phase complete (20 datasets identified, 17/20 licenses verified, 9 ready for download)  
**Quimbot:** DEVLOG created, model switched to Qwen3-8B-Base, Movement 1 training environment prepared  
**Next:** Petrarch begins downloads (Tier 1), Quimbot monitors/reports Movement 1 training status


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
- [ ] **[Petrarch]** ~~Download Tier 1 datasets~~ — COMPLETE (OpenHermes, Magpie downloaded; WAXAL moved to stage2-variants)
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

**Next Update Due:** 2026-02-06 10:00 EST (Petrarch) | 2026-02-06 18:05 EST (Quimbot)
