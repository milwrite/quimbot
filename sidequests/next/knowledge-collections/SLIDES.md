# SLIDES.md — Curating Knowledge Collections
## Workshop 2: CUNY AI Lab Sandbox

Companion to `index.html`. Keep this file in sync whenever slide titles or text content change.
Upstream source: <https://github.com/CUNY-AI-Lab/knowledge-collections>
Live deck: <https://cuny-ai-lab.github.io/knowledge-collections/>
Previous workshop: <https://github.com/CUNY-AI-Lab/system-prompting>

> **CHANGE (2026-03-22, Iteration 1): `data-slide` attributes added to all slide divs. 32/32 applied.**
> **CHANGE (2026-03-22, Iteration 2): Deck collapsed 32 → 27 slides. Five collapses. System prompt hooks added to slides 3 and three-layers.**
> **CHANGE (2026-03-22, Iteration 3): Model-setup prereq slide inserted (slide 3, `data-slide="model-setup"`). Deck now 28 slides. Slides 4–5 updated for model-first framing. See Changelog.**

---

## Slide 1 — Title (`title-slide`, `data-slide="title"`)

**Title:** Curating Knowledge Collections
**Subtitle:** A Workshop for the CUNY AI Lab Sandbox
**Date:** March 23, 2026
**Authors:** Stefano Morello and Zach Muhlbauer

---

## Slide 2 — Workshop Roadmap (`layout-full-dark`, `data-slide="roadmap"`)

**Label:** Workshop Series
**Title:** Three Weeks, Three Skills

| Date | Session | Description |
|------|---------|-------------|
| March 16 — Last Week | Composing System Prompts ✓ | Defined how the AI thinks, responds, and engages with your students |
| March 23 — This Week | **Curating Knowledge Collections** _(active)_ | Upload syllabi, readings, and relevant sources to ground AI models in course materials |
| March 30 | Customizing Skills & Tools | Build specialized skills, tools, and workflows tailored to your courses |

---

## Slide 3 — Before We Start: Configure Your Model (`layout-split`, `data-slide="model-setup"`)

**CHANGE (Iteration 3 — NEW SLIDE): Prereq activity inserted before KC content begins. Participants open Workspace → Models, verify system prompt, and keep the tab open. Two-step carousel (c→d images: model list, model editor Knowledge section). Frames the whole session as "attaching to your existing model."**

**Label:** Before We Start
**Title:** Open Your Model in the Workspace

**Cards (left):**
1. Go to Workspace → Models — find the model from last week
2. Check your system prompt — verify it's in place, adjust if needed
3. Keep this tab open — you'll return here to attach the collection

**Carousel (right):**
- `slide4-c.png` — Model list; "keep it open"
- `slide4-d.png` — Model editor Knowledge section; "this is where the collection attaches"

---

## Slide 4 — What Is a Knowledge Collection? (`layout-split`, `data-slide="what-is"`)

**CHANGE (Iteration 3): Tip-box second sentence updated: "Your model is ready — now give it something to draw on." Removes forward reference; acknowledges prereq is done.**

**CHANGE (Iteration 2 — original system prompt hook, now superseded by Iteration 3 wording above)**

**Label:** The Basics
**Title:** What Is a Knowledge Collection?

**Content (left):**
A **knowledge collection** is a set of documents you upload to ground an AI model in specific course materials. The model draws on these documents when responding to students.

> Think of it as the **reading list** for your AI tool: the sources it can reference, the assignments it knows about, and the disciplinary context it works within.

**Key distinction:** The *system prompt* tells the model how to behave. The *knowledge collection* tells it what to draw on. Together, they create a tool grounded in your teaching context.

**Stage (right):** Theater diagram
- Backstage (what you build): System Prompt + Knowledge Collection (both hidden from students)
- Curtain: "student never sees above"
- Frontstage: Student asks "What does the rubric say about evidence?" → AI Model (draws on uploaded course materials) → AI responds with rubric-specific grounded answer

