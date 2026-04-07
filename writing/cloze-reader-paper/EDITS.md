# EDITS.md — Cloze Reader Paper
## Kanban: Proposed • Staged • Approved

**Format:** Each edit is a numbered card with location, issue, proposed change, and status.  
**Status flow:** `Proposed` → `Staged` (drafted, ready for milwrite review) → `Approved` (accepted and applied to canonical draft).  
**Working draft:** `drafts/draft_v43.md` (current canonical)  
**Contributors:** Petrarch + Quimbot  
**Rule:** All suggested edits go here first. Nothing touches the draft without moving through this board.

---

## ✅ Approved (applied in v43 — 2026-03-30)

### ED-001 — Intro: reductionistic opener
- **Location:** Introduction, sentence 1
- **Issue:** "simple procedural idea" — reductionistic; undercuts the procedure before establishing what it does
- **Change:** "simple procedural idea" → "narrowly defined operation"
- **Status:** Approved · applied v43

### ED-002 — Intro: "rather than" contrastive
- **Location:** Introduction, Taylor sentence
- **Issue:** "rather than through isolated subskills" — contrastive construction concealing positive description
- **Change:** → "in place of the syllable-counting and sentence-length measures that targeted isolated textual features"
- **Status:** Approved · applied v43

### ED-003 — Intro: consecutive thin independents
- **Location:** Educational Genealogy section, opening two sentences
- **Issue:** "formally simple. Delete words… The theoretical ambition behind it was larger." — three thin sentences in sequence
- **Change:** Merged: "formally minimal: its theoretical ambition reached beyond measurement"
- **Status:** Approved · applied v43

### ED-004 — Devlin sentence: "rather than" + em-dash patch
- **Location:** Introduction, Devlin paragraph
- **Issue:** "within a single joint pass rather than merging separately trained directional runs at the output. Devlin called this… — same task, larger scale, different architecture."
- **Change:** "eliminating the separate directional runs ELMo merged at the output layer" — positive clause; em dash retained (legitimate aside)
- **Status:** Approved · applied v43

### ED-005 — Educational Genealogy: "rather than isolating"
- **Location:** Oller paragraph
- **Issue:** "They measure the whole rather than isolating any single subskill" — contrastive; claim belongs in positive frame
- **Change:** → "they index holistic linguistic ability, not any isolated subskill" (via colon construction)
- **Status:** Approved · applied v43

### ED-006 — ML Genealogy: "not accidental" opener
- **Location:** ML Genealogy section, sentence 1
- **Issue:** "The structural resemblance… is not accidental" — negative opener; buries the real claim
- **Change:** → "runs deeper than analogy"
- **Status:** Approved · applied v43

### ED-007 — ML Genealogy: Harris/Firth thin consecutives
- **Location:** Harris/Firth sequence
- **Issue:** Two adjacent thin sentences, same subject pattern
- **Change:** Merged with semicolon
- **Status:** Approved · applied v43

### ED-008 — Cloze Reader: nominalized opener
- **Location:** Cloze Reader section, first paragraph
- **Issue:** "A recursive structure embedded in the architecture itself sets the game apart" — nominalized subject, delayed verb
- **Change:** → "One architectural feature separates the game from ordinary educational applications"
- **Status:** Approved · applied v43

### ED-009 — Cloze Reader: "rather than hidden behind"
- **Location:** Feedback loop paragraph
- **Issue:** Contrastive "rather than hidden behind a fixed deletion schedule or a hand-authored word list"
- **Change:** Recast positive: "the selection rules are written in plain language, inspectable in the public source module, where a fixed deletion schedule or hand-authored word list would have buried the logic"
- **Status:** Approved · applied v43

### ED-010 — Cloze Reader: bare "This" × 2
- **Location:** Difficulty architecture paragraph; Discreteness paragraph
- **Issue:** "This difficulty architecture points toward…" / "This discreteness extends further." — bare "This" without clarifying noun
- **Change:** → "The difficulty architecture…" / "The discreteness extends further."
- **Status:** Approved · applied v43

### ED-011 — Cloze Reader: "This is a structural property… not a failure"
- **Location:** Stochasticity paragraph
- **Issue:** Bare "This is" + negative construction "not a failure to be corrected"
- **Change:** → "The variability is a structural property of the system, not a failure to be corrected."
- **Status:** Approved · applied v43

