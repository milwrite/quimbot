# Cloze Reading and Twin Histories of Occlusion

**Zach Muhlbauer**
The Graduate Center, CUNY
<https://reader.inference-arcade.com>

---

## Introduction

Cloze reading began as a simple procedural idea. Delete words from a passage at regular intervals, require the reader to supply the missing terms, and treat the accuracy of their restorations as a measure of how well they understood the surrounding text. Taylor (1953) drew on the Gestalt principle of closure, the perceptual tendency to complete incomplete familiar patterns described by Koffka (1935), and reframed it as a methodology for gauging reading comprehension holistically rather than through isolated subskills. The approach tested whether a reader could bring syntax, semantics, and discourse knowledge to bear on a single missing word, and the results suggested that this kind of contextual prediction tracked genuine comprehension in ways that syllable-counting and sentence-length measures could not. The intervention proved durable enough to migrate from educational psychology into computational laboratories, where cloze-like objectives now structure how machines learn language.

The modern genealogy of this idea runs through the emergence of masked language modeling as a core training objective for large language models. Early distributional-theory work anchored the intuition that word meaning is shaped by surrounding context (Harris 1954; Firth 1957), and Mikolov et al. (2013) showed that context-aware embeddings arise from predictive objectives trained at scale. Peters et al. (2018) introduced deep contextualized representations with ELMo, generating word-level encodings sensitive to sentential context through bidirectional LSTM language modeling, and Devlin et al. (2019) formalized BERT, whose bidirectional attention over masked tokens redefined how models internalize language by training on a cloze-like objective across billions of words of unannotated text. The shared motif across this trajectory is that contextual prediction serves as a lever for linguistic competence, whether interpreted as a human ability to infer missing content or as a statistical signal that refines model parameters through gradient descent.

Cloze Reader sits at the intersection of these two lines. It preserves the cloze prompt as a human-facing task while delegating word removal to a language model guided by heuristic instructions, and this design foregrounds both the continuity of the cloze premise across seventy years of research and the divergence in how the removal process operates and what it reveals about the system performing it. The paper traces these genealogies, interrogates empirical divergences between human and model performance on cloze tasks, and presents Cloze Reader's architectural decisions as a critical instrument for examining what prediction-based training actually produces.

## The Educational Genealogy of Cloze

Wilson Taylor's 1953 procedure was formally simple. Delete words from a passage at fixed intervals and ask readers to supply what was missing. The theoretical ambition behind it was larger. Taylor adapted the Gestalt principle of closure as a framework for measuring reading comprehension holistically, and where prior readability instruments counted syllables and sentence lengths, the cloze procedure tested whether readers could integrate semantic, syntactic, and contextual knowledge simultaneously to recover a deleted word from the evidence surrounding it (Taylor 1953).

Subsequent research developed both the theoretical account and the practical scope of the procedure. Oller (1979) formalized the mechanism underlying cloze performance as "pragmatic expectancy grammar," the system of linguistic knowledge that allows readers and speakers to anticipate what can and cannot come next in a well-formed utterance. On this account, cloze tests assess the same integrated competence deployed in ordinary comprehension, activating the whole rather than isolating a discrete subskill. This theoretical move repositioned cloze from a readability metric to a general index of linguistic competence, with implications for second-language acquisition research that Abraham and Chapelle (1992) would later pursue in their examination of cloze validity across L2 populations.

Two debates complicated the procedure's adoption as a universal instrument. The first concerned scoring method. Researchers disputed whether only the exact original word should be accepted or whether acceptable synonyms warranted credit. Exact-word scoring produces higher inter-rater reliability and correlates well with other comprehension measures, while synonym scoring better reflects the inferential flexibility that Oller's theoretical account predicts (Jongsma 1980). The dispute surfaces a genuine ambiguity that persists in the procedure's design. Cloze tests measure prediction of the original author's word choice as much as they measure contextual comprehension, and a reader who supplies a semantically equivalent term has demonstrated comprehension even though the procedure marks them wrong.

The second debate concerned deletion method. Taylor's fixed-ratio approach (every fifth or seventh word) deletes without regard to the semantic weight of the deleted item. Bachman (1985) argued for rational deletion, selecting words based on their inferential salience, on the grounds that fixed-ratio deletion conflates easy and difficult predictions and flattens the difficulty gradient the procedure is meant to reveal. Cloze Reader's architecture resolves this debate by design. Word selection is delegated to a language model, which chooses items by heuristic instruction rather than by fixed interval or researcher judgment. The implications of that design choice are the paper's primary subject.

## The Machine Learning Genealogy

