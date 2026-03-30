# Fill in the Blank: Cloze Reader and the Twin Histories of Occlusion

**Zach Muhlbauer**
The Graduate Center, CUNY
<https://reader.inference-arcade.com>

---

## Introduction

Cloze reading began as a simple procedural idea. Delete words from a passage at regular intervals, require the reader to supply the missing terms, and treat the accuracy of their restorations as a measure of how well they understood the surrounding text. Taylor (1953) drew on the Gestalt principle of closure, the perceptual tendency to complete incomplete familiar patterns described by Koffka (1935), and reframed it as a methodology for gauging reading comprehension holistically rather than through isolated subskills. The approach tested whether a reader could bring syntax, semantics, and discourse knowledge to bear on a single missing word, and the results suggested that this kind of contextual prediction tracked comprehension in ways that syllable-counting and sentence-length measures could not.

Taylor named closure as his theoretical reference, but the procedure he designed is better described by a related and more specific Gestalt concept. Closure names the tendency to complete a gap in a continuous form, to perceive a broken circle as whole, whereas occlusion names the tendency to complete a form that another object blocks from view, describing the hidden portion that does not appear in the visual field yet is treated by the perceptual system as present, its shape and extent inferred from the visible contours surrounding the obstruction (Kanizsa 1979). A cloze blank works similarly. The deleted word still governs the surrounding syntax, still selects for specific collocates, and still shapes what can grammatically precede and follow it, so that removing the word from view does not remove its structural presence. The reader must see through the blank to the word the context implies, and treat the surrounding passage as evidence of what the sentence conceals rather than what it lacks, yoking together structures of concealment and inference that thread across the genealogies this paper seeks to trace.

The intervention proved durable enough to move from educational psychology to computational laboratories, where cloze-like objectives now structure how machines learn language.

In this paper, I suggest we can learn from the technical genealogy of the cloze procedure, tracing its arc of use from early reading comprehension assessment to its later adoption by machine learning researchers training masked language models (MLMs) to predict missing tokens from surrounding context.

The genealogy begins with two accounts of how language carries meaning, both of which Mikolov, Peters, and Devlin would later compress into a single training objective. Harris (1954) set meaning aside entirely, arguing that phonemes, morphemes, and words could be identified through their co-occurrence patterns alone. Elements appearing in the same environments belong to the same grammatical class, and the restrictions on how those classes combine generate the grammar. Firth (1957) took that structural observation and redirected it toward semantics. In "Modes of Meaning," he proposed that words carry content through their habitual collocations, the words they characteristically appear alongside. "You shall know a word by the company it keeps." For Firth, *time*'s tendency to collocate with *saved*, *spent*, or *wasted* was itself semantic information, since nothing internal to the word determines those pairings.

Given enough text, can a model learn what words mean by observing what they appear near? Mikolov showed that it could. The word2vec framework trained shallow neural networks to predict a word's context from the word itself (skip-gram) or the word from its context (CBOW), producing dense vectors in which distributionally similar words clustered near each other. The limitation word2vec exposed was context-independence: each word received a single vector regardless of how it appeared in a specific sentence, treating *bank* identically whether it preceded *account* or followed *river*. Peters addressed this by running two LSTM language models in parallel, one forward and one backward, then combining their outputs at each position to produce representations the surrounding sentence shaped. Devlin extended that logic, training a Transformer encoder to predict masked tokens from full bidirectional context within a single joint pass rather than merging separately trained directional runs at the output. Devlin called this masked language modeling and drew the analogy to the cloze task directly — same task, larger scale, different architecture.

