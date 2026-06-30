# Source Expansion Review — *Fill in the Blank and Cloze Reader's Twin Histories of Occlusion*

**Prepared for:** Zach Muhlbauer
**Subject draft:** `writing/cloze-reader-paper/draft.md`
**Date:** 30 June 2026

## Purpose and method

This review surveys scholarly literature adjacent to the draft's two genealogies
(educational cloze and machine-learning masking) and its design argument, and
recommends sources that would strengthen specific claims. The draft is already
well-cited and tightly argued; the goal here is *targeted* expansion, not
inflation. Each candidate below names the exact claim it supports, where it
would attach in the draft, and a priority:

- **High** — fills a genuine gap or anticipates an obvious reviewer objection.
- **Medium** — strengthens an existing claim or adds useful range.
- **Optional** — good to know; add only if the section is expanded.

Candidates were located through scholarly and web search across the draft's
thematic clusters and cross-checked against the existing reference list to avoid
duplication. A closing note flags where adding sources would *hurt* the draft.

---

## 1. The most important gap: the cloze-validity critique

The draft's educational-genealogy section presents the affirmative tradition —
Taylor's comprehension claim, Oller's "pragmatic expectancy grammar," Jongsma on
scoring, Abraham & Chapelle on item difficulty, Bachman on rational deletion —
and then poses the open question that anchors the whole essay: *"when does
restoring a missing word genuinely test reading?"* (draft §"The Educational
Genealogy of Cloze," ll. 16–18). But the draft never cites the canonical work
that put exactly that question on the table by arguing cloze **fails** to reach
beyond the sentence.

- **Shanahan, T., Kamil, M. L. and Tobin, A. W. (1982)** 'Cloze as a measure of
  intersentential comprehension,' *Reading Research Quarterly*, 17(2),
  pp. 229–255. — The landmark critique: by scrambling sentence order and
  comparing cloze performance on coherent vs. scrambled passages, the authors
  showed standard cloze items are largely insensitive to *intersentential*
  constraint and chiefly measure within-sentence processing. **This is the
  empirical objection the draft's open question gestures at**, and engaging it
  directly turns a rhetorical question into a positioned argument: Cloze Reader's
  single-blank, sentence-scale framing is *consistent with* what cloze can
  validly measure, rather than over-claiming passage-level comprehension.
  **Priority: High.** Anchor at l. 18, just before "one practical question
  remains open."

- **Klein-Braley, C. (1997)** 'C-Tests in the context of reduced redundancy
  testing: an appraisal,' *Language Testing*, 14(1), pp. 47–84. — Introduces the
  C-test as a psychometrically "cleaner" descendant of cloze (deleting the second
  half of every other word) developed to escape cloze's reliability problems.
  Useful as a one-clause acknowledgment that the measurement tradition itself
  kept revising the deletion mechanism — which is precisely what Cloze Reader
  does at the scale of one blank. **Priority: Medium.** Anchor near the Bachman
  rational-deletion sentence (l. 17).

---

## 2. Educational genealogy — NLP cloze datasets

The draft cites CLOTH (Xie et al. 2018) as the bridge from classroom cloze to NLP
evaluation (l. 18). A brief widening here would show CLOTH is one of a *family* of
cloze-form benchmarks, reinforcing the claim that the cloze surface form
migrated wholesale into model evaluation.

- **Hill, F., Bordes, A., Chopra, S. and Weston, J. (2016)** 'The Goldilocks
  Principle: Reading children's books with explicit memory representations,' in
  *Proceedings of ICLR 2016*. arXiv:1511.02301. — The Children's Book Test (CBT):
  cloze items auto-generated from Project Gutenberg children's books. **Doubly
  relevant** because it, like Cloze Reader, draws its blanks from Gutenberg
  texts — a direct precedent for the draft's own source choice. **Priority:
  High** (best single addition to this paragraph).

- **Paperno, D. et al. (2016)** 'The LAMBADA dataset: Word prediction requiring a
  broad discourse context,' in *Proceedings of ACL 2016*, pp. 1525–1534.
  arXiv:1606.06031. — Last-word prediction items deliberately selected so the
  answer needs the *whole* passage, not just the local sentence. A precise
  counterpoint: LAMBADA engineers the intersentential dependency that Shanahan et
  al. found ordinary cloze lacks. **Priority: Medium.**

