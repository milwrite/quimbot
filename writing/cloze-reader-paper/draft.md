
# Fill in the Blank: Cloze Reader and the Twin Histories of Occlusion

**Zach Muhlbauer**
The Graduate Center, CUNY
<https://reader.inference-arcade.com>
Site deployment: <https://milwrite.github.io/quimbot/cloze-reader-draft/>

---

# Abstract

This essay traces the cloze procedure across two linked histories. The
first begins with Wilson Taylor's use of deleted words as a measure of
reading comprehension. The second runs from distributional linguistics
to masked language modeling. I argue that Cloze Reader, a browser-based
game I built through the CUNY AI Lab and the Inference Arcade
initiative, serves as a critical artifact at their intersection. The
game delegates word selection to a large language model, then returns
the blank to a human reader who must infer a term from local context.
This design makes a technical genealogy visible, yet it also returns
Project Gutenberg passages to a scale at which a reader must attend to
syntax, genre, and historical texture. Cloze Reader turns a pretraining
operation into a scene of slow reading. In so doing, it asks how digital
humanities might surface the archive inside the dataset, expose the
assumptions built into model-mediated pedagogy, and examine what happens
when literary works move from historical content to training data and
back again.

# Introduction

Cloze reading began as a procedural test. A passage is redacted of specific words  at fixed intervals, and the reader supplied what was missing. Taylor (1953) drew
on the Gestalt principle of closure that Koffka (1935) described and
recast it as a way to gauge comprehension as an integrated act. The
procedure asked whether a reader could use syntax, semantics, and
discourse at once. Its results suggested that contextual prediction
tracked comprehension more closely than older readability formulas did.

The premise later reappeared in machine learning, where researchers in
distributional linguistics and neural language modeling also treated the
missing word as an index of linguistic competence. The shared structure
tempts a flat analogy between human reading and model prediction, which
I treat as a historical clue whose force lies in the trace it leaves.

I argue that Cloze Reader, a browser-based game I built through the CUNY
AI Lab and the Inference Arcade initiative, works as a critical artifact
at the crossing point between those two histories. The game delegates
word removal to a language model through heuristic prompts, then returns
the blank to a human reader who must infer a term from local context.
This arrangement makes the continuity of the cloze procedure visible. It
also exposes a split in purpose. Taylor used cloze to assess
comprehension. Masked language modeling uses the same structure to
induce representations through pretraining.

This split matters in digital humanities because many texts that feed
model training also circulate as literary and historical materials with
their own provenance, genre, and rhetorical force. Cloze Reader draws
its passages from Project Gutenberg. Those books already sit inside
major training corpora such as The Pile (Gao et al. 2020). Once
pretraining absorbs them, they tend to appear as token distributions and
latent weights, detached from sequence, authorship, and scene. The game
returns them to the surface one passage at a time, which asks a player
to stop at a single lexical site and rebuild sense from syntax, genre,
and historical diction.

This return to the passage forms the paper's central claim. Cloze Reader
does not prove that human readers and language models infer in the same
way. It stages their contact inside a shared textual procedure and lets
that contact expose what pretraining leaves out. The result is a case
for slow reading within model culture. It is also a way to ask how
digital humanities might surface the archive inside the dataset, expose
the assumptions built into pedagogical interfaces, and track what
happens when works from Project Gutenberg move from literary objects to
training data and back again.

The sections that follow trace the educational genealogy of cloze, then
the machine learning genealogy, before I turn to the game's
architecture. I close with an argument about continuity and asymmetry.
The blank marks the point at which a text reappears as something more
than an input stream.

# The Educational Genealogy of Cloze

Wilson Taylor's 1953 procedure looked simple. Delete words from a
passage at fixed intervals and ask readers to restore them. Yet the
method carried a larger claim. Taylor adapted Gestalt closure to measure
comprehension as a whole, and he treated the recovered word as evidence
that a reader could coordinate syntax, semantics, and discourse inside a
single act of interpretation (Taylor 1953).

Oller (1979) gave that method a fuller theory. He described cloze
performance through what he called "pragmatic expectancy grammar," the
linguistic knowledge that lets readers and speakers anticipate what can
and cannot come next in a well-formed utterance. On this account, cloze
does not isolate a subskill. It tests an integrated competence that
ordinary comprehension already uses. At that point, cloze ceased to be
only a readability tool. It became a model of expectancy within prose.

