# Session 2b — Hold-State Memo (2026-03-24)
Status: AWAITING APPROVAL (S2->S3) | No scope expansion

---

## What Happened This Session

Still in hold-state on S2. Gate remains closed pending `APPROVED S2->S3` from milwrite.

Three concrete outputs this session, all within existing scope:

### 1. Citation Stub Resolution (draft_intro.txt)

Applied Petrarch's 2026-03-20 verification results to the intro draft.

**Before:**
- `PMC 2024` — anonymous stub
- `arXiv 2024` — anonymous stub

**After:**
- `Veldre et al. 2024` — Veldre, A. et al., "Language models outperform cloze predictability in a cognitive model of reading," *PLOS Computational Biology*, 20(9). Correct DOI/URL confirmed.
- `Jacobs, Grobol & Tsang 2024` — "Large-scale cloze evaluation reveals that token prediction tasks are neither lexically nor semantically aligned," arXiv:2410.12057. Confirmed correct for divergence argument.

Both reference list entries updated in `drafts/draft_intro.txt`. The inline citation at the empirical paragraph now reads:
> "(Veldre et al. 2024; Jacobs, Grobol & Tsang 2024; Xie et al. 2018)"

### 2. Veldre et al. Framing Flag (open decision)

Petrarch flagged this in s2 verification: Veldre et al. (2024) argues LLM predictability *outperforms* cloze norming for predicting eye-movement data — which cuts against a divergence-as-failure framing. The current intro only says "models systematically misalign with human response distributions," which is too blunt for what Veldre shows.

Recommended reframe (no prose committed yet, awaiting milwrite decision):
> "Veldre et al. (2024) find that LLM predictability outperforms cloze norms as a predictor of eye-movement data — a result that complicates any simple divergence narrative. Better predictor for fixation times is not the same as reader-equivalent comprehension. The divergence the article traces is not a performance failure but a functional one: models optimize toward statistical distributions, not interpretive acts."

This language would live in the evidence section (Session 7), not the intro. The intro citation is fine as-is once the evidence section flags the complication explicitly. Decision needed: retain Veldre as productive complication, or drop?

### 3. Liu et al. 2021 Scope Check

Petrarch flagged that Liu et al. 2021 covers contrastive/generative self-supervised learning broadly, with a CV orientation. The intro currently cites it for self-supervised learning in NLP. Cross-checking against Bommasani et al. 2021, Section 2 — which explicitly covers NLP self-supervised pretraining including masked language modeling — suggests Bommasani is the stronger cite for this specific claim. Recommended action:

> Replace: `(Liu et al. 2021; Bommasani et al. 2021)`
> With: `(Bommasani et al. 2021)` (single citation, stronger NLP coverage)

Not applied yet. This is a one-line change; flag for milwrite confirmation or approve as editorial housekeeping.

---

## Open Items Before S3 Can Begin

| Item | Owner | Status |
|------|-------|--------|
| `APPROVED S2->S3` gate | milwrite | OPEN — blocking |
| Veldre et al. framing decision | milwrite | OPEN — needs decision |
| Para 18 merge confirmation (v03 docx) | milwrite | OPEN — needs confirmation |
| Liu et al. → Bommasani swap | milwrite | OPEN — low-stakes, approve or decline |

---

## State of draft_intro.txt (as of 2026-03-24)

- Citation stubs resolved: 2 of 2 (Veldre, Jacobs/Grobol/Tsang)
- Reference list: clean (no anonymous stubs remaining in intro)
- Prose: unchanged from v03 docx baseline except citation strings
- Contrastive construction flag (session2_holdstate_memo): flagged, not applied
- Pea setup phrase: flagged, not applied
- BERT paragraph opener variation: deferred to Session 9

No new research branches. No scope expansion. Holding for approval.
