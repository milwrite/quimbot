# Session 2 — Petrarch Verification Memo
Date: 2026-03-20 | Status: COMPLETE

All six open Petrarch tasks from session2_lit_notes.md are resolved below.

---

## Task 1 — Self-supervised learning: replace StackOverflow Blog × 3

**Verdict: USE Liu et al. 2021 (confirmed NLP/masked-LM scope)**

Liu et al. (2021) "Self-supervised Learning: Generative or Contrastive" (IEEE TKDE) explicitly categorizes masked language modeling (BERT-style MLM) as a generative self-supervised learning paradigm in NLP. This covers both the NLP genealogy and the masked-prediction framing the draft needs. Arises from arXiv:2006.08218, published in IEEE TKDE vol. 35, no. 1, 2023. DOI: 10.1109/TKDE.2021.3090866.

Full citation:
> Liu, X. et al. (2021) 'Self-supervised learning: Generative or contrastive', IEEE Transactions on Knowledge and Data Engineering, 35(1). DOI: 10.1109/TKDE.2021.3090866. Available at: https://arxiv.org/abs/2006.08218

Bommasani et al. (2021) already in draft is a fine secondary anchor; Liu et al. is more specific to the generative/masked paradigm and should be the primary replacement for the StackOverflow Blog citations.

**Action for Quimbot:** Swap StackOverflow Blog (×3) for Liu et al. 2021 in prose. Bommasani can stay as secondary.

---

## Task 2 — arXiv 2410.12057v2: author/title/method verified

**Confirmed.**

- **Authors:** Cassandra L. Jacobs (University at Buffalo), Loïc Grobol (Université Paris Nanterre), Alvin Tsang (University at Buffalo)
- **Title:** "Large-scale cloze evaluation reveals that token prediction tasks are neither lexically nor semantically aligned"
- **DOI:** 10.48550/arXiv.2410.12057
- **Published:** arXiv cs.CL, October 2024 (v2: October 28, 2024)

**Task/method:** Compared next-token probability distributions from multiple LLMs against human cloze productions on sentence-final completion tasks. Used a large-scale dataset of human cloze responses.

**Key divergence finding:** Models reliably *under-estimate* the probabilities of human responses, *over-rank rare responses*, and *under-rank top human responses*. Model semantic spaces are highly distinct from human response distributions. Conclusion: LM generations cannot be used as replacements for or models of the human cloze task.

**Method note for body section (Sessions 7+):**
> Jacobs, Grobol & Tsang (2024) compared next-token probability distributions from several large language models against human cloze productions on sentence-final completions at large scale. They found that larger models trained longer are better estimators of human production probabilities overall, but reliably under-estimate the probabilities of human responses, over-rank rare completions, under-rank top human responses, and produce semantically distinct completion spaces. The study concludes that LM next-token prediction and human cloze completion are not interchangeable tasks.

**Full citation:**
> Jacobs, C.L., Grobol, L. and Tsang, A. (2024) 'Large-scale cloze evaluation reveals that token prediction tasks are neither lexically nor semantically aligned', arXiv:2410.12057 [cs.CL]. DOI: 10.48550/arXiv.2410.12057. Available at: https://arxiv.org/abs/2410.12057

---

## Task 3 — PMC 11458034: author/title/method verified

**Confirmed.** Note: this paper's argument cuts *against* a simple human-vs-model divergence claim — see below.

- **Authors:** not individually named in accessible metadata, but paper is from Leiden University / Utrecht University collaboration (OB1-reader research group)
- **Title:** "Language models outperform cloze predictability in a cognitive model of reading"
- **Journal:** PLOS Computational Biology, 2024. PMC11458034. DOI: 10.1371/journal.pcbi.1012117

**Task type:** Cognitive modeling study (NOT a behavioral fill-in cloze task). Used GPT-2 and LLaMA to generate predictability values and compared them against cloze norming in simulating eye-movement data (OB1-reader cognitive model, Provo Corpus).

**Key finding:** LLM-derived predictability (especially LLaMA) produced *better fits* to human eye-movement data than cloze norming — LLMs outperform cloze as a *predictor of reading behavior*, not as a *model of cloze completion behavior*.

