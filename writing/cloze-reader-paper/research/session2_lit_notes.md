# Session 2 — Literature Expansion Notes
Date: 2026-03-14 | Status: IN PROGRESS (awaiting approval)

---

## Track 1: MLM Genealogy

### What the intro currently covers
- Taylor 1953 → BERT 2018/2019 in one jump
- Alammar 2019 (illustrated BERT) as secondary gloss
- Self-supervised learning framed through StackOverflow Blog 2025 (flagged for replacement)

### Gaps identified

**1. Distributional semantics bridge**
The contextual prediction insight did not arrive with BERT. It traces through:
- Harris (1952): distributional hypothesis — "words that occur in similar contexts have similar meanings"
- Firth (1957): "You shall know a word by the company it keeps"
These are the philosophical ancestors of the masked objective. The intro skips them, which risks making BERT look like a clean invention rather than an optimization of a long insight.

**Recommendation:** One sentence in the body (not intro) anchoring BERT's masked objective in the distributional tradition. Not needed in the intro, which is already dense.

**2. ELMo — the missing link**
Peters et al. (2018), "Deep contextualized word representations," introduced contextualized embeddings via bidirectional LSTM language modeling. BERT's bidirectionality advances ELMo's approach. The intro's claim that BERT "distinguished it from earlier unidirectional language models" is accurate but incomplete without naming ELMo as the direct predecessor.

CITATION TO ADD:
> Peters, M.E. et al. (2018) 'Deep contextualized word representations', in Proceedings of NAACL-HLT 2018. New Orleans, LA: Association for Computational Linguistics, pp. 2227–2237. Available at: https://aclanthology.org/N18-1202

**3. Self-supervised learning — replace StackOverflow Blog**
The three citations to StackOverflow Blog 2025 for "self-supervised learning" must be replaced. Peer-reviewed alternatives:

Primary:
> LeCun, Y. and Misra, I. (2021) 'Self-supervised learning: The dark matter of intelligence', AI Research, Meta. Available at: https://ai.meta.com/blog/self-supervised-learning-the-dark-matter-of-intelligence/ [NOTE: still a blog, but authoritative; for peer-reviewed, prefer:]
> Liu, X. et al. (2021) 'Self-supervised learning: Generative or contrastive', IEEE Transactions on Knowledge and Data Engineering, 35(1). DOI: 10.1109/TKDE.2021.3090866

FLAGGED FOR PETRARCH: Verify Liu et al. 2021 covers the NLP / masked-LM framing specifically, not just contrastive CV methods. If not, check:
> Bommasani, R. et al. (2021) 'On the opportunities and risks of foundation models', arXiv:2108.07258 — Section 2 covers self-supervised pretraining with NLP genealogy.

**4. BERT → downstream paradigm (scope note)**
The paper does not need to cover RoBERTa, SpanBERT, etc. in the intro. The genealogy can close at BERT. But the body section (Session 7+) should note that masked language modeling as a paradigm persisted — it's not a historical curiosity but a live infrastructure.

---

## Track 2: Cloze Education Research

### Citation repair — PRIORITY 1

**"Pragmatic expectancy grammar" — replace Clozemaster 2026**

Current citation is a blog post. The term traces to:
> Oller, J.W. (1979) Language Tests at School. London: Longman.

Oller coined "pragmatic expectancy grammar" to describe the system of knowledge that language users deploy to generate and interpret utterances — the claim in the draft is sound; the source is not. This is a direct replacement.

SECONDARY:
> Bachman, L.F. (1985) 'Performance on cloze tests with fixed-ratio and rational deletions', TESOL Quarterly, 19(3), pp. 535–556. DOI: 10.2307/3586277

Bachman distinguishes rational deletion (choosing specific words) from fixed-ratio deletion and is relevant to the Cloze Reader's selective word-removal strategy. Worth flagging to Petrarch for optional inclusion in the body.

**Gestalt anchor**
The intro's phrase "Gestalt psychology's concept of 'closure'" is adequate but citationless. Options:
> Koffka, K. (1935) Principles of Gestalt Psychology. New York: Harcourt, Brace and World.
> Wertheimer, M. (1938) 'Laws of organization in perceptual forms', in Ellis, W.D. (ed.) A Source Book of Gestalt Psychology. London: Routledge & Kegan Paul, pp. 71–88.

Koffka is the more authoritative anchor for "closure" specifically.

**Taylor 1953 — confirm URL**
The existing citation links to https://journals.sagepub.com/doi/10.1177/107769905303000401 — this DOI format looks off (the article is from 1953; Journalism Quarterly, not JMCQ). FLAGGED FOR PETRARCH: verify DOI resolves correctly. Standard citation:
> Taylor, W.L. (1953) '"Cloze procedure": A new tool for measuring readability', Journalism Quarterly, 30(4), pp. 415–433.

---

## Track 3: Human/Model Comparative Studies

Both citations in the intro are stubs. EX-03 correctly defers figures to the evidence section, but method notes need to be drafted for the body section writer (Sessions 7+).

### arXiv 2410.12057v2

URL: https://arxiv.org/html/2410.12057v2
Accessed per draft: 2 February 2026

FLAGGED FOR PETRARCH: Identify author(s), title, and confirm this is the cloze-divergence paper. Likely candidate: Takmaz et al. or similar psycholinguistic-norming vs. model-logprob study.

Method note template (to be filled):
- Authors:
- Task design:
- Metric for divergence:
- Corpus/language:
- Key finding for this paper's argument:

### PMC 11458034

URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11458034/
Accessed per draft: 2 February 2026

FLAGGED FOR PETRARCH: Identify author(s), title, confirm this is a cloze-specific human vs. LLM comparison. Determine whether the study uses masked prediction loss or behavioral cloze completion.

Method note template (to be filled):
- Authors:
- Title:
- Task type (masked prediction / fill-in / multiple choice):
- Population (human cohort):
- Key divergence finding:

### Xie et al. 2018 — CLOTH dataset
> Xie, Q. et al. (2018) 'Large-scale cloze test dataset created by teachers', in Proceedings of EMNLP 2018. Brussels: Association for Computational Linguistics, pp. 2344–2356. Available at: https://aclanthology.org/D18-1257/

Per SESSION_STATE.md: verify accuracy figures (50-55% / 86%) directly against this paper. Those figures should not live in the intro anyway (EX-03 resolved this). Confirm they are:
- 50-55%: human baseline on CLOTH
- 86%: BERT or subsequent model performance

If figures differ from paper, do not use them until verified. This is a Priority 2 item.

---

## Open Petrarch Tasks (generated this session)

1. Replace StackOverflow Blog × 3 — provide peer-reviewed self-supervised learning citation covering NLP/masked-LM framing (Liu et al. 2021 or Bommasani et al. 2021)
2. Verify arXiv 2410.12057v2 author/title/method
3. Verify PMC 11458034 author/title/method
4. Confirm Taylor 1953 DOI resolves correctly
5. Optional: assess Bachman 1985 for rational deletion framing in body section
6. Confirm Oller 1979 as replacement for "pragmatic expectancy grammar" citation

---

## Quimbot Tasks (generated this session)

- [ ] EX-04: Replace closing flourish ("something else entirely") with explicit claim language in Session 3 style pass
- [ ] Thesis paragraph sharpening deferred to Session 3 per plan (Priority 3)
- [ ] MLM genealogy insertion (ELMo + distributional semantics) drafted for body — not intro
