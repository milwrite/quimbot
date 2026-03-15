# Literature Review Draft — Session 2
## Cloze Reader and the Twin Histories of Occlusion
### Date: 2026-03-14 | Status: Draft — awaiting milwrite approval

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

### III. Continuity and Asymmetry

Both histories share a structural premise: that contextual prediction is a meaningful
index of linguistic competence. Taylor operationalized that premise as an assessment
instrument. BERT's developers operationalized it as a training objective. The two
applications differ in what they treat as the system under examination — human readers in
the first case, neural parameters in the second — and in what the procedure is meant to
produce: a measurement of existing capacity versus an induction of new representations.
Cloze Reader makes that difference playable by routing the model's output back to a human
reader as a task, placing the model and the reader on either side of the same blank.

---

**Word count:** ~750 | **Status:** Draft — no prose committed to main draft_intro.txt
**Needs before body integration:**
- [ ] Jongsma (1980) full citation confirmed
- [ ] Abraham and Chapelle (1992) full citation confirmed
- [ ] Bachman (1985) full citation confirmed (Petrarch to assess for body)
- [ ] Peters et al. (2018) URL/DOI verified
- [ ] Mikolov et al. (2013) full citation added
- [ ] Liu et al. (2021) confirmed as peer-reviewed NLP self-supervised learning source (Petrarch)
- [ ] Koffka (1935) full citation verified
