# <u>Fill in the Blank and Cloze Reader's Twin Histories of Occlusion</u>

**Zach Muhlbauer**
The Graduate Center, CUNY
<https://reader.inference-arcade.com>
<u>Site deployment</u> <https://milwrite.github.io/quimbot/cloze-reader-draft/>

# Abstract

<u>Wilson Taylor's cloze procedure began as a classroom test in which a teacher or researcher deletes words from prose and asks readers to restore them from context. Machine learning later turned missing-word prediction into a pretraining objective by hiding tokens across large corpora and training models to infer them from surrounding text. Cloze Reader, a browser game I built through the CUNY AI Lab and the Inference Arcade initiative, limits the language model to narrower work. The model chooses one or more words from a Project Gutenberg passage under prompt rules, validation checks, hint limits, and level settings. The interface then holds the player at the blank with the title, passage, sentence, and cues still visible. The player restores the word through grammar, genre, historical setting, and the immediate pressure of the sentence. Each round returns corpus material to prose, where reading on the page tests model prediction.</u>

# Introduction

<u>In 1953, Wilson Taylor turned the Gestalt idea of closure into a reading test. He deleted words from prose and asked readers to restore each one from the surrounding passage. To answer, a reader had to hold the visible sentence in mind, follow the grammar around the blank, and infer from the cues already in the passage. Taylor's results suggested that contextual prediction measured comprehension more precisely than formulas built from sentence length or word length.</u>

<u>Masked language modeling trains on blanks. A model sees text with tokens hidden, predicts those tokens from surrounding words, and uses the error to adjust its representations of word relations. Cloze Reader lets the player see the split. Prompt rules ask a language model to choose a word from a Project Gutenberg passage, and the interface presents the blank with the passage, book title, level cues, and hint limits still visible. Cloze Reader draws from Project Gutenberg because the same public-domain books circulate as library texts and as model-training material. Readers meet them as titled works with genres, publication histories, sentences, and scenes. Corpus pipelines handle them as extractable text. The Pile, for example, is an 825 GiB English corpus built from twenty-two subsets, including a Gutenberg component drawn from PG-19, a set of pre-1919 Project Gutenberg books used for long-context language modeling (Gao et al. 2020). I limit the claim to collection level. Gutenberg is corpus material here, and Cloze Reader returns one passage to the player as a sentence from a book.</u>

# The Educational Genealogy of Cloze

<u>Taylor's procedure looked simple on the page. A fixed-ratio cloze test deletes every nth word from a passage and asks the reader to restore the missing term. Taylor treated the recovered word as evidence of comprehension because one answer draws on the prior clause, the likely continuation, the passage topic, and the grammar of the blank. The reader has to hold the visible sentence in mind, judge which kind of word can occupy the opening, and choose a term that the passage can absorb. Koffka's account of Gestalt perception clarifies how a broken form can remain active through the visible contour around it (Koffka 1935), and Taylor adapted that logic to prose, where a deleted word leaves enough shape around the absence for a reader to work. Oller (1979) later called the linguistic version of that coordination "pragmatic expectancy grammar," the knowledge that lets readers anticipate likely next words in a well-formed utterance. Cloze interrupts a sentence and asks the reader to answer from the visible context.</u>

<u>Scoring rules exposed the method's limits. Exact-word scoring anchors rating to the author's original word. Synonym scoring accepts a word that fits the same local meaning, protecting the semantic flexibility that Oller's account implies (Jongsma 1980). A reader who writes a semantically apt synonym may have understood the passage, even when the test records failure. Abraham and Chapelle (1992) sharpened the point by treating item difficulty as part of what a cloze score means, since each blank samples a different mixture of grammar, vocabulary, and passage-level inference. Bachman (1985) showed that selected words can test inference more directly than a fixed interval can. The missing word occupies a chosen site in a sentence. Cloze Reader inherits that design problem. Prompt rules define the candidate site through difficulty, part of speech, word length, and passage position, and code checks whether the model's chosen word can bear that work.</u>

<u>NLP evaluation adopted cloze through test datasets. Xie et al. (2018) built CLOTH from middle-school and high-school language exams, where teachers had already written blanks and answer choices to test passage-level inference. The ACL record says CLOTH contains blanks "carefully created by teachers" and candidate choices "purposely designed to be nuanced," and that description ties the dataset to exam design as NLP evaluation repurposes it. Xie et al. also describe CLOTH as requiring "deeper language understanding" and a "wider attention span" than earlier automatically generated cloze datasets. Teacher-made blanks still carry assumptions about what readers should infer, how much context they should use, and where a wrong answer reveals weak comprehension. CLOTH separates classroom cloze from model evaluation while tracing the procedure across institutions, from readability research to standardized testing to NLP benchmarks. The practical question remains. Which missing word can legitimately stand for the work of reading?</u>

