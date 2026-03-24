import { makeCanvas, rafLoop } from './util_canvas.js';

// Slide 3 artifact: Nees-style "Schotter".
export function schotter(container) {
  container.innerHTML = '';
  const { ctx, resize, destroy } = makeCanvas(container);
  // 'manipulation' (not 'none') — schotter only needs tap-to-redraw, not drag.
  // 'none' would block native page scroll when the user's finger is on this canvas.
  container.style.touchAction = 'manipulation';

  let width = 0;
  let height = 0;
  let dirty = true;

  function draw() {
    ({ width, height } = resize());
    ctx.clearRect(0, 0, width, height);
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, width, height);

    ctx.strokeStyle = '#111';

    // Responsive density so mobile does not end up with tiny illegible squares.
    const targetCell = Math.max(18, Math.min(34, Math.min(width, height) / 14));

    // Scale stroke width with cell size — at small mobile sizes (cell ~18px)
    // the old fixed 2px made squares look chunky; Nees needs crisp geometry.
    ctx.lineWidth = Math.max(1, Math.min(2, targetCell * 0.08));
    const COLS = Math.max(8, Math.floor((width * 0.84) / targetCell));
    const ROWS = Math.max(12, Math.floor((height * 0.84) / targetCell));

    const pad = Math.min(width, height) * 0.08;
    const gridW = width - pad * 2;
    const gridH = height - pad * 2;
    const size = Math.min(gridW / COLS, gridH / ROWS);

    for (let row = 0; row < ROWS; row++) {
      for (let col = 0; col < COLS; col++) {
        const disorder = row / Math.max(1, ROWS - 1);
        const angle = (Math.random() - 0.5) * disorder * 0.9;
        const dx = (Math.random() - 0.5) * disorder * size * 0.8;
        const dy = (Math.random() - 0.5) * disorder * size * 0.8;
        const cx = pad + col * size + size / 2 + dx;
        const cy = pad + row * size + size / 2 + dy;

        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(angle);
        ctx.strokeRect(-size / 2, -size / 2, size, size);
        ctx.restore();
      }
    }

    const labelSize = Math.max(13, Math.min(16, Math.floor(Math.min(width, height) * 0.026)));
    ctx.fillStyle = 'rgba(17,17,17,0.7)';
    ctx.font = `${labelSize}px ui-monospace, SFMono-Regular, Menlo, monospace`;
    const safeBottom = 10;
    const y = height - Math.max(16, safeBottom + labelSize);
    ctx.fillText('Tap to redraw', 14, y);
  }

  // Pointer works on desktop and mobile.
  // Use pointerdown for immediate feedback and avoid touch click ghost events.
  const redraw = () => { dirty = true; };
  container.addEventListener('pointerdown', redraw);

  const stop = rafLoop(() => {
    const { width: w, height: h } = resize();
    if (Math.floor(w) !== Math.floor(width) || Math.floor(h) !== Math.floor(height)) {
      dirty = true;
    }
    if (!dirty) return;
    draw();
    dirty = false;
  });

  return () => {
    stop();
    container.removeEventListener('pointerdown', redraw);
    destroy();
  };
}
