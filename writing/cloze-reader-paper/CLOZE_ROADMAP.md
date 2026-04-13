# CLOZE_ROADMAP.md — Style Guide Proposals & Skill Discovery Log

*Maintained by Petrarch. Weekly review entries appended below.*

---

## Style Guide Proposals (week of 2026-03-29 – 2026-04-05)

**Source material:** EDITS.md (ED-001 through ED-024, v43 approvals); STYLE_GUIDE.md additions dated 2026-03-29 through 2026-03-31.

### Pattern 1: Bare Demonstrative Backward Pointers Are Still Getting Through

**Observation:** Despite the bare-"This"-as-subject ban, ED-020 caught "that gradient" as a backward-pointer violation — same failure mode, different demonstrative. The style guide added the "no bare demonstrative backward pointers" rule on 2026-03-31, but the existing ban language was only blocking sentence-subject "This." Demonstrative "that" as the only anchor pointing back to a preceding noun was still passing review.

**Proposed rule refinement:** Extend the diagnostic explicitly to object position and mid-sentence use, not just sentence-subject position. Current rule correctly targets "That [noun] is..." as a sentence opener, but the same problem appears mid-sentence: "...a measure of [thing], building on that gradient / that constraint / that claim."

**Before:** "...the information-theoretic basis for that gradient was not formalized until..."
**After:** "...the information-theoretic basis for difficulty variation across blank positions was not formalized until..."

**Recommendation:** Add to style guide under "No bare demonstrative backward pointers" — a clause specifying that the ban applies to object and complement positions as well as sentence-subject position.

---

### Pattern 2: Thin Independent Clauses Persist After Merge Attempts

**Observation:** ED-012 merged seven thin independents in the Continuity section; ED-003 merged openers in Educational Genealogy; ED-007 merged Harris/Firth. Despite repeated applications, the same pattern recurs in proposed edits (ED-017: "The intervention proved durable enough..." as a standalone transition sentence; ED-019: comma-that loosely attaching a core claim). Merging fixes the local instance but doesn't prevent new thin-sentence insertions.

**Proposed rule addition:** When a sentence functions as a transition between sections or paragraphs, it must do double duty — either carry forward a claim from the preceding paragraph as its subject, or open the next paragraph's argument. A sentence that only moves the reader from A to B without content belongs in neither place. Cut it or fold its content into the paragraphs it connects.

**Before:** "The intervention proved durable enough to move from educational psychology to computational laboratories, where cloze-like objectives now structure how machines learn language."
**After:** Fold into the preceding paragraph's closing clause, or open the ML Genealogy section with Taylor as subject doing the forward motion.

**Recommendation:** Add as "No pure transition sentences" under Hard Rules.

---

### Pattern 3: Colon/Semicolon Audit Not Being Applied at Drafting Stage

**Observation:** The colon/semicolon audit rule (added 2026-03-18) identifies specific replacement patterns (colon → participial phrase, semicolon → "so that," etc.), but ED-003 shows the problem recurring: "formally simple. Delete words… The theoretical ambition behind it was larger." was originally written as a colon construction before Quimbot's merge. ED-019 shows another comma-that where a colon was needed. The audit is being applied reactively (in EDITS.md), not proactively during drafting.

**Proposed workflow addition:** Before any new paragraph enters the draft, run the separator test as a checklist item: (1) locate all colons/semicolons, (2) name the logical relationship each is papering over, (3) surface the connector. This is already in the style guide but needs explicit status as a pre-commit gate, not a post-hoc edit.

**Before:** "formally simple. Delete words…" [colon collapsed to period, ambiguous relationship]
**After:** "formally minimal, requiring only that an administrator delete words at fixed intervals — a constraint that understated the procedure's theoretical ambition"

**Recommendation:** Add as checklist item to the "Required habits" section of STYLE_GUIDE.md: "Pre-commit separator audit: locate all colons/semicolons; name the relationship; surface the connector."

---

## Skill Discovery (week of 2026-03-29 – 2026-04-05)

**Source:** ClaHub (clawhub.ai) — searched 2026-04-05

**Finding:** ClaHub launched recently and currently has no published skills. The registry is live and accepts uploads via `npx clawhub@latest install [skill-name]`, but as of this search, no skills appear in the "Popular" or "All skills" listings. No academic writing, citation management, or revision tools are available for discovery at this time.

**Alternatives to monitor:**
- `zotero` skill is already installed in this workspace (see TOOLS.md) — covers citation management via Zotero Web API
- `academic-research` skill (OpenAlex, no API key) is also installed
- ClaHub worth rechecking in 2–4 weeks as the registry matures