The structural resemblance between cloze testing and masked language modeling is not accidental. Both descend from the distributional hypothesis, the claim formalized by Harris (1954) and made memorable by Firth (1957) that words occurring in similar contexts carry similar meanings. Harris proposed distributional analysis as a method for discovering linguistic structure from raw text. Firth's formulation ("you shall know a word by the company it keeps") became the informal charter of computational semantics. The contextual prediction insight that Taylor applied to human readers is the same insight that word embedding models would eventually formalize as a training objective.

The technical trajectory from that insight to masked language modeling runs through distributional semantics, neural word embeddings, and contextualized representations. Mikolov et al. (2013) demonstrated that word embeddings trained on shallow prediction objectives encoded semantic and syntactic regularities at scale. The limitation of such representations was context-independence, since each word received a single vector regardless of its usage in a specific sentence. Peters et al. (2018) addressed this with ELMo (Embeddings from Language Models), which generated contextualized representations via bidirectional LSTM language modeling with forward and backward passes trained separately and then concatenated. ELMo's representations improved downstream performance across a range of NLP benchmarks and established that context-sensitive encoding mattered.

BERT (Devlin et al. 2019) extended ELMo's bidirectionality by training on masked tokens within a single joint model rather than concatenating two directional passes. Where ELMo trained each direction independently, BERT's transformer encoder architecture allowed every token position to attend to all other positions simultaneously. The masked language modeling objective made this training feasible as a self-supervised task, since the supervisory signal was already present in unannotated text and the scale of available text made large-parameter training viable (Liu et al. 2021). BERT's state-of-the-art results on eleven NLP benchmarks established masked language modeling as the dominant pretraining paradigm, and the paradigm has persisted through subsequent variants (RoBERTa, ALBERT, DistilBERT) that modify implementation details without abandoning the core masked-prediction objective.

## Cloze Reader