### ED-012 — Continuity: consecutive thin independents (seven sentences)
- **Location:** Continuity and Asymmetry section, first two paragraphs
- **Issue:** Seven short independent clauses in sequence ("Taylor operationalized… BERT's developers operationalized… The two applications differ… I divided… Masked language modeling treats them as one. The model identifies… The reader decides…")
- **Change:** Merged into three compound sentences with semicolons and subordination
- **Status:** Approved · applied v43

### ED-013 — Continuity: "What Taylor was measuring" pseudo-cleft
- **Location:** Returning to origins paragraph
- **Issue:** "What Taylor was measuring was also a description of ordinary cognition" — pseudo-cleft; real subject deferred
- **Change:** → "His measurement also described ordinary cognition"
- **Status:** Approved · applied v43

### ED-014 — Continuity: "That asymmetry is not merely theoretical"
- **Location:** Continuity section
- **Issue:** Negative opener, "not merely" hedge
- **Change:** → "The asymmetry has empirical support"
- **Status:** Approved · applied v43

### ED-015 — Continuity: "To be clear" opener + thin consecutives
- **Location:** Penultimate paragraph
- **Issue:** "To be clear, the convergence… is real" — throat-clear opener; followed by "The purposes differ. Taylor wanted… BERT's developers wanted…" three thin sentences
- **Change:** Opener removed; paragraph opens on the claim; thin sentences merged with semicolon
- **Status:** Approved · applied v43

---

## 🔶 Staged (drafted, pending milwrite review)

*None currently.*

---

## 💡 Proposed (flagged, not yet drafted)

### ED-016 — Intro: occlusion paragraph "rather than what it lacks"
- **Location:** Occlusion/closure distinction paragraph, final clause
- **Issue:** "treat the surrounding passage as evidence of what the sentence conceals rather than what it lacks" — the "rather than" here is doing real contrastive work (concealment vs. absence is the distinction the paragraph turns on) but verify whether it holds by the style guide exception test: is the tension real and not manufactured?
- **Action needed:** milwrite to confirm this "rather than" is load-bearing; if so, flag as permitted exception
- **Status:** Proposed

### ED-017 — Intro: "where cloze-like objectives now structure how machines learn language"
- **Location:** Transition sentence after occlusion paragraph
- **Issue:** Nominalized subject in a thin stand-alone sentence used as a transition — "The intervention proved durable enough to move from educational psychology to computational laboratories, where cloze-like objectives now structure how machines learn language." The sentence does real work but the nominalization ("The intervention") could be grounded
- **Action needed:** Evaluate whether "The intervention" has a clear antecedent or whether the sentence should open on Taylor
- **Status:** Proposed

### ED-018 — Cloze Reader section: "I could have collapsed these tasks"
- **Location:** Design constraint paragraph
- **Issue:** "I could have collapsed these tasks into a single extended prompt — Gemma-3's architecture technically supports it" — the em dash here is a parenthetical aside (permitted form) but "technically supports it" is slightly hedging; consider whether "supports it" alone is stronger
- **Action needed:** Minor word-level check
- **Status:** Proposed

### ED-019 — Continuity: "Both histories share a structural premise, that contextual prediction…"
- **Location:** Continuity section, opening sentence
- **Issue:** Comma-that construction attaches the claim loosely; could be a colon (genuine definition follows)
- **Change candidate:** "Both histories share a structural premise: contextual prediction is a meaningful index of linguistic competence." (already applied in v43 — verify this landed correctly)
- **Action needed:** Confirm v43 version
- **Status:** Proposed · verify

---

## 📚 ED-020 through ED-024 — Educational Genealogy additions (2026-03-31)
*Source: sportello research report, <https://bot.inference-arcade.com/src/search/cloze-test-reading-comprehension-assessment-2026-03.html>*

### ED-020 — Educational Genealogy: entropy and deletion rate
- **Location:** Educational Genealogy section, Bachman / rational deletion paragraph (line 35)
- **Issue:** Current text notes that fixed-ratio deletion "flattens the difficulty gradient" but gives no mechanism. The research documents that entropy is the mechanism: gaps following high-predictability contexts (low entropy) are easier; gaps in semantically ambiguous contexts (high entropy) are harder. Maltaev et al. (2019) formalized this computationally. The paper currently names the asymmetry but not its information-theoretic ground.
- **Addition candidate:** One sentence after the Bachman rational-deletion claim:
  > The information-theoretic basis for this variation in gap difficulty was not formalized until Maltaev and colleagues (2019), who demonstrated that Shannon entropy — a measure of how many plausible completions a given context admits — predicts which positions are easy and which resist completion: gaps following highly constrained contexts yield few alternatives; gaps in ambiguous contexts yield many.
