# Cloze Reader Rewrite — Excerpts and Suggested Edits

## EX-01 — Prompt heuristic term

**SOURCE EXCERPT**
"...choose single, verifiable words with strong contextual salience..."

**SUGGESTED EDIT**
Keep this wording in the code-prompt excerpt and avoid legacy terminology.

**RATIONALE**
This keeps the heuristic interpretable while avoiding unstable terms that require formal definition the paper does not provide.

---

## EX-02 — Heuristic interpretation paragraph

**SOURCE EXCERPT**
"These heuristic instructions ask the model to target words with high contextual weight, yet the model still interprets those instructions through statistical regularities in its training data rather than through formal definitions."

**SUGGESTED EDIT**
Retain this sentence as the lead claim for the architecture-as-argument block.

**RATIONALE**
It states mechanism and limit directly, which supports the paper's asymmetry argument without overclaim.

---

## EX-03 — Intro empirical bridge

**SOURCE EXCERPT**
"Empirical work comparing human and model cloze responses shows that structural similarity does not guarantee functional equivalence... Detailed performance figures are deferred to the evidence section."

**SUGGESTED EDIT**
Keep this compressed framing in the intro and reserve dense CLOTH metrics for the evidence section.

**RATIONALE**
This improves intro pacing and keeps empirical detail where it can be methodologically framed.

---

## EX-04 — Thesis inheritance risk

**SOURCE EXCERPT**
"...waiting to be read by a human who interprets context through something else entirely."

**SUGGESTED EDIT**
Replace this closing flourish in later pass with explicit claim language that body sections can inherit.

**RATIONALE**
The current line is evocative but underspecified for structural carry-through.

---

## EX-05 — Functional asymmetry paragraph (for insertion after "visible side by side through play")

**PROPOSED INSERTION — for milwrite approval**

**Placement:** After "Cloze Reader makes those two operations visible side by side through play." in the *Continuity and Asymmetry* section, before the empirical citation paragraph.

**Text:**

> When a player supplies the right word, they have recovered an author's specific lexical choice by attending to tone, syntax, the pressure of the sentence. When BERT's training objective lands on the same word, the model has updated weights so that the token's context raises its probability in the output distribution. These are not two performances of the same task. One produces a reading; the other produces a parameter update.

**RATIONALE:**
The *Continuity and Asymmetry* section currently names the Taylor/BERT asymmetry without giving it a concrete location. This paragraph supplies one: the moment of correct completion, where the same answer emerges from operations that differ in kind. It bridges the structural claim ("selection and interpretation stay separate") to the empirical section that follows. Style compliance: no em-dashes outside enclosing use, no contrastive pivots, no trailing significance clauses, no invented noun phrases. "Without reading it as such" is a finite clause, not a dangling absolute.

**Status:** AWAITING MILWRITE APPROVAL

---

## EX-06 — "decentered" passage (restore or revise)

**SOURCE EXCERPT (pre-v43)**
"...the kind of close reading practices that have been decentered by the advent of LLMs, reacquainting them with otherwise flattened or forgotten texts that have been totalized through extraction and foreclosure at scale."

**CURRENT STATE (v43+)**
"...the kind of slow reading that large language model pretraining renders unnecessary, reacquainting players with texts that have been totalized through extraction and foreclosure at scale."

**NOTE:**
"decentered by the advent of LLMs" was cut as melodramatic. "renders unnecessary" is more precise about the mechanism (pretraining, not LLMs generally). "totalized through extraction and foreclosure at scale" retained as established critical theory vocabulary. If milwrite prefers to restore "decentered," can do so — the cut was a judgment call, not a hard rule violation.

**Status:** AWAITING MILWRITE REVIEW — restore or keep current?
