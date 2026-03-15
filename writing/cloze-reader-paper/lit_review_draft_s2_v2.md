# Literature Review — Twin Histories (Session 2, v2)
## Bold = new or changed text from v1

---

## Twin Histories: Educational Assessment and Masked Language Modeling

### I. The Educational Genealogy of Cloze

Wilson Taylor's 1953 procedure was formally simple: delete words from a passage at
regular intervals and ask readers to supply the missing terms. Its theoretical stakes were
larger. Taylor adapted the Gestalt principle of closure — the perceptual tendency to
complete incomplete familiar patterns, described systematically by Koffka (1935) and
rooted in the broader Gestalt program of Wertheimer, Köhler, and Koffka — as a framework
for measuring reading comprehension holistically. Where prior readability instruments
counted syllables and sentence lengths, the cloze procedure tested whether readers could
integrate semantic, syntactic, and contextual knowledge simultaneously (Taylor 1953).

Subsequent research developed both the theoretical account and the practical scope of
cloze. Oller (1979) formalized the mechanism underlying cloze performance as "pragmatic
expectancy grammar": the system of linguistic knowledge that allows readers and speakers
to anticipate what can and cannot come next in a well-formed utterance. On this account,
cloze tests assess the same integrated competence deployed in ordinary comprehension —
they do not measure a discrete subskill but activate the whole. This theoretical move was
significant because it repositioned cloze from a readability metric to a general index of
linguistic competence, with implications for second-language acquisition research that
would follow (Abraham and Chapelle 1992).

Two debates complicated the procedure's adoption as a universal instrument. The first
concerned scoring method: researchers disputed whether only the exact original word
should be accepted or whether acceptable synonyms warranted credit. Exact-word scoring
produces higher inter-rater reliability and correlates well with other comprehension
measures; synonym scoring better reflects the inferential flexibility that Oller's
theoretical account predicts (Jongsma 1980). Neither resolves neatly, and the dispute
surfaces a genuine ambiguity: cloze tests measure prediction of the original author's
word choice as much as they measure contextual comprehension. A reader who supplies a
semantically equivalent term has demonstrated comprehension; the procedure marks them
wrong regardless.

The second debate concerned deletion method. Taylor's fixed-ratio procedure (every fifth
or seventh word) deletes without regard to the semantic weight of the deleted item.
Bachman (1985) argued for rational deletion — selecting words based on their inferential
salience — on the grounds that fixed-ratio deletion conflates easy and difficult
predictions, flattening the difficulty gradient the procedure is meant to reveal. Cloze
Reader's architecture resolves this debate by design: word selection is delegated to a
language model, which chooses items by heuristic instruction rather than by fixed interval
or researcher judgment. The implications of that design choice are the paper's primary
subject.

### II. The Machine Learning Genealogy

The structural resemblance between cloze testing and masked language modeling is not
accidental. Both descend from the distributional hypothesis — the claim, formalized by
Harris (1952) and made memorable by Firth (1957), that words occurring in similar
contexts carry similar meanings. Harris proposed distributional analysis as a method for
discovering linguistic structure from raw text; Firth's formulation ("you shall know a
word by the company it keeps") became the informal charter of computational semantics. The
contextual prediction insight that Taylor applied to human readers is the same insight
that word embedding models would eventually formalize as a training objective.

The technical trajectory from that insight to masked language modeling runs through
distributional semantics, neural word embeddings, and contextualized representations.
Mikolov et al. (2013) demonstrated that word embeddings trained on shallow prediction
objectives encoded semantic and syntactic regularities at scale. The limitation of such
representations was context-independence: each word received a single vector regardless
of its usage in a specific sentence. Peters et al. (2018) addressed this with ELMo
(Embeddings from Language Models), which generated contextualized representations via
bidirectional LSTM language modeling — forward and backward passes trained separately,
then concatenated. ELMo's representations improved downstream performance across a range
of NLP benchmarks and established that context-sensitive encoding mattered.

BERT (Devlin et al. 2019) extended ELMo's bidirectionality by training on masked tokens
within a single joint model rather than concatenating two directional passes. Where ELMo's
bidirectionality was shallow — each direction trained independently — BERT's transformer
encoder architecture allowed every token position to attend to all other positions
simultaneously. The masked language modeling objective made this training feasible as a
self-supervised task: the supervisory signal was already present in unannotated text, and
the scale of available text made large-parameter training viable (Liu et al. 2021). BERT's
state-of-the-art results on eleven NLP benchmarks established masked language modeling as
the dominant pretraining paradigm, and the paradigm has persisted through subsequent
variants (RoBERTa, ALBERT, DistilBERT) that modify implementation details without
abandoning the core masked-prediction objective.

### III. Continuity and Asymmetry [REVISED — changes in bold]

Both histories share a structural premise: that contextual prediction is a meaningful
index of linguistic competence. Taylor operationalized that premise as an assessment
instrument. BERT's developers operationalized it as a training objective. **The
comparison matters because it exposes what the structural similarity conceals.** Taylor's
cloze procedure probed a capacity that already existed in human readers — the holistic,
inferential competence that Oller called pragmatic expectancy grammar. BERT's masked
language modeling did something categorically different: it used the same fill-in-the-blank
structure to induce representations in a system that began with no linguistic knowledge at
all, optimizing billions of parameters through gradient descent until prediction loss
fell. **One procedure measured comprehension. The other manufactured the statistical
preconditions for something that resembles it.**

**The scoring-method debate surfaces this asymmetry in miniature.** When a human reader
supplies a synonym rather than the exact word, the cloze procedure penalizes a
demonstrated act of comprehension. When a language model generates a high-probability
completion, it optimizes for what its training corpus made predictable, which need not
correspond to what a human reader would recognize as contextually appropriate. Empirical
studies comparing human and model responses on cloze tasks document the divergence
directly: models systematically under-rank top human responses and over-rank rare
completions, producing response distributions that diverge from human norms even when
accuracy metrics appear comparable (PMC 2024; arXiv 2024; Xie et al. 2018).

**Cloze Reader stages this asymmetry as a playable encounter.** The application routes the
output of a BERT-descended language model — Gemma-3, which inherits the masked-prediction
paradigm through its training lineage — back to human readers as a reading exercise. The
model selects which words to remove; the human works to restore them. This division holds
apart what masked language modeling conflates: selection, which the model performs through
statistical inference, and interpretation, which the reader performs through the integrated
competence that Taylor's procedure was designed to measure. **The purpose of placing these
two histories side by side is not to argue that machine learning borrowed from educational
psychology, though the structural parallel is real. It is to show what gets lost when a
measurement tool for human comprehension becomes a training objective for statistical
prediction — and what Cloze Reader recovers by returning the blank to a human reader.**

---

**Word count (v2):** ~900 | **Status:** Draft — awaiting milwrite approval