- **Mostafazadeh, N. et al. (2016)** 'A corpus and cloze evaluation for deeper
  understanding of commonsense stories,' in *Proceedings of NAACL-HLT 2016*,
  pp. 839–849. — The Story Cloze Test: choose the correct ending of a
  five-sentence story. Shows "cloze" stretched to discourse-level inference.
  **Priority: Optional** (cite only if the CLOTH paragraph is expanded into a
  survey sentence).

---

## 3. Machine-learning genealogy

The draft's distributional → word2vec → ELMo → BERT arc is solid. Three additions
would (a) give the distributional hypothesis a modern anchor, (b) supply the
"masking is not the only objective" point the draft already half-makes via Zhang
& Hashimoto, and (c) add a survey the draft can lean on for "what masking learns."

- **Lenci, A. and Sahlgren, M. (2023)** *Distributional Semantics*. Cambridge:
  Cambridge University Press. — The authoritative recent synthesis of the
  Harris/Firth tradition the draft invokes (ll. 21). Lets the draft cite a single
  modern source for the distributional hypothesis instead of resting the whole
  lineage on the 1954/1957 primary texts. **Priority: Medium.** Anchor at l. 21
  after the Harris/Firth sentence.

- **Clark, K., Luong, M.-T., Le, Q. V. and Manning, C. D. (2020)** 'ELECTRA:
  Pre-training text encoders as discriminators rather than generators,' in
  *Proceedings of ICLR 2020*. arXiv:2003.10555. — Replaced-token detection: an
  alternative pretraining objective motivated precisely by MLM's inefficiency
  (signal at only ~15% of positions). **Strengthens the draft's existing point**
  (via Zhang & Hashimoto, l. 22) that the inheritance from Taylor's *deliberate*
  deletion to BERT's *random* masking "runs looser than the shared cloze label
  suggests" — ELECTRA is the field walking away from the cloze form altogether.
  **Priority: Medium.** Anchor at l. 22.

- **Rogers, A., Kovaleva, O. and Rumshisky, A. (2020)** 'A primer in BERTology:
  What we know about how BERT works,' *Transactions of the ACL*, 8, pp. 842–866.
  Available at: https://aclanthology.org/2020.tacl-1.54/ — Survey of what MLM
  pretraining actually induces. A convenient citation for any claim about BERT's
  learned representations and the limits of probing them — relevant to the
  draft's recurring acknowledgment that "the model's learned distributions elude a
  clear view" (l. 32). **Priority: Optional.**