# The Machine Learning Genealogy

<u>Machine learning reached cloze through distributional accounts of language, where words acquire structure through the contexts in which they appear. Harris (1954) treated co-occurrence as evidence of grammatical patterning, and Firth (1957) pushed co-occurrence toward meaning by arguing that a word's company shapes what the word can mean. If recurring neighbors mark grammatical and semantic relations, a system with enough text can learn about words by tracking the positions they occupy around one another. Mikolov's word2vec system made prediction the engine of that account by training shallow networks to infer surrounding context from a target word or to infer a target word from surrounding context (Mikolov et al. 2013). The skip-gram and continuous-bag-of-words objectives used local prediction to produce dense vectors, and those vectors captured syntactic and semantic regularities. Word2vec still assigned each word one numerical identity across uses, so a word such as bank shared the same vector near account and near river even when the sentence required different readings.</u>

<u>Peters et al. (2018) tied representation to sentence context with ELMo, assigning each token a representation that depends on "the entire input sentence" through bidirectional language modeling. Devlin et al. (2019) then trained BERT to predict masked tokens while "jointly conditioning" on left and right context in every layer, making bidirectional context part of one transformer encoder pass. Devlin et al. trace the inheritance explicitly when they write that MLM is "often referred to as a Cloze task" and cite Taylor in the same paragraph. Their implementation masks 15 percent of WordPiece tokens at random before predicting the original vocabulary item. Masking could scale because unannotated text already contained the training signal, with large corpora supplying enough examples for pretraining (Liu et al. 2021, Bommasani et al. 2021). The cloze form moved from a human response sheet into an automated training loop, where millions of blanks teach a model to distribute expectation across text. Taylor and BERT still do different work because Taylor used deletion to test whether a reader could coordinate passage meaning, while BERT uses masking to adjust representations. Taylor's procedure measures a performance, and BERT trains a system.</u>

<u>Recent cloze evaluation documents the asymmetry. Xie et al. reported teacher-authored cloze items where model performance lagged human test takers on exam-style blanks, and Jacobs, Grobol, and Tsang (2024) later compared language-model predictions with human cloze productions at the level of single-token completions. Their arXiv abstract reports that models under-estimate human responses, over-rank rare responses, under-rank top responses, and produce distinct semantic spaces. Cloze Reader takes a modest lesson from that work. Human cloze completion and model token prediction share a surface form. They do different work, one cognitive and one technical. I use the model's prediction capacity to choose where the blank appears, then require the player to restore a word inside a titled passage, with sentence meaning and book context still in view.</u>

# Cloze Reader

<u>In Cloze Reader, a round begins with a book passage, a title, and a source record. Public source modules document my passage retrieval through the Hugging Face Datasets API and my calls to Google's Gemma-3-27B model for word selection, hints, and contextualization (Cloze Reader 2026a). The book service streams records from a Gutenberg dataset, falls back to local books if streaming fails, and extracts title and author metadata when it can. It also cleans away Gutenberg headers, scanning notes, URLs, chapter lists, page numbers, bracketed notes, and other lines that would push a cloze round toward metadata work and away from reading (Cloze Reader 2026a). The game engine pulls a passage from the middle of a text and rejects front matter, tables of contents, all-capital noise, reference patterns, number-heavy lines, and brittle formatting. It builds the round only after the passage has enough sentence structure to support a blank (Cloze Reader 2026c). Those filters narrow the archive before the model predicts a word, so the player receives a passage that can still be read as prose.</u>

![Cloze Reader interface showing one blank and the hint panel](../../docs/cloze-reader-draft/cloze-reader-screenshot-current.png)

<u><em>Figure 1. A Cloze Reader round in use. I present a passage from Our Legal Heritage, 4th Ed. by S. A. Reilly at Level 1 with one blank. The blank falls inside a discussion of royal preaching restrictions and Puritan dissent, and the hint panel remains available.</em></u>

<u><em>Figure description. A historical prose passage appears with one blank and a hint control. The blank anchors a local lexical decision inside a passage with legal and religious context.</em></u>

