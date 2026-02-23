<template>
  <div class="config-panel" :class="{ collapsed: isCollapsed }">
    <!-- Toggle Button -->
    <button class="toggle-btn" @click="togglePanel" title="Toggle Config Panel (Ctrl+K)">
      <span v-if="isCollapsed">⚙️</span>
      <span v-else>✕</span>
    </button>

    <!-- Panel Content -->
    <div v-if="!isCollapsed" class="panel-content">
      <!-- Tabs -->
      <div class="tabs">
        <button 
          v-for="tab in tabs" 
          :key="tab"
          :class="{ active: activeTab === tab }"
          @click="activeTab = tab"
        >
          {{ tab }}
        </button>
      </div>

      <!-- Builder Tab -->
      <div v-if="activeTab === 'Builder'" class="tab-content">
        <h3>Current Slide: {{ currentSlideIndex + 1 }}</h3>
        
        <!-- Slide Title -->
        <div class="form-group">
          <label>Title</label>
          <input 
            v-model="currentSlide.title" 
            type="text" 
            placeholder="Slide title"
          />
        </div>

        <!-- Model Selector -->
        <div class="form-group">
          <label>AI Model</label>
          <select v-model="currentSlide.llmQuery.model">
            <option value="openai/gpt-4.1-mini">GPT-4.1 Mini</option>
            <option value="anthropic/claude-sonnet-4">Claude Sonnet 4</option>
            <option value="anthropic/claude-3.5-sonnet">Claude 3.5 Sonnet</option>
            <option value="google/gemini-2.5-pro">Gemini 2.5 Pro</option>
            <option value="google/gemini-flash-1.5">Gemini Flash 1.5</option>
            <option value="meta-llama/llama-3.3-70b-instruct">Llama 3.3 70B</option>
            <option value="x-ai/grok-4">Grok 4</option>
          </select>
        </div>

        <!-- Position Grid -->
        <div class="form-group">
          <label>Position</label>
          <div class="position-grid">
            <button 
              v-for="pos in positions" 
              :key="pos"
              :class="{ active: currentSlide.llmQuery.position === pos }"
              @click="currentSlide.llmQuery.position = pos"
            >
              {{ pos.split('-').map(w => w[0].toUpperCase()).join('') }}
            </button>
          </div>
        </div>

        <!-- System Prompt -->
        <div class="form-group">
          <label>System Prompt</label>
          <textarea 
            v-model="currentSlide.llmQuery.systemPrompt"
            rows="3"
            placeholder="Define the AI's role and behavior..."
          />
        </div>

        <!-- Auto Prompt -->
        <div class="form-group">
          <label>Auto Prompt (optional)</label>
          <input 
            v-model="currentSlide.llmQuery.autoPrompt"
            type="text"
            placeholder="Leave empty for interactive mode"
          />
        </div>

        <!-- Auto Execute Toggle -->
        <div class="form-group checkbox">
          <label>
            <input 
              v-model="currentSlide.llmQuery.autoExecute"
              type="checkbox"
            />
            Auto-execute on slide load
          </label>
        </div>

        <!-- Slide Content -->
        <div class="form-group">
          <label>Slide Content (Markdown)</label>
          <textarea 
            v-model="currentSlide.content"
            rows="8"
            placeholder="Enter markdown content here..."
          />
        </div>

        <!-- Slide Navigation -->
        <div class="slide-nav">
          <button @click="prevSlide" :disabled="currentSlideIndex === 0">← Prev</button>
          <button @click="addSlide">+ Add Slide</button>
          <button @click="nextSlide" :disabled="currentSlideIndex === config.slides.length - 1">Next →</button>
        </div>
      </div>

      <!-- Templates Tab -->
      <div v-if="activeTab === 'Templates'" class="tab-content">
        <h3>Slide Templates</h3>
        <div class="template-gallery">
          <div 
            v-for="template in templates" 
            :key="template.id"
            class="template-card"
            @click="insertTemplate(template)"
          >
            <h4>{{ template.name }}</h4>
            <p>{{ template.description }}</p>
          </div>
        </div>
      </div>

      <!-- Export Tab -->
      <div v-if="activeTab === 'Export'" class="tab-content">
        <h3>Export / Import</h3>
        
        <button @click="exportMarkdown" class="export-btn">
          📄 Export slides.md
        </button>
        
        <button @click="exportConfig" class="export-btn">
          💾 Export config.json
        </button>
        
        <div class="form-group">
          <label>Import config.json</label>
          <input type="file" @change="importConfig" accept=".json" />
        </div>

        <button @click="copyToClipboard" class="export-btn">
          📋 Copy Markdown to Clipboard
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// State
const isCollapsed = ref(false)
const activeTab = ref('Builder')
const currentSlideIndex = ref(0)

