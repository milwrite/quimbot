---
name: cail-doc-calibrator
description: Write and refine documentation for the CUNY AI Lab Sandbox (cail-docs) using the voice, structure, and progressive disclosure patterns of the Discord Educational Toolkit and Teach@CUNY AI Toolkit. Use when creating, rewriting, or reviewing documentation pages for instructor-facing platform guides, especially Open WebUI workspace features. Covers prose style calibration, procedural walkthrough formatting, pedagogical framing, multimedia planning, and the three-kit progressive disclosure model (Starter Kit, Design Kit, Instructional Kit).
---

# CAIL Doc Calibrator

Calibrate CUNY AI Lab Sandbox documentation to match the voice, structure, and granularity of two proven instructor-facing toolkits: the Discord Educational Toolkit and the Teach@CUNY AI Toolkit.

## Voice

Write as a colleague, not a manual. Address the reader as "you." Anticipate their concerns. Explain why before how.

**Do:**
- "When you build a Knowledge Collection, the AI searches your uploaded documents before responding. This grounds conversations in your course materials rather than generic training data."
- "Pick and choose what suits you best, add it to your toolbox, and practice up!"

**Don't:**
- "Knowledge Collections enable Retrieval-Augmented Generation (RAG), a technique that combines language models with retrieved knowledge from external sources."
- "Users should configure the embedding model via the Admin Panel."

### Prose Rules

- **Sentence length:** Vary. Short declaratives for emphasis. Longer sentences for explanation. No metronome rhythm.
- **Paragraphs:** 2-4 sentences. Break up dense text.
- **Active voice:** "Instructors should..." not "It is recommended that..."
- **Transitions:** Connect ideas ("In turn," "Toward that end," "Here it is key," "With a little practice").
- **Direct address:** "you," "your students," "your server"
- **No em dashes.** Use periods, commas, colons, semicolons, or parentheses.
- **No AI slop.** Ban: delve, tapestry, robust, seamless, comprehensive, meticulous, transformative, cornerstone, reimagine, empower.
- **No contrastive constructions.** Kill "not this but that," "rather than," "instead of," "goes beyond," "more than just." State what it IS. Drop the comparison.

## Structure: Three-Kit Model

Organize docs using progressive disclosure through three kits:

### Starter Kit (Getting Started)
First-time users. Minimum viable steps. Login, first chat, first model.
- High procedural granularity (every click documented)
- GIFs for key workflows
- "Voila!" energy when something works

### Design Kit (Building & Configuring)
Users ready to customize. Models, knowledge bases, tools, roles, permissions.
- Separate "Model Uses" (pedagogical rationale) from "Feature Suggestions" (technical steps)
- Numbered steps with sub-bullet rationale
- Screenshots for reference states

### Instructional Kit (Teaching Patterns)
Instructors integrating the platform into pedagogy. Workflows, activities, templates.
- Use-case-first framing (scenario before feature)
- Learning objectives for each activity
- Attribution and external citations
- Reflective questions for critical engagement

## Page Template

Every doc page follows this structure. Read `references/page-template.md` for the full template.

1. **Title + context sentence** (what this page covers and why it matters)
2. **Quick orientation** (1-2 paragraphs framing the feature for instructors)
3. **Model Uses** (pedagogical scenarios, 3-5 bullets)
4. **Step-by-step procedure** (numbered, every click, with sub-bullet rationale)
5. **Visual support** (GIF or screenshot placeholder with alt text)
6. **Callout box** (tip, warning, or best practice)
7. **Additional Resources** (2-3 external links)
8. **Navigation footer** (`← Previous` / `Continue →`)

## Procedural Granularity

For UI walkthroughs, document every click:

```markdown
1. Click **Workspace** in the left sidebar
2. Select **Models**
3. Click **+ New Model**
   - This opens the model configuration editor where you define behavior, attach knowledge, and bind tools
4. Choose a base model from the dropdown
   - Available models depend on your instance's provider connections
5. Write a system prompt
   - This defines how the model responds. See the Design Kit for prompt-writing guidance
6. Click **Save**
```

Add a GIF placeholder after multi-step procedures:

```markdown
![Creating your first model](images/create-model.gif)
<!-- TODO: Record GIF of model creation flow -->
```

## Pedagogical Framing

Lead with the teaching scenario. Then explain the feature. Then walk through the steps.

**Pattern:**

> **Scenario:** You want students to discuss assigned readings without the AI fabricating citations or drawing on outdated training data.
>
> **Solution:** Knowledge bases let you upload your syllabus, course readings, and institutional policies. When students ask questions, the AI searches your materials first.
>
> **How to set it up:** [numbered steps]

## Multimedia Strategy

- **GIFs** for multi-step UI workflows (creating a model, uploading documents, binding tools)
- **Screenshots** for static reference states (settings panels, completed configurations)
- **Embedded examples** (sample prompts, template text, policy language)
- **External links** for depth (research papers, workshop materials, official docs)

Always include alt text. Use placeholder syntax when images aren't yet captured.

## Progressive Disclosure

Layer information so readers can stop when they have what they need:

1. **Overview** (what this is, why it matters) - always present
2. **Quick Start** (minimum steps to get going) - for most readers
3. **Deep Dive** (detailed procedures and configuration) - for builders
4. **Advanced** (edge cases, customization, pipelines) - for power users
5. **Further Reading** (external resources, research) - for the curious

## CUNY Context

Ground documentation in CUNY's institutional reality:

- Reference CUNY's diverse student body when discussing accessibility and multilingual support
- Connect features to CUNY's academic integrity standards
- Link to Teach@CUNY resources where relevant
- Acknowledge that instructors balance teaching, research, and service
- Use realistic examples from CUNY disciplines (composition, digital humanities, social work, public health)

## Calibration Checklist

For each page, verify:

- [ ] Contextual framing before technical details
- [ ] Active voice throughout
- [ ] Short paragraphs (2-4 sentences)
- [ ] Procedural steps numbered with sub-bullet rationale
- [ ] "Model Uses" separated from "Feature Suggestions" where applicable
- [ ] Visual placeholders with alt text
- [ ] Cross-links to related pages
- [ ] "Additional Resources" section with 2-3 external links
- [ ] Navigation footer (← Previous / Continue →)
- [ ] CUNY-specific context where appropriate
- [ ] No AI slop vocabulary
- [ ] No em dashes

## Reference Files

- `references/page-template.md` - Full page template with all sections
- `references/voice-examples.md` - Before/after transformations showing voice calibration
- `references/toolkit-patterns.md` - Key patterns extracted from Discord and AI Toolkit exemplars
