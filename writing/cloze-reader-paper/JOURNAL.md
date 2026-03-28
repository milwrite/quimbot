# Cloze Reader Paper — Shared Journal

**Project:** Cloze Reader and the Twin Histories of Occlusion  
**Journal:** Running log of sessions, decisions, edits, and open questions  
**Contributors:** Petrarch + Quimbot  
**Repo:** <https://github.com/milwrite/quimbot>  
**Live draft:** <https://milwrite.github.io/quimbot/cloze-reader-draft/>

---

## 2026-03-10 — Session 1 (Petrarch)

**Focus:** Theoretical anchors and citation gap inventory

Completed annotated bibliography of 15 sources across five clusters: media archaeology (Kittler, Ernst, Chun), LLM critique (Bender et al., Crawford, Shankar), educational psychology (Taylor, Jongsma, Abraham & Chapelle, Xie et al.), pre-BERT NLP (Peters, Devlin, Radford), DH critical making (Ratto, Bogost). Gap map identified five structural problems in the draft: a 65-year hole in cloze test research, an absent pre-BERT NLP trajectory, no theoretical grounding for "artifact as argument," weak epistemological scaffolding for the prediction/comprehension distinction, and no empirical analysis of Cloze Reader's own output.

**milwrite decisions (thread):** Cut "semantic inbetweenness" language. Migrate dense CLOTH metrics out of intro into a dedicated evidence section. Use Project Gutenberg as substrate framing with explicit awareness that re-centering core training materials is a critical move in artifact construction.

---

## 2026-03-14 — Session 2, Part 1 (Quimbot)

**Focus:** Prose revision, argument structure, citation integration

Rewrote introduction paragraphs for concision and claim discipline. Replaced "The modern genealogy of this idea runs through..." with a tighter four-sentence sequence (Harris/Firth → Mikolov → ELMo → BERT) that names each step without overclaiming its significance. Added Bommasani et al. (2021) to BERT paragraph for "implicitly induced rather than explicitly constructed" framing. Integrated Oller (1979) to replace Clozemaster blog for "pragmatic expectancy grammar." Rebuilt Oller paragraph to lead with his contribution rather than with "subsequent research developed."

Opened `EXCERPTS.md` to track specific suggested edits with rationale. Four excerpts logged (EX-01 through EX-04). EX-04 flags the closing line "waiting to be read by a human who interprets context through something else entirely" as underspecified for structural carry-through.

**Style decisions applied:** No contrastive "not X but Y." No melodramatic transformation claims. Bounded claims throughout.

---

## 2026-03-16 — Session 2, Part 2 (Quimbot)

**Focus:** Further prose tightening, em-dash audit, v14 → v19 on live site

Audited all em-dashes. Rule applied: em-dashes only when enclosing a parenthetical phrase on both sides; never as sentence pivots or trailing beats. Removed all non-enclosing instances from Cloze Reader section. Rewrote chat panel sentence to eliminate run-on construction. Version bumped to v19 on live site.

Scaffolding citations integrated into hint system paragraph: Wood, Bruner & Ross (1976) and Vygotsky (1978) as theoretical grounding; Pea (2004) as productive challenge (static scaffolding does not meet original contingency criteria — acknowledged as a deliberate design constraint rather than a flaw).

---

## 2026-03-18 — Citation Chain Session (Petrarch)

**Focus:** Citation chain analysis, words 1000–2000; Gutenberg rationale paragraph

Traced three undercited concepts in the 1000–2000 word range:

1. **Self-supervised learning** — three StackOverflow Blog citations replaced with Devlin et al. (already present) + Bommasani et al. (2021)
2. **Scaffolded hint system** — zero citations for a technical term; added Wood/Bruner/Ross, Vygotsky, Pea
3. **Corpus provenance** — "statistical residue" claim had no grounding; added Carlini et al. (2021) on LLM memorization and Gao et al. (2020) on The Pile

Drafted Gutenberg rationale paragraph at milwrite's direction. Core argument: Gutenberg texts have been flattened into parameter weights, unattributed and unacknowledged; Cloze Reader works against this flattening by positioning the model as one layer of a call stack rather than the whole of it. Closing sentence: "Pretraining reduces text to token distributions. The blank makes that reduction legible as loss, and refilling it demonstrates what the model, having processed the same passage, cannot do: read it."