<u>I route each round through word selection before any blank appears. The public aiService.js module records my call to google/gemma-3-27b-it and the selection prompt for exact lowercase words from the middle or end of a passage (Cloze Reader 2026b). The prompt limits candidates by length, difficulty, and part of speech, while the validation layer checks that the chosen words appear in the passage and meet the constraints. When the model produces unusable results, a fallback routine excludes common function words (Cloze Reader 2026c). I write pedagogical aims into a procedure that the model must satisfy before the player sees a puzzle. A fixed-ratio cloze test hides its selection logic inside arithmetic, since every fifth or seventh word disappears independent of the word's role in the passage. Cloze Reader's natural-language prompt leaves selection logic open to criticism. The prompt exposes difficulty, word length, part of speech, and passage position as readable parts of the procedure. The prompt directs the model, and validation code audits the answer.</u>

<u>I also separate selection from hinting because each model call creates a different pedagogical risk. At selection time, Gemma receives only the selection call. I build the later hint call around the blank after the code has stored the selected word in game state. Shared context between selection and hint generation would pull selection toward words the hint system can handle easily, so word selection, hint generation, and passage summary run as separate calls. Each call receives only the passage text and the instructions for one task (Cloze Reader 2026b). The code stores the model's output in game state once, and the next call receives a fresh instruction. A smaller-model substitution proposal made the boundary clearer. Word selection might be partly reproducible with frequency scores and part-of-speech tags, since the code already checks lowercase form, passage position, length, and word presence. Hint generation is harder because the model receives the answer privately and must guide the player while preserving the target word and avoiding near equivalents. I assemble the puzzle from separate procedures, each narrow enough to inspect even though the model's learned distributions remain hard to see.</u>

## <u>Smaller Models and Task Boundaries</u>

<u>Smaller models shift the boundary between model choice and code checks. In my implementation, word selection depends most heavily on the model, although the code already enforces many hard constraints after generation. The chosen word must appear in the passage, match the target length, avoid the opening words, and survive validation before the round can proceed (Cloze Reader 2026c). A frequency table and a part-of-speech tagger could handle much of that work before a model chooses from the remaining candidates. Prompt rules, validation code, fallback logic, and model output all decide what the player sees. I design hints differently because the model receives the answer privately and must guide the player while withholding it. I place preset prompts about part of speech, sentence role, word category, or synonymy in the embedded panel (Cloze Reader 2026d), and the code instructs the model to withhold the answer word (Cloze Reader 2026b). A compact model that writes fluent hints would still fail the round by leaking the answer, echoing the answer's morphology, or offering a synonym that collapses the puzzle. The hint has to preserve the player's obligation to read while giving the player enough grammar and meaning to continue.</u>

<u>The gameplay structure joins those code boundaries to paced action. I vary each run of Cloze Reader by drawing every session from a streamed Gutenberg dataset, calling for selections at temperature 0.5, and preloading books from random offsets in the dataset proxy (Cloze Reader 2026a). At early levels, I display one blank and include word length with first and last letters. Later levels introduce two or three blanks and reduce the cue to a first letter (Cloze Reader 2026c). I also shift the selection prompt from easy to medium to challenging vocabulary as levels rise (Cloze Reader 2026b). After a submission, the engine tracks attempts per blank, locks correct answers, stores retryable indices, and either marks retryable blanks or advances the level when the pass conditions are met (Cloze Reader 2026c). The pass rule changes with blank count, requiring the single answer in a one-blank round, both answers in a two-blank round, and all but one answer once the round has three or more blanks (Cloze Reader 2026c). Gee (2005) clarifies the learning design because he describes good games as keeping new challenges at "the outer edge of" a learner's "regime of competence," with feedback that lets players see effort paying off. Gee's "cycle of expertise" describes the rhythm of practice, failure, reflection, and renewed practice that levels can create. His account of information "just in time" and "on demand" also describes why the hint panel appears after the player has already met the blank. Squire (2006) calls game play a "designed experience," and Cloze Reader uses that structure at the sentence scale. The player commits a word, receives a score, opens a clue if needed, and tries another blank with the same passage still on screen. Wood, Bruner, and Ross (1976), Vygotsky (1978), and Pea (2004) clarify the pedagogical limit of that assistance. The hint panel supports one decision at a time and leaves long-term learner history outside its scope, staying local and stopping short of a full learner model.</u>

