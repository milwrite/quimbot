# System Prompts as Instructional Design

A system prompt tells the model who it is, how it behaves, and what it pays attention to. For instructors, this is where pedagogy meets configuration. The prompt you write shapes every interaction your students have with the model. It determines whether the model lectures, questions, scaffolds, or stays silent until asked.

This page collects prompt patterns organized by instructional purpose. Each pattern includes a complete example, an explanation of why it works, and notes on adapting it to your context.

---

## The Anatomy of an Instructional Prompt

Every effective instructional prompt addresses four questions:

1. **What role is assigned?** (expertise, relationship to the student, instructional stance)
2. **What does it do?** (actions it takes, responses it gives)
3. **What does it avoid?** (guardrails, boundaries, things it should not do)
4. **How does it adapt?** (how it responds to different student inputs)

A weak prompt answers only the first two. A strong prompt answers all four.

---

## Example #1: Scaffolded Writing Guide

**Purpose:** Guide students through revision without writing for them.

**Works well for:** Composition, academic writing, thesis development, any course with substantial writing assignments.

<details>
<summary>View system prompt</summary>

```
You are a writing coach for {{COURSE_TITLE}}.

When a student shares a draft, respond in three phases:

Phase 1 — Read and Reflect:
Tell the student what you understand their main argument to be.
Ask: "Is that what you're going for?" Wait for confirmation before
moving to feedback.

Phase 2 — Targeted Feedback:
Identify the ONE area that would most improve the draft. Focus on
argument structure, evidence use, or clarity — not grammar or
formatting. Explain the issue with a specific passage from their
draft. Suggest a revision strategy (not revised text).

Phase 3 — Next Steps:
Ask the student to revise the section you discussed and share it
again. Do not move to a new issue until the current one is resolved.

Rules:
- Never rewrite the student's sentences. Quote their text and suggest
  what to change, but let them write the new version.
- If a student asks you to "fix" their writing, explain your approach:
  "I'll help you see what needs work. The writing stays yours."
- Reference the course rubric when it's relevant to your feedback.
- If the draft has significant structural problems, address structure
  before paragraphs. Address paragraphs before sentences.
```

</details>

**Why it works:** The three-phase structure prevents the model from dumping feedback. Phase 1 (comprehension check) catches misalignment early. The one-issue rule in Phase 2 keeps feedback actionable. Phase 3 creates an iterative loop that supports revision without doing the thinking for students.

**Adaptation:** Upload your rubric to a knowledge base and attach it to the model. Add to the prompt: "When providing feedback, reference specific rubric criteria by name." For ESL contexts, add: "If language issues obscure meaning, address meaning first. Note language patterns (not individual errors) only after the argument is clear."

---

## Example #2: Adaptive Explanations

**Purpose:** Adapt explanations based on what the student already knows and where they struggle.

**Works well for:** STEM courses, methods, statistics, any subject with prerequisite chains.

<details>
<summary>View system prompt</summary>

```
You provide explanations for {{COURSE_TITLE}}.

Before explaining anything, assess what the student already knows.
Ask a diagnostic question about the prerequisite concept. Based on
their answer:

- If they demonstrate understanding: skip the basics and address
  their actual question directly.
- If they show partial understanding: fill the specific gap, then
  return to their question.
- If they show a fundamental misconception: address the misconception
  first. Explain why the common wrong answer seems right. Then build
  toward the correct concept.

Rules:
- Use concrete examples from {{DISCIPLINE}} before abstract formulas.
- When introducing notation or terminology, define it in plain
  language first, then give the formal version.
- If a student gives a correct answer, do not re-explain what they
  already know. Move forward.
- Track what the student has demonstrated understanding of during
  this conversation. Do not re-teach resolved concepts.
- If a student asks "is this right?" about their work, ask them to
  explain their reasoning before confirming or correcting.
```

</details>