- **Revision note:** "that gradient" replaced. The issue is the bare demonstrative "that" as backward pointer ("that gradient," "that claim," "that distinction") — same family as the bare "This" rule. Replace with a noun phrase that names what it refers to.
- **Why it matters:** Bridges the Educational Genealogy directly to the ML Genealogy (Harris/Shannon thread) and gives the Bachman claim empirical teeth without disrupting milwrite's existing sentence rhythm.
- **Status:** Proposed

### ED-021 — Educational Genealogy: exact-word vs. synonym scoring — what the correlation reveals
- **Location:** Scoring debate paragraph (line 33), after the Jongsma sentence
- **Issue:** The draft notes the dispute but stops before the more interesting inference. Research reports Laing's finding that exact and acceptable scoring correlate at 0.92 for full test scores — which implies readers are relying on part-of-speech information and broad semantic appropriateness rather than author-specific lexical choice. The paper attributes the exact/synonym tension to design ambiguity; the correlation evidence suggests a deeper interpretive consequence.
- **Addition candidate:** One sentence after the Jongsma sentence:
  > That the two methods correlate at 0.92 across full test scores (Laing, cited in Brown 1980) suggests readers are operating on part-of-speech and semantic-category information rather than recovering the author's specific word choice — a finding that clarifies rather than resolves the ambiguity.
- **Why it matters:** Sharpens the existing paragraph's claim from "dispute surfaces an ambiguity" to "the evidence clarifies what the procedure actually samples." More argumentatively useful.
- **Status:** Proposed

### ED-022 — Educational Genealogy: second-language institutionalization and the TOEFL
- **Location:** After the Abraham and Chapelle sentence (line 31), or as a third paragraph before the scoring debate
- **Issue:** The draft moves from Oller to the scoring dispute without noting that the procedure was institutionalized into standardized testing — particularly TOEFL — as a consequence of the integration thesis. The research documents that multiple-choice cloze variants were adopted in TOEFL, that research comparing free-response and MC formats produced mixed findings, and that the adoption happened before validity questions were resolved. The current genealogy implies a clean theoretical arc; the institutional history reveals adoption outran evidence.
- **Addition candidate:** New paragraph after the Abraham and Chapelle sentence:
  > The adoption of cloze variants in the Test of English as a Foreign Language demonstrated how quickly Oller's integration thesis moved from theory to practice. Multiple-choice cloze items appeared in standardized testing before construct validity questions were settled, and subsequent research comparing free-response and multiple-choice formats produced mixed findings: moderate correlations between the two variants suggested they sampled similar but not identical constructs, with free-response formats more sensitive to syntactic pattern recognition and multiple-choice more sensitive to lexical knowledge (Brown 1980).
- **Why it matters:** Gives the genealogy institutional texture and anticipates the paper's argument that theoretical and practical uses of cloze have always diverged — relevant to the Cloze Reader design premise.
- **Status:** Proposed

### ED-023 — Educational Genealogy: Saito (2003) and the sentential-level finding
- **Location:** Currently absent. Could follow the Bachman sentence or begin a fourth paragraph
- **Issue:** The draft mentions Bachman's rational-deletion argument but does not note that structural equation modeling — Saito (2003) applying it to the ECPE — found that cloze measures "form and meaning of grammar" at sentential and suprasentential levels, not overall language proficiency. This is the most direct empirical challenge to Oller's integration thesis and it is currently missing from the genealogy.
- **Addition candidate:** New paragraph (fourth, before or replacing the transition to scoring debate):
  > The most direct challenge to Oller's integration thesis arrived from structural equation modeling. Saito (2003), analyzing data from the Examination for the Certificate of Proficiency in English, found that cloze performance indexed grammatical form and meaning at the sentence level rather than the broad pragmatic competence Oller had theorized. The procedure measured what local context made predictable, not what the text as a whole required comprehenders to know.
- **Why it matters:** Closes the theoretical loop: Taylor's procedure → Oller's integration thesis → empirical deflation → what the procedure actually samples. This is the real argument the paper inherits.
- **Status:** Proposed

### ~~ED-024 — Educational Genealogy: cloze probability as psycholinguistic index (N400 bridge)~~
- **Status:** Withdrawn — milwrite: out of scope for this paper. The eye-movement/N400/surprisal lineage is fascinating but not a thread this intro pulls.

---

---

## ✅ Approved (applied in cloze-paper-session 2026-04-05 17:02 ET)

