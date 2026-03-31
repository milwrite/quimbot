# Master TODO

**Last Updated**: 2025-11-08 (November 8, 2025)
**Previous Update**: 2025-01-28 (9+ months ago)

This file tracks ongoing tasks across the dissertation project. Reference this at the start and end of each session to maintain continuity and ensure systematic progress.

---

## 🚨 CRITICAL PRIORITIES (Immediate Action Required)

### Data Completion - CUNY Hub Gap
- [ ] **Process 1,397 pending users in CUNY database** 🔄 IN PROGRESS
  - Impact: Completes primary dataset (currently ~80% done)
  - Command: `python3 scripts/universal_reddit_scraper.py --subreddit CUNY --db-path databases/current/CUNY_historical_data.db --process-pending`
  - Time: ~26 minutes (94 batches remaining)
  - Status: Restarted 2025-11-09 09:17 after database recovery, Processing batch 1/94
  - Monitor: `tail -f scraper_recovery.log`
  - **Database Recovery**: ✅ SUCCESS - 75,814 comments recovered from corrupted database

### Chapter 2 - Macroscopic Analysis Completion
- [ ] **Complete Sections 2.3-2.6** (need 5,000 more words)
  - [ ] Section 2.3: Linguistic Patterns (CORRECT "won't be able to" stat: 1.60x not 13.63x)
  - [ ] Section 2.4: Network Architecture (add response rate evidence)
  - [ ] Section 2.5: Financial Aid Discourse (integrate 23.7x intensification data)
  - [ ] Section 2.6: Chapter Summary
  - Resources: Use validated stats from `databases/current/scripts/ch2/`
  - Current: 3,029/8,000 words (37.9% complete)

### Chapter 3 - Evidence Integration Backlog
- [ ] **Integrate 68 unprocessed evidence IDs into narrative**
  - [ ] Rate-my-schedule phenomenon (Section 3.2.4)
  - [ ] Coursicle commercial capture (Section 3.5)
  - [ ] Infrastructure decay testimonies
  - [ ] Transit vertical immobility crisis
  - Target: 8,000 words minimum
  - Current: 2,292/18,000 words (13% complete)

---

## 📦 PORTABLE BUNDLE MAINTENANCE (Atomic / Bundle-Safe)

These tasks are intentionally small, local to this writing bundle, and safe to complete without access to the full research repo, live databases, or analysis scripts.

**Execution rule**: complete **one task per pass**. Update this checklist when finished. If a task depends on external data, stop and note the blocker rather than improvising.

**Ownership rule**:
- `Owner: Quimbot` = reserved for Quimbot automation and Quimbot manual passes
- `Owner: Open` = available for Petrarch to claim by editing the line to `Owner: Petrarch`
- once a task is marked `Owner: Petrarch`, Quimbot leaves it alone unless explicitly asked

- [x] **DISS-BUNDLE-01** (`Owner: Quimbot`) — Compared `addendum/methodological_addendum_ai_scaffold 2.md` against `addendum/methodological_addendum_ai_scaffold.md`; files were identical, so the duplicate copy was removed. Completed 2026-03-31.
- [ ] **DISS-BUNDLE-02** (`Owner: Quimbot`) — Create `reference/EVIDENCE_MASTER_ALLOCATION.md` as a scaffold for evidence ownership, chapter placement, conflict notes, and status tracking.
- [ ] **DISS-BUNDLE-03** (`Owner: Quimbot`) — Create `reference/DOC_PAIRS.md` mapping editable Markdown files to their generated `.docx` counterparts, with a clear note on which file is canonical.
- [ ] **DISS-BUNDLE-04** (`Owner: Quimbot`) — Create `visualizations/INDEX.md` listing visualization number, topic, dissertation chapter, and files present in this bundle.
- [ ] **DISS-BUNDLE-05** (`Owner: Open`) — Normalize `drafts.md` entry structure so each item has consistent placement, source, and status fields while preserving the drafted prose.
- [ ] **DISS-BUNDLE-06** (`Owner: Quimbot`) — Create `chapter_drafts/ch1_source_map.md` mapping reusable Chapter 1 prose blocks to target sections in the dissertation.
- [ ] **DISS-BUNDLE-07** (`Owner: Open`) — Create `chapter_drafts/bridge-users/README.md` identifying canonical files, supporting files, and recommended reading order for Chapter 3 bridge-user work.
- [ ] **DISS-BUNDLE-08** (`Owner: Open`) — Do a light formatting-only cleanup pass on `core_docs/progress_reports.md` for headings, spelling, and list consistency without changing substantive claims.
- [ ] **DISS-BUNDLE-09** (`Owner: Quimbot`) — Add a short “bundle limitations” note to `README.md` and/or `CLAUDE.md` explaining which tasks require the full research repo.