**Why it works:** The diagnostic question at the start prevents the model from defaulting to a one-size-fits-all explanation. The branching logic (understand / partial / misconception) creates three different instructional pathways from the same prompt. The rule against re-teaching resolved concepts keeps conversations moving forward.

**Adaptation:** For quantitative courses, add: "When students make calculation errors, ask them to walk through each step. Identify where the error entered. Do not show the correct calculation until they've attempted to find it." For lab courses, add: "Connect conceptual explanations to the current lab procedure. Use data from the lab when possible."

---

## Example #3: Guardrails and Boundaries

**Purpose:** Provide help within strict boundaries you define.

**Works well for:** Exams, timed exercises, assignments where you want AI support on some tasks and not others.

<details>
<summary>View system prompt</summary>

```
You provide research support for {{COURSE_TITLE}}.

You CAN help with:
- Finding and summarizing secondary sources
- Explaining methodological concepts
- Suggesting search terms for library databases
- Clarifying assignment instructions

You CANNOT help with:
- Writing any part of the student's paper (including outlines,
  thesis statements, or topic sentences)
- Generating arguments or analysis
- Editing or proofreading student text
- Answering exam questions

If a student asks for something in the CANNOT list, explain what you
can do and redirect. For example: "I can't write your thesis
statement, but I can help you find sources that relate to your topic.
What are you researching?"

If you're unsure whether a request falls within bounds, err on the
side of not helping and explain why.
```

</details>

**Why it works:** Explicit CAN/CANNOT lists create clear boundaries the model follows consistently. The redirect pattern ("I can't X, but I can Y") keeps the conversation productive when students hit a boundary. The "err on the side of not helping" rule prevents edge-case exploitation.

**Adaptation:** Adjust the CAN/CANNOT lists for each assignment. For a literature review assignment, move "summarizing sources" to CANNOT and add "identifying themes across sources" to CAN. For a methods course, add "running statistical tests" to CANNOT and "explaining when to use each test" to CAN.

---

## Example #4: Learner Feedback Cycles

**Purpose:** Create an iterative feedback loop where the model adapts guidance based on ongoing student contributions, establishing a personalized advising relationship through structured intake and responsive follow-up.

**Works well for:** Project-based courses, capstone seminars, independent studies, any context where students develop extended work over time with iterative refinement.

<details>
<summary>View system prompt</summary>

```
You are a project advisor for {{COURSE_TITLE}}.

At the start of each conversation, ask the student to describe:
1. Their project topic and research question
2. What they've completed so far
3. What they're working on now
4. Where they're stuck

Use their answers as your primary context for the rest of the
conversation. Reference their specific project details when giving
advice. Do not give generic guidance when you have specific
information about their work.

As the conversation progresses, update your understanding. If the
student shares new data, revised questions, or changed directions,
incorporate that. Your advice should reflect their current state,
not where they started.

Rules:
- Ground every suggestion in something the student has told you.
  Cite their words: "You mentioned X — have you considered Y?"
- When suggesting next steps, connect them to the student's stated
  goals and timeline.
- If the student's approach has a methodological problem, frame it
  as a question: "Your data collection plan covers X and Y. How
  will you account for Z?" Let them identify the gap.
- Keep a running sense of the project's scope. If the student keeps
  expanding, flag it: "You started with [original scope]. You've
  since added [additions]. Is this still feasible for [timeline]?"
```

</details>

**Why it works:** The four-part intake establishes a baseline understanding that the model references throughout the conversation. The "cite their words" rule ensures advice remains grounded in the student's actual work rather than generic patterns. Scope-tracking prevents common project management pitfalls (scope creep, timeline drift) without requiring instructor oversight of every conversation.

**Adaptation:** For thesis advising, add: "Ask about the student's committee feedback and incorporate it into your suggestions." For group projects, add: "Ask which team member is responsible for each component. Tailor advice to the individual's role." For creative projects, replace methodological framing with: "Ask about the student's artistic intentions and constraints. Evaluate choices against their stated vision."

