import { makeCanvas, rafLoop } from './util_canvas.js';

// Slide 6 / 14 artifact: Creative coding triangle with draggable point.
export function triangle(container) {
  container.innerHTML = '';
  const { ctx, resize, destroy } = makeCanvas(container);

  let p = { x: 0.45, y: 0.45 }; // bary-ish in screen coords normalized
  let dragging = false;

  function toNorm(e) {
    const r = container.getBoundingClientRect();
    return { x: (e.clientX - r.left) / r.width, y: (e.clientY - r.top) / r.height };
  }

  function clampToTri(n, A, B, C) {
    // Project point to triangle via barycentric clamping.
    const v0 = { x: B.x - A.x, y: B.y - A.y };
    const v1 = { x: C.x - A.x, y: C.y - A.y };
    const v2 = { x: n.x - A.x, y: n.y - A.y };
    const d00 = v0.x * v0.x + v0.y * v0.y;
    const d01 = v0.x * v1.x + v0.y * v1.y;
    const d11 = v1.x * v1.x + v1.y * v1.y;
    const d20 = v2.x * v0.x + v2.y * v0.y;
    const d21 = v2.x * v1.x + v2.y * v1.y;
    const denom = d00 * d11 - d01 * d01;
    let v = (d11 * d20 - d01 * d21) / denom;
    let w = (d00 * d21 - d01 * d20) / denom;
    let u = 1 - v - w;
    // Clamp barycentrics to [0,1] and renormalize.
    u = Math.max(0, Math.min(1, u));
    v = Math.max(0, Math.min(1, v));
    w = Math.max(0, Math.min(1, w));
    const s = u + v + w || 1;
    u /= s; v /= s; w /= s;
    return { x: u * A.x + v * B.x + w * C.x, y: u * A.y + v * B.y + w * C.y };
  }

  // Prevent page scroll while dragging the triangle point on mobile.
  container.style.touchAction = 'none';

  const onDown = (e) => { dragging = true; p = toNorm(e); };
  const onMove = (e) => { if (dragging) p = toNorm(e); };
  const onUp = () => { dragging = false; };

  container.addEventListener('pointerdown', onDown);
  container.addEventListener('pointermove', onMove);
  window.addEventListener('pointerup', onUp);

  const stop = rafLoop((t) => {
    const { width, height } = resize();

    const pad = Math.min(width, height) * 0.12;
    const A = { x: width / 2, y: pad }; // Rules
    const B = { x: pad, y: height - pad }; // Randomness
    const C = { x: width - pad, y: height - pad }; // Interpretation

    // Clamp draggable point to triangle.
    const raw = { x: p.x * width, y: p.y * height };
    const P = clampToTri(raw, A, B, C);

    // Compute barycentric weights as "influence" for background.
    const area = (p1, p2, p3) => (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x);
    const total = area(A, B, C);
    const wA = area(P, B, C) / total;
    const wB = area(A, P, C) / total;
    const wC = area(A, B, P) / total;

    // Background: blend between grid (Rules), scatter (Randomness), curated arcs (Interpretation).
    ctx.fillStyle = '#0b0e14';
    ctx.fillRect(0, 0, width, height);

    // Rules → grid
    const gridAlpha = 0.55 * wA;
    ctx.strokeStyle = `rgba(120,180,255,${gridAlpha})`;
    ctx.lineWidth = 1;
    const step = 22;
    for (let x = 0; x <= width; x += step) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke(); }
    for (let y = 0; y <= height; y += step) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke(); }

    // Randomness → particles
    const n = Math.floor(240 * wB);
    ctx.fillStyle = `rgba(255,180,120,${0.55 * wB})`;
    for (let i = 0; i < n; i++) {
      const x = Math.random() * width;
      const y = Math.random() * height;
      const r = 1 + Math.random() * 2;
      ctx.fillRect(x, y, r, r);
    }

    // Interpretation → arcs / selected curves
    ctx.strokeStyle = `rgba(180,255,180,${0.7 * wC})`;
    ctx.lineWidth = 2;
    const k = Math.floor(5 + 8 * wC);
    for (let i = 0; i < k; i++) {
      const phase = t / 1200 + i;
      const cx = width * (0.3 + 0.4 * Math.sin(phase * 0.7));
      const cy = height * (0.3 + 0.4 * Math.cos(phase * 0.9));
      const rr = Math.min(width, height) * (0.08 + 0.03 * i);
      ctx.beginPath();
      ctx.arc(cx, cy, rr, phase, phase + 2.2);
      ctx.stroke();
    }

    // Triangle outline
    ctx.strokeStyle = 'rgba(255,255,255,0.75)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(A.x, A.y); ctx.lineTo(B.x, B.y); ctx.lineTo(C.x, C.y); ctx.closePath();
    ctx.stroke();

    // Labels — responsive: shorter text on narrow viewports to avoid clipping.
    const narrow = width < 420;
    const labelPx = Math.max(10, Math.min(16, Math.floor(Math.min(width, height) * 0.032)));
    ctx.fillStyle = 'rgba(255,255,255,0.9)';
    ctx.font = `${labelPx}px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto`;

    ctx.textAlign = 'center';
    ctx.fillText(narrow ? 'Rules' : 'Rules (System Prompt)', A.x, Math.max(labelPx + 4, A.y - 10));

    ctx.textAlign = 'left';
    // Clamp left label so it doesn't bleed off the left edge.
    const leftLabelX = Math.max(4, B.x);
    ctx.fillText(narrow ? 'Randomness' : 'Randomness (Temperature)', leftLabelX, Math.min(height - 6, B.y + labelPx + 6));

    ctx.textAlign = 'right';
    // Clamp right label so it doesn't bleed off the right edge.
    const rightLabelX = Math.min(width - 4, C.x);
    ctx.fillText(narrow ? 'Interpretation' : 'Interpretation (Curation)', rightLabelX, Math.min(height - 6, C.y + labelPx + 6));

    // Draggable point
    ctx.fillStyle = 'rgba(255,255,255,0.95)';
    ctx.beginPath();
    ctx.arc(P.x, P.y, 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = 'rgba(0,0,0,0.55)';
    ctx.lineWidth = 2;
    ctx.stroke();

    const hintPx = Math.max(10, Math.min(14, Math.floor(Math.min(width, height) * 0.028)));
    ctx.fillStyle = 'rgba(255,255,255,0.55)';
    ctx.font = `${hintPx}px ui-monospace, SFMono-Regular, Menlo, monospace`;
    ctx.textAlign = 'left';
    ctx.fillText('Drag to shift emphasis', 12, height - Math.max(14, hintPx + 4));
  });

  return () => {
    stop();
    container.removeEventListener('pointerdown', onDown);
    container.removeEventListener('pointermove', onMove);
    window.removeEventListener('pointerup', onUp);
    destroy();
  };
}