---

## Slide 5 — Where It Lives (`layout-split`, `data-slide="where-it-lives"`)

**CHANGE (Iteration 3): Intro text rewritten — model-first framing: "Your model is open. Now you need two things to attach to it." Step 1 = model already done; Step 2 = today's collection task. Tip box updated: "Order matters: Model first, collection second."**
**CHANGE (Iteration 3): Carousel reordered c→d→a→b. Now shows model config screenshots first (c: model list, d: Knowledge section) before knowledge base creation (a: Knowledge tab, b: Create form).**

**Label:** Open WebUI
**Title:** Where It Lives

**Content (left):**
In the CUNY AI Lab Sandbox, knowledge collections live in two places:

1. **Knowledge Base** — Workspace → Knowledge. Create a new collection, upload PDFs/text files, name and describe it.
2. **Model Configuration** — Workspace → Models. Open your custom model, attach the collection under **Knowledge**.

**Workflow:** Create the collection first, then attach it to your model. The system prompt from last week tells the model *how* to use these materials.

**Stage (right):** 4-step carousel
- `slide4-a.png` — Knowledge Base Step 1: Workspace → Knowledge → "+ New Knowledge"
- `slide4-b.png` — Knowledge Base Step 2: Name, describe, set access → "Create Knowledge"
- `slide4-c.png` — Model Configuration Step 1: Workspace → Models → click your model
- `slide4-d.png` — Model Configuration Step 2: Knowledge section → "Select Knowledge"

---

## Slide 5 — Why Knowledge Collections Matter (`layout-content`, `data-slide="why-it-matters"`)

**Label:** Why Bother?
**Title:** Why Knowledge Collections Matter

**Setup:** A student asks a custom model: **"What should I focus on for the midterm essay?"**

**Comparison (step-reveal):**

Without Knowledge Collection _(shown first)_:
"For a midterm essay, you should generally focus on your thesis statement, use evidence from your readings, and structure your argument clearly. Make sure to address counterarguments."
*Generic advice. No awareness of the assignment, the rubric, or the course readings.*

With Knowledge Collection _(revealed on advance)_:
"Based on the assignment prompt, your essay should analyze one primary source from the Reconstruction unit using the SOAPS framework we practiced. The rubric weights evidence and sourcing at 40%. Which document are you considering?"
*Grounded in the actual assignment, rubric, and course methodology.*

---

## Slide 6 — What Can You Upload? (`layout-full-dark`, `data-slide="upload-types"`)

**Label:** Building Materials
**Title:** What Can You Upload?

**Subtitle:** Any document that helps the AI understand your course context. The model retrieves relevant passages when students ask questions.

| Document Type | Description |
|--------------|-------------|
| Syllabi | Course schedule, learning objectives, policies, and expectations |
| Assignment Prompts | Instructions, requirements, and criteria for each assignment |
| Rubrics | Grading criteria so the model can reference specific expectations |
| Course Readings | Primary sources, articles, chapters, and excerpts students are working with |
| Lecture Notes | Key concepts, frameworks, and terminology from your lectures |
| Style Guides | Citation formats, disciplinary conventions, writing guidelines |
| Sample Work | Anonymized exemplars that model the quality you expect |
| Data Sets | Spreadsheets, CSV files, or structured data students analyze in labs or projects |
| Glossaries | Discipline-specific terminology, definitions, and key concepts for the course |
| Problem Sets | Exercises, practice questions, or worked examples with solutions |
| Lab Protocols | Step-by-step procedures, safety guidelines, and equipment instructions |
| Case Studies | Real-world scenarios, historical cases, or clinical examples used in coursework |

---

## ~~Slide 7 — Section Divider: How Retrieval Works~~ **REMOVED (Iteration 2): Merged into slide 7 below.**

---

## Slide 7 — How the Model Uses Your Documents (`layout-split`, `data-slide="retrieval"`)

**CHANGE (Iteration 2): Was slide 8. Slide 7 (pure divider) merged in. Section label "Under the Hood" now appears inline above the RAG label.**

