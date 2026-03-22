# Session 2 — Hold-State Memo
Date: 2026-03-18 | Status: AWAITING APPROVAL (S2->S3)

This memo records hold-state work completed while S2 approval is pending.
No scope expansion. Three outputs: prose audit flags, citation status update, EX-04 candidate language.

---

## 1. Prose Audit Flags (draft_v14.md)

### Contrastive constructions to cut
Per SOUL.md rules, "not X but Y" constructions must go. In draft_v14:

**Closing paragraph of "Continuity and Asymmetry":**
> "The convergence between Taylor's procedure and masked language modeling is real, grounded in the shared insight that contextual prediction offers a window onto linguistic competence. The purposes differ. Taylor wanted to measure comprehension. BERT's developers wanted to induce representations."

This is clean. No contrastive structure, direct statements. Keep as-is.

**Intro paragraph 4 (draft_intro.txt):**
> "The argument is not that masked language modeling misappropriated an educational technique, nor that the cloze procedure anticipated neural network training..."

This IS a contrastive construction. Recommended replacement:
> "The convergence is real and grounded in a shared insight: contextual prediction offers a window onto linguistic competence. The purposes differ. Taylor wanted to measure comprehension. BERT's developers wanted to induce representations."
(Already incorporated in v14. Confirm draft_intro.txt v03 docx matches v14 closing.)

**Para 18 / hint system block:**
The phrase "a limit Pea (2004) would recognize as a departure from the original scaffolding criteria" is a setup phrase ("a limit X would recognize"). Recommend:
> "Pea's (2004) criteria would mark this as a departure from original scaffolding — the hints are static, not adaptive, and this constraint is itself a design choice."

### Sentence opener variation — BERT paragraph (body section)
In "The Machine Learning Genealogy," five consecutive sentences open with "The [noun]":
- "The structural resemblance..."
- "The technical trajectory..."
- "The limitation..."
- "The masked language modeling objective..."
- "The paradigm..."
Vary at least two openers before final draft. Flag for Session 9 style pass.

### Weak institutional source doing conceptual work
`Liu et al. (2021)` cited for self-supervised learning — Petrarch flagged that this covers contrastive CV methods primarily, not masked-LM NLP genealogy. If Liu et al. 2021 does not cover NLP framing: replace with `Bommasani et al. (2021)` Section 2, which is already in the reference list and does cover self-supervised pretraining with NLP genealogy. This is a citation swap, not new research.

---

## 2. Citation Status Update

| Citation | Status | Action |
|----------|--------|--------|
| StackOverflow Blog 2025 | REMOVED in v03 docx | Replaced with Bommasani et al. 2021 |
| Clozemaster 2026 | REMOVED in v03 docx | Replaced with Oller 1979 |
| Liu et al. 2021 | IN USE — verify scope | Petrarch task: confirm NLP coverage |
| PMC 2024 | Stub — no author/method | Petrarch task: verify before body use |
| arXiv 2024 (2410.12057) | Stub — no author/method | Petrarch task: verify before body use |
| Carlini et al. 2021 | In v03 docx references | Verify URL active |
| Gao et al. 2020 (The Pile) | In v03 docx references | Verify URL active |
| Wood, Bruner & Ross 1976 | In v03 docx references | Good — no action |
| Vygotsky 1978 | In v03 docx references | Good — no action |
| Pea 2004 | In v03 docx references | Good — no action |

**Two open Petrarch tasks before body sections can cite PMC 2024 and arXiv 2024:**
1. Identify authors and method for PMC 2024 (pmc.ncbi.nlm.nih.gov/articles/PMC11458034/)
2. Identify authors and method for arXiv 2024 (arxiv.org/html/2410.12057v2)

---

## 3. EX-04 Candidate Language

EXCERPTS.md flags that the closing of the "something else entirely" passage needs replacement with claim language the body sections can inherit.

v14 closing paragraph of "Continuity and Asymmetry" currently reads:
> "Pretraining reduces text to token distributions, and the blanked-out word makes that selection and reduction of human language legible by way of metonym, which is to say, through an act of occlusion that foregrounds how Gutenberg Project texts have been broken down, mathematized, and rendered into training data. The act of inferring the word from context, read against the summary and hint mechanisms, therefore requires human players to partake in precisely the sort of close reading practices that have been decentered by the advent of LLMs, reacquainting them with otherwise flattened or forgotten texts that have been totalized through extraction and foreclosure at scale. At the same time, the process demonstrates what the model, having processed the same passage and selected a word to occlude, cannot do by virtue of its low-latency engine: read, or better yet, read slowly."

This is evocative but the phrase "by virtue of its low-latency engine" is mechanism-obscuring. "Low-latency engine" does not carry the theoretical weight the sentence needs.

**Candidate replacement for inherit-chain close (EX-04):**
> "The blank makes reduction legible as loss. Refilling it demonstrates what the model, having processed the same passage, cannot do: read it — which is to say, integrate syntax, discourse history, and world knowledge toward a local interpretive act rather than a probability assignment. This is the asymmetry the paper traces: prediction optimized at scale is not comprehension, and Cloze Reader uses game mechanics to hold the two apart long enough for players to feel the difference."

This gives body sections three inheritable claim threads:
- Reduction-legibility (architecture-as-argument section)
- Interpretive act vs. probability assignment (empirical evidence section)
- Game mechanics as critical instrument (design analysis section)

---

## 4. Para 18 Merge Confirmation Needed

SESSION_STATE.md open item:
> "Para 18 (hint system): scaffolding citations already in draft_intro.txt — confirm merge into docx v04"

v03 docx was produced 2026-03-18 with track changes. Before v04 is opened, milwrite should confirm whether the scaffolding citations (Wood/Bruner/Ross 1976, Vygotsky 1978, Pea 2004) are visible as tracked insertions or already accepted in v03. If accepted, v04 can treat them as baseline and no merge is needed.

---

## Summary

- Prose: 4 specific flags (contrastive construction, sentence openers, Pea setup phrase, "low-latency engine")
- Citations: 2 stubs pending Petrarch verification (PMC 2024, arXiv 2024); 1 scope check (Liu 2021)
- EX-04: candidate close language drafted, three inheritable claim threads identified
- Para 18: merge status requires milwrite confirmation on v03 docx state

No new research branches opened. No scope expansion. Ready for S3 on approval.
