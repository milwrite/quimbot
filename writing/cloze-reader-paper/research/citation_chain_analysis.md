# Citation Chain Analysis — Cloze Reader Draft Intro
## Quimbot: Words 1–1000 | Petrarch: Words 1000–2000

---

## Quimbot Zone (Words 1–1000)

Three concepts recur most frequently across this section:
1. Cloze procedure (as comprehension assessment)
2. Masked language modeling / self-supervised learning
3. Gestalt closure

---

### Concept 1: The Cloze Procedure

**Origin:**
- Taylor, W.L. (1953). "Cloze Procedure": A New Tool for Measuring Readability. *Journalism Quarterly*, 30(4), 415–433.
- Derived from Gestalt psychology's "closure" concept; Taylor adapted it as a readability/comprehension measure. First presented at the 1953 AEJ convention. No prior formal cloze procedure exists — this is the clear origin.

**Challenge:**
- Bormuth, J.R. (1967). Cloze readability procedure. *Elementary English*, 44(4), 429–436.
  - Challenged Taylor's fixed-deletion model: proposed ratio-based deletions rather than every-nth-word, argued the method needed standardization to be psychometrically valid.
- Oller, J.W. (1979). *Language Tests at School: A Pragmatic Approach*. Longman.
  - Reconceptualized what cloze measures: not just readability but "pragmatic expectancy grammar" — a holistic proficiency measure. Challenged the earlier readability-only framing by arguing cloze taps a general language competence factor.

**Refinement:**
- Bachman, L.F. (1985). Performance on cloze tests with fixed-ratio and rational deletions. *TESOL Quarterly*, 19(3), 535–556.
  - Distinguished rational (selective) from fixed-ratio deletion. Cloze Reader uses rational/selective deletion — this is the refinement most directly relevant to the artifact.
- Abraham, R.G. & Chapelle, C.A. (1992). The meaning of cloze test scores. *Modern Language Journal*, 76(4), 468–479.
  - Extended to L2 validity: challenged the assumption that cloze measures the same construct across native and non-native speakers. Contested the unitary-proficiency claim.

**Current Status: Contested.**
The foundational procedure is settled (Taylor 1953 is unambiguous origin), but what cloze *measures* remains contested. The Oller unitary-trait hypothesis (cloze = general language proficiency) was later challenged; most current researchers treat cloze as measuring a specific form of contextual prediction rather than global competence. Cloze Reader implicitly takes this narrower view.

**Citations to integrate in draft (words 1–1000):**
- Replace Clozemaster (2026) with: `(Oller 1979; Bachman 1985)`
- Add Koffka (1935) already present — keep
- Taylor 1953 DOI: `https://journals.sagepub.com/doi/10.1177/107769905303000401` — verify format

---

### Concept 2: Masked Language Modeling / Self-Supervised Learning

**Origin:**
- Devlin, J., Chang, M-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of NAACL-HLT 2019*, 4171–4186. https://aclanthology.org/N19-1423.pdf
- MLM in BERT: 15% token masking, bidirectional context prediction. Devlin et al. explicitly note the connection to Taylor's cloze procedure in framing their task.

**Predecessor chain (missing from draft):**
- Mikolov, T. et al. (2013). Distributed representations of words and phrases and their compositionality. *Advances in NeurIPS 26*.
  - Distributional hypothesis operationalized at scale; establishes contextual prediction as a training objective before transformers. Anchor sentence for the body, not intro.
- Peters, M.E. et al. (2018). Deep contextualized word representations (ELMo). In *Proceedings of NAACL-HLT 2018*, 2227–2237. https://aclanthology.org/N18-1202/
  - Direct predecessor. ELMo uses bidirectional LSTMs; BERT addresses ELMo's shallow bidirectionality with deep transformer encoding. **The intro currently implies BERT arrived from nowhere — one sentence citing Peters et al. 2018 fixes this.**
- Radford, A. et al. (2018). Improving language understanding by generative pre-training (GPT). OpenAI Blog.
  - Simultaneous unidirectional approach (left-to-right). BERT's bidirectionality is a direct response to GPT's architectural limitation.

**Challenge:**
- Liu, Y. et al. (2019). RoBERTa: A robustly optimized BERT pretraining approach. arXiv:1907.11692.
  - Showed BERT was undertrained; challenged the original hyperparameter/training choices. Refinement rather than conceptual challenge.
- Bommasani, R. et al. (2021). On the opportunities and risks of foundation models. arXiv:2108.07258. https://arxiv.org/abs/2108.07258
  - Broader theoretical challenge: asks what self-supervised pretraining actually produces and what emergent capabilities mean. The framing of "foundation models" displaces BERT-specific MLM discussion into a larger paradigm question. **Best peer-reviewed replacement for StackOverflow Blog (2025) for the self-supervised learning definition.**

