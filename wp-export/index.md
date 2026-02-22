# CUNY AI Lab Sandbox Documentation

**Platform:** Open WebUI  
**Access:** [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu)

This guide explains how to use workspace features on the CUNY AI Lab Sandbox — a shared AI infrastructure for CUNY faculty, students, and researchers.

---

## What is Open WebUI?

Open WebUI is a self-hosted AI platform that works offline and supports multiple model providers (Ollama, OpenAI, and others). Unlike simple chat interfaces, it offers workspace features that let you:

- Create custom AI agents with specific behaviors
- Build knowledge bases from institutional documents
- Extend AI capabilities with tools and integrations
- Share configurations across research groups or courses

The Sandbox gives CUNY users access to these features through a centralized instance at the Graduate Center.

---

## Getting Started

### First Steps

1. **Log in** to [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu) with your CUNY credentials
2. **Explore existing models** — several pre-configured models are available for common tasks
3. **Access Settings** via your profile avatar (top-right) to customize your experience

### Settings Overview

Open WebUI has two settings areas:

- **User Settings** (Profile > Settings) — your personal preferences, default model, interface theme
- **Admin Settings** (Admin Panel > Settings) — instance-wide configuration (faculty/admin only)

---

## Core Workspace Features

### 1. Models

**What they do:** Models are configuration wrappers around base AI models. You can create custom agents by defining their behavior, attaching knowledge, and binding tools.

**How to use:**

1. Go to **Workspace > Models**
2. Click **+ New Model**
3. Configure the following:
   - **Base Model:** Select from available models (GPT-4, Claude, Llama, etc.)
   - **System Prompt:** Define how the model behaves
   - **Advanced Parameters:** Adjust temperature, stop sequences, etc.
   - **Prompt Suggestions:** Add starter prompts that appear above the input

**Dynamic Variables:** Use Jinja2 placeholders in system prompts:
- `{{ CURRENT_DATE }}` — today's date (YYYY-MM-DD)
- `{{ CURRENT_TIME }}` — current time (24-hour format)
- `{{ USER_NAME }}` — logged-in user's display name

**Example System Prompt:**
```
You are an academic assistant for {{ USER_NAME }}. The current date is {{ CURRENT_DATE }}. You support research and learning at CUNY. Prioritize clarity and educational value. Encourage critical thinking rather than providing direct answers to assignments.
```

**Switching Models Mid-Chat:**  
Click the model name in the chat interface to switch between models during a conversation. Use different models for different tasks (e.g., general reasoning → visual analysis → synthesis).

---

### 2. Knowledge Collections (RAG)

**What they do:** Knowledge Collections enable Retrieval-Augmented Generation (RAG) — the AI retrieves relevant information from uploaded documents before generating responses. This grounds responses in institutional data rather than relying solely on training data.

**How to use:**

1. Go to **Workspace > Knowledge**
2. Click **+ Create a Knowledge Base**
3. Specify:
   - **Name:** e.g., "CUNY Graduate Handbook"
   - **Purpose:** What you're trying to achieve
   - **Visibility:** Private, Limited (shared with specific users), or Public
4. **Upload files** (drag-and-drop or browse) — supports PDF, Markdown, plain text
5. **Bind to models** — attach the knowledge base when creating/editing a model

**Centralized File Manager:**  
Access via **Settings > Data Controls > Manage Files** to search all uploaded files, sort by name/date, and view metadata. Deleting a file removes it from all knowledge bases and cleans up vector embeddings.

**Embedding Models:**  
Configure via **Admin Panel > Settings > Documents > Embedding Model**. The default (Sentence Transformers MiniLM) works well for most use cases. Embeddings convert documents into numerical representations for semantic search.

**RAG Template:**  
Defines how retrieved information is presented to the model. Configure via **Admin Settings > Documents > RAG Template**. Specify task instructions, citation formats, and output characteristics.

---

### 3. Tools

**What they do:** Tools extend AI capabilities beyond text generation — web scraping, API calls, computations, media search, database queries, etc.

**Types of Tools:**

- **Native Features:** Built-in (Web Search, Image Generation, URL Fetch, Memory)
- **Workspace Tools:** Python scripts running in Open WebUI
- **MCP (Model Context Protocol):** Anthropic's standard for connecting external data/tools
- **OpenAPI Servers:** Generic web services via OpenAPI specs

**How to use:**

- **Per-chat:** Click the **➕** icon in the input area and select tools for that session
- **Per-model:** Go to **Workspace > Models**, edit a model, scroll to **Tools**, and check the tools you want always available

**Community Tools:**  
Browse the **Community Tool Library** for pre-built tools:
- arXiv Search (academic papers, no API key needed)
- Perplexica Search (web search with citations)
- Pexels Media Search (stock photos/videos)
- YouTube Search & Embed

**Security:** Only import tools from trusted sources. Tools are Python scripts that execute on the server.

---

### 4. Skills

**What they do:** Skills are specialized knowledge domains that can be bound to models without modifying system prompts. They provide on-demand access to comprehensive instructions.

**How to use:**

1. Go to **Workspace > Models > Edit**
2. Navigate to the **Skills** section
3. Bind skills to the model

