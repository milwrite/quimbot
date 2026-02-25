import { makeCanvas, rafLoop } from './util_canvas.js';

// Slide 1 artifact: 10 PRINT-style maze.
export function tenPrint(container) {
  container.innerHTML = '';
  const { ctx, resize, destroy } = makeCanvas(container);
  container.style.touchAction = 'manipulation';

  let width = 0;
  let height = 0;
  let x = 0;
  let y = 0;
  let cell = 22;

  function syncSize() {
    const s = resize();
    const nw = Math.max(1, Math.floor(s.width));
    const nh = Math.max(1, Math.floor(s.height));
    const changed = nw !== width || nh !== height;
    width = nw;
    height = nh;

    const minSide = Math.min(width, height);
    // Smaller cells on phones, larger cells on desktop.
    cell = Math.max(10, Math.min(24, Math.floor(minSide * 0.045)));
    return changed;
  }

  function clear(resetCursor = false) {
    ctx.fillStyle = '#050b07';
    ctx.fillRect(0, 0, width, height);
    if (resetCursor) {
      x = 0;
      y = 0;
    }
  }

  syncSize();
  clear(true);

  ctx.strokeStyle = '#00FF41';
  ctx.lineWidth = 2;
  ctx.lineCap = 'square';

  function reseed() { clear(true); }
  container.addEventListener('pointerup', reseed);

  const stop = rafLoop(() => {
    if (syncSize()) {
      clear(true);
      return;
    }

    // Work scales with viewport so mobile stays smooth.
    const steps = Math.max(36, Math.min(150, Math.floor((width * height) / 9000)));

    for (let i = 0; i < steps; i++) {
      if (Math.random() > 0.5) {
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + cell, y + cell);
        ctx.stroke();
      } else {
        ctx.beginPath();
        ctx.moveTo(x + cell, y);
        ctx.lineTo(x, y + cell);
        ctx.stroke();
      }

      x += cell;
      if (x >= width) {
        x = 0;
        y += cell;
      }
      if (y >= height) {
        y = 0;
        clear();
      }
    }
  });

  return () => {
    stop();
    container.removeEventListener('pointerup', reseed);
    destroy();
  };
}
