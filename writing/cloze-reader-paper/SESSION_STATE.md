# Cloze Reader Paper — Session State

## Paper
- **Title:** Cloze Reader and the Twin Histories of Occlusion
- **Target journal:** Digital Humanities Quarterly (DHQ)
- **Author:** Zach Muhlbauer, CUNY AI Lab / The Graduate Center, CUNY
- **Project URL:** https://reader.inference-arcade.com
- **Repo:** https://github.com/milwrite/cloze-reader

## Schedule
- **Anchor date:** 2026-03-10
- **Cadence:** Every other day at 5:00 PM ET
- **Next session:** 2026-03-10 at 17:00 ET (Session 1)

## Session Log

| # | Date | Focus | Status | Approval |
|---|------|-------|--------|----------|
| 1 | 2026-03-10 | Considerations charter + scope lock | COMPLETE | APPROVED by milwrite (thread decision) |
| 2 | 2026-03-14 | Literature expansion: MLM genealogy, cloze ed research, human/model comparative studies | IN PROGRESS | AWAITING APPROVAL |

## Labor Division
- **Quimbot:** artifact/code analysis, argument structure, prose refinement, consistency checks
- **Petrarch:** literature mapping, historiography, citation audits
- **Joint:** phase-end synthesis memos with open risks

## Approval Protocol
- Gate: milwrite must post `APPROVED S{n}->S{n+1}` before session n+1 begins
- Hold-state (no approval): tighten prose, clean citations, no scope expansion
- Max 3 concrete outputs per session
- No new research branch without prior milwrite approval

## Phases

### Phase 1: Foundation & Framework (Sessions 1–3)
- Session 1 — Scope charter, theoretical anchors, citation gap inventory
- Session 2 — Literature expansion: MLM genealogy, cloze ed research, human/model comparative studies
- Session 3 — Theoretical framework refinement, "twin histories" argument structure

### Phase 2: Close Reading & Analysis (Sessions 4–6)
- Session 4 — Deep Cloze Reader artifact engagement
- Session 5 — Architecture as argument: code rhetoric, selection heuristics, corpus selection
- Session 6 — Player experience, pedagogy, AI-mediated reading debates

### Phase 3: Development & Refinement (Sessions 7–9)
- Session 7 — Draft body sections (genealogy, technical, critical analysis)
- Session 8 — Integration, transitions, evidence-to-claim ratios
- Session 9 — Style pass, voice calibration, AI slop audit

### Phase 4: Verification & Polish (Sessions 10–12)
- Session 10 — Citation verification (URLs, DOIs, DHQ formatting)
- Session 11 — Peer review simulation (hostile + enthusiastic reads)
- Session 12 — Final polish, abstract, keywords, bio/affiliation

## Revision Todo (logged 2026-03-10)

### Priority 1 — Citation repairs (Petrarch)
- [ ] Replace StackOverflow Blog (2025) for "self-supervised learning" claim — find peer-reviewed source
- [ ] Replace Clozemaster (2026) for "pragmatic expectancy grammar" — trace to Oller 1979 or equivalent
- [ ] Add method notes in prose for arXiv (2024) and PMC (2024) citations (dataset scale, task format, limits)

### Priority 2 — Claim discipline (joint)
- [ ] Verify CLOTH accuracy figures (50-55% / 86%) against Xie et al. 2018 directly
- [x] Remove "semantic inbetweenness" terminology entirely

### Priority 3 — Structural tightening (Quimbot)
- [ ] Sharpen thesis paragraph — must generate claim language each section inherits
- [ ] Cut MLM/BERT technical block by ~15% (GLUE score detail, bidirectionality)
- [x] Project Gutenberg framing locked: model substrate, with explicit awareness that re-centering core training materials is a critical artifact construction move

### Priority 4 — Style pass (both)
- [ ] Audit for contrastive constructions ("not X but Y", "more than", "beyond that")
- [ ] Replace weak institutional sources doing conceptual work
- [ ] Humanizer pass: vary sentence openers in BERT paragraph; one precise word per paragraph

### Decisions resolved by milwrite (thread)
1. Cut "semantic inbetweenness" language
2. Migrate empirical figures (CLOTH + PMC/arXiv divergence) out of intro into dedicated evidence section
3. Use Project Gutenberg as substrate framing, with awareness that re-centering core training materials is a critical move in artifact construction

### Session gate status
- Session 1 approved by decision thread
- Session 2 is unblocked with above constraints

## Added Role (2026-03-12)
- Excerptor role added for rewrite support: `writing/cloze-reader-paper/ROLE_EXCERPTOR.md`
- Excerpt log: `writing/cloze-reader-paper/EXCERPTS.md`
- Suggested-edits Word file with track changes: `writing/cloze-reader-paper/docx_versions/cloze_reader_intro_suggested-edits_v02_trackchanges.docx`

## Current Session Deliverable
**Session 2 — Literature Expansion**
Due: 2026-03-14 17:00 ET
Notes: session2_lit_notes.md produced. Six Petrarch tasks queued. Citation repairs drafted for Oller 1979, ELMo, self-supervised learning source. Two PMC/arXiv stubs require Petrarch author/method verification before body can use them. No prose committed until approval.