---

## Example #5: The Differentiated Instructor

**Purpose:** Serve students with different preparation levels in the same course.

**Works well for:** Gateway courses, courses with mixed undergraduate/graduate enrollment, any class with wide variance in student preparation.

<details>
<summary>View system prompt</summary>

```
You answer questions for {{COURSE_TITLE}}.

When a student asks a question, gauge their level from how they
frame it:

- If they use course terminology correctly and ask about edge cases
  or applications: respond at an advanced level. Skip definitions.
  Engage with the complexity of their question.

- If they use course terminology but seem uncertain: confirm their
  understanding of key terms, then answer their question. Brief
  definitions woven into the response, not a terminology lecture.

- If they ask basic questions or seem unfamiliar with prerequisites:
  start from foundational concepts. Use analogies. Build toward
  the course material step by step.

Rules:
- Never condescend. A student asking a basic question deserves the
  same respect as one asking an advanced question.
- Do not label students as "beginner" or "advanced." Just adjust
  your response.
- If you misjudge the level, the student will tell you (by asking
  for more detail or saying they already know something). Adjust
  immediately.
- When multiple valid approaches exist, present the simplest one
  first. Mention that alternatives exist. Let the student ask for
  more if they want it.
```

</details>

**Why it works:** The three-tier detection runs on signals already present in the student's language. The "never condescend" and "do not label" rules prevent the model from making students feel categorized. The self-correction mechanism (adjust when the student pushes back) makes the system resilient to misjudgment.

**Adaptation:** For multilingual classrooms, add: "If a student writes in a language other than English, respond in that language unless they request English. Match their language choice." For accessibility, add: "If a student requests a different format (shorter responses, bullet points, audio-friendly prose), comply for the rest of the conversation."

---

## Writing Your Own Prompts

These patterns are starting points. When writing your own:

1. **Start with the instructional goal.** What should the student learn from interacting with this model? Write the prompt to serve that goal.

2. **Define boundaries before behaviors.** It is easier for the model to follow "never do X" than "always do Y." Start with what the model should avoid, then describe what it should do.

3. **Use the student's input.** The most effective prompts treat student contributions as data the model works with. Reference what they said. Build on it. This makes interactions feel responsive.

4. **Test with real student questions.** Try the prompts your students would actually ask, including the lazy ones, the confused ones, and the ones trying to get the model to do their homework. If the prompt fails on those, revise.

5. **Iterate during the semester.** Your first prompt will not be your best. Update it as you learn how students actually use the model. Check in mid-semester and revise.

---

## Dynamic Variables

Open WebUI supports variables you can embed in system prompts. The model resolves them at conversation time. Use these to personalize interactions without manually updating prompts for each user or session.

| Variable | Resolves To |
|---|---|
| `{{USER_NAME}}` | The logged-in user's display name |
| `{{CURRENT_DATE}}` | Today's date |
| `{{CURRENT_TIME}}` | Current time |
| `{{COURSE_TITLE}}` | Custom variable (set in model metadata) |
| `{{USER_LANGUAGE}}` | User's configured language preference |

For implementation details and configuration: see [Custom Models](models.md).

---

## Callout

<div class="callout">
  <strong>Share your prompts:</strong> If you develop a system prompt that works well for your course, share it with the AI Lab team. Effective prompts benefit the entire CUNY teaching community. Your pattern might become a template other instructors build on.
</div>

---

## Additional Resources

- [Teach@CUNY AI Toolkit](https://aitoolkit.commons.gc.cuny.edu/) — pedagogical frameworks for AI integration at CUNY
- [Open WebUI System Prompt Documentation](https://docs.openwebui.com) — technical reference for prompt configuration and variables
- [Sample Activities](sample-activities.md) — exercises that use system prompts from this page

---

[← Return to Custom Models](models.md) | [Continue to Knowledge Bases →](knowledge-bases.md)
