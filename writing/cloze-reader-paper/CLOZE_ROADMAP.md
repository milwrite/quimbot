# CLOZE_ROADMAP.md — Cloze Reader Paper Planning & Proposals

Running log of style guide proposals, skill discoveries, and editorial planning.

---

## Style Guide Proposals (week of 2026-03-23)

Three recurring patterns from this week's edits (rules logged 2026-03-25 through 2026-03-28):

---

### Proposal 1: "Earned assertion" gate

**Pattern identified:** Multiple rules added this week address the same root error — prose that *asserts* a relationship (significance, contrast, difference-in-kind) before the surrounding sentences have established the ground for that claim. This appears in:
- **Vacuous openers** (added 2026-03-28): "The difference is concrete," "This is significant," "The point is clear" — the assertion is made before the evidence lands.
- **"Which is to say" overuse** (added 2026-03-28): used to restate what the prior clause already said, not to genuinely gloss a term or unpack compression.
- **False dilemma / submarine rule** (added 2026-03-21, re-articulated 2026-03-28): claiming two things compete at the same task when they are categorically different operations.

**Proposed refinement:** Add a single diagnostic to the STYLE_GUIDE that consolidates these: *Before any sentence that asserts significance, contrast, or equivalence, ask: has the preceding prose earned this claim? If the claim could be deleted without leaving a gap, delete it; if it names a relationship the prior clause has already demonstrated, cut the restatement.*

**Before example:**
> The difference is concrete. A language model updates weights during pretraining; a reader recovers a word choice.

**After example:**
> A language model updates weights during pretraining. A reader recovers a word choice. These are not two performances of the same operation at different skill levels — they are categorically different activities.

---

### Proposal 2: "Same-question test" for contrastive citation

**Pattern identified:** The submarine rule keeps requiring re-articulation because the error keeps appearing in different forms. The rule as written (don't frame two studies as competing when they address different domains) is correct but abstract. The recurring slip is more specific: setting up a contrast sentence that implies methodological commensurability before verifying it.

**Proposed addition to STYLE_GUIDE** (under "No false dilemmas in contrastive citation"):

> **Same-question test:** Before writing any contrastive sentence about two sources, write out explicitly: (1) what precise question Source A answers, (2) what precise question Source B answers, (3) whether those questions share the same dependent variable, population, and measure. If they don't share all three, the sources are submarines and swimmers — describe each in its own domain.

**Before example:**
> Curiously, in their 2024 study, Veldre et al. found LLM-enabled inference outperformed humans in conducting cloze procedures related to eye-movement data. This doesn't contradict the paper's argument.

**After example:**
> Veldre et al. (2024) asked whether LLM output predicts eye-movement regression data better than offline human cloze norms — a regression-modeling question about predictor strength. The paper's argument concerns what cloze *demonstrates* about a reader's inferential process. These are different questions with different measures; Veldre et al.'s finding has no direct bearing on the artifact's claim.

---

### Proposal 3: "Single separator" rule — extend punctuation audit

**Pattern identified:** The stacked punctuation ban (added 2026-03-28) catches colon + semicolon combinations but doesn't generalize the underlying diagnostic. The pattern shows up as: any clause using two structural separators (colon, semicolon, em-dash, parenthetical dash) to do the work one explicit connector should do.

**Proposed refinement to STYLE_GUIDE** (under "Colon and semicolon audit"):

> **Single separator rule:** A clause should not use more than one structural separator (colon, semicolon, em-dash pair). Two separators in one clause means two logical relationships are being papered over at once. Split into two sentences; surface both connectors explicitly.

**Before example:**
> Educational cloze tests assess the capacity that constitutes reading comprehension: the synthesis of linguistic knowledge, world knowledge, and inferential skill; the Cloze Reader exploits this same capacity to make the model's limit legible.

**After example:**
> Educational cloze tests assess the synthesis of linguistic knowledge, world knowledge, and inferential skill — the capacity that constitutes reading comprehension. The Cloze Reader exploits this same capacity so that the model's limit becomes legible where the synthesis fails.

---

## Skill Discovery (week of 2026-03-23)

Searched [ClawhHub](https://clawhub.ai) — the AgentSkill registry — on 2026-03-29.

**Result:** No skills published yet. The platform launched recently ("No skills yet. Be the first.") and the highlighted and popular sections are both empty.

**What would be useful for this project (to revisit when skills appear):**
- A citation-verification skill that cross-references claims against DOI/abstract text
- A prose diff skill for flagging style rule violations between draft versions
- A bibliography formatter skill for DHQ/MLA/Chicago register switching

**Action:** Re-check ClawhHub in 2–4 weeks as the catalog fills in. No installs available today.

---

*File created: 2026-03-29 | Maintained by: Petrarch + Quimbot*
