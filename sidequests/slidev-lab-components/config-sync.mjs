#!/usr/bin/env node
/**
 * config-sync.mjs - Watch config.json and auto-regenerate slides.md
 * 
 * Usage: node config-sync.mjs [--watch]
 * 
 * Modes:
 *   - Default: One-time sync (read config.json, write slides.md)
 *   - --watch: Continuous watch mode (auto-sync on config.json changes)
 */

import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

const CONFIG_PATH = path.join(__dirname, 'config.json')
const SLIDES_PATH = path.join(__dirname, 'slides.md')

/**
 * Generate Slidev markdown from config
 */
function generateMarkdown(config) {
  let md = `---
theme: default
title: ${config.title || 'Presentation'}
---

`

  config.slides.forEach(slide => {
    md += `---
layout: default
---

# ${slide.title}

`
    
    // Handle multi-model slides
    if (slide.extraModels && slide.extraModels.length > 0) {
      // Multi-model layout
      const allModels = [slide.llmQuery, ...slide.extraModels]
      
      allModels.forEach(llm => {
        md += `<LLMQuery\n`
        md += `  model="${llm.model}"\n`
        md += `  position="${llm.position}"\n`
        if (llm.systemPrompt) {
          md += `  system-prompt="${llm.systemPrompt}"\n`
        }
        if (llm.autoPrompt) {
          md += `  prompt="${llm.autoPrompt}"\n`
        }
        md += `  :auto-execute="${llm.autoExecute}"\n`
        md += `/>\n\n`
      })
      
      md += slide.content
      md += '\n\n'
    } else {
      // Single-model layout
      md += `<LLMQuery\n`
      md += `  model="${slide.llmQuery.model}"\n`
      md += `  position="${slide.llmQuery.position}"\n`
      if (slide.llmQuery.systemPrompt) {
        md += `  system-prompt="${slide.llmQuery.systemPrompt}"\n`
      }
      if (slide.llmQuery.autoPrompt) {
        md += `  prompt="${slide.llmQuery.autoPrompt}"\n`
      }
      md += `  :auto-execute="${slide.llmQuery.autoExecute}"\n`
      md += `>\n\n`
      md += slide.content
      md += `\n\n</LLMQuery>\n`
    }
    
    md += '\n'
  })
  
  return md
}

/**
 * Sync config to slides
 */
function syncSlides() {
  try {
    // Read config
    const configRaw = fs.readFileSync(CONFIG_PATH, 'utf-8')
    const config = JSON.parse(configRaw)
    
    // Generate markdown
    const markdown = generateMarkdown(config)
    
    // Write slides.md
    fs.writeFileSync(SLIDES_PATH, markdown, 'utf-8')
    
    console.log(`✅ Synced ${config.slides.length} slides to ${SLIDES_PATH}`)
    return true
  } catch (error) {
    console.error(`❌ Sync failed:`, error.message)
    return false
  }
}

/**
 * Watch mode
 */
function watchConfig() {
  console.log(`👀 Watching ${CONFIG_PATH} for changes...`)
  
  let timeout
  fs.watch(CONFIG_PATH, (eventType) => {
    if (eventType === 'change') {
      // Debounce: wait 500ms after last change
      clearTimeout(timeout)
      timeout = setTimeout(() => {
        console.log(`\n📝 Config changed, syncing...`)
        syncSlides()
      }, 500)
    }
  })
  
  // Initial sync
  syncSlides()
}

// Main
const watchMode = process.argv.includes('--watch')

if (watchMode) {
  watchConfig()
} else {
  const success = syncSlides()
  process.exit(success ? 0 : 1)
}