When enabled, skill manifests are injected into the model context, and the model can load full skill instructions via the `view_skill` built-in tool.

**Example Skills for CUNY:**
- Quantitative Methods (statistical analysis, research design)
- Academic Writing (scholarly writing, citation practices)
- Research Ethics (IRB compliance, data privacy)
- Digital Humanities (text analysis, visualization)

---

## Practical Use Cases

### Literature Review Assistant

**Components:**
- System prompt guiding systematic review methodology
- Knowledge base with foundational papers in the field
- Tools for academic database access (arXiv, PubMed)
- Skills for research methodology and qualitative analysis

**Workflow:** Ask the AI to summarize theoretical evolution across recent research. It retrieves papers from the knowledge base, searches external databases, identifies patterns, and synthesizes findings.

---

### Capstone Project Mentor

**Components:**
- System prompt establishing course learning outcomes
- Knowledge base with disciplinary literature and past student projects
- Tools for assignment submission and resource access
- Skills for project management, research ethics, and methodology

**Workflow:** Students interact throughout the semester for consistent guidance grounded in institutional expectations and disciplinary norms.

---

### Multilingual Research Support

**Components:**
- Knowledge base with sources in multiple languages
- Translation tools
- Language-specific analysis skills
- Multilingual prompting

**Workflow:** Pose queries in your native language, receive responses synthesizing across-language sources, and access translations supporting deeper engagement with original texts.

---

## Advanced Features

### Pipelines

**What they do:** Pipelines intercept and transform LLM interactions at multiple stages.

**Types:**
- **Filter Pipelines:** Intercept requests/responses (RAG integration, safety filtering)
- **Pipe Pipelines:** Complete takeover of interaction workflows (new providers, agent workflows)

**Use cases:** Custom RAG systems, prompt injection filtering, safety checks (LlamaGuard), institutional compliance enforcement.

---

### Function Calling

Models with native function calling (indicated by the **TOOLS** tag in Ollama models) can invoke tools with improved reliability. The model determines when to call a tool, what arguments to pass, and how to incorporate results — no prompt engineering required.

---

## Security & Governance

### Role-Based Access Control (RBAC)

Administrators create user roles, groups, and permissions. Example roles at CUNY:
- **Faculty:** Create/modify models used across courses
- **Graduate Students:** Create knowledge bases for research groups
- **Undergraduates:** Access institutional resources (view-only)

### SCIM 2.0 Provisioning

Integration with identity providers (Okta, Azure AD, Google Workspace) for automated user lifecycle management. User roles sync across systems.

### Memory

Models can remember facts and preferences across conversations. Memories are:
- Stored locally in your Open WebUI account
- Never shared across users
- Clearable at any time via Settings

### File Management Security

Deleting files removes them from all knowledge bases and deletes vector embeddings. Administrators should establish:
- Backup/recovery procedures for critical knowledge bases
- Retention policies for institutional documents
- Audit logs tracking access and modifications

---

## Monitoring & Observability

### Production Observability (OpenTelemetry)

Built-in instrumentation for monitoring with traces, metrics, and logs. Export to Prometheus, Grafana, Jaeger. Track:
- Most-used models
- Knowledge base query volume
- Computational resource usage

### Message Monitoring (Langfuse)

Analyze conversation patterns in real-time:
- Which models support productive learning interactions
- Which knowledge bases receive highest engagement
- Where users encounter confusion or need support

---

## Best Practices

### For Faculty

- **Craft system prompts** that reflect institutional values and academic integrity standards
- **Organize knowledge bases** around course materials, research protocols, or departmental resources
- **Use prompt suggestions** to guide students toward the model's capabilities
- **Review model configurations** periodically to align with emerging pedagogical insights

### For Students

- **Understand model limitations** — AI assists learning but doesn't replace critical thinking
- **Cite AI contributions** appropriately in academic work
- **Use knowledge bases** to explore institutional resources and disciplinary literature
- **Switch models mid-chat** to leverage different strengths for different tasks

### For Researchers

- **Create specialized models** for literature review, methodology support, and data analysis
- **Build knowledge bases** from curated research outputs and methodological frameworks
- **Develop custom tools** for domain-specific workflows (database queries, computational methods)
- **Maintain rigor and transparency** — document how AI systems support your research process

---

## Getting Help

- **Documentation:** [This guide]
- **Community:** [CUNY AI Lab Discord/Slack channel]
- **Technical Support:** [Contact info for CUNY AI Lab administrators]
- **Governance Questions:** Contact the Governance Steering Committee

---

## Recommended Implementation Phases

### Phase One: General-Purpose Models
Start with general-purpose models bound to institutional knowledge bases. All users can access AI grounded in CUNY's context.

### Phase Two: Discipline-Specific Models
Introduce discipline-specific models and knowledge bases as academic units develop configurations.

### Phase Three: Advanced Research Support
Establish fully-integrated workflows for specific projects, demonstrating the potential of combined models, knowledge, tools, and skills.

---

## Resources

- **Open WebUI Documentation:** [Official docs link]
- **Model Context Protocol (MCP):** [Anthropic MCP spec]
- **CUNY Academic Commons:** [Commons link]
- **CUNY AI Community Engagement Lab:** [Lab link]

---

*Last updated: February 2026*
