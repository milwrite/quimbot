# Orchestra Kanban Board
**Last Updated:** 2026-02-04 18:14 EST  
**Update Frequency:** Minimum 2x daily (unless no changes)

---

## 🎯 Active Sprint: Linguist Track Fine-Tuning

### Backlog
- [ ] Verify licenses for all conversational datasets
- [ ] Verify licenses for multilingual/dialect datasets
- [ ] Set up unified ChatML preprocessing pipeline
- [ ] Configure Gemma 3 14B training environment
- [ ] Plan deduplication strategy across datasets
- [ ] Design evaluation metrics for base + secondary fine-tuning

### To Do
- [ ] **[Petrarch]** Download initial conversational datasets (LMSYS-Chat-1M, DialogStudio samples)
- [ ] **[Quimbot]** Complete Movement 1 (Linguist) training with dailydialog
- [ ] **[Petrarch]** Download multilingual datasets (WAXAL, SwitchLingua samples)
- [ ] **[Both]** Design dataset mixing ratios (initial + secondary)

### In Progress
- [x] **[Petrarch]** Research conversational datasets (10 found) - COMPLETED 2026-02-04 17:56
- [x] **[Petrarch]** Research multilingual/dialect datasets (10 found) - COMPLETED 2026-02-04 18:13

### Review/Blocked
- ⏸️ **[Quimbot]** Movement 2 (Scribe) - Waiting on handwriting dataset source (IAM or alternative)
- ⏸️ **[Quimbot]** Movement 3 (Gamer) - Tinker API resolved, ready to proceed after Movement 1

### Done
- [x] **[Petrarch]** Test GitHub push to milwrite/quimbot repo (2026-02-04 13:56)
- [x] **[Petrarch]** Conversational dataset research + documentation (2026-02-04 17:56)
- [x] **[Petrarch]** Multilingual/dialect dataset research + documentation (2026-02-04 18:13)
- [x] **[Quimbot]** Dataset ingestion for Movement 1 (roskoN/dailydialog)
- [x] **[Quimbot]** ChatML preprocessing (train/val/test)

---

## 📋 Task Assignments

### Petrarch's Responsibilities
**Machine:** Zach's Mac Studio (local)  
**Focus:** Dataset research, curation, documentation, file management

**Current Tasks:**
1. Dataset research (initial conversational + multilingual/dialect) ✅
2. Download & verify datasets
3. License verification
4. Pre-processing pipeline design
5. Documentation maintenance

**Daily Commits:**
- Morning: Status update + research/downloads
- Evening: Findings + next steps

---

### Quimbot's Responsibilities
**Machine:** Remote (separate instance)  
**Focus:** Model training, Tinker API integration, RL loops

**Current Tasks:**
1. Movement 1 (Linguist): Train on dailydialog with Gemma 3 14B
2. Movement 2 (Scribe): Source handwriting dataset → train
3. Movement 3 (Gamer): Wire RL loop after Tinker API fix

**Daily Commits:**
- Morning: Training progress + metrics
- Evening: Checkpoints + blockers

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
- **Morning (TBD - set by Quimbot)**
- **Evening (TBD - set by Quimbot)**

### Coordination Points
- **Daily sync:** Review Kanban, assign new tasks, resolve blockers
- **Handoff events:** Explicit notification in Discord #orchestra channel

---

## 📊 Progress Metrics

### Datasets
- **Conversational:** 10 identified, 0 downloaded, 0 verified
- **Multilingual/Dialect:** 10 identified, 0 downloaded, 0 verified
- **Total unique languages:** ~80+

### Training
- **Movement 1 (Linguist):** Dataset ready, training TBD
- **Movement 2 (Scribe):** Blocked on dataset sourcing
- **Movement 3 (Gamer):** Ready after Movement 1

---

## 🚧 Blockers

1. **Dataset licenses:** Need verification before download (Petrarch)
2. **Scribe dataset:** Handwriting dataset source unclear (Quimbot - handoff to Petrarch?)
3. **Training environment:** Gemma 3 14B setup not yet confirmed (Quimbot)

---

## 📝 Notes

- **GitHub workflow:** Both agents push to `milwrite/quimbot` main branch
- **Commit convention:** `[Agent] Action: Description` (e.g., `[Petrarch] Docs: Add multilingual datasets`)
- **Conflict resolution:** Petrarch handles `/research/`, Quimbot handles `/fine-tuning/`, both update `KANBAN.md`
- **Communication:** Discord #orchestra for handoffs, Kanban for async status

---

**Next Update Due:** 2026-02-05 10:00 EST (Petrarch) | TBD (Quimbot)
