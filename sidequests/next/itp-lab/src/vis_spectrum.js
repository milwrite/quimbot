import { makeCanvas, rafLoop } from './util_canvas.js';

// Slide 8 artifact: Vibe ↔ Deliberate spectrum slider with shifting visuals.
export function spectrum(container) {
  container.innerHTML = '';
  // Allow vertical scrolling past the spectrum canvas on mobile; the slider
  // itself sets touch-action: none so drags stay on the thumb.
  container.style.touchAction = 'pan-y';

  const root = document.createElement('div');
  root.style.position = 'relative';
  root.style.width = '100%';
  root.style.height = '100%';
  root.style.touchAction = 'pan-y';
  container.appendChild(root);

  const ui = document.createElement('div');
  ui.style.position = 'absolute';
  // Pixel fallbacks for browsers without CSS max() (iOS < 14, old Android WebView).
  // The second assignment overrides in browsers that support max() + env().
  ui.style.left = '12px';
  ui.style.left = 'max(12px, env(safe-area-inset-left, 0px))';
  ui.style.right = '12px';
  ui.style.right = 'max(12px, env(safe-area-inset-right, 0px))';
  ui.style.bottom = '12px';
  ui.style.bottom = 'max(12px, env(safe-area-inset-bottom, 0px))';
  ui.style.display = 'flex';
  ui.style.gap = '10px';
  ui.style.alignItems = 'center';
  ui.style.color = 'rgba(255,255,255,0.9)';
  ui.style.font = '500 14px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto';
  ui.style.flexWrap = 'nowrap';

  const left = document.createElement('div');
  left.textContent = 'Vibe';
  left.style.opacity = '0.85';
  left.style.whiteSpace = 'nowrap';

  const right = document.createElement('div');
  right.textContent = 'Deliberate';
  right.style.opacity = '0.85';
  right.style.whiteSpace = 'nowrap';

  const range = document.createElement('input');
  range.type = 'range';
  range.min = '0';
  range.max = '1';
  range.step = '0.001';
  range.value = '0.45';
  range.style.flex = '1';
  range.style.minWidth = '110px';
  // Explicit height meets Apple's 44px minimum touch target on mobile.
  // touch-action: none lets the browser give pointer events to the slider
  // instead of triggering a scroll while dragging.
  range.style.height = '44px';
  range.style.cursor = 'pointer';
  range.style.touchAction = 'none';
  // Cross-browser: override native styling so the track/thumb render
  // consistently on iOS Safari, Chrome Android, and Firefox mobile.
  range.style.webkitAppearance = 'none';
  range.style.appearance = 'none';
  range.style.background = 'transparent';

  // Inject a <style> for pseudo-element selectors (can't set via .style).
  const sliderCSS = document.createElement('style');
  sliderCSS.textContent = `
    input[type=range].spectrum-slider::-webkit-slider-runnable-track {
      height: 6px; background: rgba(255,255,255,0.25); border-radius: 3px;
    }
    input[type=range].spectrum-slider::-webkit-slider-thumb {
      -webkit-appearance: none; appearance: none;
      width: 28px; height: 28px; border-radius: 50%;
      background: #fff; border: 2px solid rgba(0,0,0,0.3);
      margin-top: -11px; cursor: pointer;
    }
    input[type=range].spectrum-slider::-moz-range-track {
      height: 6px; background: rgba(255,255,255,0.25); border-radius: 3px; border: none;
    }
    input[type=range].spectrum-slider::-moz-range-thumb {
      width: 28px; height: 28px; border-radius: 50%;
      background: #fff; border: 2px solid rgba(0,0,0,0.3); cursor: pointer;
    }
  `;
  root.appendChild(sliderCSS);
  range.classList.add('spectrum-slider');

  const hint = document.createElement('div');
  hint.textContent = 'Drag';
  hint.style.opacity = '0.6';
  hint.style.minWidth = '40px';
  hint.style.textAlign = 'right';

  ui.appendChild(left);
  ui.appendChild(range);
  ui.appendChild(right);
  ui.appendChild(hint);
  root.appendChild(ui);

  const { ctx, resize, destroy } = makeCanvas(root);

  let W = 0;
  let H = 0;
  function updateResponsiveUI() {
    const isNarrow = W < 560;
    const isTiny = W < 400;
    const fontPx = Math.max(12, Math.min(15, Math.floor(Math.min(W, H) * 0.03)));
    ui.style.font = `500 ${fontPx}px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto`;
    ui.style.gap = isNarrow ? '7px' : '10px';
    ui.style.flexWrap = isTiny ? 'wrap' : 'nowrap';
    hint.style.display = isNarrow ? 'none' : 'block';
    left.textContent = isNarrow ? 'V' : 'Vibe';
    right.textContent = isNarrow ? 'D' : 'Deliberate';
    left.style.flex = isTiny ? '0 0 auto' : '0 0 auto';
    right.style.flex = isTiny ? '0 0 auto' : '0 0 auto';
    range.style.flex = isTiny ? '1 0 100%' : '1';
    range.style.minWidth = isTiny ? '100%' : (isNarrow ? '90px' : '110px');
  }

  const stop = rafLoop((t) => {
    const { width, height } = resize();
    if (Math.floor(width) !== W || Math.floor(height) !== H) {
      W = Math.max(1, Math.floor(width));
      H = Math.max(1, Math.floor(height));
      updateResponsiveUI();
    }

    const v = parseFloat(range.value); // 0 vibe → 1 deliberate

    ctx.fillStyle = '#070a10';
    ctx.fillRect(0, 0, W, H);

    // Left: chaotic particles.
    const particleCount = Math.floor(420 * (1 - v));
    ctx.fillStyle = `rgba(255,120,180,${0.55 * (1 - v)})`;
    for (let i = 0; i < particleCount; i++) {
      const x = Math.random() * W;
      const y = Math.random() * H;
      const r = 1 + Math.random() * 3;
      ctx.fillRect(x, y, r, r);
    }

    // Center: flow-ish field.
    const flow = 1 - Math.abs(v - 0.5) * 2;
    const cols = W < 560 ? 18 : 28;
    const rows = W < 560 ? 12 : 18;
    const sx = W / cols;
    const sy = H / rows;
    ctx.strokeStyle = `rgba(120,200,255,${0.45 * flow})`;
    ctx.lineWidth = W < 560 ? 1.5 : 2;
    for (let j = 0; j < rows; j++) {
      for (let i = 0; i < cols; i++) {
        const x = (i + 0.5) * sx;
        const y = (j + 0.5) * sy;
        const a = 1.7 * Math.sin((i * 0.35) + (j * 0.25) + t / 1200);
        const len = (W < 560 ? 8 : 10) + (W < 560 ? 12 : 16) * flow;
        ctx.beginPath();
        ctx.moveTo(x - Math.cos(a) * len, y - Math.sin(a) * len);
        ctx.lineTo(x + Math.cos(a) * len, y + Math.sin(a) * len);
        ctx.stroke();
      }
    }

    // Right: precise grid.
    const g = v;
    ctx.strokeStyle = `rgba(255,255,255,${0.35 * g})`;
    ctx.lineWidth = 1;
    const step = W < 560 ? 20 : 26;
    for (let x = 0; x <= W; x += step) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, H);
      ctx.stroke();
    }
    for (let y = 0; y <= H; y += step) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(W, y);
      ctx.stroke();
    }

    // Title.
    ctx.fillStyle = 'rgba(255,255,255,0.92)';
    const titleSize = Math.max(14, Math.min(20, Math.floor(Math.min(W, H) * 0.045)));
    ctx.font = `600 ${titleSize}px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto`;

    const titleLong = 'Spectrum: Vibe coding → Deliberate collaboration';
    if (W < 620) {
      ctx.fillText('Spectrum: Vibe coding', 14, 24 + titleSize * 0.6);
      ctx.fillText('→ Deliberate collaboration', 14, 24 + titleSize * 1.7);
    } else {
      ctx.fillText(titleLong, 22, 34);
    }
  });

  return () => {
    stop();
    destroy();
    root.remove();
  };
}
