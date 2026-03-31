# Cloze Reader TODO

## Viewport / Responsive Polish
- [ ] iPhone SE (375x667): prose text still overflows viewport on long passages — needs to fit without scrolling past sticky controls
- [ ] iPhone SE: caret intersects with footer bar — needs clear separation
- [ ] Desktop 1080p: title ("Cloze Reader") and summary/context box text still feel small relative to viewport
- [ ] Desktop 1440p: all fonts still undersized for the screen real estate — needs another scaling pass
- [ ] Desktop: caret button looks awkward floating above footer — consider embedding in footer or hiding on large screens
- [ ] Sticky control buttons on desktop should scale commensurately with prose text
- [ ] Test all changes across iPhone SE, iPhone 14, iPad mini, 1080p, and 1440p viewports with Playwright

## Model Evaluation
- [ ] Try fine-tuned model (Quimbot LoRA) as word selector against current Gemma-3-27B (OpenRouter)
- [ ] Compare word selection quality: difficulty calibration, vocabulary range, blank placement
- [ ] Evaluate hint generation quality: fine-tuned vs Gemma-3-27B
- [ ] Document results in dataset_review.md

## Deployment
- Live: https://cloze-reader.cuny.qzz.io
- Push to `main` on zmuhls/cloze-reader triggers Kale Deploy
- Secrets managed via Kale MCP (`set_project_secret`)
