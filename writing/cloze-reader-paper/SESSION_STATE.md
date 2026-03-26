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
| 2 | 2026-03-14 | Literature expansion: MLM genealogy, cloze ed research, human/model comparative studies | COMPLETE | AWAITING milwrite |

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
- Excerptor role added for rewrite support: `tools/ROLE_EXCERPTOR.md`
- Excerpt log: `EXCERPTS.md`
- Suggested-edits Word file with track changes: `docx_versions/cloze_reader_intro_suggested-edits_v02_trackchanges.docx`

## Current Session Deliverable
**Session 2 — Literature Expansion**
Due: 2026-03-14 17:00 ET
Notes: session2_lit_notes.md produced. Six Petrarch tasks queued. Citation repairs drafted for Oller 1979, ELMo, self-supervised learning source. Two PMC/arXiv stubs require Petrarch author/method verification before body can use them. No prose committed until approval.

## Open Items — Next Session
- [ ] Para 18 (hint system): scaffolding citations already in drafts/draft_intro.txt — confirm merge into docx v04
- [ ] EX-04: replace "something else entirely" with specific claim language the body sections can inherit
- [ ] Citation chain integration: v03 docx produced 2026-03-18, track changes on

## v03 Docx Status (2026-03-18)
- `cloze_reader_intro_suggested-edits_v03.docx` — 37 paragraphs, track changes enabled
- Citation chain applied: StackOverflow Blog/Clozemaster removed; Bommasani, Oller, Bachman, Peters, Gao, Carlini, Vygotsky, Wood/Bruner/Ross, Pea added
- Closing revision applied: "Pretraining reduces text to token distributions. The blank makes that reduction legible as loss, and refilling it demonstrates what the model, having processed the same passage, cannot do: read it."

## Session 2b Verification Results (Petrarch, 2026-03-20)

### Citation repairs resolved:
1. **SSL ×3** → Liu et al. 2021, "Self-supervised learning: Generative or contrastive," IEEE TKDE. DOI: 10.1109/TKDE.2021.3090866. Covers MLM/NLP. Bommasani stays as secondary.
2. **arXiv 2410.12057** → Jacobs, Grobol & Tsang (2024), "Large-scale cloze evaluation reveals that token prediction tasks are neither lexically nor semantically aligned." ✅ correct for divergence argument.
3. **PMC 11458034** → Veldre et al. (2024), "Language models outperform cloze predictability in a cognitive model of reading," PLOS Comput Biol. ⚠️ FLAGGED: argues LLM predictability *outperforms* cloze norming for eye-movement data. Does not support divergence-as-failure framing. Quimbot recommendation: reframe as productive complication (better predictor ≠ comprehension). Decision needed from milwrite before Session 7.
4. **Taylor 1953 DOI** → Confirmed correct. 403 = paywall, not dead link.
5. **Bachman 1985** → Recommend integrating in Session 5 body section (architecture as argument).
6. **Oller 1979** → Already integrated in s2_v2 lit review draft. No further action.

### Gate status
- Session 2 complete pending `APPROVED S2->S3` from milwrite
- One open decision: Veldre et al. — retain as reframe or drop?

## Thursday Hold-State Pass (Quimbot, 2026-03-26) — v38→v39

Applied Petrarch's v38 closing block to draft file (was in SESSION_STATE but not yet merged). Draft now current at v39. PROP-01 and PROP-02 still held. No scope expansion.

---

## Wednesday Para-Level Pass (Petrarch, 2026-03-25) — v37→v38

### Closing block rewrite (Continuity and Asymmetry section)
Final two paragraphs condensed into one. Five violations cleared:
- "by way of metonym, which is to say" — colon-bypass circumlocution, cut
- "an act of occlusion that foregrounds" — setup phrase disguised as participle, cut
- "decentered by the advent of LLMs" — melodramatic banned construction, cut
- "totalized through extraction and foreclosure at scale" — invented academic noun phrase, cut
- "by virtue of its low-latency engine" — factually wrong (LLMs are not low-latency), whole final paragraph deleted

### New closing paragraph (v38):
> Pretraining reduces text to token distributions. The blank makes that reduction visible: one word absent from a passage the model was trained on, now requiring a reader to supply what statistical weighting cannot. Filling it demands close reading: attending to what the surrounding sentence contributes before committing to an answer. The model selected that word through the same regularities by which it was trained. It cannot return to the passage and read it. The game asks players to do exactly that.

### Structural proposals (HOLD for milwrite):
- **PROP-01:** "Cloze Reader returns a practice..." paragraph — second-abstract problem: mid-body paragraph describes what the paper does without advancing a claim. Candidate for cut or rewrite as a genuine claim.
- **PROP-02:** Floating citation paragraph ("Recent work on cloze, predictability...") — one sentence, three citations, no synthesis. Integrate into surrounding argument or cut.

Both held. No action until milwrite approves.

## Veldre et al. Ruling (milwrite, 2026-03-26)
- **Decision: CUT** — paper's argument around cloze/prediction doesn't yet have clear enough shape to situate Veldre appropriately. "Divergence-as-failure framing" was Quimbot's frame, not the paper's thesis. Remove Veldre from citation list for now.
- Revisit in Session 7 when body sections are drafted and the argument has its proper form.
- No other source fills this slot in the interim.

## Wednesday Pass Reversal (milwrite, 2026-03-26)
- **Petrarch's v38 closing paragraph REJECTED** by milwrite — "violates basically every rule in the style guide"
- **Original paragraph restored as authoritative:** "Pretraining reduces text to token distributions, and the blanked-out word makes that selection and reduction of human language legible by way of metonym..." (full text in HTML draft)
- The HTML draft never received the v38 change — original was always intact there
- The docx v38 version should NOT be carried forward; treat v37 closing as current
- "totalized through extraction and foreclosure at scale" — milwrite confirms this language is correct and should stay