**Refinement:**
- The transformer architecture itself: Vaswani, A. et al. (2017). Attention is all you need. *Advances in NeurIPS 30*, 5998–6008.
  - BERT's encoder stack is built on this. Optional addition to the body genealogy section; not needed in the intro.

**Current Status: Settled as training technique, contested as theory of language.**
MLM as a training objective is now standard; the conceptual question of what the models learn from it (prediction vs. comprehension) is exactly what the paper intervenes on. The Bommasani et al. 2021 framing helps the paper position itself within ongoing debate rather than treating MLM as closed.

**Citations to integrate (words 1–1000):**
- Replace all three StackOverflow Blog (2025) citations with: `(Bommasani et al. 2021)` for the self-supervised learning definition
- Add: `(Peters et al. 2018)` one sentence before BERT introduction to establish ELMo as precursor
- Keep Devlin et al. (2019) — already correct
- Keep Alammar (2019) — useful explainer, can stay as secondary

---

### Concept 3: Gestalt Closure

**Origin:**
- Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II. *Psychologische Forschung*, 4, 301–350.
  - The original formulation of Gestalt organizing principles, including closure (Geschlossenheit). **This is the deeper anchor, though Koffka 1935 is the standard English-language citation.**
- Koffka, K. (1935). *Principles of Gestalt Psychology*. Harcourt, Brace & World. [Archive.org: https://archive.org/details/in.ernet.dli.2015.7888]
  - Systematized closure as a perceptual principle in English; the standard citation for this concept in the anglophone literature. Already in the draft.

**Challenge:**
- No major challenge to the closure concept itself in the literature Taylor drew on. The concept transferred from visual perception to language without significant resistance in the educational psychology context.

**Refinement:**
- Taylor's adaptation is itself the key refinement: applying a visual/perceptual principle to linguistic comprehension. This is the conceptual move the intro describes.

**Current Status: Settled (in the perceptual psychology sense). Transferred and adapted in Taylor's cloze work.**

**Citation action:** Koffka (1935) already in draft. Wertheimer (1923) is optional for the body if the paper wants to deepen the Gestalt genealogy, but not required in the intro.

---

## Revised Citation Insertions for Words 1–1000

### Replace StackOverflow Blog (2025) × 3:

**Before:**
> ... provided a self-supervised learning objective... (StackOverflow Blog 2025). Because the value of each masked word... (StackOverflow Blog 2025). The cloze-like task represented what researchers termed a "self-supervised learning" objective... (StackOverflow Blog 2025).

**After:**
> ... provided a self-supervised learning objective that could leverage vast quantities of unannotated text (Bommasani et al. 2021). Because the value of each masked word was already present in the original text, large-scale language models could be trained on billions of words without human labeling, a practical advantage over supervised approaches (Devlin et al. 2019). The cloze-like task represented what researchers termed a "self-supervised learning" objective, wherein supervisory signals are present within the data itself rather than requiring human annotation (Bommasani et al. 2021).

### Replace Clozemaster (2026) × 2:

**Before:**
> ...rested on what researchers termed the "pragmatic expectancy grammar," where test-takers employ the same linguistic prediction mechanisms... (Clozemaster 2026)... requiring readers to understand semantic relationships... (Clozemaster 2026).

**After:**
> ...rested on what researchers termed the "pragmatic expectancy grammar," where test-takers employ the same linguistic prediction mechanisms and rule systems they bring to any authentic language comprehension scenario (Oller 1979). This assumption suggested that cloze tests measure not discrete vocabulary knowledge but integrated comprehension abilities, requiring readers to understand semantic relationships, grammatical constraints, discourse coherence, and contextual appropriateness simultaneously (Oller 1979; Bachman 1985).

### Add ELMo precursor sentence:

**Insert before BERT paragraph:**
> Prior to BERT, ELMo (Peters et al. 2018) had demonstrated that bidirectional language representations improved performance across NLP tasks, though its bidirectionality was achieved by concatenating separately trained left-to-right and right-to-left LSTMs rather than through deep joint training.

---

## New Reference Entries to Add

```
Bachman, L.F. (1985) 'Performance on cloze tests with fixed-ratio and rational deletions', TESOL Quarterly, 19(3), pp. 535–556.

Bommasani, R. et al. (2021) 'On the opportunities and risks of foundation models', arXiv:2108.07258. Available at: https://arxiv.org/abs/2108.07258

Koffka, K. (1935) Principles of Gestalt Psychology. New York: Harcourt, Brace & World. Available at: https://archive.org/details/in.ernet.dli.2015.7888

Oller, J.W. (1979) Language Tests at School: A Pragmatic Approach. London: Longman.

Peters, M.E. et al. (2018) 'Deep contextualized word representations', in Proceedings of NAACL-HLT 2018. New Orleans, LA: Association for Computational Linguistics, pp. 2227–2237. Available at: https://aclanthology.org/N18-1202/
```

**Remove:**
- StackOverflow Blog (2025) — all three instances
- Clozemaster (2026) — both instances