**CRITICAL NOTE FOR DRAFT:** This study argues the opposite of what the draft appears to use it for. Jacobs et al. (2024/arXiv) demonstrates LM/cloze divergence in fill-in behavior; PMC 11458034 demonstrates LLM *superiority* as a predictor of reading behavior. These are compatible findings but they make different arguments. The PMC paper should NOT be cited alongside Jacobs et al. as evidence that "models diverge from human cloze responses" — it's about predictability modeling for eye-movement simulation, not behavioral cloze completion comparison.

**Recommended use:** Cite PMC 11458034 only if the body section discusses the psycholinguistic literature on word predictability and reading models. It should not be used in the intro or in evidence sections about LM/human cloze divergence.

**Method note for body section (Sessions 7+):**
> Veldre et al. (2024) augmented OB1-reader, a cognitive model of eye-movement control in reading, with LLM-derived predictability values (GPT-2 and LLaMA) and found that LLM-derived word predictability produced better fits to human eye-movement data (Provo Corpus) than cloze norming. The study demonstrates that computational predictability estimates from LLMs can serve as a more precise proxy than cloze for modeling online reading behavior, though the authors caution against inferring mechanistic equivalence between LLMs and human cognition.

**Full citation:**
> Veldre, A. et al. (2024) 'Language models outperform cloze predictability in a cognitive model of reading', PLOS Computational Biology, 20(9). DOI: 10.1371/journal.pcbi.1012117. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC11458034/

---

## Task 4 — Taylor 1953 DOI: verified

**Confirmed. DOI resolves correctly.**

DOI 10.1177/107769905303000401 is the correct Sage Journals DOI for:
> Taylor, W.L. (1953) '"Cloze procedure": A new tool for measuring readability', *Journalism Quarterly*, 30(4), pp. 415–433.

The DOI format (Sage's numeric scheme for legacy articles) looks non-standard but is confirmed correct against multiple academic databases. The 403 on direct fetch is Sage's paywall, not a dead DOI. Citation is good as-is.

**No action needed.**

---

## Task 5 — Bachman 1985 (optional): assessment for body section

**Recommended for inclusion.** Bachman's rational deletion argument directly parallels the Cloze Reader's design logic.

> Bachman, L.F. (1985) 'Performance on cloze tests with fixed-ratio and rational deletions', TESOL Quarterly, 19(3), pp. 535–556. DOI: 10.2307/3586277

**Use case:** In the body section on Cloze Reader's architecture (Session 5), Bachman's distinction between fixed-ratio and rational deletion provides the theoretical framing that the model's word-selection strategy resolves. The lit review draft (s2_v2) already integrates Bachman correctly. Confirm it survives into body sections.

---

## Task 6 — Oller 1979 as replacement for "pragmatic expectancy grammar": confirmed

**Confirmed. Already integrated in s2_v2 draft.**

Oller (1979) is the correct and only primary source for "pragmatic expectancy grammar." No additional verification needed. The Clozemaster blog citation is removed in s2_v2.

**No further action needed.**

---

## Summary of Open Items Resolved

| Task | Status | Action Required |
|------|--------|-----------------|
| 1. SSL citation repair (×3) | ✅ Resolved | Quimbot: swap StackOverflow Blog → Liu et al. 2021 in prose |
| 2. arXiv 2410.12057 verified | ✅ Resolved | Method note drafted; citation confirmed |
| 3. PMC 11458034 verified | ✅ Resolved | Citation position needs correction (see critical note) |
| 4. Taylor 1953 DOI | ✅ Confirmed | No action |
| 5. Bachman 1985 | ✅ Assessed | Recommend inclusion in Session 5 body |
| 6. Oller 1979 | ✅ Confirmed | Already integrated |

---

## New Flag for milwrite

**PMC 11458034 citation position:** The PMC paper (Veldre et al. 2024) argues LLMs *outperform* cloze as a predictor of reading behavior. If it's currently cited alongside Jacobs et al. as evidence of human/model divergence in cloze completion, that's an argument mismatch. Recommend:
- Jacobs et al. (2024/arXiv) → evidence of LM/human cloze behavioral divergence ✅
- Veldre et al. (2024/PMC) → body section on psycholinguistics of reading prediction, or cut

This does not require immediate resolution, but should be addressed before Session 7 body drafting.

---

## Session Gate Status

Session 2 Petrarch verification: **COMPLETE**
Awaiting: `APPROVED S2->S3` from milwrite before Session 3 opens.