Gitelman and Jackson (2013) *Raw Data Is an Oxymoron* added to support "mythology of raw data" framing.

**Style corrections this session:**
- "pretraining's reduction of text to token distributions" → nominalization cut, split into two sentences
- Em-dash rule reinforced: enclosing phrases only
- "not just local syntactic constraints" → removed per style guide

**Committed as v20 to live site.**

---

## Style Rules (running record)

| Rule | Source | Date |
|---|---|---|
| No "not just / more than / beyond that / rather than" pivots | milwrite | 2026-03-10 |
| No melodramatic overcommitment ("restructuring," "transforming") | milwrite | 2026-03-10 |
| Bounded claims — say what events *demonstrated*, not what they caused | milwrite | 2026-03-10 |
| Em-dashes only when enclosing a phrase on both sides | milwrite | 2026-03-18 |
| No nominalized verb phrases as subjects | milwrite | 2026-03-18 |
| Avoid vague intensifiers ("clearly," "obviously," "fundamentally") | SOUL.md | ongoing |
| Evidence before interpretation | SOUL.md | ongoing |
| No listicles — write in paragraphs | project standard | ongoing |
| **Invented noun phrases**: cut compounds that sound scholarly but have no disciplinary grounding ("LLM-derived predictability," "semantic inbetweenness"). Do not cut established terms of art — "extraction," "foreclosure," "totalization" have real critical theory genealogies. Check peer-reviewed literature before cutting. | milwrite | 2026-03-25 |
| **Factual accuracy before style**: do not cut a phrase on stylistic grounds if it carries a factual error. Identify the error, correct the mechanism, preserve the argumentative function. | milwrite | 2026-03-25 |
| **"which is to say"**: permitted when it genuinely glosses a term or unpacks a compressed claim. Cut it when it merely restates what the previous clause already said. | milwrite | 2026-03-28 |

---

## Open Questions

- [ ] EX-04: "waiting to be read by a human who interprets context through something else entirely" — needs replacement with claim language body sections can inherit (Quimbot)
- [ ] StackOverflow Blog still appears in para body text (3 occurrences) — replace with Devlin + Bommasani in prose (Petrarch, next session)
- [ ] Empirical analysis of Cloze Reader output — what words does the model actually select? Does difficulty correlate with educational research findings? (Quimbot, Session 4+)
- [ ] Gitelman framing in Gutenberg para: confirm "applies with particular force" is not an overcommitment per style rules
- [ ] Thesis paragraph (closing of intro) — sharpen claim language so body sections have specific assertions to develop

---

## Version Log

| Version | Date | Summary |
|---|---|---|
| v1 | 2026-03-09 | Original draft submitted by milwrite |
| v14 | 2026-03-16 | Quimbot rewrites: cleaner genealogy, Oller, ELMo/BERT tightened |
| v15–v19 | 2026-03-16/17 | Em-dash audit, chat panel sentence, scaffolding citations |
| v20 | 2026-03-18 | Approved Gutenberg rationale para (Petrarch); Carlini, Gao, Gitelman integrated |>>>>>>> 7f6ef9e07405464285fa6a2360e0f3259e64dd86

---

## 2026-03-15 | Off-day | Quimbot | TOEFL batch generation

10,000 TOEFL examples generated to `fine-tuning/data/toefl_batch_20260315.jsonl`. Zero parse errors. Running total: ~29,133 pre-merge with superset5. Superset7 later built: 39,133 unique entries from superset5 + batch_0315 + batch_0317.

---

## Open Items (as of 2026-03-18)

- [ ] Formal `APPROVED S1->S2` token from milwrite before Session 2 scope opens
- [ ] Petrarch: commit session deliverables to shared repo (not local machine only)
- [ ] Verify CLOTH accuracy figures against Xie et al. 2018 directly
- [ ] arXiv (2024) and PMC (2024): add author + method notes in prose
- [ ] EX-04: milwrite rejected Quimbot candidate closing (2026-03-18 17:08) — current closing is milwrite's own version (v22), keep as is
- [ ] Session 3 does not open until S2 is formally approved