<u>I draw passages from Project Gutenberg books with titles, genres, and histories, and I state the source claim at the corpus level. Gao et al. describe The Pile as an 825 GiB English corpus built from twenty-two subsets, including a Gutenberg component drawn from PG-19. The PG-19 project describes its benchmark as books extracted from Project Gutenberg and published before 1919, with title and publication metadata included in the release (Rae et al. 2019, Gao et al. 2020). I state the connection at collection level because the live game streams Project Gutenberg passages, while the model's exact training mixture remains unavailable from the public game code. Carlini et al. (2021) also document how large language models can reproduce memorized training passages under targeted conditions, so training-data circulation remains part of the round's design while leaving specific passage-in-weight claims outside the evidence. A corpus pipeline handles the book differently before Cloze Reader opens it. The pipeline breaks sequence into tokens, stores those tokens through metadata decisions and cleaning rules, and folds their statistics into model training. Gitelman and Jackson (2013) describe how institutions, formats, categories, and labor prepare documents as data. I place a passage before a reader after those collection and modeling practices have already made Gutenberg useful to machine learning.</u>

<u>Figure 1 holds the claim at passage scale. I present a passage from Our Legal Heritage, 4th Ed. by S. A. Reilly, where a discussion of royal preaching restrictions and Puritan dissent appears as a sentence with one missing word. The player has to use syntax, local diction, and topic to advance. During that pause, prose that a large corpus can compress into training signal appears with a title, a source, a passage boundary, and a human decision attached. Ratto (2011) describes critical making as "materially productive engagement," and the phrase fits the build process because each code boundary changed what I could claim. The service has to clean and validate a passage before the model can choose a blank. The hint withholds the answer so the player still has to read. The score counts only the target word, even when a plausible synonym might signal comprehension. Flanagan's account of critical play, where play environments represent "questions about aspects of human life," guards the design from becoming a decorative wrapper for a quiz (Flanagan 2009). Flanagan and Nissenbaum's values-at-play framework sharpens the design claim because values in a game live in mechanics as well as theme. Cloze Reader's values sit in exact-match scoring, answer withholding, retry rules, source display, and the decision to cast a model-generated blank as play. Cloze Reader poses its critical problem at the scale of one word as the player experiences the difference between statistical recoverability and reading a sentence.</u>

<u>Reading research places this pause within a longer history. Fluent readers generate expectations about upcoming words as they read through a sentence (Rayner et al. 2012). Cloze completion rates later served as a standard measure of word predictability, and computational models of reading use those rates to estimate how expectation changes eye movement and reading time (Snell et al. 2018). Rego, Snell, and Meeter (2024) extend that work through a cognitive model that incorporates language-model predictability. Hofmann et al. (2021) still note that offline cloze completion differs from the rapid expectations of ordinary reading. I slow that difference down until the player can see prediction as an action, with the player's attempt, the score response, and any hint use marking work that usually happens quickly while reading.</u>

# Continuity, Asymmetry, and Slow Reading

<u>Each round combines Taylor's deletion and BERT's mask. Taylor used deletion to test whether a reader could restore sense from context, while BERT used masked tokens to induce representations from large-scale text. I let the model select the site of deletion and require the player to restore the word, separating selection from interpretation at the level of the round. The model identifies a word that should carry pressure inside a passage, the interface hides it, the player tests a word, and the score records the attempt. Because scoring follows model selection, the player completes the sentence with the model's chosen site still visible as a design decision. Ramsay and Rockwell (2012) argue that digital artifacts can advance knowledge when they render the world legible in new ways, and Cloze Reader renders one model-mediated reading problem legible through procedure. The argument depends on the source code, prompt rules, passage filters, hint limits, score response, and screenshot because each one decides what kind of reading can happen.</u>

<u>The literacy-crisis discourse Graff critiques often casts historical change as a story of loss, and research on digital social reading documents new records of reception and exchange on networked platforms (Graff 2022, Graff 2023, Rebora et al. 2021). I ground that debate in a smaller object, one sentence with one missing word. I take language models seriously while keeping reading in the frame, at the moment when a model points to a word and a human reader has to recover the sentence around it. The player works at the scale of clauses and cues, studying the clause before the blank, the clause after it, the passage topic, the length cue, and the hint panel's partial guidance. The interface records attention as a sequence of constrained decisions, and the constraint pulls the discussion away from the usual scale of AI talk. Model culture often discusses language at corpus, benchmark, and platform scale. Cloze Reader brings the scale down until a player can feel how much meaning gathers around one word.</u>