## 📝 ACTIVE WRITING TASKS

### Chapter 1: Introduction & Context
- [ ] Complete Section 1.1: Introduction and research questions
- [ ] Expand theoretical framework discussion
- [ ] Add pre-pandemic baseline findings
- Current: 4,780/14,000 words (34% complete)
- Reference implementations: Sections 1.2.2, 1.2.3, 1.3.1

### Methods Chapter (New Priority)
- [ ] Draft computational ethnography methodology section
- [ ] Document user-centric scraping innovation
- [ ] Explain evidence-anchored narrative approach
- [ ] Detail computational snowball sampling parallel
- Target: 6,000-8,000 words

### Evidence Management
- [ ] Create EVIDENCE_MASTER_ALLOCATION.md to prevent cross-chapter conflicts
- [ ] Resolve 14 identified cross-chapter evidence conflicts
- [ ] Establish primary ownership for high-impact IDs (submission_1akbu5y, etc.)
- [ ] Document preview/statistical exception rules

---

## 🔬 ANALYTICAL TASKS

### Recent Discovery Documentation
- [ ] Formalize "rate my schedule" as class anxiety marker analysis
- [ ] Complete Coursicle platform capitalism critique
- [ ] Document AI vernacular pedagogy patterns
- [ ] Synthesize infrastructure decay evidence

### Validation Requirements
- [ ] Verify all Chapter 1 statistical claims against database
- [ ] Cross-reference Chapter 2 temporal patterns
- [ ] Validate Chapter 3 ethnographic testimonies exist in databases
- [ ] Ensure engagement scores (upvotes) are accurate

---

## 🌐 WEBSITE & DISSEMINATION

### Jekyll Site Maintenance
- [ ] Sync October research log entries to website posts
- [ ] Fix remaining evidence page YAML issues
- [ ] Update navigation for new evidence structure
- [ ] Deploy recent changes to GitHub Pages

### Research Documentation
- [ ] Update `dissertation/master_document.md` with October findings
- [ ] Consolidate chronicle/ entries into coherent narrative
- [ ] Archive September handoff metadata properly

---

## 🤖 AGENT ECOSYSTEM COORDINATION

### Documentation Needs
- [ ] Create agent workflow coordination guide
- [ ] Document inter-agent communication patterns
- [ ] Establish agent query pattern library
- [ ] Map agent responsibilities to dissertation chapters

### Active Agents (18 total)
- **Data**: sqlite-query-master, data-quality-validator
- **Research**: research-process-logger, discourse-query-architect
- **Analysis**: vernacular-discourse-analyst, cuny-network-analyst
- **Integration**: research-evidence-integrator, dissertation-orchestrator
- **Specialized**: hypothesis-annotation-manager, reddit-data-recovery-specialist

---

## ✅ COMPLETED RECENTLY (Since January 2025)

### Infrastructure Achievements (November 2025)
- [x] Database corruption recovery (2025-11-09)
  - Advanced SQLite .recover operation
  - 75,814 comments recovered from corrupted table
  - Zero data loss from 2-month collection period
  - Integrity verified: OK status achieved
- [x] Scraper speed optimization (2025-11-08)
  - Rate limits reduced 33% (1.5s → 1.0s content extraction)
  - Batch sizes increased 3x (5 → 15 pending users)
  - Checkpoint frequency optimized (every 5 batches vs every batch)
  - 47% faster processing (~28 min vs 53 min for 1,500 users)