### ED-025 — ML Genealogy: penultimate sentence nominalization
- **Location:** ML Genealogy section, penultimate sentence
- **Before:** "The masked language modeling objective made this feasible as a self-supervised task, since the supervisory signal was already present in unannotated text, and the scale of available text made large-parameter training viable (Liu et al. 2021; Bommasani et al. 2021)."
- **After:** "Masking was feasible as a self-supervised objective because unannotated text already contained the supervisory signal, and the scale of available text made large-parameter training viable (Liu et al. 2021; Bommasani et al. 2021)."
- **Rationale:** "made this feasible as a self-supervised task" buries the subject; leading with "Masking" and "because" makes the causal logic explicit.
- **Status:** Approved · applied 2026-04-05

### ED-026 — ML Genealogy: closing sentence split
- **Location:** ML Genealogy section, final sentence
- **Before:** "Devlin's results made masking the dominant pretraining objective, the training regime that Cloze Reader's word-selection step operates within and makes visible to players."
- **After:** "Devlin's results established masking as the dominant pretraining objective. Cloze Reader's word-selection step operates within that regime and makes it visible to players."
- **Rationale:** Trailing relative clause doubled two verbs on a single antecedent; splitting gives each claim its own sentence and sharpens the bridge to the next section.
- **Status:** Approved · applied 2026-04-05

### ED-027 — ML Genealogy: dangling participial opener (–2)
- **Location:** ML Genealogy, sentence –2 from close
- **Before:** "Moving from word embeddings to contextualized representations to joint bidirectional masking, each step in that elaboration sharpened the prediction task that Cloze Reader gives back to human players."
- **After:** "Each step in that elaboration sharpened the prediction task Cloze Reader gives back to human players: word embeddings first, then contextualized representations, then joint bidirectional masking."
- **Rationale:** Dangling participial opener — "Moving from X, each step" — has no valid subject; restructured with a colon.
- **Status:** Approved · applied 2026-04-05

### ED-028 — ML Genealogy: encoded → captured (–1)
- **Location:** Mikolov sentence
- **Before:** "...encoded semantic and syntactic regularities at scale."
- **After:** "...captured semantic and syntactic regularities at scale."
- **Rationale:** "captured" carries more force and avoids technical neutrality.
- **Status:** Approved · applied 2026-04-05

### ED-029 — ML Genealogy: contextual induction → contextual prediction (+1)
- **Location:** Sentence immediately following the closing pair
- **Before:** "...return them to human readers as exercises in contextual induction."
- **After:** "...return them to human readers as exercises in contextual prediction."
- **Rationale:** "Contextual prediction" is the paper's term of art; "induction" was a drift.
- **Status:** Approved · applied 2026-04-05

### ED-030 — ML Genealogy: "for the live application" redundancy (+2)
- **Location:** Source modules sentence
- **Before:** "Public source modules for the live application show that..."
- **After:** "Public source modules show that..."
- **Rationale:** "for the live application" is redundant; no other application is in scope.
- **Status:** Approved · applied 2026-04-05

### ED-031 — Critical artifact smoke test split with Petrarch (2026-04-06)
- **Location:** Cloze Reader section, second half focused on the critical artifact
- **Issue:** User requested a coordinated smoke test using the dissertation MCP workflow, with Quimbot revising the first two paragraphs of the critical-artifact stretch and Petrarch revising the short incomplete paragraphs that follow.
- **Scope split:**
  - **Quimbot:** first two paragraphs beginning `I chose Project Gutenberg as the source archive...` and `The books have, in a precise sense...`
  - **Petrarch:** the short paragraphs following, beginning `Against this flattening...`, `The difficulty system...`, `The difficulty architecture...`, and adjacent incomplete short units in that stretch
- **Status:** Staged · coordination split logged before draft edits

### ED-032 — diss-mcp smoke-test paragraph revision (2026-04-07)
- **Location:** Cloze Reader section, paragraph beginning `Against this flattening, Cloze Reader...`
- **Issue:** Paragraph stated the restoration claim too generally and did not yet pass through the new mandatory diss-mcp writing path.
- **Change:** Revised paragraph to make the critical-artifact claim more explicit: the passage returns as an object the reader must work through, while the model becomes one layer in a larger procedure rather than the whole interpretive scene.
- **diss-mcp result:**
  - `track_changes` call attempted and failed because the Quimbot draft file does not have a git HEAD in the `diss` project context the server expects
  - `audit_status(chapter="draft.md", action="get")` succeeded and returned that no audit record exists yet for `draft.md`
- **Status:** Approved · applied as smoke test, with project-context limitation documented

*Last updated: 2026-04-07 · Quimbot*
