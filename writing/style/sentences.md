# Sentences — Sentence-Level Rules

*Load this for: building, auditing, or rewriting individual sentences*

---

## Basic Shape

- Mix short and long sentences. After a long clause-heavy sentence, drop a short one. It lands harder and reads like thought.
- Vary openers. Don't start three sentences in a row with "The." Use time markers, verbs, prepositional phrases, names.
- Use fragments for emphasis. Sparingly.
- **No consecutive simple independent clauses.** Three or more short sentences in a row with simple subject-verb structure reads as a list, not prose. After two short sentences, the third must subordinate, embed, or extend — not simply add another clause. Restructure by finding the logical relationship (cause, consequence, contrast, qualification) and encoding it syntactically.
- **Sentence ceiling: 5 lines (~60–75 words).** Earn length through subordination and embedding, not coordination. When a sentence runs long on "and," split it or find a subordinator.
- **Meaningful verbs, concrete subjects.** The subject should be a person, thing, or action. The verb carries the sentence's commitment; weak verbs defer it. Weak copula + adjective ("was important") almost always has a stronger replacement. Find the verb that does the work directly.
- **No weak expletive openers.** Ban "There is/are/was/were" as sentence openers. Name the thing instead.  
  **Bad:** "There is no long-range interaction in the Ising model."  
  **Good:** "The Ising model has no long-range interaction."

## Subject Rules

**Simple subjects.** Lead with people, things, or actions. No noun-phrase pileups.

**No abstract subjects in short sentences.**  
Stub sentences where an abstraction stands alone as subject ("Meaning played no part...") read as fragment-summary insertions.  
**Fix:** Fold the claim back into the person, method, or action it belongs to.  
**Test:** If a short sentence has an abstraction (meaning, distribution, context, prediction, structure) as its subject and the verb is "is/was/played/remained," it probably needs to be folded into the surrounding prose with a human or method as the grammatical agent.

**No interrupted subjects.**  
Ban sentences where the subject is followed by a comma-bracketed phrase before the verb.  
Pattern to kill: "Subject, [qualifier], verb."

**Bad:** "The second debate, equally consequential for what the procedure measures, concerned deletion method."  
**Bad:** "Taylor, working within the Gestalt tradition, developed the cloze procedure."  

**Fix:** Move the qualifier after the verb, make it a separate sentence, or rewrite as subordinate clause.  
**After:** "The second debate concerned deletion method and carried equal weight for what the procedure measures."  
**After:** "Taylor developed the cloze procedure within the Gestalt tradition."

**Exception:** Very short non-restrictive appositives ("Oller, a linguist, argued...") are acceptable if the phrase is two or three words. When in doubt, restructure.

## Banned Constructions

**No contrastive pivots.**  
Kill: "not X but Y," "not just X," "more than X," "beyond that," "not merely X but Y," "not only X but also Y," "less about X more about Y."  
State the point directly.

**No setup phrases.**  
Kill: "What makes this interesting is...," "Here's the thing:," "The key insight is...," "What this shows is..."  
Make the point. Skip the announcement.

**No pseudo-cleft subjects.**  
Kill: "What connects X to Y is...," "What made X distinct was...," "What separates X from Y is..."  
These defer the real subject behind a nominalized construction. Identify the actual agent or action and lead with it.  
**Bad:** "What connects the Ising model to the other artifacts on this site is the argument embedded in its construction."  
**Good:** "Every artifact on this site encodes the same premise, with local rules applied uniformly generating structure no individual element was instructed to produce."

**No bridging constructions.**  
Kill: "is what," "is this:," "What X is Y"  
**Test:** If you can delete "is what" or "is this:" and the sentence parses, delete it.

| Before | After |
|---|---|
| The noise is what makes it feel drawn | The noise makes it feel drawn |
| Flocking is what happens when every bird runs... | Flocking happens when every bird runs... |

**No list subjects.**  
A sentence whose subject is "X, Y, Z, and W" almost always has a better singular subject available. Find it.  
Two consecutive list-subject sentences is a hard stop — restructure one or both.

**No "what X does" openers.**  
Kill the "What X [verb] as Y applies/shows/reveals..." construction.

**Bad:** "What Gitelman and Jackson describe as the mythology of raw data applies to..."  
**Good:** "Gitelman and Jackson describe the mythology of raw data as it applies to..."

