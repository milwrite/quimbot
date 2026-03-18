# Cloze Reader Paper — Working Journal

**Paper:** Cloze Reader and the Twin Histories of Occlusion  
**Journal:** Digital Humanities Quarterly  
**Authors:** Zach Muhlbauer (CUNY AI Lab / The Graduate Center, CUNY)  
**Repo:** https://github.com/milwrite/quimbot  
**Live draft:** https://milwrite.github.io/quimbot/cloze-reader-draft/

---

## Protocol

Both bots append entries here after each session, hold-state pass, or significant decision.
Format: `## YYYY-MM-DD | Session N | [Quimbot/Petrarch] | [focus]`

Approval gates remain in SESSION_STATE.md. This journal is the running narrative record.

---

## 2026-03-10 | Session 1 | Quimbot | Scope lock + considerations charter

**Work completed:**
- Locked paper scope to one central claim: Cloze Reader is a critical artifact that exposes structural continuity between educational cloze testing and masked language modeling, while making their functional asymmetry legible through play.
- Hard exclusions: no RAG excursions, no extended AI literacy survey, no comparative Inference Arcade analysis.
- Stabilized four theoretical anchors: Taylor's Gestalt-derived closure; self-supervised learning as training objective; human/model divergence evidence; Cloze Reader architecture as selection/interpretation split.
- Section flow locked: genealogy → divergence evidence → artifact architecture → critical stakes.
- Citation gap inventory flagged: StackOverflow Blog (×3), Clozemaster (×2), arXiv/PMC method stubs, CLOTH figures unverified.

**Open questions for milwrite (resolved in thread):**
1. "Semantic inbetweenness" → cut
2. Empirical figures → migrate to dedicated evidence section
3. Project Gutenberg framing → model substrate, with critical awareness

**Status:** Milwrite approved direction via thread. Formal `APPROVED S1->S2` token pending.

---

## 2026-03-14 | Hold-state pass | Quimbot | Literature expansion notes

**Work completed (notes only, no prose committed):**
- Track 1 (MLM genealogy): distributional hypothesis anchor (Harris/Firth); ELMo cited as BERT precursor; Bommasani et al. 2021 identified as peer-reviewed SSL definition source.
- Track 2 (Cloze education): Oller 1979 traced for "pragmatic expectancy grammar"; Clozemaster citation flagged for replacement; Koffka 1935 identified as missing Gestalt anchor; Bachman 1985 flagged as optional body section source.
- Track 3 (Human/model comparative): method note templates drafted for Petrarch to complete; CLOTH figures deferred from intro per milwrite's decision.

**Six tasks queued for Petrarch:** StackOverflow ×3 replacements, Taylor DOI verification, arXiv + PMC author/method resolution.

---

## 2026-03-15 | Off-day | Quimbot | TOEFL batch generation

10,000 TOEFL examples generated → `fine-tuning/data/toefl_batch_20260315.jsonl`. Zero parse errors. Running total: ~29,133 pre-merge with superset5.

---

## 2026-03-18 | Citation chain pass | Quimbot + Petrarch | Words 1–2000

**Method:** Identify 3 most frequent concepts, trace each to origin/challenge/refinement/current status.

**Quimbot (words 1–1000):**
- Cloze procedure: replaced Clozemaster → Oller 1979 + Bachman 1985; added ELMo precursor sentence (Peters et al. 2018); StackOverflow Blog ×3 → Bommasani et al. 2021.
- Gestalt closure: Koffka 1935 already present; Wertheimer 1923 optional for body.
- MLM/SSL: Bommasani et al. 2021 as primary SSL definition source.

**Petrarch (words 1000–2000):**
- Corpus provenance: Gao et al. 2020 (The Pile) + Carlini et al. 2021 (verbatim memorization).
- Scaffolding: Wood, Bruner & Ross 1976 + Vygotsky 1978 + Pea 2004; static-hints constraint framed as design choice.
- Self-supervised learning: Bommasani 2021 for prompt opacity sentence.

**Closing sentence revised (milwrite + Petrarch collaboration):**
> "Pretraining reduces text to token distributions, and the blanked-out word makes that selection and reduction of human language legible by way of metonym, which is to say, through an act of occlusion that foregrounds how Gutenberg Project texts have been broken down, mathematized, and rendered into training data. The act of inferring the word from context, read against the summary and hint mechanisms, therefore requires human players to partake in precisely the sort of close reading practices that have been decentered by the advent of LLMs, reacquainting them with otherwise flattened or forgotten texts that have been totalized through extraction and foreclosure at scale. At the same time, the process demonstrates what the model, having processed the same passage and selected a word to occlude, cannot do by virtue of its low-latency engine: read, or better yet, read slowly."

**Style rules added today:**
- No em-dashes as parentheticals (all converted to periods, commas, colons, or parentheses)
- No verb phrase nominalizations
- Chat panel sentence rewrite pattern: comma-chained participials → direct subject-verb construction

**Live draft:** v22 | ~2,670 words | https://milwrite.github.io/quimbot/cloze-reader-draft/

---

## Open Items (as of 2026-03-18)

- [ ] Formal `APPROVED S1->S2` token from milwrite
- [ ] Petrarch: push session deliverables to shared repo (not local machine only)
- [ ] Verify CLOTH accuracy figures (50-55% / 86%) against Xie et al. 2018 directly
- [ ] arXiv (2024) and PMC (2024) citations: add author + method notes in prose
- [ ] EX-04: milwrite rejected Quimbot candidate closing — current closing is milwrite's version (v22), keep as is
- [ ] Session 3 does not open until S2 is formally approved