---

## Style Guide Proposals (week of 2026-04-13)

**Source material:** `STYLE_GUIDE.md`; `JOURNAL.md` skimmed for 2026-04-06 through 2026-04-13 (**no entries logged this week**); active patterns inferred from the current `EDITS.md` board and the most recent approved/still-open cloze revisions.

### Pattern 1: Transition sentences still arrive with weak abstract subjects

**Observation:** The recurring problem is not only thin syntax but transitional syntax built on abstract carriers: *the intervention*, *the structure*, *the resemblance*. These sentences move the reader between sections but keep the real historical agent offstage.

**Proposed refinement:** Add a rule banning **abstract transition subjects**. If a sentence is moving from one genealogy to another, it should open on the actor or mechanism doing that movement — Taylor, BERT's developers, masked-language-model training, the scoring procedure — not on an abstract placeholder.

**Before:** "The intervention proved durable enough to move from educational psychology to computational laboratories, where cloze-like objectives now structure how machines learn language."
**After:** "Cloze testing moved from educational psychology into computational linguistics, where masked-word objectives now structure how language models are trained."

**Recommendation:** Add under Hard Rules: **No abstract transition subjects.** Transitional sentences must open on the historical actor, procedure, or mechanism that actually carries the claim forward.

---

### Pattern 2: Bare demonstratives keep reappearing in longer noun phrases

**Observation:** The existing backward-pointer rule catches sentence-openers like *That asymmetry* or *This difficulty architecture*, but the same habit persists inside otherwise improved sentences: *that gradient*, *that distinction*, *that premise*. The underlying issue is still undernaming.

**Proposed refinement:** Expand the demonstrative rule from sentence openings to **all load-bearing noun phrases**. If the noun phrase carries an argument, it should name the referent directly instead of leaning on *this* or *that*.

**Before:** "The information-theoretic basis for that gradient was not formalized until Maltaev et al. (2019)."
**After:** "Maltaev et al. (2019) formalized the information-theoretic basis for variation in gap difficulty."

**Recommendation:** Revise the existing rule to read: **No bare demonstrative backward pointers in any load-bearing noun phrase**, not only at sentence start.

---

### Pattern 3: Citation-bearing sentences are doing too much interpretive work at once

**Observation:** Several open edit proposals strengthen the genealogy by adding evidence, but the proposed sentences often bundle source report, interpretation, and argumentative payoff into one long unit. The pressure point is not sentence length alone; it is **citation compression**.

**Proposed addition:** Add a rule for **one interpretive step per citation-bearing sentence**. A sentence can report what a study found, or state what that finding means for the paper's argument, but when it tries to do both plus supply historical transition, clarity drops.

**Before:** "That the two methods correlate at 0.92 across full test scores (Laing, cited in Brown 1980) suggests readers are operating on part-of-speech and semantic-category information rather than recovering the author's specific word choice — a finding that clarifies rather than resolves the ambiguity."
**After:** "Laing, as cited in Brown (1980), reported a 0.92 correlation between exact and acceptable scoring across full test scores. That result suggests the procedure samples part-of-speech and semantic-category information more readily than author-specific lexical choice."

**Recommendation:** Add under Required Habits: **Split citation report from argumentative gloss when a sentence is carrying evidence, inference, and transition at once.**

## Skill Discovery (week of 2026-04-13)

**Source:** ClawHub (`clawhub.ai`) search on 2026-04-13

1. **Blind Review Sanitizer** — <https://clawhub.ai/googolme/blind-review-sanitizer>
   - Use case: strips identifying metadata, acknowledgments, and heavy self-citation signals from manuscripts before double-blind review
   - Why relevant: useful for submission prep and citation hygiene when circulating article drafts

2. **Academic Writing Refiner** — <https://clawhub.ai/skills/academic-writing-refiner>
   - Use case: polishing, editing, and refining academic prose
   - Why relevant: potentially useful as a comparison tool for revision passes, though it would need strict style-guide oversight

3. **Word / DOCX** — <https://clawhub.ai/ivangdavila/word-docx>
   - Use case: edits DOCX files with styles and tracked changes support
   - Why relevant: promising for round-tripping article drafts into Word review workflows without losing markup structure

**Note:** ClawHub search is still sparse and some listings need closer vetting before adoption. These are plausible leads, not install recommendations yet.

---

*Last updated: 2026-04-13 · Petrarch*