**No in this light.**  
"X, in this light, Y" stalls the sentence and signals hedging. If the logical connection is real, the verb makes it. Restructure.

## Colon and Semicolon Audit

Colons and semicolons in body prose are usually hiding an explicit logical connector. Surface it.

| Relationship | Fix |
|---|---|
| Elaboration / participial | Rewrite as participial phrase: "requiring that," "consisting of" |
| Result | Use "so that" before the result clause |
| Parallel elaboration | Use "with-phrase" or "where...while" contrast |
| Causal / justification | Use "since" or "because" as subordinator |

**No colon pivots.** A colon that precedes a single clause rather than a list or named definition is a structural hinge — it's doing work the syntax should do itself. Restructure.  
**Bad:** "The difficulty was making those numbers visible: how do you draw a four-dimensional object on two-dimensional paper."  
**Good:** "The difficulty was pictorial — specifically, how to make those counts visible without reducing them to a table." (wait, no em dash) → "The difficulty was pictorial, a question of how to make those counts visible without reducing them to a table."

**The one legitimate colon:** Colon + restatement. General claim [colon] named specifics. "Educational cloze tests assess the capacity that constitutes reading comprehension: the synthesis of linguistic knowledge, world knowledge, and inferential skill."

**Semicolons:** Same audit. Exception: short two-part sentences for rhetorical punch ("The player is not simulating the inference engine; they are one") — only if rhythm depends on the pause and no connector exists.

**Examples from cloze-reader draft:**
- "simple and automatable: delete words..." → "simple and automatable, requiring only that..."
- "legible in the difficulty of restoration: when a player struggles..." → "legible in the difficulty of restoration, so that when a player struggles..."
- "scales independently of blank count: early levels..." → "scales independently of blank count, with early levels..."
- "But the purposes differ: Taylor..." → "The purposes diverge, since Taylor..."

## Logical Connectors Over Conjunctive Ones

When a preposition relates two elements, prefer a logical connector (showing cause, consequence, contrast, or purpose) over a conjunctive one (showing mere addition or temporal sequence).

**Test:** Can "and," "while," or "as well as" be expressed as a logical relationship — "to," "so that," "because," "which reveals," "since"? If yes, make that the connector.

**Before:** "I trace these genealogies and interrogate the divergences..."  
**After:** "I trace these genealogies to show where the divergences lie..."

**Before:** "I kept each task separate, with no information carried forward."  
**After:** "I kept each task separate so that no information carries forward."

**Not a rule against "and":** Short parallel constructions ("build, test, push") are fine. The rule targets compound predicates where the second element is the logical consequence or purpose of the first.

## Nominalization Ban

No verb phrase nominalizations. "Pretraining's reduction of text to token distributions" → "pretraining reduces text to token distributions."

Pattern: `[gerund/noun]'s [noun] of [noun]` before the verb arrives = always rewrite as two short sentences. Split the nominalization into its verb, then carry the consequence forward as a second sentence.

## Trailing Participle Ban

Don't tack a present participle phrase onto the end of a sentence to inject shallow significance.

**Banned forms:** "highlighting its importance," "reflecting broader trends," "contributing to the development of...," "underscoring its role as...," "showcasing how...," "demonstrating the enduring legacy of..."

**Fix:** Delete the participial phrase entirely, or state the actual claim as its own sentence with a subject and verb.  
**Test:** If the "-ing" clause can be removed without losing information, remove it.

## Anaphora — Controlled Use Only

Don't repeat the same sentence opener multiple times in succession.

**Bad:** "They assume that... They assume that... They assume that..."  
**Exception:** Deliberate rhetorical anaphora is allowed once per piece, sparingly, when it's clearly the point of the passage.

## Passive Voice — Strategic Use

Use the passive when you want to soften institutional agents ("Users were compelled to hand over data") or foreground the object.  
Use the active when the actor matters ("Reddit handed over data").  
Choose based on what you want the reader to see, not by default.

## Data in Prose

Don't bolt data onto the end of a sentence. Embed it inside a subordinate clause at the point where consequence becomes legible.

**Pattern:** general claim → named mechanism → named instance → quantitative grounding, all continuous.  
**Bad:** "campus subreddits, such as r/CUNY, which receives X posts per day"  
**Good:** "r/CUNY, where posts average [X] per day, sorts students' trajectories by ranking criteria..."

Use brackets [X] for unconfirmed data. Never write "many" or "significant numbers."