Once cloze took that form, two debates exposed what the procedure could
and could not claim. The first concerned scoring. Should a reader
receive credit only for the author's original word, or should a synonym
count as well? Exact-word scoring produced reliable agreement across
raters and correlated with other comprehension measures. Synonym scoring
preserved the flexibility that Oller's theory implies (Jongsma 1980).
The dispute matters because it reveals an unresolved question at the
center of the method. Does cloze test comprehension of a passage, or
does it test successful recovery of one author's lexical choice? A
reader who supplies a semantically apt synonym has understood the
passage even if the test records failure.

This debate shifted attention from scoring to selection, showing that
deletion is never neutral. Someone, or something, decides which lexical
sites will bear the weight of the test. The point matters for Cloze
Reader because the game inherits the old problem in a new form. I
delegate selection to a language model through instructions about
difficulty, part of speech, and passage position. The game therefore
stands inside the older argument about what counts as a meaningful
blank.

This older history also prepares the move into machine learning. Once
cloze became a formal account of expectancy, its core logic could
travel. The next genealogy gives that logic a new technical vocabulary
and a new scale.

# The Machine Learning Genealogy

The move from classroom instrument to training objective did not happen
by accident. Cloze testing and masked language modeling both rest on the
distributional hypothesis, the idea that words acquire structure and
meaning through the company they keep. Harris (1954) formalized
co-occurrence as a basis for grammatical structure. Firth (1957) pushed
the same observation toward semantics. His claim that one knows a word
by the company it keeps gave later computational work a concise
expression of the problem.

Early neural language models operationalized that problem at scale.
Mikolov's word2vec system trained shallow networks to predict
surrounding context from a target word or the reverse relation through
skip-gram and continuous bag-of-words objectives (Mikolov et al. 2013).
The resulting vectors captured regularities in syntax and semantics, yet
each word still received one representation. Context did not alter the
vector. The word bank kept the same numerical identity beside account
and beside river.

ELMo changed that condition. Peters et al. (2018) trained forward and
backward LSTM language models and combined their outputs so that a
word's representation depended on the sentence in which it appeared.
BERT extended that move through a joint transformer encoder that
predicted masked tokens from full bidirectional context inside one model
(Devlin et al. 2019). Masking could serve as a self-supervised objective
because unannotated text already contained the relevant signal (Liu et
al. 2021). The scale of available corpora then made that objective
effective for large-parameter pretraining (Bommasani et al. 2021).

By the time Devlin named masked language modeling through an explicit
analogy to cloze, the older reading procedure had become infrastructure,
which meant that a pedagogical test of expectancy now functioned as a
dominant pretraining task. The continuity still needs a careful account
of asymmetry. Taylor examined a reader's comprehension through deletion
and recovery. BERT optimized parameter updates through the same formal
structure. Cloze Reader takes that infrastructural form and turns it
back into a readable event.

# Cloze Reader

Cloze Reader uses a language model to generate cloze tasks and return
them to human readers as exercises in contextual prediction. Public
source modules show that the app draws passages from Project Gutenberg
through the Hugging Face Datasets API and uses Google's Gemma-3-27B
model for word selection, hints, and contextualization (Cloze Reader
2026a). The same source code records separate services for word
selection, hint generation, and conversation management (Cloze Reader
2026b). The app therefore exposes its own architecture with unusual
clarity.

<img src="../../docs/cloze-reader-draft/cloze-reader-screenshot-current.png" style="width:5.15in;height:5.63144in" />

*Figure 1. Cloze Reader in use. The interface presents a passage from
Our Legal Heritage, 4th Ed. by S. A. Reilly at Level 1 with one blank.
The blank falls inside a discussion of royal preaching restrictions and
Puritan dissent, and the hint panel remains available.*

*Figure description. Interface view of a historical prose passage with
one blank and a hint control. The blank anchors a local lexical decision
inside a passage with legal and religious context.*