- **Bender, E. M. and Koller, A. (2020)** 'Climbing towards NLU: On meaning, form,
  and understanding in the age of data,' in *Proceedings of ACL 2020*,
  pp. 5185–5198. Available at: https://aclanthology.org/2020.acl-main.463/ — The
  "octopus" argument: a system trained on form alone has no path to meaning.
  **High value as a framing citation.** The draft is scrupulous about *not*
  claiming the model understands ("a person completing a cloze and a model
  predicting a token share a surface form, the one a cognitive act and the other
  a technical one," l. 23). Bender & Koller is the standard reference for exactly
  that form/meaning distinction and would let the draft state its restraint as a
  positioned commitment. **Priority: High.** Anchor at l. 23 or in the
  "Continuity, Asymmetry" section (l. 41).

---

## 4. Data, corpora, and training-data provenance

This is the draft's strongest opportunity for *contemporary* range. It already
cites Gitelman & Jackson, Lee 2025, Lavin, Dobson, Carlini et al., Gao et al.,
and Rae et al. The following additions connect the draft's documentation ethos —
publishing source modules, documenting passage retrieval and model calls — to the
ML community's own dataset-documentation and provenance literature.

- **Gebru, T. et al. (2021)** 'Datasheets for datasets,' *Communications of the
  ACM*, 64(12), pp. 86–92. Available at: https://doi.org/10.1145/3458723 — and —
  **Bender, E. M. and Friedman, B. (2018)** 'Data statements for natural language
  processing: Toward mitigating system bias and enabling better science,'
  *Transactions of the ACL*, 6, pp. 587–604. Available at:
  https://aclanthology.org/Q18-1041/ — Together these are the field's standard
  for documenting *what a dataset is and how it was made*. **They are the natural
  scholarly frame for the draft's central design value**: the author documents
  retrieval, cleaning, and model calls in public source modules (ll. 26, 31, 34)
  and casts that legibility as a critical-making commitment. Citing the
  datasheet/data-statement tradition shows Cloze Reader's transparency mirrors,
  at game scale, a recognized practice for corpus-scale artifacts. **Priority:
  High** (cite at least one; both if the data-practices paragraph at l. 36 is
  expanded). Anchor at l. 36 alongside Gitelman & Jackson.

- **Biderman, S. et al. (2022)** 'Datasheet for the Pile,' arXiv:2201.07311.
  Available at: https://arxiv.org/abs/2201.07311 — A companion to the Gao et al.
  (2020) Pile citation the draft already uses (ll. 13, 36). If the draft wants to
  say anything precise about how the Pile's Gutenberg/PG-19 component was
  assembled and documented, this is the source. **Priority: Medium.**

- **Bender, E. M., Gebru, T., McMillan-Major, A. and Shmitchell, S. (2021)** 'On
  the dangers of stochastic parrots: Can language models be too big?,' in
  *Proceedings of FAccT '21*, pp. 610–623. Available at:
  https://doi.org/10.1145/3442188.3445922 — The canonical statement that large
  models produce fluent text by recombining training patterns "without any
  communicative intent." Supports the draft's "statistical recoverability vs.
  reading a sentence" contrast (l. 37) and its corpus-scale framing of training
  data. **Priority: Medium.**

- **Kandpal, N. et al. (2025)** 'The Common Pile v0.1: An 8 TB dataset of public
  domain and openly licensed text.' arXiv:2506.05209. Available at:
  https://arxiv.org/abs/2506.05209 — A current (2026-relevant) marker that the
  field is moving toward public-domain and openly-licensed corpora in direct
  response to the Books3/copyright controversy. Reinforces *why* Project
  Gutenberg specifically sits at the intersection of "library text" and "training
  material" the draft builds its claim on (ll. 13, 36, 43). **Priority: Medium**
  — strong because it is timely and squarely on the draft's Gutenberg-as-data
  thesis. Pairs well with a one-line acknowledgment of the Books3 dispute to
  motivate the public-domain framing.

---

## 5. Reading research and predictability

The draft's reading-science paragraph (l. 38) cites Rayner et al., Snell et al.,
Rego/Snell/Meeter, and Hofmann et al. The one missing pillar is **surprisal
theory**, the dominant computational account linking word predictability to
processing effort — and the most direct bridge between "cloze completion rates"
and "language-model probability," which is exactly the move Rego et al. make.

- **Hale, J. (2001)** 'A probabilistic Earley parser as a psycholinguistic
  model,' in *Proceedings of NAACL 2001*. — and — **Levy, R. (2008)**
  'Expectation-based syntactic comprehension,' *Cognition*, 106(3),
  pp. 1126–1177. — The origin of surprisal theory: processing difficulty scales
  with a word's negative log-probability in context. **This is the theoretical
  hinge** that makes cloze predictability and LM token probability commensurable —
  the draft's whole premise that a player and a model face "the same surface
  form." **Priority: High** (cite Levy 2008 at minimum). Anchor at l. 38 between
  the Rayner and Snell sentences.

- **Smith, N. J. and Levy, R. (2013)** 'The effect of word predictability on
  reading time is logarithmic,' *Cognition*, 128(3), pp. 302–319. — The
  quantitative refinement showing the predictability/reading-time relationship is
  log-linear. Add only if surprisal is discussed in more than one sentence.
  **Priority: Optional.**

---

## 6. Game design, critical making, and play

The draft cites Gee, Squire, Vygotsky, Wood/Bruner/Ross, Pea (learning design);
Ratto, Ramsay & Rockwell (critical making); Flanagan, Flanagan & Nissenbaum
(critical play / values). Two additions would deepen, not pad.

- **Bogost, I. (2007)** *Persuasive Games: The Expressive Power of Videogames*.
  Cambridge, MA: MIT Press. — and — **Sicart, M. (2011)** 'Against procedurality,'
  *Game Studies*, 11(3). Available at: https://gamestudies.org/1103/articles/sicart_ap
  — Bogost's **procedural rhetoric** (meaning carried by rules and mechanics, not
  just theme) is the precise theoretical name for the draft's claim that "values
  in a game live in mechanics as well as theme" and that Cloze Reader's values are
  "built into scoring by exact match, withholding the answer, limiting retries"
  (l. 37). Sicart's rebuttal — that players, not rules, make meaning — is a
  productive tension the draft can use, since Cloze Reader deliberately constrains
  the player's action down to one word. **Priority: Medium** (Bogost High if the
  values-in-mechanics claim is foregrounded). Anchor at l. 37 with the
  Flanagan & Nissenbaum sentence.