<u>Project Gutenberg records an earlier promise for computation and literary circulation. On July 4, 1971, Michael Hart typed the Declaration of Independence into a University of Illinois mainframe, and Project Gutenberg's record recalls the file in uppercase because those early systems displayed uppercase characters only. Hart later described the act as a wager that computers would improve the storage, retrieval, and search of library texts (Hart 1992, Project Gutenberg 2025). Newby (2019) places that act at the start of a volunteer-built archive organized around public-domain circulation. I work with that archive after corpus builders have also used public-domain books from it as training material. Digital humanities needs artifacts at this scale because large models now carry public-domain books through tokenization, filtering, weighting, and interface design before readers meet them again. Cloze Reader condenses that chain into a small, inspectable form. Read the sentence, use the clue if needed, commit one word, and see how much of the passage had to remain present for the answer to cohere. Cloze Reader's claim begins there, with a public-domain sentence brought out of dataset scale and a player learning how grammar, genre, source, and judgment convert prediction into reading on the page.</u>

# References

<u>Abraham, R. G. and Chapelle, C. A. (1992) 'The meaning of cloze test scores: An item difficulty perspective,' The Modern Language Journal, 76(4), pp. 468–479.</u>

Bachman, L. F. (1985) 'Performance on cloze tests with fixed-ratio and rational deletions,' TESOL Quarterly, 19(3), pp. 535–556.

Bommasani, R. et al. (2021) 'On the opportunities and risks of foundation models,' arXiv:2108.07258. Available at: https://arxiv.org/abs/2108.07258

Carlini, N. et al. (2021) 'Extracting training data from large language models,' in Proceedings of the 30th USENIX Security Symposium. USENIX Association, pp. 2633–2650.

Cloze Reader (2026a) 'bookDataService.js'. Available at: https://reader.inference-arcade.com/src/bookDataService.js (Accessed: 18 March 2026).

Cloze Reader (2026b) 'aiService.js'. Available at: https://reader.inference-arcade.com/src/aiService.js (Accessed: 18 March 2026).

Cloze Reader (2026c) 'clozeGameEngine.js'. Available at: https://reader.inference-arcade.com/src/clozeGameEngine.js (Accessed: 18 March 2026).

Cloze Reader (2026d) 'conversationManager.js'. Available at: https://reader.inference-arcade.com/src/conversationManager.js (Accessed: 18 March 2026).

Devlin, J. et al. (2019) 'BERT: Pre-training of deep bidirectional transformers for language understanding,' in Proceedings of NAACL-HLT 2019. Minneapolis, MN: Association for Computational Linguistics, pp. 4171–4186.

Dobson, J. (2021) 'Interpretable Outputs: Criteria for Machine Learning in the Humanities,' Digital Humanities Quarterly, 15(2). Available at: https://doi.org/10.63744/gqdn7tfwn6r8

Firth, J. R. (1957) 'A synopsis of linguistic theory, 1930–1955,' in Studies in Linguistic Analysis. Oxford: Philological Society, pp. 1–32.

Flanagan, M. (2009) Critical Play: Radical Game Design. Cambridge, MA: MIT Press.

Flanagan, M. and Nissenbaum, H. (2014) Values at Play in Digital Games. Cambridge, MA: MIT Press.

Gao, L. et al. (2020) 'The Pile: An 800GB dataset of diverse text for language modeling,' arXiv:2101.00027. Available at: https://arxiv.org/abs/2101.00027

<u>Gee, J. P. (2005) 'Learning by design: Good video games as learning machines,' E-Learning and Digital Media, 2(1), pp. 5–16. Available at: https://doi.org/10.2304/elea.2005.2.1.5</u>

Gitelman, L. and Jackson, V. (2013) 'Introduction,' in Gitelman, L. and Jackson, V. (eds) 'Raw Data' Is an Oxymoron. Cambridge, MA: MIT Press, pp. 1–14.

Graff, H. J. (2022) 'The New Literacy Studies and the Resurgent Literacy Myth,' Literacy in Composition Studies, 9(1), pp. 47–53. Available at: https://doi.org/10.21623/1.9.1.4

Graff, H. J. (2023) 'Opinion: The Persistent “Reading Myth” and the “Crisis of the Humanities”,' College Composition & Communication, 74(3), pp. 575–580. Available at: https://doi.org/10.58680/ccc202332367

Harris, Z. S. (1954) 'Distributional structure,' Word, 10(2–3), pp. 146–162.

Hart, M. (1992) 'The History and Philosophy of Project Gutenberg.' Available at: https://www.gutenberg.org/about/background/history_and_philosophy.html (Accessed: 13 April 2026).

Hofmann, M. J. et al. (2021) 'The influence of information in the sentence context on predictions in reading,' Neuropsychologia, 158, 107885.

