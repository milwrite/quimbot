# PROCESS_GUIDE.md
## Writing Process Routing Guide
*For agents (Quimbot, Petrarch) working on milwrite projects. Load the file that matches the current task.*

---

## Conditional Pathways

### PATH A · Drafting from scratch or from notes
**Goal:** Get ideas into prose with correct structure from the first pass.
**Load:** `STYLE_GUIDE.md` → sections: Academic Prose, Data-in-Context, Humanizer
**Guiding questions:**
- Who is the grammatical subject of this sentence?
- What is the paragraph's claim, and does the topic sentence state it directly?
- Is the evidence concrete and named, or floating?

---

### PATH B · Revising an existing draft (argument not flowing)
**Goal:** Fix paragraph structure, transitions, claim discipline, evidence grounding.
**Load:** `CHECKLIST_REVISE.md` (full)
**Sequence:**
1. R1: Does each paragraph have a proper topic sentence?
2. R2: Do transitions carry explicit logical relationships?
3. R3: Are claims bounded and rivals addressed?
4. R5: Are mechanisms named and consequences concrete?
5. R7: Humanizer pass — short sentences, specific instances, varied openers

---

### PATH C · Revising prose (sentences are fine, style violations exist)
**Goal:** Fix banned constructions, vocabulary, punctuation before submission.
**Load:** `CHECKLIST_COPY.md` (full)
**Sequence:**
1. C1: Punctuation sweep (em dashes, colons, semicolons)
2. C2: Vocabulary sweep (AI slop, jargon, invented noun phrases)
3. C3: Construction sweep (contrastive pivots, setup phrases, bridging, trailing participles)
4. C4: Sentence structure (interrupted subjects, abstract subjects, nominalization chains)
5. C5: Rhythm (anaphora, tricolon, sentence variation)
6. C6: Citation logic (attribution, false dilemmas, sourcing)

---

### PATH D · Adding a new style rule
**Goal:** Persist a new rule so all future agents apply it.
**Steps:**
1. Add the full rule with rationale and examples to `STYLE_GUIDE.md`
2. Tag it `[COPY]`, `[REVISE]`, or `[DRAFT]`
3. Add the short form (no rationale) to the appropriate checklist section in `CHECKLIST_COPY.md` or `CHECKLIST_REVISE.md`
4. Add the rule to `SOUL.md` (Writing Rules section) if it's always-on
5. Commit all four files together

---

### PATH E · Copy editing a near-final draft
**Goal:** Final pass before submission. Catch everything.
**Sequence:**
1. Run `CHECKLIST_COPY.md` top to bottom — every item
2. Run `CHECKLIST_REVISE.md` R3 and R4 (argument and citation integrity)
3. Confirm version number in draft footer is current

---

### PATH F · Style audit on an existing passage (spot check)
**Goal:** Identify violations without full revision.
**Load:** `CHECKLIST_COPY.md` C2, C3, C4 only
**Return:** List of violations by section code (e.g., "C3: trailing participle line 47; C4: interrupted subject line 52")

---

## File Map

| File | When to load | Granularity |
|---|---|---|
| `PROCESS_GUIDE.md` | First — to route the task | Meta |
| `CHECKLIST_COPY.md` | PATH B, C, E, F | Sentence |
| `CHECKLIST_REVISE.md` | PATH B, E | Paragraph / argument |
| `STYLE_GUIDE.md` | PATH A, D; reference for any rule | Reference |

---

## Rule Tagging Key

When adding rules to `STYLE_GUIDE.md`, tag each entry:
- `[COPY]` — sentence-level, belongs in CHECKLIST_COPY.md
- `[REVISE]` — paragraph/argument level, belongs in CHECKLIST_REVISE.md
- `[DRAFT]` — drafting heuristic, referenced in PROCESS_GUIDE.md PATH A
- `[ALL]` — applies at all stages