Cloze Reader ([reader.inference-arcade.com](https://reader.inference-arcade.com)), a browser-based educational game developed through the CUNY AI Lab and the Inference Arcade initiative, sits at the intersection of these two lines. It preserves the cloze prompt as a human-facing task while delegating word removal to a language model guided by heuristic instructions. That design holds two things in view at once: the continuity of the cloze premise across seventy years of research, and the divergence in what removal reveals about the system performing it.

I trace these genealogies to show where human and model cloze performance diverge, presenting Cloze Reader as an instrument that inverts the training signal. Where masked language models learned to fill blanks implicitly, at scale, through gradient descent, the game requires players to do the same work explicitly, at human pace, returning them to the passages the model was trained on and asking them to read.

## The Educational Genealogy of Cloze

Wilson Taylor's 1953 procedure was formally simple. Delete words from a passage at fixed intervals and ask readers to supply what was missing. The theoretical ambition behind it was larger. Taylor adapted the Gestalt principle of closure as a framework for measuring reading comprehension holistically, and where prior readability instruments counted syllables and sentence lengths, the cloze procedure tested whether readers could integrate semantic, syntactic, and contextual knowledge simultaneously to recover a deleted word from the evidence surrounding it (Taylor 1953).

Oller (1979) gave the procedure a stronger theoretical account. He formalized what cloze performance draws on as "pragmatic expectancy grammar," the system of linguistic knowledge that allows readers and speakers to anticipate what can and cannot come next in a well-formed utterance. Cloze tests, on this account, assess the same integrated competence deployed in ordinary comprehension. They measure the whole rather than isolating any single subskill. The move repositioned cloze from a readability instrument to a general index of linguistic competence. Abraham and Chapelle (1992) extended that claim into second-language acquisition, examining how cloze validity holds across L2 populations.

Two debates complicated the procedure's adoption as a universal instrument. The first concerned scoring method. Researchers disputed whether only the exact original word should be accepted or whether acceptable synonyms warranted credit. Exact-word scoring produces higher inter-rater reliability and correlates well with other comprehension measures, while synonym scoring better reflects the inferential flexibility that Oller's theoretical account predicts (Jongsma 1980). The dispute surfaces a genuine ambiguity that persists in the procedure's design. Cloze tests measure prediction of the original author's word choice as much as they measure contextual comprehension, and a reader who supplies a semantically equivalent term has demonstrated comprehension even though the procedure marks them wrong.

The second debate concerned deletion method, and its stakes for what the procedure actually measures were equally consequential. Taylor's fixed-ratio approach (every fifth or seventh word) deletes without regard to the semantic weight of the deleted item. Bachman (1985) argued for rational deletion, selecting words based on their inferential salience, on the grounds that fixed-ratio deletion conflates easy and difficult predictions and flattens the difficulty gradient the procedure is meant to reveal. Cloze Reader's architecture takes this asymmetry as its design premise. I delegated word selection to a language model, which chooses items by heuristic instruction rather than by fixed interval or researcher judgment. That delegation is this paper's primary subject.

## The Machine Learning Genealogy

The structural resemblance between cloze testing and masked language modeling is not accidental. Both descend from the distributional hypothesis, the claim formalized by Harris (1954) and made memorable by Firth (1957) that words occurring in similar contexts carry similar meanings. Harris proposed distributional analysis as a method for discovering linguistic structure from raw text. Firth's formulation ("you shall know a word by the company it keeps") became the informal charter of computational semantics. The contextual prediction insight that Taylor applied to human readers is the same insight that word embedding models would eventually formalize as a training objective.

That shared premise required several decades of technical work to become trainable at scale. Mikolov showed that shallow prediction objectives encoded semantic and syntactic regularities in word vectors, but each word still received a single vector regardless of usage. Peters fixed this with ELMo, which ran two LSTM language models in opposite directions, concatenating their outputs to produce representations the surrounding sentence shaped. ELMo improved performance across downstream benchmarks and established that context-sensitive encoding mattered.

Devlin built on ELMo's bidirectionality by training BERT on masked tokens within a single joint model. Where ELMo combined two separately trained directional passes, BERT's transformer encoder let every token position attend to all others at once. The masking objective made this self-supervised: the training signal was already present in unannotated text, and the volume of available text made large-scale training viable (Liu et al. 2021; Bommasani et al. 2021). Devlin's results on eleven benchmarks made masking the dominant pretraining objective, and subsequent variants — RoBERTa, ALBERT, DistilBERT — refined it without abandoning it.

## Cloze Reader

*Figure 1. Cloze Reader in use: Our Legal Heritage, 4th Ed. by S. A. Reilly, Level 1, one blank. The model has selected a word from a passage on Puritan dissent and royal preaching restrictions. The AI hint panel (speech bubble icon) is available but not yet consulted.*

Cloze Reader ([reader.inference-arcade.com](https://reader.inference-arcade.com)) is a browser-based educational game that uses a language model to generate cloze tasks and return them to human readers as exercises in contextual induction. Public source modules for the live application show that passages are drawn from Project Gutenberg through the Hugging Face Datasets API and that the app uses Google's Gemma-3-27B model for word selection, hints, and contextualization (Cloze Reader 2026a; 2026b; Project Gutenberg 2026). Players propose completions for missing words and can consult an embedded chat panel that withholds the answer while offering structural hints and preset questions about part of speech, sentence role, word category, and synonymy (Cloze Reader 2026b; 2026c; 2026d).

A recursive structure embedded in the architecture itself sets the game apart from ordinary educational applications. Word selection is delegated to a predictive language model rather than a fixed deletion rule. The public aiService.js module shows the live app calling google/gemma-3-27b-it for selection and supplying heuristic constraints that translate pedagogical intent into operational rules (Cloze Reader 2026b; Gemma Team 2025). The following prompt governs which words are removed:

```
Select ${count} ${level <= 2 ? 'easy' : level <= 4 ? 'medium' : 'challenging'} words (${wordLengthConstraint}) from this passage.

CRITICAL RULES:
- Select EXACT words that appear in the passage (copy them exactly as written)
- ONLY select lowercase words (no capitalized words, no proper nouns)
- ONLY select words from the MIDDLE or END of the passage (skip the first ~10 words)
- Words must be ${wordLengthConstraint}
- Choose nouns, verbs, or adjectives
- AVOID compound words like "courthouse" or "steamboat" - choose single, verifiable words with semantic inbetweenness
- AVOID indexes, tables of contents, and capitalized content
- Return ONLY a JSON array like ["word1", "word2"]
```

The prompt translates pedagogical goals into instructions that the model interprets through the statistical regularities of its training corpus rather than through explicit definitions. Bommasani et al. (2021) describe these as capabilities "implicitly induced rather than explicitly constructed," and this opacity is itself part of what the project stages for critical examination. The prompt further modulates difficulty through vocabulary and word-length constraints, requesting "easy," "medium," or "challenging" selections by level, while a validation layer filters outputs by passage presence and length, with a manual fallback that excludes common function words if the AI response fails or returns unusable items (Cloze Reader 2026b; 2026c).

Taken together, these constraints enact a feedback loop. A model shaped by large-scale predictive pretraining now generates cloze tasks for humans, and the prompt governing that generation serves as an interface between pedagogical intent and statistical prediction. The live app makes that interface unusually visible because the selection rules are written in plain language rather than hidden behind a fixed deletion schedule or a hand-authored word list (Cloze Reader 2026b; Gemma Team 2025).

The game's use of Gemma-3 is organized around a design constraint I imposed from the start. The model must not know, when selecting a word to remove, what it will later be asked to say about that word. Shared context between word selection and hint generation would make word selection more liable to drift toward words the hint system handles fluently, compromising the puzzle. I kept each task (word selection, hint generation, and passage summarization) as a separate and self-contained request, so no information carries forward from one to the next.

I could have collapsed these tasks into a single extended prompt — Gemma-3's architecture technically supports it (Google 2025) — but keeping them discrete preserves the independence of each inferential step. Each call receives only the passage text and the instructions relevant to its specific task; the model's output is used once and discarded. The three types of contextual hint the game offers (one tied to syntax and position, one to word meaning and usage, one to explicit definition or restatement) are generated through separate requests in this way, each scoped to a narrow question about the passage.

The result is that Gemma-3 functions as a set of discrete procedures, each answering one question at a time, with no conversational thread running through the puzzle.

This discreteness extends further. No two runs of Cloze Reader are identical. Each session draws from a streamed Gutenberg dataset, and word selection is performed with non-zero-temperature decoding, with the live app requesting selections at temperature: 0.5 and preloading books from random offsets in its Hugging Face dataset proxy, so the same passage need not yield the same blank on successive runs (Cloze Reader 2026a; 2026b). This is a structural property of how the system works, not a failure to be corrected.

The stochasticity of token sampling propagates up through the word-selection process and into the player's experience. A returning player may encounter a different word removed, or encounter the same word from a different angle because the surrounding hint differs. The opacity is inherited from probabilistic inference, since the model selects by learned regularities rather than by explicit semantic criteria, and its choices vary in ways that keep the game from resolving into a fixed, memorizable test.

I chose Project Gutenberg as the source archive because its texts occupy a specific position in the history of language model training. They are canonical pretraining data, present in The Pile and its successors, already disaggregated into token distributions before a reader encounters them in the game. That prior absorption is the point. The texts that populate the corpus belong to Project Gutenberg's public-domain holdings (Project Gutenberg 2026; Cloze Reader 2026a). Gutenberg's digitized holdings appear as standard components of large-scale training corpora. The Pile, an 800-gigabyte pretraining dataset assembled by EleutherAI, explicitly includes Gutenberg texts among its source collections (Gao et al. 2020), and empirical work on LLM memorization has demonstrated that models trained on such corpora can reproduce verbatim passages from these books under targeted prompting conditions (Carlini et al. 2021).

The books have, in a precise sense, been flattened into parameter weights, disaggregated from their narrative forms and recomposed as statistical distributions over tokens, unattributed and unacknowledged in the model's outputs. Gitelman and Jackson (2013) describe exactly this process. The literary canon enters the extractive regime of machine learning infrastructure, texts arriving as data, stripped of authorship, their contexts flattened, their patterns remediated as weighted co-occurrence statistics.

Against this flattening, Cloze Reader works by restoring the passage to the surface. The language model is positioned as one layer of a call stack rather than the whole of it, a component whose outputs become legible only when a human reader engages the passage it was trained on.

The difficulty system distributes challenge across two independent dimensions. Blank count rises from one (levels 1–5) to two (levels 6–10) to three (level 11 and beyond). Structural hints also change by level, with levels 1–2 providing word length plus first and last letter, and later levels providing only the first letter. Vocabulary difficulty scales separately, with the word-selection prompt moving from "easy" to "medium" to "challenging" as levels increase. The result is a two-dimensional difficulty curve that separates the number of inferential tasks from the lexical difficulty of the selected words (Cloze Reader 2026b; 2026c).

This difficulty architecture points toward a deeper pedagogical design. The hint system models a form of graduated scaffolding, following Wood, Bruner, and Ross (1976) and Vygotsky's (1978) zone of proximal development, directing attention without supplying the answer. The live code enforces that withholding explicitly ("Never reveal the answer word directly"), while the hints remain static rather than adaptive, a constraint Pea (2004) would recognize as a departure from the original scaffolding criteria (Cloze Reader 2026b).

The embedded chat panel runs on the same Gemma-3-27B endpoint and offers preset prompts about part of speech, sentence role, word category, and synonymy rather than a free-form explanatory tutor (Cloze Reader 2026b; 2026d). When a player consults it, they see one way of parsing the passage's contextual constraints, which may clarify their own thinking or feel beside the point. That variability is itself instructive, surfacing the difference between machine-generated guidance and human interpretive judgment.

Returning to origins clarifies what the game's design ultimately asks of its players. When Wilson Taylor introduced the cloze procedure in 1953, he described it as a measurement instrument, a tool for gauging readability by deleting every nth word and observing how much of the text readers could reconstruct from contextual probability. What Taylor was measuring was also a description of ordinary cognition, since reading research from Fillenbaum et al. (1963) onward has established that fluent readers continuously generate anticipatory completions during comprehension, producing probabilistic expectations about upcoming words well before each word arrives.

Subsequent reading research formalized this as a quantifiable variable, using cloze completion rates, the proportion of readers who supply a given word when asked to fill a blank, as the standard measure of word predictability; computational models of reading then use those rates to simulate how a reader's gaze accelerates or slows depending on how expected the next word is (Snell et al. 2018; Rego, Snell, and Meeter 2024). Schema theory maps the same phenomenon from the reader's side, treating comprehension as active anticipation, supplementation, and selection driven by prior knowledge structures the reader brings to the text (Rumelhart 1980).

The Provo Corpus operationalized this for naturalistic reading by collecting completions from 470 participants across 55 passages, producing per-word predictability norms that track real inferential behavior, even as Hofmann et al. (2021) noted that offline cloze completion diverges from the split-second online prediction it approximates. Cloze Reader closes that divergence by design. I built the game so that committing to a predicted word or phrase is what advances the passage, making implicit predictive machinery explicit and consequential.

The player is not simulating the inference engine; they are one, scored on the precision of their probabilistic reasoning about what the text's next step must be.

## Continuity and Asymmetry

Both histories share a structural premise, that contextual prediction is a meaningful index of linguistic competence. Taylor operationalized that premise as an assessment instrument. BERT's developers operationalized it as a training objective. The two applications differ in what they treat as the system under examination (human readers in one case, neural parameters in the other) and in what the procedure is meant to produce — a measurement of existing capacity or an induction of new representations.

Cloze Reader addresses this tension structurally. I divided the cloze task between model and player so that selection and interpretation stay separate. Masked language modeling treats them as one. The model identifies where context matters. The reader decides what context means. That division stages the asymmetry rather than resolving it. Taylor's procedure assessed comprehension as a holistic capacity. BERT's objective optimized prediction as a training signal. Cloze Reader makes those two operations visible side by side through play.

That asymmetry is not merely theoretical. On the CLOTH dataset — 96,000 fill-in-the-blank items authored by teachers — baseline language models achieved roughly 50–55% accuracy; human test-takers achieved 86% (Xie et al. 2018). The gap is behavioral as well as quantitative: Jacobs, Grobol, and Tsang (2024) found that models systematically under-rank the completions humans most frequently produce and over-rank low-frequency alternatives that are statistically plausible but contextually odd — the completion spaces diverge lexically and semantically, not just numerically. Rego, Snell, and Meeter (2024) corroborate the pattern from a different angle, showing that language model predictability outperforms human cloze norms as a predictor of reading behavior in a cognitive model of eye movement, which suggests the two tasks measure different underlying processes even where their surface outputs overlap. Detailed performance figures follow in the evidence section.

I trace the pedagogical and computational genealogies of the cloze procedure to locate Cloze Reader within both, examine empirical evidence of divergence between human and model performance, and present the architectural decisions behind the game as a critical intervention into debates about AI literacy and the limits of prediction as a proxy for understanding.

To be clear, the convergence between Taylor's procedure and masked language modeling is real, grounded in the shared insight that contextual prediction offers a window onto linguistic competence. The purposes differ. Taylor wanted to measure comprehension. BERT's developers wanted to induce representations. Cloze Reader inherits both histories and uses game mechanics to hold them apart for examination.

Pretraining reduces text to token distributions. The blank makes that reduction visible: one word absent from a passage the model was trained on, now requiring a reader to supply what statistical weighting cannot. Filling it demands close reading: attending to what the surrounding sentence contributes before committing to an answer. The model selected that word through the same regularities by which it was trained. It cannot return to the passage and read it. The game asks players to do exactly that.

---

## References

Abraham, R.G. and Chapelle, C.A. (1992) 'The meaning of cloze test scores: An item difficulty perspective,' *The Modern Language Journal*, 76(4), pp. 468–479.

Bachman, L.F. (1985) 'Performance on cloze tests with fixed-ratio and rational deletions,' *TESOL Quarterly*, 19(3), pp. 535–556.

Bommasani, R. et al. (2021) 'On the opportunities and risks of foundation models,' *arXiv:2108.07258*. Available at: <https://arxiv.org/abs/2108.07258>

Carlini, N. et al. (2021) 'Extracting training data from large language models,' in *Proceedings of the 30th USENIX Security Symposium*. USENIX Association, pp. 2633–2650.

Cloze Reader (2026a) 'bookDataService.js'. Available at: <https://reader.inference-arcade.com/src/bookDataService.js> (Accessed: 18 March 2026).

Cloze Reader (2026b) 'aiService.js'. Available at: <https://reader.inference-arcade.com/src/aiService.js> (Accessed: 18 March 2026).

Cloze Reader (2026c) 'clozeGameEngine.js'. Available at: <https://reader.inference-arcade.com/src/clozeGameEngine.js> (Accessed: 18 March 2026).

Cloze Reader (2026d) 'conversationManager.js'. Available at: <https://reader.inference-arcade.com/src/conversationManager.js> (Accessed: 18 March 2026).

Devlin, J. et al. (2019) 'BERT: Pre-training of deep bidirectional transformers for language understanding,' in *Proceedings of NAACL-HLT 2019*. Minneapolis, MN: Association for Computational Linguistics, pp. 4171–4186.

Fillenbaum, S., Jones, L.V. and Rapoport, A. (1963) 'The predictability of words and their associations,' *Journal of General Psychology*, 69(2), pp. 227–238.

Firth, J.R. (1957) 'A synopsis of linguistic theory, 1930–1955,' in *Studies in Linguistic Analysis*. Oxford: Philological Society, pp. 1–32.

Gao, L. et al. (2020) 'The Pile: An 800GB dataset of diverse text for language modeling,' *arXiv:2101.00027*. Available at: <https://arxiv.org/abs/2101.00027>

Gemma Team (2025) 'Gemma 3 Technical Report,' *arXiv:2503.19786*. Available at: <https://arxiv.org/abs/2503.19786>

Gitelman, L. and Jackson, V. (2013) 'Introduction,' in Gitelman, L. and Jackson, V. (eds) *'Raw Data' Is an Oxymoron*. Cambridge, MA: MIT Press, pp. 1–14.

Harris, Z.S. (1954) 'Distributional structure,' *Word*, 10(2–3), pp. 146–162.

Hofmann, M.J. et al. (2021) 'The influence of information in the sentence context on predictions in reading,' *Neuropsychologia*, 158, 107885.

Jacobs, C.L., Grobol, L. and Tsang, A. (2024) 'Large-scale cloze evaluation reveals that token prediction tasks are neither lexically nor semantically aligned,' *arXiv:2410.12057*. Available at: <https://arxiv.org/abs/2410.12057>

Jongsma, E. (1980) *Cloze instruction research: A second look*. Newark, DE: International Reading Association.

Kanizsa, G. (1979) *Organization in Vision: Essays on Gestalt Perception*. New York: Praeger.

Koffka, K. (1935) *Principles of Gestalt Psychology*. New York: Harcourt, Brace and World.

Liu, X. et al. (2021) 'Self-supervised learning: Generative or contrastive,' *IEEE Transactions on Knowledge and Data Engineering*, 35(1).

Mikolov, T. et al. (2013) 'Efficient estimation of word representations in vector space,' *arXiv:1301.3781*.

Oller, J.W. (1979) *Language Tests at School*. London: Longman.

Ondov, B., Attal, K. and Demner-Fushman, D. (2024) 'Pedagogically aligned objectives create reliable automatic cloze tests,' in *Proceedings of NAACL-HLT 2024*. Mexico City: Association for Computational Linguistics. Available at: <https://aclanthology.org/2024.naacl-long.220/>

Pea, R.D. (2004) 'The social and technological dimensions of scaffolding and related theoretical concepts for learning, education, and human activity,' *Journal of the Learning Sciences*, 13(3), pp. 423–451.

Peters, M.E. et al. (2018) 'Deep contextualized word representations,' in *Proceedings of NAACL-HLT 2018*. New Orleans, LA: Association for Computational Linguistics, pp. 2227–2237.

Project Gutenberg (2026) *Project Gutenberg*. Available at: <https://www.gutenberg.org/> (Accessed: 18 March 2026).

Rego, A.T.L., Snell, J. and Meeter, M. (2024) 'Language models outperform cloze predictability in a cognitive model of reading,' *PLOS Computational Biology*, 20(9), e1012117. Available at: <https://doi.org/10.1371/journal.pcbi.1012117>

Rumelhart, D.E. (1980) 'Schemata: The building blocks of cognition,' in Spiro, R.J., Bruce, B.C. and Brewer, W.F. (eds.) *Theoretical Issues in Reading Comprehension*. Hillsdale, NJ: Erlbaum, pp. 33–58.

Snell, J. et al. (2018) 'OB1-reader: A model of word recognition and eye movements in text reading,' *Psychological Review*, 125(6), pp. 969–1013.

Taylor, W.L. (1953) '"Cloze procedure": A new tool for measuring readability,' *Journalism Quarterly*, 30(4), pp. 415–433.

Vygotsky, L.S. (1978) *Mind in Society: The Development of Higher Psychological Processes*. Cambridge, MA: Harvard University Press.

Wood, D., Bruner, J.S. and Ross, G. (1976) 'The role of tutoring in problem solving,' *Journal of Child Psychology and Psychiatry*, 17(2), pp. 89–100.

Xie, Q. et al. (2018) 'Large-scale cloze test dataset created by teachers,' in *Proceedings of EMNLP 2018*. Brussels: Association for Computational Linguistics, pp. 2344–2356.

Zhang, Z. and Hashimoto, T. (2021) 'On the inductive bias of masked language modeling: From statistical to syntactic dependencies,' in *Proceedings of NAACL-HLT 2021*. Online: Association for Computational Linguistics. Available at: <https://aclanthology.org/2021.naacl-main.404/>

---

*Draft v42 · Updated 2026-03-28 EDT · "genuine" removed from intro Taylor paragraph; PASSAGE A (occlusion/closure distinction, Kanizsa 1979) inserted after Taylor paragraph before "The intervention proved durable"; Kanizsa (1979) added to bibliography*
