# Cloze Reading and Twin Histories of Occlusion

**Zach Muhlbauer**
The Graduate Center, City University of New York
<https://reader.inference-arcade.com> | <https://github.com/milwrite/cloze-reader>

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

---

*Draft v14 — 2026-03-16 | Single source of truth*
*Status: working draft, pending milwrite review*
