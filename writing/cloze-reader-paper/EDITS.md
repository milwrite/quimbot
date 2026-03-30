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

*Last updated: 2026-03-30 · Petrarch*