The game's central operation begins with word selection. The public
aiService.js module shows the live app calling google/gemma-3-27b-it and
supplying a prompt that asks for exact lowercase words from the middle
or end of a passage, limited by length and difficulty, and restricted to
nouns, verbs, or adjectives (Cloze Reader 2026b). A validation layer
then checks that the chosen words appear in the passage and meet the
relevant constraints, and a fallback routine excludes common function
words if the model returns unusable results (Cloze Reader 2026c). These
instructions convert pedagogical aims into a small rule set that a model
must interpret through the statistical regularities of its training
corpus. The rules stay plain enough to read, which makes the procedure's
opacity easier to locate even as its probabilistic choices remain
opaque.

This visibility matters because the selection prompt exposes the point
at which educational intent enters model procedure. A fixed-ratio cloze
test hides its assumptions inside arithmetic. Cloze Reader writes them
out in natural language, which lets the player infer, and the critic
inspect, the heuristics that shape each blank. Bommasani et al. (2021)
describe foundation model abilities as outcomes of training. Cloze
Reader does not dissolve that opacity, but it moves the interface closer
to the point where opacity begins.

I imposed another constraint from the start. The model must not know, at
the moment it selects a blank, what it will later be asked to say about
that blank. Shared context between selection and hint production would
pull the game toward words that the hint system handles with ease. I
kept word selection, hint generation, and passage summary as separate
requests. Each call receives only the passage text and the instructions
for one task (Cloze Reader 2026b). The result is a chain of discrete
procedures. Gemma does not maintain a conversational memory across the
puzzle. It answers one bounded question at a time.

This design choice also shapes the player's experience. No two runs of
Cloze Reader are identical because each session draws from a streamed
Gutenberg dataset and the live app requests selections at temperature
0.5 as it preloads books from random offsets in its dataset proxy (Cloze
Reader 2026a). The same passage may therefore produce a different blank
on a later visit. This variability is not a defect in the system. It is
a property of the procedure, which refuses the stable form of a workbook
exercise because the model selects through learned regularities under
changing conditions.

Project Gutenberg gives this variability a distinct historical charge. I
chose that archive because its books already occupy a clear place in the
history of language model training. Cloze Reader draws its passages from
Project Gutenberg's public-domain holdings (Project Gutenberg 2026). The
same holdings recur in major pretraining corpora. The Pile includes
Gutenberg texts among its source collections (Gao et al. 2020). Work on
memorization has also shown that models trained on large corpora can
reproduce verbatim passages from such sources under targeted prompting
conditions (Carlini et al. 2021). Cloze Reader begins after that
absorption has already taken place.

This prior absorption sets the terms of the game. When a Gutenberg book
enters a training corpus, the book passes through an extractive pipeline
that breaks sequence into token statistics and folds those statistics
into model weights. Gitelman and Jackson (2013) describe the broader
cultural logic through which situated documents arrive as data stripped
of much of their original frame. I use Cloze Reader to press against
that flattening. The game does not recover an untouched archive. It puts
a passage back before a reader after pretraining has already acted on
it, which asks the reader to meet it again as prose.

Figure 1 makes that claim tangible. A discussion of royal preaching
restrictions and Puritan dissent does not remain an anonymous excerpt
inside a corpus. The blank arrests the reader inside a specific
historical scene with legal, theological, and rhetorical force. To
advance, the player must attend to sentence structure, local diction,
and topic. The game slows the encounter. One word must carry the
pressure of the scene. In that pause, material that large corpora
compress comes back into view.

The game's difficulty system supports that return to the passage. Blank
count rises from one at early levels to two and then three at later
levels, and structural hints shift from word length plus first and last
letter to a first-letter cue alone (Cloze Reader 2026c). The selection
prompt also moves from easy to medium to challenging vocabulary as
levels rise (Cloze Reader 2026b). Difficulty therefore runs on two axes,
which means that each level calibrates a distinct reading task. Flanagan
and Nissenbaum (2014) argue that values enter games through rules and
constraints, and the level structure here makes that point concrete. I
use progression to privilege lexical patience, contextual attention, and
slow reading, demonstrating that the game treats reading as a situated
encounter with prose that unfolds under pressure.

The hint system extends the same logic. Players can ask about part of
speech, sentence role, word category, or synonymy through preset prompts
in the embedded panel (Cloze Reader 2026d). The code explicitly bars the
system from revealing the answer word (Cloze Reader 2026b), which keeps
assistance inside a bounded pedagogical frame. In that sense, the game
borrows the logic of scaffolding from Wood, Bruner, and Ross (1976) and
from Vygotsky's (1978) account of guided learning. Flanagan (2009) helps
sharpen the design stakes here because a critical game makes its
argument through rules, rewards, and constraints as much as through
theme. I built the hint panel to point toward a lexical solution and to
preserve the player's obligation to decide. Pea (2004) helps mark the
limit of this structure, since the hints remain static and do not adapt
to a specific learner's history. Even so, the panel offers an
interpretable account of the passage's constraints at the moment of
need.