<u>Jacobs, C. L., Grobol, L. and Tsang, A. (2024) 'Large-scale cloze evaluation reveals that token prediction tasks are neither lexically nor semantically aligned,' arXiv:2410.12057. Available at: https://arxiv.org/abs/2410.12057</u>

Jongsma, E. (1980) Cloze instruction research: A second look. Newark, DE: International Reading Association.

Koffka, K. (1935) Principles of Gestalt Psychology. New York: Harcourt, Brace and World.

Lavin, M. (2021) 'Why Digital Humanists Should Emphasize Situated Data over Capta,' Digital Humanities Quarterly, 15(2).

Lee, B. C. G. (2025) 'The “Collections as ML Data” checklist for machine learning and cultural heritage,' Journal of the Association for Information Science and Technology, 76(2), pp. 375–396. Available at: https://doi.org/10.1002/asi.24765

Liu, X. et al. (2021) 'Self-supervised learning: Generative or contrastive,' IEEE Transactions on Knowledge and Data Engineering, 35(1).

Mikolov, T. et al. (2013) 'Efficient estimation of word representations in vector space,' arXiv:1301.3781.

Newby, G. B. (2019) Forty-Five Years of Digitizing Ebooks: Project Gutenberg's Practices. Available at: https://www.gutenberg.org/ebooks/60600 (Accessed: 13 April 2026).

Oller, J. W. (1979) Language Tests at School. London: Longman.

Pea, R. D. (2004) 'The social and technological dimensions of scaffolding and related theoretical concepts for learning, education, and human activity,' Journal of the Learning Sciences, 13(3), pp. 423–451.

Peters, M. E. et al. (2018) 'Deep contextualized word representations,' in Proceedings of NAACL-HLT 2018. New Orleans, LA: Association for Computational Linguistics, pp. 2227–2237.

Project Gutenberg (2025) The Declaration of Independence of the United States of America. Available at: https://www.gutenberg.org/0/1/1-h/1-h.htm (Accessed: 13 April 2026).

Project Gutenberg (2026) Project Gutenberg. Available at: https://www.gutenberg.org/ (Accessed: 18 March 2026).

<u>Rae, J. W. et al. (2019) 'Compressive transformers for long-range sequence modelling,' arXiv:1911.05507. Available at: https://arxiv.org/abs/1911.05507</u>

Ramsay, S. and Rockwell, G. (2012) 'Developing Things: Notes toward an Epistemology of Building in the Digital Humanities,' in Gold, M. K. (ed.) Debates in the Digital Humanities. Minneapolis: University of Minnesota Press, pp. 75–84.

Ratto, M. (2011) 'Critical Making: Conceptual and Material Studies in Technology and Social Life,' The Information Society, 27(4), pp. 252–260. Available at: https://doi.org/10.1080/01972243.2011.583819

Rayner, K. et al. (2012) Psychology of Reading. 2nd edn. New York: Psychology Press.

Rebora, S. et al. (2021) 'Digital humanities and digital social reading,' Digital Scholarship in the Humanities, 36(Supplement_2), pp. ii230–ii250. Available at: https://doi.org/10.1093/llc/fqab020

Rego, A. T. L., Snell, J. and Meeter, M. (2024) 'Language models outperform cloze predictability in a cognitive model of reading,' PLOS Computational Biology, 20(9), e1012117. Available at: https://doi.org/10.1371/journal.pcbi.1012117

Snell, J. et al. (2018) 'OB1-reader: A model of word recognition and eye movements in text reading,' Psychological Review, 125(6), pp. 969–1013.

<u>Squire, K. (2006) 'From content to context: Videogames as designed experience,' Educational Researcher, 35(8), pp. 19–29. Available at: https://doi.org/10.3102/0013189X035008019</u>

Taylor, W. L. (1953) '"Cloze procedure": A new tool for measuring readability,' Journalism Quarterly, 30(4), pp. 415–433.

Vygotsky, L. S. (1978) Mind in Society: The Development of Higher Psychological Processes. Cambridge, MA: Harvard University Press.

Wood, D., Bruner, J. S. and Ross, G. (1976) 'The role of tutoring in problem solving,' Journal of Child Psychology and Psychiatry, 17(2), pp. 89–100.

<u>Xie, Q. et al. (2018) 'Large-scale cloze test dataset created by teachers,' in Proceedings of EMNLP 2018. Brussels: Association for Computational Linguistics, pp. 2344–2356. Available at: https://aclanthology.org/D18-1257/</u>
