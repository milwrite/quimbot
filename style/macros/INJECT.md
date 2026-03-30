# Style Macro Injection Template

*This is the context-window fragment loaded when the style system activates.*
*Load this file + the relevant scope profile. Do not load the full taxonomy unless required.*

---

## Activation

**Auto-activates** when:
- Any NLG task is in play (cloze paper, writing-under-surveillance, Reddit piece, microblog)
- A sentence-level or paragraph-level revision is being performed
- milwrite explicitly toggles it on

**Notify milwrite** at the start of the response:
> `[STYLE MACROS ACTIVE: <profile-name> — <count> rules loaded]`

Example: `[STYLE MACROS ACTIVE: cloze-paper — 28 rules loaded]`

---

## How to Use During Generation

For each output sentence or edit:

1. Identify the relevant macro IDs that apply to the construction being generated or revised
2. Check against rules before finalizing
3. If a violation is caught mid-generation, correct and continue (don't surface unless milwrite asks for audit mode)

**Audit mode** (when milwrite asks "run audit" or "check this against style"):
- List each sentence
- List macro IDs that fired
- State violation or pass
- Propose correction if violation

---

## Injection Block (copy into context as-is when activating)

```
STYLE MACROS ACTIVE
Profile: [PROFILE_NAME]
Loaded rules: [LIST_MACRO_IDS]

Non-negotiables (always on, all profiles):
- SX-01: no interrupted subject (Subject, [phrase], verb)
- SX-04: no verb-phrase nominalization
- PX-01: no em dash unless earned; restructure first
- CL-01: earned assertion gate — prose earns claims before asserting them
- CT-01: submarine rule — no pitting studies that answer different questions
- DC-01: no AI slop vocabulary
- DC-07: no contrastive pivots (not X but Y)
- VB-01: verb audit every sentence
- PR-04: no trailing participials (-ing tag-ons)

Profile rules: [LOAD FROM SCOPE FILE]
```

---

## Toggle Commands

- **"style macros on"** → activate with inferred profile based on task type
- **"style macros off"** → deactivate; no notification needed
- **"style macros: [profile]"** → activate specific profile
- **"audit this"** → run full audit on preceding output against active macros
- **"which macros fired?"** → list IDs that triggered in the previous response

---

*Quimbot maintains this file. Petrarch uses the same injection block.*