At this point I can return to Taylor with more precision. Reading
research has shown that fluent readers generate anticipatory
expectations about upcoming words during comprehension (Rayner et al.
2012). Cloze completion rates later became a standard measure of word
predictability, and computational models of reading use those rates to
estimate how expectation alters eye movement and reading time (Snell et
al. 2018). Rego, Snell, and Meeter (2024) extend that line of work
through a cognitive model that uses language-model predictability. Large
participant completion datasets have also brought this logic into more
natural reading conditions, even as Hofmann et al. (2021) note a gap
between offline cloze completion and the rapid expectations of ordinary
reading, a difference I built Cloze Reader to make felt at the level of
play.

I do not treat that gap as evidence that human inference and model
inference share one scale. The model selects and describes through
learned distributions. The player reads a historically situated passage
in which lexical choice carries semantic, rhetorical, and archival
force. I built the game to bring those distinct acts into contact
without collapsing one into the other, which lets the shared cloze form
expose both continuity and limit.

# Continuity, Asymmetry, and Slow Reading

The blank is the point where the two genealogies of this essay meet. One
comes from the classroom instrument Taylor used to measure
comprehension. The other comes from the masking procedure that language
models use during pretraining. I built Cloze Reader so those histories
would touch inside a single round of play, which means that each puzzle
begins with model selection and only becomes legible once a reader
confronts the sentence and commits to a word.

This design gives the game critical force. In digital humanities,
scholars such as Ratto (2011) and Ramsay and Rockwell (2012) treat
making as a site of argument, and Flanagan (2009) gives a more precise
account of game forms that rework familiar conventions so they can carry
conceptual, aesthetic, and political critique. I use Cloze Reader in
that combined sense. Occlusion serves as the rule that organizes play.
The blank restages the pedagogical deletion and the training mask inside
the same playable form, and score, hints, and progression keep the
missing word in motion as a game task. Flanagan and Nissenbaum (2014)
also show how rules and constraints encode values, which clarifies why
each cloze task matters as a level. Every level distributes attention,
risk, and assistance in a specific way, turning contextual inference
into a critical encounter with the text's layered histories.

This gamified occlusion matters because it resurfaces history inside
procedure. A player does not see an abstract token position but a
missing word in a sentence drawn from a particular archive, from a book
with an edition history, a genre, and a rhetorical scene. I want the
interface to make that layered condition palpable, which means that the
same missing word carries the residue of classroom assessment, corpus
extraction, and literary address.

From there a broader implication follows for digital humanities. Model
culture often encounters books as datasets before it encounters them as
works, which causes sequence, provenance, and local pressure to recede
once a text enters that pipeline. I use the model here for another task.
It helps return the reader to a textual surface that pretraining has
already thinned out. In Dobson's terms, machine learning in the
humanities requires interpretable outputs, and in Lavin's terms it
requires situated data that stays tethered to context (Dobson 2021;
Lavin 2021). Cloze Reader tries to make that tether visible again. I use
the model to stage slow reading inside model culture.

The claim also bears on current talk about reading, where literacy
crisis discourse often treats screens, platforms, or AI as proof that
reading has entered terminal decline. Graff shows how crisis narratives
about literacy and the humanities turn historical change into mythic
decline (Graff 2022; Graff 2023). Work on digital social reading points
elsewhere, since networked platforms generate new records of reception,
exchange, and literary community (Rebora et al. 2021). I want another
account, one that uses language models and refuses inevitability
discourse. The goal is to recenter texts that model pipelines flatten
into weights and instrumentalize for ad hoc use, and to refuse the
premise that reading now survives only as a relic or symptom.