const tabs = ['Builder', 'Templates', 'Export']
const positions = ['top-left', 'top-right', 'bottom-left', 'bottom-right']

// Slide Configuration
const config = ref({
  slides: [
    {
      id: 'slide-1',
      type: 'code-review',
      title: 'Review My Code',
      content: '```python\ndef fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n```',
      llmQuery: {
        model: 'anthropic/claude-sonnet-4',
        position: 'top-right',
        systemPrompt: 'You are a senior code reviewer. Keep responses under 10 lines.',
        autoPrompt: 'Review this code for best practices and potential improvements',
        autoExecute: true
      }
    }
  ],
  defaults: {
    model: 'openai/gpt-4.1-mini',
    position: 'top-right'
  }
})

// Templates
const templates = [
  {
    id: 'code-review',
    name: 'Code Review',
    description: 'Auto-review code with Claude',
    template: {
      type: 'code-review',
      title: 'Code Review',
      content: '```python\n# Your code here\n```',
      llmQuery: {
        model: 'anthropic/claude-sonnet-4',
        position: 'top-right',
        systemPrompt: 'You are a senior code reviewer. Keep responses under 10 lines.',
        autoPrompt: 'Review this code for best practices',
        autoExecute: true
      }
    }
  },
  {
    id: 'multi-model',
    name: 'Multi-Model Compare',
    description: 'Compare responses from 4 models',
    template: {
      type: 'multi-model',
      title: 'Model Comparison',
      content: 'Ask the same question to different models!',
      llmQuery: {
        model: 'openai/gpt-4.1-mini',
        position: 'top-left',
        systemPrompt: 'Focus on practical implementation',
        autoPrompt: '',
        autoExecute: false
      }
    }
  },
  {
    id: 'educational',
    name: 'Educational Q&A',
    description: 'Interactive learning assistant',
    template: {
      type: 'educational',
      title: 'Ask Me Anything',
      content: '## Topic\n\nExplain concepts here...',
      llmQuery: {
        model: 'google/gemini-2.5-pro',
        position: 'top-right',
        systemPrompt: 'You are a CS professor teaching undergraduates. Use examples.',
        autoPrompt: '',
        autoExecute: false
      }
    }
  }
]

// Computed
const currentSlide = computed(() => config.value.slides[currentSlideIndex.value])

// Methods
const togglePanel = () => {
  isCollapsed.value = !isCollapsed.value
}

const addSlide = () => {
  const newSlide = {
    id: `slide-${Date.now()}`,
    type: 'custom',
    title: 'New Slide',
    content: '',
    llmQuery: {
      model: config.value.defaults.model,
      position: config.value.defaults.position,
      systemPrompt: '',
      autoPrompt: '',
      autoExecute: false
    }
  }
  config.value.slides.push(newSlide)
  currentSlideIndex.value = config.value.slides.length - 1
}

const prevSlide = () => {
  if (currentSlideIndex.value > 0) {
    currentSlideIndex.value--
  }
}

const nextSlide = () => {
  if (currentSlideIndex.value < config.value.slides.length - 1) {
    currentSlideIndex.value++
  }
}

const insertTemplate = (template) => {
  const newSlide = {
    id: `slide-${Date.now()}`,
    ...template.template
  }
  config.value.slides.splice(currentSlideIndex.value + 1, 0, newSlide)
  currentSlideIndex.value++
}

const generateMarkdown = () => {
  return config.value.slides.map(slide => {
    let md = `---\nlayout: default\n---\n\n# ${slide.title}\n\n`
    
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
    
    return md
  }).join('\n---\n\n')
}

