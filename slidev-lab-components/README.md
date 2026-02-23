# ConfigPanel Integration Guide

## Overview

`ConfigPanel.vue` is a side panel component for Slidev that provides a visual interface for building and editing LLMQuery-powered slides in real-time.

## Features

- **Builder Tab**: Edit current slide (title, content, model, position, prompts)
- **Templates Tab**: Insert pre-built slide templates (Code Review, Multi-Model Compare, Educational Q&A)
- **Export Tab**: Export slides as markdown or JSON config, import existing configs
- **Settings Tab**: Auto-sync configuration, presentation settings, defaults
- **Auto-Sync**: Real-time sync from ConfigPanel → config.json → slides.md

## Installation

### 1. Copy Components

```bash
cp ConfigPanel.vue ~/Quimbot/slidev-lab/components/
cp config-sync.mjs ~/Quimbot/slidev-lab/
chmod +x ~/Quimbot/slidev-lab/config-sync.mjs
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
- **Delete Slides**: Red "Delete" button (can't delete last slide)
- **Apply Templates**: Click any template in Templates tab to insert it after current slide
- **Export**: Use Export tab to save slides.md or config.json
- **Auto-Sync**: Enable in Settings tab + run `node config-sync.mjs --watch`

## Auto-Sync Workflow (Phase 2)

ConfigPanel can automatically sync changes to `slides.md` using the companion script:

### 1. Enable Auto-Sync

1. Open ConfigPanel (press `Ctrl+K`)
2. Go to Settings tab
3. Check "Auto-sync to config.json"

This will automatically download `config.json` whenever you make changes (500ms debounce).

### 2. Run Sync Script

In a separate terminal, run the sync script in watch mode:

```bash
cd ~/Quimbot/slidev-lab
node config-sync.mjs --watch
```

This will:
- Watch for `config.json` changes
- Auto-regenerate `slides.md` whenever config updates
- Trigger Vite HMR to reload the presentation

### 3. Make Changes

Now any changes in the ConfigPanel will flow through automatically:
1. Edit slide in ConfigPanel
2. config.json auto-downloads (500ms after last edit)
3. Move downloaded config.json to slidev-lab directory
4. config-sync.mjs detects change and regenerates slides.md
5. Vite HMR reloads presentation with new content

### Manual Sync (Alternative)

If you prefer manual control:

1. Keep auto-sync disabled in Settings
2. Edit slides in ConfigPanel
3. Export config.json when ready (Export tab)
4. Run one-time sync: `node config-sync.mjs`
5. Reload Slidev manually

## Two-Way Sync (Phase 3 - Future)

Future implementation will support:
- Parse existing slides.md on ConfigPanel load
- Filesystem watcher for external changes to slides.md
- Conflict detection (manual edit vs ConfigPanel edit)
- Merge strategies with user prompts
- Bidirectional sync: ConfigPanel ↔ slides.md

## Keyboard Shortcuts

- `Ctrl+K` - Toggle config panel
- `←` `→` - Navigate slides (when in Builder tab)

## State Persistence

The component stores slide config in reactive state. To persist across sessions:

1. Export `config.json` before closing (Export tab)
2. Import `config.json` on next session (Export tab)
3. Or enable auto-sync (Settings tab) and let config-sync.mjs handle it

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

For multi-model templates, add `extraModels` array:

```javascript
{
  id: 'multi-model-custom',
  name: 'Custom 4-Model Compare',
  description: 'Compare 4 models on one slide',
  template: {
    type: 'multi-model',
    title: 'Model Comparison',
    content: 'Your question or content here',
    llmQuery: {
      model: 'openai/gpt-4.1-mini',
      position: 'top-left',
      systemPrompt: 'System prompt for GPT',
      autoPrompt: '',
      autoExecute: false
    },
    extraModels: [
      { model: 'anthropic/claude-sonnet-4', position: 'top-right', systemPrompt: '...', autoPrompt: '', autoExecute: false },
      { model: 'google/gemini-2.5-pro', position: 'bottom-left', systemPrompt: '...', autoPrompt: '', autoExecute: false },
      { model: 'x-ai/grok-4', position: 'bottom-right', systemPrompt: '...', autoPrompt: '', autoExecute: false }
    ]
  }
}
```

## Phase Roadmap

### Phase 1 ✅ (Complete)
- [x] ConfigPanel.vue with Builder/Templates/Export tabs
- [x] Model selector, position grid, prompt editors
- [x] 3 pre-built templates (Code Review, Multi-Model, Educational)
- [x] Markdown generation & JSON export/import
- [x] Keyboard shortcut (Ctrl+K) toggle

### Phase 2 ✅ (Complete)
- [x] Settings tab
- [x] Auto-sync toggle (ConfigPanel → config.json)
- [x] config-sync.mjs companion script (config.json → slides.md)
- [x] Presentation settings (title, theme, defaults)
- [x] Multi-model template support
- [x] Delete slide button
- [x] Panel defaults to collapsed

### Phase 3 (Future)
- [ ] Two-way sync with conflict detection
- [ ] Parse slides.md on load
- [ ] Filesystem watcher for external changes
- [ ] Merge strategies
- [ ] Drag-drop slide reordering
- [ ] Undo/redo
- [ ] Live preview pane
- [ ] localStorage persistence

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

**Panel starts open and covers slides:**
- Fixed in Phase 2 - panel now defaults to collapsed
- Toggle with Ctrl+K or gear icon

**Markdown export missing attributes:**
- Ensure all required fields are filled (title, model, position)
- Check that `llmQuery` object exists for each slide
- For multi-model, verify `extraModels` array is populated

**Templates not inserting:**
- Click the template card (entire card is clickable)
- Check that `currentSlideIndex` is valid
- Verify `config.slides` array is populated

**Auto-sync not working:**
- Verify auto-sync checkbox is enabled (Settings tab)
- Check that config-sync.mjs is running (`node config-sync.mjs --watch`)
- Ensure downloaded config.json is moved to slidev-lab directory
- Check terminal output for sync errors

**config-sync.mjs errors:**
- Verify config.json is valid JSON
- Check that slides.md is writable
- Ensure Node.js has filesystem permissions