Several research questions follow from the broader critical move at
issue here. What kinds of critical artifacts can stage the passage from
archive to dataset to interface without losing the provenance, labor,
and historical texture lodged in the text? How might digital humanities
build playful systems that surface edition history, volunteer labor,
public-domain status, and corpus selection at the moment of reading,
which Lee's 'Collections as ML Data' checklist identifies as a core
problem for collections that enter machine learning workflows (Lee
2025)? What forms of interpretation emerge when a model helps organize
attention around a passage and frames the passage as prose, history, and
archive within the interface? Dobson (2021) asks for interpretable
outputs, Lavin (2021) asks for situated data, and Flanagan (2009) shows
how critical play can turn a rule-bound system into conceptual critique.
Taken together, those lines of work pose a wider question. How else
might scholars build critical artifacts that use model procedures to
reopen historical texture, expose infrastructural history, and recenter
the works that large-scale training compresses into weights?

I end with the scene that Project Gutenberg keeps on record because it
marks an earlier moment when computation attached itself to literary
circulation through a different promise. On July 4, 1971, Michael Hart
typed the Declaration of Independence into a University of Illinois
mainframe, and Project Gutenberg's record recalls the file in uppercase
because those early systems had no lowercase. Hart later cast the act as
a wager that the highest value of computation would lie in the storage,
retrieval, and search of library texts (Hart 1992; Project Gutenberg
2025). Newby (2019) places that act at the start of a volunteer-driven
archive built around public-domain circulation. Cloze Reader meets that
wager at a later technical moment, when the same archive also circulates
inside training corpora and model weights. I use the model to send the
reader back to the sentence, the page, and the book, which lets an older
dream of electronic access answer a newer regime of textual extraction.
The return does not restore an untouched past, but it demonstrates that
computation can still serve the text as text.

# References

Bachman, L. F. (1985) 'Performance on cloze tests with fixed-ratio and
rational deletions,' TESOL Quarterly, 19(3), pp. 535–556.

Bommasani, R. et al. (2021) 'On the opportunities and risks of
foundation models,' arXiv:2108.07258. Available at:
https://arxiv.org/abs/2108.07258

Carlini, N. et al. (2021) 'Extracting training data from large language
models,' in Proceedings of the 30th USENIX Security Symposium. USENIX
Association, pp. 2633–2650.

Cloze Reader (2026a) 'bookDataService.js'. Available at:
https://reader.inference-arcade.com/src/bookDataService.js (Accessed: 18
March 2026).

Cloze Reader (2026b) 'aiService.js'. Available at:
https://reader.inference-arcade.com/src/aiService.js (Accessed: 18 March
2026).

Cloze Reader (2026c) 'clozeGameEngine.js'. Available at:
https://reader.inference-arcade.com/src/clozeGameEngine.js (Accessed: 18
March 2026).

Cloze Reader (2026d) 'conversationManager.js'. Available at:
https://reader.inference-arcade.com/src/conversationManager.js
(Accessed: 18 March 2026).

Devlin, J. et al. (2019) 'BERT: Pre-training of deep bidirectional
transformers for language understanding,' in Proceedings of NAACL-HLT
2019. Minneapolis, MN: Association for Computational Linguistics, pp.
4171–4186.

Dobson, J. (2021) 'Interpretable Outputs: Criteria for Machine Learning
in the Humanities,' Digital Humanities Quarterly, 15(2). Available at:
https://doi.org/10.63744/gqdn7tfwn6r8

Firth, J. R. (1957) 'A synopsis of linguistic theory, 1930–1955,' in
Studies in Linguistic Analysis. Oxford: Philological Society, pp. 1–32.

Flanagan, M. (2009) Critical Play: Radical Game Design. Cambridge, MA:
MIT Press.

Flanagan, M. and Nissenbaum, H. (2014) Values at Play in Digital Games.
Cambridge, MA: MIT Press.

Gao, L. et al. (2020) 'The Pile: An 800GB dataset of diverse text for
language modeling,' arXiv:2101.00027. Available at:
https://arxiv.org/abs/2101.00027

Gitelman, L. and Jackson, V. (2013) 'Introduction,' in Gitelman, L. and
Jackson, V. (eds) 'Raw Data' Is an Oxymoron. Cambridge, MA: MIT Press,
pp. 1–14.

Graff, H. J. (2022) 'The New Literacy Studies and the Resurgent Literacy
Myth,' Literacy in Composition Studies, 9(1), pp. 47–53. Available at:
https://doi.org/10.21623/1.9.1.4