const exportMarkdown = () => {
  const markdown = generateMarkdown()
  const blob = new Blob([markdown], { type: 'text/markdown' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'slides.md'
  a.click()
  URL.revokeObjectURL(url)
}

const exportConfig = () => {
  const json = JSON.stringify(config.value, null, 2)
  const blob = new Blob([json], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'config.json'
  a.click()
  URL.revokeObjectURL(url)
}

const importConfig = (event) => {
  const file = event.target.files[0]
  if (!file) return
  
  const reader = new FileReader()
  reader.onload = (e) => {
    try {
      const imported = JSON.parse(e.target.result)
      config.value = imported
      currentSlideIndex.value = 0
    } catch (err) {
      alert('Invalid config file')
    }
  }
  reader.readAsText(file)
}

const copyToClipboard = () => {
  const markdown = generateMarkdown()
  navigator.clipboard.writeText(markdown).then(() => {
    alert('Markdown copied to clipboard!')
  })
}

// Keyboard shortcut
const handleKeydown = (e) => {
  if (e.ctrlKey && e.key === 'k') {
    e.preventDefault()
    togglePanel()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
.config-panel {
  position: fixed;
  right: 0;
  top: 0;
  height: 100vh;
  width: 400px;
  background: #1a1a1a;
  color: #fff;
  box-shadow: -2px 0 10px rgba(0,0,0,0.5);
  transition: transform 0.3s ease;
  z-index: 1000;
  overflow-y: auto;
}

.config-panel.collapsed {
  transform: translateX(100%);
}

.toggle-btn {
  position: absolute;
  left: -40px;
  top: 20px;
  width: 40px;
  height: 40px;
  background: #1a1a1a;
  color: #fff;
  border: none;
  border-radius: 4px 0 0 4px;
  cursor: pointer;
  font-size: 18px;
}

.toggle-btn:hover {
  background: #2a2a2a;
}

.panel-content {
  padding: 20px;
}

.tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  border-bottom: 1px solid #333;
}

.tabs button {
  background: none;
  border: none;
  color: #888;
  padding: 10px 15px;
  cursor: pointer;
  transition: color 0.2s;
}

.tabs button.active {
  color: #fff;
  border-bottom: 2px solid #4a9eff;
}

.tabs button:hover {
  color: #ccc;
}

.tab-content {
  padding-top: 10px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: #aaa;
  font-size: 12px;
  text-transform: uppercase;
}

.form-group input[type="text"],
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 8px;
  background: #2a2a2a;
  border: 1px solid #333;
  border-radius: 4px;
  color: #fff;
  font-family: inherit;
}

.form-group textarea {
  font-family: 'Monaco', 'Courier New', monospace;
  font-size: 12px;
}

.form-group.checkbox {
  display: flex;
  align-items: center;
}

.form-group.checkbox input {
  width: auto;
  margin-right: 10px;
}

.position-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.position-grid button {
  padding: 15px;
  background: #2a2a2a;
  border: 1px solid #333;
  border-radius: 4px;
  color: #888;
  cursor: pointer;
  transition: all 0.2s;
}

.position-grid button.active {
  background: #4a9eff;
  color: #fff;
  border-color: #4a9eff;
}

.position-grid button:hover {
  border-color: #4a9eff;
}

.slide-nav {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.slide-nav button {
  flex: 1;
  padding: 10px;
  background: #2a2a2a;
  border: 1px solid #333;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
}

.slide-nav button:hover:not(:disabled) {
  background: #3a3a3a;
}

.slide-nav button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.template-gallery {
  display: grid;
  gap: 15px;
}

.template-card {
  padding: 15px;
  background: #2a2a2a;
  border: 1px solid #333;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.template-card:hover {
  background: #3a3a3a;
  border-color: #4a9eff;
}

.template-card h4 {
  margin: 0 0 5px 0;
  color: #fff;
}

.template-card p {
  margin: 0;
  color: #888;
  font-size: 13px;
}

.export-btn {
  width: 100%;
  padding: 12px;
  margin-bottom: 10px;
  background: #2a2a2a;
  border: 1px solid #333;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  font-size: 14px;
}

.export-btn:hover {
  background: #3a3a3a;
}

h3 {
  margin-top: 0;
  color: #fff;
  font-size: 16px;
}
</style>