### Major Analytical Breakthroughs
- [x] Class-based linguistic markers ("have to go in person" 16.37x CUNY)
- [x] Transit evidence taxonomy (9,782 discussions, vertical immobility)
- [x] AI vernacular pedagogy emergence (ChatGPT filling support voids)
- [x] Infrastructure decay documentation (500+ facility failures)
- [x] Parenting discourse absence analysis (2.6% rate reveals inequality)
- [x] Pre-pandemic baseline establishment (patterns since 2011)
- [x] Compound crisis typology (679% increase multi-topic discourse)
- [x] Computational snowball sampling methodology
- [x] Warner's publics theory validation (4,447 metadiscourse items)
- [x] Coursicle commercial capture analysis

### Infrastructure Achievements
- [x] Agent ecosystem deployment (18 specialized agents)
- [x] Jekyll evidence pages implementation
- [x] Chronicle directory establishment
- [x] Hypothesis annotation system operational
- [x] Database completion: 7/8 CUNY at 95%+
- [x] NYU expanded to 174K posts
- [x] Columbia collection at 98K posts

---

## 📊 PROJECT METRICS

### Data Collection Status
- **Overall**: 624,336 posts from 55,448 users (93.5% complete)
- **CUNY Core**: 7/8 databases at 95%+ (Baruch, Hunter, Queens, CCNY, Brooklyn, JohnJay, CSI)
- **CUNY Hub**: 77% complete ⚠️ (1,585 pending users)
- **Comparative**: NYU (96.3%), Columbia (93.8%), Fordham (96.8%)

### Writing Progress
- **Chapter 1**: 4,780/14,000 words (34%)
- **Chapter 2**: 3,029/8,000 words (37.9%)
- **Chapter 3**: 2,292/18,000 words (13%)
- **Total**: 10,101/40,000 core chapter words (25.3%)

### Evidence Integration
- **Total Evidence IDs**: ~200 unique across corpus
- **Integrated**: ~120 (60%)
- **Pending**: ~80 (40%)
- **Conflicts**: 14 cross-chapter overlaps

---

## 📅 SESSION CHECKLIST

### At Start of Session
1. **Check data status**: `./query-overview | grep pending`
2. **Review recent research log**: Last 3 entries in `dissertation/research_process_log.md`
3. **Check active scrapers**: `ps aux | grep universal_reddit`
4. **Identify target section**: Which chapter/section will you work on?
5. **Note word count**: Current count for tracking progress

### During Session
- Use `grounded_query_tool.py` for evidence queries
- Document new findings in research_process_log.md
- Track evidence IDs in chapter files
- Commit frequently with descriptive messages

### At End of Session
1. **Update word counts** in chapter headers
2. **Log findings** in research_process_log.md
3. **Document evidence IDs** added to chapters
4. **Commit changes**: `git add . && git commit -m "descriptive message"`
5. **Update this TODO** if priorities shifted

---

## 🗑️ DEPRECATED/REMOVED (No Longer Tracked)

The following items were in January TODO but are completed, abandoned, or deprioritized:

- ~~Hypothesis implementation details~~ (system operational)
- ~~Semantic search optimization~~ (current implementation sufficient)
- ~~Dashboard tool updates~~ (not actively used)
- ~~Conference paper abstracts~~ (premature)
- ~~Cross-institutional linguistic comparison~~ (scope creep)
- ~~Network visualization updates~~ (existing outputs sufficient)
- ~~Baruch orphan recovery~~ (487 orphans acceptable in 138K posts)
- ~~Bibliography management tool~~ (manual process working)
- ~~Automated evidence validation~~ (manual verification preferred)

---

## 📌 NOTES

### Evidence Protocol
- Minimum 2-3 evidence IDs per major claim
- Include engagement scores: (score: 54)
- One primary location per ID, cross-reference elsewhere
- Format: submission_XXXXX or comment_XXXXX

### Query Tools
- **Primary**: `databases/current/scripts/grounded_query_tool.py`
- **Presets**: `query_with_preset.py --preset [name]`
- **Chapter scripts**: `ch1/`, `ch2/`, `ch3/` directories

### Git Workflow
- Lowercase commit messages, no emojis
- No "Co-Authored-By: Claude" signatures
- Descriptive but concise (max 100 chars)

### Critical Paths
1. CUNY pending users → Statistical validity
2. Chapter 2 completion → Committee milestone
3. Chapter 3 evidence → Ethnographic depth
4. Methods chapter → Defensibility

---

*TODO Assessment: This update reflects 9 months of project evolution from data collection to analysis and writing. The shift requires different priorities focused on synthesis rather than infrastructure.*