# Custom Models

Building custom AI models using preset configurations in Open WebUI. A custom model lets you shape how the AI behaves in your course, what documents it draws from, and which tools it can use. You are not training a new AI from scratch. You are assembling existing components into something tuned to your teaching context.

## Why This Matters

A base model answers questions from its general training data. That data may be outdated, incomplete, or irrelevant to your discipline. A custom model lets you define the boundaries: what the AI should do, what it should refuse to do, and what materials it should draw from when responding.

## Creating a Model

Here's how to build a custom model:

1. Click **Workspace** in the left sidebar
2. Select **Models**
3. Click **+ New Model**
   - This opens the model editor. You will define the model's behavior, connect it to your documents, and choose which tools it can access.
4. Choose a **base model** from the dropdown
   - The available models depend on which providers your Sandbox is connected to. If you need a specific model and do not see it listed, contact the AI Lab team.
5. Write a **system prompt** (see below for guidance)
6. Attach **knowledge bases** if you want the model to draw from your documents
   - See [Knowledge Bases](knowledge-bases.md) for how to create one
7. Bind **tools** if you want the model to search the web, run code, or access other services
   - See [Tools & Skills](tools-skills.md) for available options
8. Add **prompt suggestions**
   - These appear as clickable chips above the input bar when students open a new chat. They show users what the model can do and how to talk to it.
9. Set **visibility**
   - **Private**: only you can use it
   - **Limited**: shared with specific users or groups (e.g., your course section)
   - **Public**: available to all Sandbox users
10. Click **Save**

![Creating a custom model](images/create-model.gif)
<!-- TODO: Record GIF of the model creation flow from Workspace → Models → + New Model → Save -->

## Writing System Prompts

The system prompt defines how the model behaves: its role, boundaries, and instructional approach. A good prompt establishes what the model will and won't do, with enough specificity that students know what kind of help to expect.

<details>
<summary>View example prompt</summary>

Here is an example for a data analysis model:

```
You support {{ USER_NAME }} in analyzing datasets for {{ COURSE_TITLE }}.
The current date is {{ CURRENT_DATE }}. When a student shares data,
guide them through: (1) identifying variables and measurement scales,
(2) selecting appropriate visualizations, (3) choosing statistical
methods, and (4) interpreting results. Ask questions that help them
understand *why* a method fits their data. Do not generate complete
analysis reports. Point to course materials when relevant concepts appear.
```

</details>

Learn more about drafting system prompts [at this link](system-prompts.md).

### Prompt Suggestions

Prompt suggestions are the clickable chips that appear when a user opens a fresh chat. They serve as onboarding: a quick way to show students what the model can do. For a data analysis model:

- "What visualization works best for this data?"
- "Help me interpret these statistical results"
- "Which test should I use for this research question?"

For a methods guidance model:

- "Compare qualitative and quantitative approaches for my study"
- "What sampling strategy fits my research design?"
- "How do I address potential confounding variables?"

## Advanced Settings

### Advanced Parameters

Most instructors will not need to adjust these. They are here for users who want finer control over how the model generates responses.

- **Max Tokens** sets the maximum length of the model's response. One token is roughly three-quarters of a word. Lower values (100-500) produce concise answers: useful for quick definitions or focused feedback. Higher values (1000-4000) allow detailed explanations: appropriate for essay analysis or research summaries. If responses cut off mid-sentence, increase this value.
- **Temperature** controls randomness. Lower values (0.1 to 0.3) produce focused, deterministic responses: good for factual research tasks. Higher values (0.7 to 1.0) allow more creative variation: useful for brainstorming or creative writing activities.
- **Top P** (nucleus sampling) controls the diversity of word selection. A value of 0.9 means the model considers words covering 90% of the probability mass. Leave this at default unless you have a specific reason to change it.
- **Stop Sequences** force the model to stop generating when it encounters specific text strings. Enter sequences like `<|end_of_text|>` or `User:` and press Enter. Useful for models that might otherwise generate both sides of a conversation.

### Switching Models Mid-Chat

You can change models during a conversation by clicking the model name at the top of the chat. The conversation context carries across the switch. This lets you use different models for different stages of a task: start with a general-purpose model for brainstorming, switch to a code-focused model for implementation, then move to a writing model for documentation.

> **Tip:** Encourage students to experiment with model switching. Different models have different strengths. A model optimized for close reading will give different results than one designed for quantitative analysis. Learning when to switch is part of developing AI literacy.

## Callout

<div class="callout">
  <strong>For instructors:</strong> When building models for your courses, make your expectations for AI use explicit in the system prompt. If the model should refuse to generate complete assignments, encode that boundary. If it should encourage process over product, say so directly. Students benefit from clarity about what the tool will and will not do. Vague instructions produce vague behavior.
</div>

## Additional Resources

- [Open WebUI Model Configuration Docs](https://docs.openwebui.com) — official reference for all model settings
- [Teach@CUNY AI Toolkit: Course Policies](https://aitoolkit.commons.gc.cuny.edu/course-policies/) — guidance on setting expectations for AI use in your courses
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) — OpenAI's strategies for writing effective prompts

---

[← Return to Getting Started](getting-started.md) | [Continue to Knowledge Bases →](knowledge-bases.md)