- **Csikszentmihalyi, M. (1990)** *Flow: The Psychology of Optimal Experience*.
  New York: Harper & Row — and/or — **Malone, T. W. and Lepper, M. R. (1987)**
  'Making learning fun: A taxonomy of intrinsic motivations for learning,' in
  Snow, R. E. and Farr, M. J. (eds) *Aptitude, Learning, and Instruction, Vol. 3*.
  Hillsdale, NJ: Erlbaum, pp. 223–253. — The draft's reliance on Gee's "regime of
  competence" and "cycle of expertise" (l. 35) rests on a challenge-calibration
  idea that originates with flow theory and the Malone/Lepper taxonomy. One
  citation grounds the difficulty-ramp design (levels, narrowing cues) in the
  motivation literature. **Priority: Optional.**

---

## 7. Literacy debate and slow reading

The draft's closing sections invoke Graff (literacy myth) and Rebora et al.
(digital social reading), and argue for reading "at the scale of one word."

- **Hayles, N. K. (2010)** 'How we read: Close, hyper, machine,' *ADE Bulletin*,
  150, pp. 62–79. (Also in *How We Think: Digital Media and Contemporary
  Technogenesis*, University of Chicago Press, 2012.) — Hayles's three-mode
  taxonomy — close, hyper, and machine reading — is the standard frame for
  situating a "machine-mediated" reading act against close reading. **The draft's
  thesis is essentially a small instance of Hayles's argument**: Cloze Reader
  stages a meeting of machine reading (the model's prediction) and close reading
  (the player's sentence-scale recovery). Citing Hayles names the conversation the
  draft is joining. **Priority: High** for the "Continuity, Asymmetry, and Slow
  Reading" section (ll. 41–43). Anchor near the Graff/Rebora sentence (l. 42).

---

## Summary table

| # | Source | Cluster | Anchor (draft line) | Priority |
|---|--------|---------|--------------------|----------|
| 1 | Shanahan, Kamil & Tobin (1982) | cloze validity critique | l. 18 | **High** |
| 2 | Hill et al. (2016), CBT | NLP cloze datasets | l. 18 | **High** |
| 3 | Bender & Koller (2020), octopus | form vs. meaning | l. 23 / l. 41 | **High** |
| 4 | Gebru et al. (2021) / Bender & Friedman (2018) | data documentation | l. 36 | **High** |
| 5 | Levy (2008) (+ Hale 2001) | surprisal / predictability | l. 38 | **High** |
| 6 | Hayles (2010) | reading modes / slow reading | l. 42 | **High** |
| 7 | Klein-Braley (1997), C-test | cloze refinement | l. 17 | Medium |
| 8 | Lenci & Sahlgren (2023) | distributional hypothesis | l. 21 | Medium |
| 9 | Clark et al. (2020), ELECTRA | MLM alternatives | l. 22 | Medium |
| 10 | Bender, Gebru et al. (2021), parrots | recoverability vs. reading | l. 37 | Medium |
| 11 | Kandpal et al. (2025), Common Pile | public-domain training data | l. 36 | Medium |
| 12 | Bogost (2007) / Sicart (2011) | procedural rhetoric / play | l. 37 | Medium |
| 13 | Paperno et al. (2016), LAMBADA | discourse-level cloze | l. 18 | Optional |
| 14 | Mostafazadeh et al. (2016), Story Cloze | discourse-level cloze | l. 18 | Optional |
| 15 | Biderman et al. (2022), Pile datasheet | corpus provenance | l. 36 | Optional |
| 16 | Rogers et al. (2020), BERTology | what MLM learns | l. 32 | Optional |
| 17 | Smith & Levy (2013) | predictability (log-linear) | l. 38 | Optional |
| 18 | Csikszentmihalyi (1990) / Malone & Lepper (1987) | flow / motivation | l. 35 | Optional |

## Caution: where *not* to add

The draft's strength is its narrow scale — "one sentence with one missing word."
Several candidates above (stochastic parrots, the Books3 dispute, ELECTRA, the
full NLP-benchmark family) carry their own large debates. Import them as
**single positioning citations**, not as paragraphs; a survey of LLM-ethics or
benchmark history would pull the essay off its declared scale and dilute the
critical-making argument. The two additions that most repay the space are
**Shanahan et al. (1982)** and **Bender & Koller (2020)**, because each converts
a move the draft already makes implicitly — its restraint about comprehension,
its restraint about understanding — into an explicit, positioned scholarly claim.
