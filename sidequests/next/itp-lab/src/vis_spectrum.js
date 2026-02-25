import { makeCanvas, rafLoop } from './util_canvas.js';

// Slide 8 artifact: Vibe ↔ Deliberate spectrum slider with shifting visuals.
export function spectrum(container) {
  container.innerHTML = '';
  const root = document.createElement('div');
  root.style.position = 'relative';
  root.style.width = '100%';
  root.style.height = '100%';
  root.style.touchAction = 'manipulation';
  container.appendChild(root);

  const ui = document.createElement('div');
  ui.style.position = 'absolute';
  ui.style.left = 'max(12px, env(safe-area-inset-left))';
  ui.style.right = 'max(12px, env(safe-area-inset-right))';
  ui.style.bottom = 'max(12px, env(safe-area-inset-bottom))';
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
    const fontPx = Math.max(12, Math.min(15, Math.floor(Math.min(W, H) * 0.03)));
    ui.style.font = `500 ${fontPx}px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto`;
    ui.style.gap = isNarrow ? '7px' : '10px';
    hint.style.display = isNarrow ? 'none' : 'block';
    left.textContent = isNarrow ? 'V' : 'Vibe';
    right.textContent = isNarrow ? 'D' : 'Deliberate';
    range.style.minWidth = isNarrow ? '90px' : '110px';
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
