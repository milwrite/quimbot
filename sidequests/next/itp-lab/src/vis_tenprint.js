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

  // Set initial stroke style (will be re-applied after any resize).
  // Scale lineWidth with cell size so lines stay crisp on small mobile screens
  // (at cell=10 the old fixed 2px ate 20% of each cell, muddying the pattern).
  function applyStrokeStyle() {
    ctx.strokeStyle = '#00FF41';
    ctx.lineWidth = Math.max(1, Math.min(2, cell * 0.12));
    ctx.lineCap = 'square';
  }
  applyStrokeStyle();

  function reseed() { clear(true); }
  container.addEventListener('pointerup', reseed);

  const stop = rafLoop(() => {
    if (syncSize()) {
      clear(true);
      // Canvas resize resets all context state — reapply stroke properties.
      applyStrokeStyle();
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

    // Caption — responsive font size matching other vis files.
    const captionPx = Math.max(11, Math.min(14, Math.floor(Math.min(width, height) * 0.032)));
    ctx.fillStyle = 'rgba(0,255,65,0.45)';
    ctx.font = `${captionPx}px ui-monospace, SFMono-Regular, Menlo, monospace`;
    ctx.fillText('10 PRINT (1982) • tap to reseed', 14, height - Math.max(14, captionPx + 4));
  });

  return () => {
    stop();
    container.removeEventListener('pointerup', reseed);
    destroy();
  };
}
