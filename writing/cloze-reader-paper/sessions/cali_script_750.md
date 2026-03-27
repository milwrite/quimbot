# CALI T(h)inkering Track — 750-word version

The third track is T(h)inkering. The name carries a parenthetical "h" because tinkering and thinking are, for us, the same act approached from different angles. One side poses a question: where do these tools break, how do they work, and on whose terms do they operate? The other side responds by building — translating a scholarly or pedagogical question into something you can test, configure, and iterate on. Critical making, not critique alone.

This track invites you to consider what a discipline-specific AI tool could do for your teaching, and what the act of building one might teach you about the technology itself. That pairing of inquiry and construction is what distinguishes t(h)inkering from general AI literacy: you don't stop at analysis. You make something, and the making becomes a form of knowing.

The clearest illustration of this is AmigAI. In year one of the Institute, instructors teaching heritage and non-native Spanish classes came to us with a concrete problem. Consumer AI tools — including the most widely used commercial platforms — flatten dialect-specific Spanish. Out of the box, a model corrects toward a standardized register and away from the specific varieties of Spanish that their students actually speak and write, often the very varieties those instructors are trying to affirm and build on. This isn't incidental. It reflects the composition of the training data, the defaults of the system prompts, and decisions made by developers who weren't designing for multilingual communities at CUNY.

Working directly with those instructors over the course of the year, we built AmigAI: a conversation partner configured to hold space for the Spanish students bring into the classroom. That project required the instructors to get technically specific — not just to say "the model is biased" but to trace where the flattening happens, what parameters control it, and what it takes to push back. Building AmigAI was a form of critical analysis that produced something usable. It is now in active use across several CUNY courses, and it remains a running collaboration between the Lab and the instructors who continue to shape it.

AmigAI also pushed us to build dedicated infrastructure. The CUNY AI Lab is a standalone extension of the Institute, providing safe and secure shared access to large language models and the tools built on and around them.

**The Sandbox** is an Open WebUI instance we host and configure ourselves. Faculty and students access a range of open-weight models — small ones on our own hardware, larger frontier models hosted externally — through a single interface. You can compare models side by side, write system prompts, adjust parameters, export transcripts for documentation, and share preset configurations the way you'd share an open educational resource. Consumer platforms hide those design decisions. The Sandbox makes them visible and available for collective scrutiny.

**The tools suite** at tools.ailab.gc.cuny.edu covers audio transcription (Whisper, running locally — nothing leaves our servers), image description, OCR for scanned and handwritten documents, Agent Studio (describe what you want in plain language; an agent writes and executes visible Python code to analyze your data), and Site Studio for building and publishing project websites directly from the platform. Each tool does one thing, runs on open models, and keeps your data on our infrastructure.

Together these resources support critical making: using AI as a coding scaffold, a research assistant, and an object of study simultaneously. The infrastructure is there to be configured, tested against, and pushed.

---

I'd like to give a warm welcome to the participants who applied to this track and to the projects they're bringing into it:

- **Katharine Chen** — Research Writing Scaffold
- **Chantale Damas** — Laboratory Workflow Tool
- **Agustina Checa** — Deep Listening Tool
- **Virginia Thompson** — Interdisciplinary Math Connections
- **Maria Mavrides Calderon** — Systems and Assets Mapping Tool

These projects each begin where good disciplinary work begins: with a problem that the existing tools don't solve, and a question about whether a purpose-built tool might. We'll work through that together over the course of the year.

For everyone else in the room: this infrastructure isn't exclusive to this track. If you're working in Ecological Implications or Critical Foundations and there's a dataset you want to analyze, a transcription workflow you need, a model you'd like to test against your syllabi or your students' writing — reach out. Give me a holler. The Lab is here for all of it.
