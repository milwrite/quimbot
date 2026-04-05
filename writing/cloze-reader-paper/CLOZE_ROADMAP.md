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

*Last updated: 2026-04-05 · Petrarch*