Graff, H. J. (2023) 'Opinion: The Persistent “Reading Myth” and the
“Crisis of the Humanities”, College Composition & Communication, 74(3),
pp. 575–580. Available at: https://doi.org/10.58680/ccc202332367

Harris, Z. S. (1954) 'Distributional structure,' Word, 10(2–3), pp.
146–162.

Hart, M. (1992) 'The History and Philosophy of Project Gutenberg.'
Available at:
https://www.gutenberg.org/about/background/history_and_philosophy.html
(Accessed: 13 April 2026).

Hofmann, M. J. et al. (2021) 'The influence of information in the
sentence context on predictions in reading,' Neuropsychologia, 158,
107885.

Jongsma, E. (1980) Cloze instruction research: A second look. Newark,
DE: International Reading Association.

Koffka, K. (1935) Principles of Gestalt Psychology. New York: Harcourt,
Brace and World.

Lavin, M. (2021) 'Why Digital Humanists Should Emphasize Situated Data
over Capta,' Digital Humanities Quarterly, 15(2).

Lee, B. C. G. (2025) 'The “Collections as ML Data” checklist for machine
learning and cultural heritage,' Journal of the Association for
Information Science and Technology, 76(2), pp. 375–396. Available at:
https://doi.org/10.1002/asi.24765

Liu, X. et al. (2021) 'Self-supervised learning: Generative or
contrastive,' IEEE Transactions on Knowledge and Data Engineering,
35(1).

Mikolov, T. et al. (2013) 'Efficient estimation of word representations
in vector space,' arXiv:1301.3781.

Newby, G. B. (2019) Forty-Five Years of Digitizing Ebooks: Project
Gutenberg's Practices. Available at:
https://www.gutenberg.org/ebooks/60600 (Accessed: 13 April 2026).

Oller, J. W. (1979) Language Tests at School. London: Longman.

Pea, R. D. (2004) 'The social and technological dimensions of
scaffolding and related theoretical concepts for learning, education,
and human activity,' Journal of the Learning Sciences, 13(3), pp.
423–451.

Peters, M. E. et al. (2018) 'Deep contextualized word representations,'
in Proceedings of NAACL-HLT 2018. New Orleans, LA: Association for
Computational Linguistics, pp. 2227–2237.

Project Gutenberg (2025) The Declaration of Independence of the United
States of America. Available at:
https://www.gutenberg.org/0/1/1-h/1-h.htm (Accessed: 13 April 2026).

Project Gutenberg (2026) Project Gutenberg. Available at:
https://www.gutenberg.org/ (Accessed: 18 March 2026).

Ramsay, S. and Rockwell, G. (2012) 'Developing Things: Notes toward an
Epistemology of Building in the Digital Humanities,' in Gold, M. K.
(ed.) Debates in the Digital Humanities. Minneapolis: University of
Minnesota Press, pp. 75–84.

Ratto, M. (2011) 'Critical Making: Conceptual and Material Studies in
Technology and Social Life,' The Information Society, 27(4), pp.
252–260. Available at: https://doi.org/10.1080/01972243.2011.583819

Rayner, K. et al. (2012) Psychology of Reading. 2nd edn. New York:
Psychology Press.

Rebora, S. et al. (2021) 'Digital humanities and digital social
reading,' Digital Scholarship in the Humanities, 36(Supplement_2), pp.
ii230–ii250. Available at: https://doi.org/10.1093/llc/fqab020

Rego, A. T. L., Snell, J. and Meeter, M. (2024) 'Language models
outperform cloze predictability in a cognitive model of reading,' PLOS
Computational Biology, 20(9), e1012117. Available at:
https://doi.org/10.1371/journal.pcbi.1012117

Snell, J. et al. (2018) 'OB1-reader: A model of word recognition and eye
movements in text reading,' Psychological Review, 125(6), pp. 969–1013.

Taylor, W. L. (1953) '"Cloze procedure": A new tool for measuring
readability,' Journalism Quarterly, 30(4), pp. 415–433.

Vygotsky, L. S. (1978) Mind in Society: The Development of Higher
Psychological Processes. Cambridge, MA: Harvard University Press.

Wood, D., Bruner, J. S. and Ross, G. (1976) 'The role of tutoring in
problem solving,' Journal of Child Psychology and Psychiatry, 17(2), pp.
89–100.
