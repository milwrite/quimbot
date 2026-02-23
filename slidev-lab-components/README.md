# ConfigPanel Integration Guide

## Overview

`ConfigPanel.vue` is a side panel component for Slidev that provides a visual interface for building and editing LLMQuery-powered slides in real-time.

## Features

- **Builder Tab**: Edit current slide (title, content, model, position, prompts)
- **Templates Tab**: Insert pre-built slide templates (Code Review, Multi-Model Compare, Educational Q&A)
- **Export Tab**: Export slides as markdown or JSON config, import existing configs

## Installation

### 1. Copy Component

```bash
cp ConfigPanel.vue ~/Quimbot/slidev-lab/components/
```

### 2. Add to Slidev Layout

Edit `slides.md` and add the component at the top:

```markdown
---
layout: cover
---

<ConfigPanel />

# Your Presentation Title

<!-- rest of slides -->
```

Or create a custom layout in `layouts/` that includes it globally.

### 3. Usage

- **Toggle Panel**: Click the gear icon (⚙️) or press `Ctrl+K`
- **Add Slides**: Use the "+ Add Slide" button in Builder tab
- **Apply Templates**: Click any template in Templates tab to insert it after current slide
- **Export**: Use Export tab to save slides.md or config.json

## Keyboard Shortcuts

- `Ctrl+K` - Toggle config panel
- `←` `→` - Navigate slides (when in Builder tab)

## State Persistence

The component stores slide config in reactive state. To persist across sessions:

1. Export `config.json` before closing
2. Import `config.json` on next session
3. Or auto-sync to localStorage (add in future phase)

## Extending Templates

Edit the `templates` array in `ConfigPanel.vue` to add custom slide templates:

```javascript
{
  id: 'your-template',
  name: 'Template Name',
  description: 'What it does',
  template: {
    type: 'custom-type',
    title: 'Default Title',
    content: 'Default markdown content',
    llmQuery: {
      model: 'openai/gpt-4.1-mini',
      position: 'top-right',
      systemPrompt: 'Your system prompt',
      autoPrompt: 'Optional auto-prompt',
      autoExecute: false
    }
  }
}
```

## Next Steps (Phase 2)

- [ ] Drag-drop slide reordering
- [ ] Undo/redo
- [ ] localStorage auto-save
- [ ] Multi-model template builder (auto-create 4-corner layouts)
- [ ] Live preview pane
- [ ] Theme customization

## Integration with LLMQuery

The panel generates markdown that wraps content in `<LLMQuery>` tags. Ensure `LLMQuery.vue` is installed in `components/` and OpenRouter API key is set in `.env`:

```bash
VITE_OPENROUTER_API_KEY=your-key-here
```

## Troubleshooting

**Panel doesn't appear:**
- Check that `ConfigPanel.vue` is in `components/` directory
- Verify component is included in a slide or layout
- Check browser console for Vue errors

**Markdown export missing attributes:**
- Ensure all required fields are filled (title, model, position)
- Check that `llmQuery` object exists for each slide

**Templates not inserting:**
- Click the template card (entire card is clickable)
- Check that `currentSlideIndex` is valid
- Verify `config.slides` array is populated