This article examines a browser-based educational game called Cloze Reader (https://reader.inference-arcade.com) that uses a language model to generate cloze tasks and returns them to human readers as exercises in contextual induction. Developed as part of the CUNY AI Lab and the broader Inference Arcade initiative, Cloze Reader presents players with short passages from public-domain texts drawn from the Project Gutenberg corpus via the Hugging Face Datasets API, and players propose completions for missing words while consulting an embedded chat panel powered by Google's Gemma-3-27B model for guidance. The hints offer paraphrase and leading questions rather than answers, but the model's primary work happens earlier, when it selects which words to remove, and this selection process instantiates the recursive structure that makes the project a critical artifact.

The recursive structure becomes visible in the architecture. Word selection is delegated to the same class of language model whose training regime descended from the cloze procedure. The system prompts Gemma-3 to identify words according to heuristic instructions that translate pedagogical intent into language the model can act upon. The following excerpt from the application's source code shows the prompt that governs word selection:

```
Select ${count} ${level <= 2 ? 'easy' : level <= 4 ? 'medium' : 'challenging'} words from this passage.

CRITICAL RULES:
- ONLY select lowercase words (no proper nouns)
- ONLY select words from the MIDDLE or END of the passage
- Choose nouns, verbs, or adjectives
- AVOID compound words - choose single, verifiable words
  with strong contextual salience
- Return ONLY a JSON array like ["word1", "word2"]
```

The prompt translates pedagogical goals into instructions that the model interprets through the statistical regularities of its training corpus rather than through explicit definitions, and this opacity is itself part of what the project stages for critical examination. The prompt further modulates difficulty through vocabulary complexity, requesting "easy vocabulary words" at early levels and "challenging words" at higher levels, while a validation layer filters the model's selections by length and presence in the passage, with a manual fallback that avoids function words if the AI response fails parsing.

This architecture enacts a feedback loop. A model trained through large-scale contextual prediction, a descendant of the masked language modeling paradigm that BERT popularized, now generates cloze-like tasks that return to human readers as exercises in contextual induction, and the prompt that governs this generation functions as an interface between pedagogical intent and machine prediction, translating the designer's goals into language the model can act upon however it interprets that language.

The Project Gutenberg corpus situates this feedback loop within a specific textual archive that predates the web-scale corpora on which contemporary language models train yet contributed to those corpora as digitized public-domain material. Over 70,000 public-domain e-books, filtered for high-quality narrative prose, supply the passages from which blanks are generated, and these texts include Shakespeare, nineteenth-century American oratory, and early twentieth-century fiction. When Gemma-3 selects words from a Melville passage, it draws on representations shaped partly by Melville's own prose, encountered during pre-training as statistical residue, and the historical distance between the texts and contemporary readers becomes legible in the difficulty of restoration. A player struggling with a blank in *Moby-Dick* faces local syntactic constraints and the accumulated distance between nineteenth-century prose conventions and contemporary linguistic intuition at the same time.

The game's difficulty system makes these dynamics playable by distributing challenge across two independent dimensions. At levels one through five, a single blank per passage and generous hints that include word length, first letter, and last letter scaffold early encounters with the inferential demands of cloze completion. Levels six through ten introduce two blanks with reduced scaffolding that provides only the first letter. Level eleven and beyond present three blanks with minimal guidance. Vocabulary complexity scales independently of blank count, with early levels requesting "easy" words from the model while later levels request "challenging" ones, and this two-dimensional difficulty curve distributes challenge across both the number of inferential tasks per passage and the sophistication of the words selected for those tasks.

The embedded chat panel, powered by Gemma-3-27B, paraphrases surrounding context, points to syntactic or semantic cues, and poses leading questions that direct attention to features of the passage that bear on the missing word. When a player consults the hint panel, they see one way of parsing the passage's contextual constraints, which may clarify their own thinking or may feel beside the point, and this variability itself becomes instructive about the difference between machine-generated guidance and human interpretive judgment.

## Continuity and Asymmetry

Both histories share a structural premise, that contextual prediction is a meaningful index of linguistic competence. Taylor operationalized that premise as an assessment instrument. BERT's developers operationalized it as a training objective. The two applications differ in what they treat as the system under examination (human readers in the first case, neural parameters in the second) and in what the procedure is meant to produce, a measurement of existing capacity versus an induction of new representations.

By dividing the cloze task between model and player, separating selection from interpretation, Cloze Reader holds apart what masked language modeling conflates and makes visible the asymmetry that the structural resemblance between educational cloze tests and machine learning tends to obscure. The model locates where context matters while the reader learns what context means. This division stages rather than resolves the asymmetry between Taylor's cloze procedure, which assessed comprehension as a holistic capacity, and BERT's masked language modeling, which optimized prediction as a training objective.

Empirical work comparing human and model cloze responses confirms that structural similarity does not guarantee functional equivalence. Across recent studies, models systematically misalign with human response distributions and struggle with contextual integration across longer spans (PMC 2024; arXiv 2024; Xie et al. 2018). Detailed performance figures follow in the evidence section.

Cloze Reader returns a practice that migrated from educational assessment into machine learning infrastructure back to human readers as an invitation to read slowly and contextually. The article traces the pedagogical and computational genealogies of the cloze procedure, examines empirical evidence documenting divergences between human and model performance on cloze tasks, and presents Cloze Reader's architectural and design decisions as a critical intervention into contemporary debates about AI literacy and the limits of prediction as a proxy for understanding. The convergence between Taylor's procedure and masked language modeling is real, grounded in the shared insight that contextual prediction offers a window onto linguistic competence. The purposes differ. Taylor wanted to measure comprehension. BERT's developers wanted to induce representations. Cloze Reader inherits both histories and uses game mechanics to hold them apart for examination.

---

## References

Abraham, R.G. and Chapelle, C.A. (1992) 'The meaning of cloze test scores: An item difficulty perspective,' *The Modern Language Journal*, 76(4), pp. 468–479.

Alammar, J. (2019) 'The illustrated BERT, ELMo, and co.,' *jalammar.github.io*. Available at: https://jalammar.github.io/illustrated-bert/

Bachman, L.F. (1985) 'Performance on cloze tests with fixed-ratio and rational deletions,' *TESOL Quarterly*, 19(3), pp. 535–556.

Devlin, J. et al. (2019) 'BERT: Pre-training of deep bidirectional transformers for language understanding,' in *Proceedings of NAACL-HLT 2019*. Minneapolis, MN: Association for Computational Linguistics, pp. 4171–4186.

Firth, J.R. (1957) 'A synopsis of linguistic theory, 1930–1955,' in *Studies in Linguistic Analysis*. Oxford: Philological Society, pp. 1–32.

Harris, Z.S. (1954) 'Distributional structure,' *Word*, 10(2–3), pp. 146–162.

Jongsma, E. (1980) *Cloze instruction research: A second look*. Newark, DE: International Reading Association.

Koffka, K. (1935) *Principles of Gestalt Psychology*. New York: Harcourt, Brace and World.

Liu, X. et al. (2021) 'Self-supervised learning: Generative or contrastive,' *IEEE Transactions on Knowledge and Data Engineering*, 35(1).

Mikolov, T. et al. (2013) 'Efficient estimation of word representations in vector space,' *arXiv:1301.3781*.

Oller, J.W. (1979) *Language Tests at School*. London: Longman.

Peters, M.E. et al. (2018) 'Deep contextualized word representations,' in *Proceedings of NAACL-HLT 2018*. New Orleans, LA: Association for Computational Linguistics, pp. 2227–2237.

Taylor, W.L. (1953) '"Cloze procedure": A new tool for measuring readability,' *Journalism Quarterly*, 30(4), pp. 415–433.

Xie, Q. et al. (2018) 'Large-scale cloze test dataset created by teachers,' in *Proceedings of EMNLP 2018*. Brussels: Association for Computational Linguistics, pp. 2344–2356.

---

*Draft v14 · 2026-03-16 · Working draft*
