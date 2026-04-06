# Style Macro Taxonomy

*Compact IDs for injection into context windows. Load only what applies.*

---

## Prefix System

| Prefix | Domain | Scope |
|---|---|---|
| `SX-` | Syntax | Sentence structure, clause order, interruptions |
| `VB-` | Verb | Verb strength, nominalizations, passive |
| `PX-` | Punctuation | Em dash, semicolon, colon, stacking |
| `CL-` | Claim | Assertion gates, evidence, scope |
| `CT-` | Citation | Contrastive citation, false dilemmas |
| `DC-` | Diction | Banned words, intensifiers, slop |
| `PR-` | Prose rhythm | Sentence variation, openers, tricolon |
| `AK-` | Academic register | DH/DHQ-specific, citation hygiene |
| `NL-` | NLG / generation | Rules specific to cloze, writing-under-surveillance, Reddit pieces |

---

## Full Macro Index

### Syntax (SX)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| SX-01 | Interrupted subject | No subject + comma-phrase + verb | `rules/SX-01.md` |
| SX-02 | List subject | No sentence whose subject is a list | `rules/SX-02.md` |
| SX-03 | Bridging construction | Kill "is what", "is this:", "is that" delays | `rules/SX-03.md` |
| SX-04 | Nominalization | No verb-phrase nominalization before verb | `rules/SX-04.md` |
| SX-05 | What-X opener | Kill "What X shows/describes/reveals as Y" | `rules/SX-05.md` |

### Verb (VB)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| VB-01 | Verb audit | Every verb: most precise + rhetorically effective option | `rules/VB-01.md` |
| VB-02 | Strong verbs | Ban utilize/leverage/facilitate/enhance | `rules/VB-02.md` |
| VB-03 | Authors as agents | Researchers do the work, not their findings | `rules/VB-03.md` |

### Punctuation (PX)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| PX-01 | No em dash default | Em dash only if earned; otherwise restructure | `rules/PX-01.md` |
| PX-02 | Colon audit | Colon papers over a logical connector; surface it | `rules/PX-02.md` |
| PX-03 | Semicolon audit | Same audit as colon; one exception for rhetorical punch | `rules/PX-02.md` |
| PX-04 | Single separator | At most one structural separator per clause | `rules/PX-04.md` |
| PX-05 | Earned punctuation | Default: restructure. Second: logical connector. Last: leave mark | `rules/PX-05.md` |

### Claim (CL)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| CL-01 | Earned assertion gate | Prose must earn a claim before asserting it | `rules/CL-01.md` |
| CL-02 | Bound the claim | Scope claims to what the evidence shows; name the source | `rules/CL-02.md` |
| CL-03 | No floating assertions | Every non-trivial claim requires traceable evidence | `rules/CL-03.md` |
| CL-04 | Counterargument slot | One serious rival reading per major claim cluster | `rules/CL-04.md` |
| CL-05 | Name the mechanism | Name what acts, not its category label | `rules/CL-05.md` |

### Citation (CT)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| CT-01 | Submarine rule | Don't pit studies that answer different questions | `rules/CT-01.md` |
| CT-02 | Same-question test | Write out DV, population, measure before any contrastive sentence | `rules/CT-02.md` |
| CT-03 | LLM-as-judge gate | Quimbot cannot solo-approve cloze paper style calls | `rules/CT-03.md` |
| CT-04 | Citation sequence | Phenomenon before scholar; theory explains what reader just saw | `rules/CT-04.md` |

### Diction (DC)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| DC-01 | AI slop ban | Full banned word list | `rules/DC-01.md` |
| DC-02 | Contrastive pivots | Kill "not X but Y", "not just X", "less about X more about Y" | `rules/DC-02.md` |
| DC-03 | Cut filler | "in order to" → "to"; "due to the fact that" → "because" | `rules/DC-03.md` |
| DC-04 | No setup phrases | Don't announce the point; make it | `rules/DC-04.md` |
| DC-05 | "This" requires a noun | Never let "This" stand alone as subject | `rules/DC-05.md` |
| DC-06 | No expletive openers | Ban "There is/are" as sentence openers | `rules/DC-06.md` |
| DC-07 | Contrastive pivots (non-negotiable) | Kill all contrastive constructions — state the point directly | `rules/DC-07.md` |
| DC-08 | No gap-bridging | No "bridges the gap", "fills the gap" | `rules/DC-08.md` |
| DC-09 | No melodramatic overclaims | No sweeping systemic claims from single events | `rules/DC-09.md` |

### Prose rhythm (PR)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| PR-01 | Sentence length variation | Mix short and long; no metronome cadence | `rules/PR-01.md` |
| PR-02 | Opener variation | Vary sentence openers; no three same-structure openers in a row | `rules/PR-02.md` |
| PR-03 | Short sentence for emphasis | Short sentence / fragment after long for contrast or landing | `rules/PR-03.md` |
| PR-04 | Trailing -ing ban | No participial phrase tag-ons at sentence end | `rules/PR-04.md` |
| PR-05 | No consecutive simple clauses | Three+ short subject-verb sentences = list; restructure | `rules/PR-05.md` |
| PR-06 | No freestanding echo sentences | No short sentence that restates what the previous sentence said | `rules/PR-06.md` |

### Academic register (AK)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| AK-01 | Concrete before abstract | Example first, inference second; theory explains what reader just saw | `rules/AK-01.md` |
| AK-02 | Don't fit the frame to the subject | Use the term that names the subject's actual condition | `rules/AK-02.md` |
| AK-03 | Citation hygiene | Peer-reviewed sources for key claims; no blog load-bearing | `rules/AK-03.md` |
| AK-04 | Separate observation/inference/speculation | Signal each epistemic level explicitly | `rules/AK-04.md` |
| AK-05 | No invented academic noun phrases | Flag unknown phrases; use field terms only | `rules/AK-05.md` |

### NLG / generation (NL)
| ID | Name | Short rule | Rules file |
|---|---|---|---|
| NL-01 | DHQ register + structural continuity | DHQ register; connect to prior sections; functional asymmetry governs | `rules/NL-01.md` |
| NL-04 | Reddit/surveillance register | Population-specific terms; bound claims to dataset; mechanisms named | `rules/NL-04.md` |

---

## Scope Profiles

Rather than injecting the full taxonomy every session, load a scope profile for the task type:

| Profile | Loads | Path |
|---|---|---|
| `phrase-edit` | SX-01–05, PX-01–05, PR-01–06 | `scope/phrase-edit.md` |
| `sentence-revision` | SX + PX + VB + CL-01–03 + DC-01–09 + PR-01–06 | `scope/sentence-revision.md` |
| `paragraph-reorg` | CL + CT + PR + AK-01–04 | `scope/paragraph-reorg.md` |
| `academic-draft` | All AK + CT + CL + VB-03 + DC-03 + NL-01 | `scope/academic-draft.md` |
| `cloze-paper` | `academic-draft` + NL-01 + NL-04 | `scope/cloze-paper.md` |
| `reddit-piece` | `academic-draft` + NL-02 + NL-04 | `scope/reddit-piece.md` |
| `microblog` | PR + DC + VB-01–02 | `scope/microblog.md` |
| `full` | Everything | `scope/full.md` |

---

*Both Quimbot and Petrarch maintain this file. When a new rule is established, assign it an ID here before adding the rule card.*