**Label:** Retrieval-Augmented Generation
**Title:** How the Model Uses Your Documents

**Content (left):**
When a student asks a question, the system doesn't feed the *entire* collection to the model. It searches for the most relevant passages and grounds its answer in them.

- **Chunking:** Your documents are split into smaller passages when uploaded
- **Search:** The student's question is matched against those passages
- **Injection:** The top matches are included in the model's context window
- **Response:** The model generates an answer grounded in those passages

**Implication:** Short, focused documents with clear headings retrieve better than long, unstructured files. How you organize your materials matters.

**Stage (right):** Flow diagram
1. Student Question — "What does the rubric say about citations?"
2. ↓ Search Collection — Finds relevant passages from your documents
3. ↓ AI Model + Retrieved Context — System prompt + relevant passages + student message
4. ↓ Grounded Response — Answer references your actual course materials

---

## Slide 8 — Section Divider: What Makes a Good Collection? (`layout-divider`, `data-slide="part1"`)

**CHANGE (Iteration 2): Was slides 9+10 (two back-to-back dividers). Merged into one. Section label now reads "Part I — Example 1"; subtitle added: "Starting with Composition & Writing".**

**Section label:** Part I — Example 1
**Title:** What Makes a Good Knowledge Collection?
**Subtitle:** Starting with Composition & Writing

---

## ~~Slide 10 — Section Divider: Composition & Writing~~ **REMOVED (Iteration 2): Folded into slide 8 above.**

---

## Slide 9 — Composition: The Bare Minimum (`layout-content`, `data-slide="composition-bad"`)

**Label:** Composition & Writing · progression 1/3 (bad)
**Title:** The Bare Minimum

**Weak collection:**
- `syllabus.pdf` (14 pages, full course syllabus)

**What goes wrong?** _(step-reveal)_
- One large document retrieves poorly: the model pulls random passages instead of relevant ones
- No assignment-specific materials for the model to reference
- No rubric, no readings, no examples of what good work looks like

---

## Slide 12 — Composition: Getting Warmer (`layout-content`, `data-slide="composition-mid"`)

**Label:** Composition & Writing · progression 2/3 (mediocre)
**Title:** Getting Warmer

**Mediocre collection:**
- `syllabus.pdf`
- `essay-1-prompt.pdf`
- `essay-1-rubric.pdf`
- `mla-style-guide.pdf`

**What improved?** _(step-reveal)_
- Separate documents for different purposes: the model can find the rubric when asked about grading
- Assignment-specific prompt gives the model context for that unit
- Style guide helps with formatting questions

**What's still missing?** _(step-reveal)_
- No course readings for the model to reference during analysis
- No examples of strong student work to model expectations
- No instructor notes on common student challenges

---

## Slide 13 — Composition: A Collection That Grounds Revision (`layout-content`, `data-slide="composition-good"`)

**Label:** Composition & Writing · progression 3/3 (strong)
**Title:** A Collection That Grounds Revision

**Strong collection:**

*Course Framework*
- `syllabus.pdf` — schedule, learning objectives, policies
- `revision-philosophy.txt` — instructor notes on what revision means in this course

*Assignment Materials (Essay 1: Rhetoric in Popular Media)*
- `essay-1-prompt.pdf` — assignment instructions and requirements
- `essay-1-rubric.pdf` — grading criteria with descriptions of each level
- `common-feedback.txt` — patterns from past semesters (e.g., thesis too broad, evidence not analyzed)

*Reference Materials*
- `mla-style-guide.pdf` — citation and formatting conventions
- `strong-intro-examples.txt` — anonymized examples of effective introductions
- `revision-checklist.pdf` — the same checklist students use in peer review

---

## Slide 14 — Section Divider: Primary Source Analysis (`layout-divider`, `data-slide="history-intro"`)

**Section label:** Example 2
**Title:** Primary Source Analysis

---

