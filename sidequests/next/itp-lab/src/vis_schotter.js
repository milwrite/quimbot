import { makeCanvas, rafLoop } from './util_canvas.js';

// Slide 3 artifact: Nees-style "Schotter".
export function schotter(container) {
  container.innerHTML = '';
  const { ctx, resize, destroy } = makeCanvas(container);
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
    ctx.lineWidth = 2;

    // Responsive density so mobile does not end up with tiny illegible squares.
    const targetCell = Math.max(18, Math.min(34, Math.min(width, height) / 14));
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
    ctx.fillText('Tap to redraw', 14, height - 16);
  }

  // Pointer works on desktop and mobile. Keep click fallback for older browsers.
  const redraw = () => { dirty = true; };
  container.addEventListener('pointerup', redraw);
  container.addEventListener('click', redraw);

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
    container.removeEventListener('pointerup', redraw);
    container.removeEventListener('click', redraw);
    destroy();
  };
}