## Slide 15 — History: The Bare Minimum (`layout-content`, `data-slide="history-bad"`)

**Label:** History · progression 1/3 (bad)
**Title:** The Bare Minimum

**Weak collection:**
- `textbook-chapter-12.pdf` (42 pages)

**What goes wrong?** _(step-reveal)_
- A full textbook chapter is too long and too general: retrieved passages are often irrelevant
- No primary sources for the model to help students analyze
- No methodological framework for the model to follow

---

## Slide 16 — History: Getting Warmer (`layout-content`, `data-slide="history-mid"`)

**Label:** History · progression 2/3 (mediocre)
**Title:** Getting Warmer

**Mediocre collection:**
- `syllabus.pdf`
- `source-analysis-assignment.pdf`
- `primary-source-1.pdf` (Freedmen's Bureau report, 1866)
- `primary-source-2.pdf` (Congressional testimony, 1871)

**What improved?** _(step-reveal)_
- Includes actual primary sources students are working with
- Assignment prompt gives the model task-specific context
- Documents are separate and focused

**What's still missing?** _(step-reveal)_
- No contextual background for the model to draw on when students ask about the period
- No rubric or analysis framework to guide the model's scaffolding
- No source metadata (author, date, document type) to support sourcing questions

---

## Slide 17 — History: A Collection That Fosters Historical Thinking (`layout-content`, `data-slide="history-good"`)

**Label:** History · progression 3/3 (strong)
**Title:** A Collection That Fosters Historical Thinking

**Strong collection:**

*Course Framework*
- `syllabus.pdf` — schedule, themes, learning objectives
- `soaps-framework.txt` — the analytical framework students use, with definitions and examples
- `source-analysis-rubric.pdf` — grading criteria for the source analysis report

*Primary Sources (Reconstruction Unit)*
- `freedmens-bureau-report-1866.pdf` — with metadata: author, date, document type, archive
- `congressional-testimony-1871.pdf` — with metadata
- `source-context-notes.txt` — brief historical context for each source (2-3 sentences each)

*Reference Materials*
- `period-timeline.txt` — key events 1865–1877 for contextualization questions
- `common-analysis-errors.txt` — patterns from past semesters (e.g., treating sources as neutral facts)
- `chicago-citation-guide.pdf` — citation format for history papers

---

## Slide 18 — Section Divider: Close Reading & Literary Analysis (`layout-divider`, `data-slide="literature-intro"`)

**Section label:** Example 3
**Title:** Close Reading & Literary Analysis

---

## Slide 19 — Literature: The Bare Minimum (`layout-content`, `data-slide="literature-bad"`)

**Label:** Literature & Cultural Studies · progression 1/3 (bad)
**Title:** The Bare Minimum

**Weak collection:**
- `course-reader.pdf` (180 pages, all readings for the semester)

**What goes wrong?** _(step-reveal)_
- A 180-page file retrieves unpredictably: the model might pull from the wrong text entirely
- No assignment context or analytical framework
- No separation between literary texts and critical essays

---

## Slide 20 — Literature: Getting Warmer (`layout-content`, `data-slide="literature-mid"`)

**Label:** Literature & Cultural Studies · progression 2/3 (mediocre)
**Title:** Getting Warmer

**Mediocre collection:**
- `syllabus.pdf`
- `close-reading-assignment.pdf`
- `sonny-blues-baldwin.pdf`
- `new-criticism-overview.pdf`

**What improved?** _(step-reveal)_
- Individual literary text rather than an omnibus reader
- Assignment prompt provides task-specific context
- Critical framework document gives the model methodological grounding

**What's still missing?** _(step-reveal)_
- No rubric for the model to reference when guiding analysis
- No examples of close-reading annotations or model analyses
- No glossary of literary terms the course uses

---

## Slide 21 — Literature: A Collection That Fosters Close Reading (`layout-content`, `data-slide="literature-good"`)

**Label:** Literature & Cultural Studies · progression 3/3 (strong)
**Title:** A Collection That Fosters Close Reading

**Strong collection:**

*Course Framework*
- `syllabus.pdf` — schedule, texts, learning objectives
- `new-criticism-framework.txt` — key concepts: close reading, tension, irony, paradox, ambiguity
- `literary-terms-glossary.txt` — definitions of terms used in the course (diction, imagery, syntax, tone)

*Assignment Materials (Close Reading Essay)*
- `close-reading-assignment.pdf` — instructions and requirements
- `close-reading-rubric.pdf` — grading criteria for textual analysis
- `annotated-passage-example.txt` — model annotation showing how to move from observation to interpretation

*Literary Texts (Current Unit)*
- `sonny-blues-baldwin.pdf` — the primary text for this assignment
- `passage-selections.txt` — key passages the instructor has flagged for class discussion

---

## ~~Slide 22 — Section Divider: Best Practices & Pitfalls~~ **REMOVED (Iteration 2): Standalone divider dropped. "Part II" section label folded into Best Practices slide header.**

---

## Slide 20 — Curation Best Practices (`layout-grid`, `data-slide="best-practices"`)

**CHANGE (Iteration 2): Was slide 23. "Part II" section-label now appears inline above the h2.**

**Title:** Curation Best Practices

| Principle | Description |
|-----------|-------------|
| One Document, One Purpose | Upload separate files for syllabus, rubric, readings, and frameworks. The model retrieves better from focused documents than from large omnibus files. |
| Add Metadata and Headings | Include titles, authors, dates, and clear section headings. These act as retrieval anchors that help the model find the right passage. |
| Write What the Model Can't Infer | The model doesn't know your pedagogical intent. A short `common-feedback.txt` or `context-notes.txt` in your own words is more valuable than another PDF. |
| Update Per Unit | Swap readings and assignment materials as the semester progresses. A collection grounded in the current unit is more useful than one covering the whole course. |

---

## Slide 24 — Common Pitfalls (`layout-content`, `data-slide="pitfalls"`)

**Label:** Watch Out
**Title:** Common Pitfalls

| Pitfall | Why It Matters |
|---------|---------------|
| Dumping Everything In | Uploading every reading for the entire semester dilutes retrieval quality. More documents means more noise. |
| One Giant PDF | A 200-page course reader retrieves unpredictably. Split into individual texts. Short, well-labeled documents retrieve far better than long ones. |
| Forgetting the System Prompt | A knowledge collection without a system prompt is a pile of documents with no instructions. The system prompt tells the model *how* to use the materials. |
| Assuming the Model Read Everything | The model only sees retrieved passages, not the full document. If something is critical, put it in its own file with a clear heading. |

---

## ~~Slide 25 — Section Divider: Build Your Collection~~ **REMOVED (Iteration 2): Folded into exercise slide. "Part III — Hands-On" section-label added inline.**

---

## Slide 22 — Build a Collection in Three Layers (`layout-content`, `data-slide="three-layers"`)

**CHANGE (Iteration 2): Was slides 25+26. Part III divider dropped; section-label folded inline above Exercise label.**
**CHANGE (Iteration 2 — system prompt integration): Step 0 added to exercise — instructors open last week's model before starting.**

**Label:** Exercise
**Title:** Build a Collection in Three Layers

Pick one assignment from your course. Build a knowledge collection for it, one layer at a time.

1. **Course Framework** — Syllabus, learning objectives, and the analytical framework students use
2. **Assignment Materials** — Prompts, rubrics, examples, and common feedback patterns
3. **Source Materials** — Readings, primary sources, and reference documents for the current unit

---

## Slide 27 — Layer 1: Course Framework (`layout-split`, `data-slide="layer-framework"`)

**Label:** Step 1
**Title:** Course Framework

**Content (left):**
Start with the documents that establish your course's identity: what students are learning, how they're assessed, and what methods they use.

- What are the course's learning objectives?
- What analytical framework or methodology do students use?
- What are the course policies the model should know about?

**Stage (right) — copyable template (`id="tpl-framework"`):**
```
Recommended uploads:

1. syllabus.pdf
   - Course schedule, objectives, and policies
   - Tip: Keep it under 10 pages if possible

2. [framework-name].txt
   - The analytical method students use
   - E.g., SOAPS, New Criticism, revision checklist
   - Write it out in plain language with definitions
```

**Tip box:** Your turn — What framework or methodology is central to your course? Write a short document (1-2 pages) explaining it in the terms you use with students.

---

## Slide 28 — Layer 2: Assignment Materials (`layout-split`, `data-slide="layer-assignment"`)

**Label:** Step 2
**Title:** Assignment Materials

**Content (left):**
Upload the documents that define the current task. The model needs to know what students are working on, how they're graded, and where they typically struggle.

- What is the assignment prompt?
- What does the rubric prioritize?
- What feedback do you give most often?

**Stage (right) — copyable template (`id="tpl-assignment"`):**
```
Recommended uploads:

1. [assignment]-prompt.pdf
   - The actual assignment instructions

2. [assignment]-rubric.pdf
   - Grading criteria with level descriptions

3. common-feedback.txt
   - 5-10 patterns you see every semester
   - E.g., "Thesis too broad," "Evidence cited but not analyzed"

4. strong-examples.txt (optional)
   - Anonymized excerpts showing what good work looks like
```

**Tip box:** Your turn — Pick one assignment. Upload the prompt and rubric. Then write a short list of the feedback you give most often.

---

## Slide 29 — Layer 3: Source Materials (`layout-split`, `data-slide="layer-sources"`)

**Label:** Step 3
**Title:** Source Materials

**Content (left):**
Upload the readings and reference materials students are working with in the current unit. This grounds the model in the actual texts.

- What texts are students reading for this assignment?
- Are there reference documents (timelines, glossaries, citation guides)?
- Can you add brief metadata or context for each source?

**Stage (right) — copyable template (`id="tpl-sources"`):**
```
Recommended uploads:

1. [reading-title].pdf
   - Individual files per text (not one big reader)
   - Add a header with: title, author, date, source

2. context-notes.txt (optional)
   - 2-3 sentences of context per source
   - Helps the model answer "why does this matter?"

3. [reference-guide].pdf
   - Citation style guide, glossary, timeline
   - Whatever students consult during the assignment
```

**Tip box:** Your turn — Upload 1-3 readings for your chosen assignment. If they're in a single PDF reader, split them into separate files first.

---

## Slide 30 — Prompt + Collection (`layout-split`, `data-slide="prompt-plus-collection"`)

**Label:** Putting It Together
**Title:** Prompt + Collection

**Content (left):**
Your system prompt and knowledge collection work together. The prompt defines *behavior*. The collection provides *context*.

- **System Prompt says:** "Request the assignment prompt and student draft before responding. Identify the highest-priority concerns before surface-level issues."
- **Knowledge Collection provides:** The actual assignment prompt, rubric, common feedback patterns, and style guide the model references when following those instructions.

**Test it:** Ask the model a question only answerable from your collection. If it gives generic advice, the retrieval isn't working. Check your document structure.

**Stage (right):** Flow diagram — System Prompt (how to behave) + Knowledge Collection (what to draw on) = Grounded Response

---

## ~~Slide 31 — The Road Ahead~~ **REMOVED (Iteration 2): Merged into closing slide.**

---

## Slide 27 — Closing (`layout-full-dark closing-slide`, `data-slide="closing"`)

**CHANGE (Iteration 2): Was slides 31+32. Road Ahead roadmap widget + build steps combined into single dark-bg slide.**

**Title:** Let's Build One Together

**Roadmap widget (condensed, faded for completed weeks):**
- March 16 — System Prompts ✓ (dimmed)
- March 23 — Today — Knowledge Collections ✓ (dimmed)
- March 30 — Next Week — Skills & Tools (active)

**Build steps:**
1. Open your model from last week in the Sandbox
2. Create a knowledge collection with 3-5 documents
3. Attach it to that model
4. Test it with a real student question

**URL:** ailab.gc.cuny.edu

---

_Last synced: 2026-03-22. Upstream: CUNY-AI-Lab/knowledge-collections @ main. Update both files together._

---

---

## Changelog

### Iteration 1 (2026-03-22)
**`data-slide` attributes added to all 32 slide divs.** Derived from `aria-label` values. Matches workshop-1 convention.

### Iteration 3 (2026-03-22)
**Model-setup prereq slide added (slide 3, `data-slide="model-setup"`). Deck: 27 → 28 slides.**

Changes:
- **NEW slide `model-setup`** inserted between roadmap (slide 2) and what-is (now slide 4). Participants open Workspace → Models, verify system prompt, keep tab open — before KC content starts.
- **`what-is` tip-box** updated: "Your model is ready — now give it something to draw on." Prereq acknowledged as done.
- **`where-it-lives` intro text** rewritten: model-first framing. "Your model is open. Now you need two things to attach to it." Step 1 = model (done); Step 2 = collection (today).
- **`where-it-lives` carousel reordered**: c → d → a → b. Model config screenshots appear first; knowledge base creation follows.
- **`three-layers` Step 0** updated: "Your model is already open" (acknowledges prereq done at session start).

### Iteration 2 (2026-03-22)
**Deck collapsed: 32 → 27 slides. Five collapses applied:**

1. **Slides 7+8 → Slide 7** — "Under the Hood" divider dropped; section-label folded inline into Retrieval slide header.
2. **Slides 9+10 → Slide 8** — Two consecutive dividers ("Part I" + "Example 1: Composition") merged into one. Subtitle added.
3. **Slide 22 removed** — "Part II" standalone divider dropped; section-label folded inline into Best Practices h2.
4. **Slides 25+26 → single slide** — "Part III" divider dropped; section-label + exercise intro merged. Step 0 (system prompt connection) added.
5. **Slides 31+32 → Slide 27** — Road Ahead + Let's Build merged into single dark closing slide.

**System prompt integration added in two places:**
- Slide 3 tip-box: forward reference to the exercise — "bring that model to mind as we go"
- Slide 22 (three-layers) Step 0: explicit instruction to open last week's model before starting the exercise

## `data-slide` attribute reference

**CHANGE (2026-03-22, Iteration 1): All 32 `data-slide` attributes implemented in local `index.html`.**
**CHANGE (2026-03-22, Iteration 2): Deck collapsed. 27 slides remain. Slugs unchanged; 5 removed slugs: `retrieval-intro`, `composition-intro`, `part2`, `part3`, `road-ahead`.**

| Slide | Proposed `data-slide` value |
|-------|-----------------------------|
| 1 | `title` |
| 2 | `roadmap` |
| 3 | `what-is` |
| 4 | `where-it-lives` |
| 5 | `why-it-matters` |
| 6 | `upload-types` |
| 7 | `retrieval-intro` |
| 8 | `retrieval` |
| 9 | `part1` |
| 10 | `composition-intro` |
| 11 | `composition-bad` |
| 12 | `composition-mid` |
| 13 | `composition-good` |
| 14 | `history-intro` |
| 15 | `history-bad` |
| 16 | `history-mid` |
| 17 | `history-good` |
| 18 | `literature-intro` |
| 19 | `literature-bad` |
| 20 | `literature-mid` |
| 21 | `literature-good` |
| 22 | `part2` |
| 23 | `best-practices` |
| 24 | `pitfalls` |
| 25 | `part3` |
| 26 | `three-layers` |
| 27 | `layer-framework` |
| 28 | `layer-assignment` |
| 29 | `layer-sources` |
| 30 | `prompt-plus-collection` |
| 31 | `road-ahead` |
| 32 | `closing` |

To implement: add `data-slide="<value>"` to the opening `<div class="slide ...">` tag for each slide in `index.html`.
