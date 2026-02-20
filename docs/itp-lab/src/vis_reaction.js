import { makeCanvas, rafLoop } from './util_canvas.js';

// Gray-Scott reaction-diffusion: two chemicals interact to produce
// organic coral/leopard/mitosis patterns. Classic generative art algorithm.

export function reactionDiffusion(container) {
  const { ctx, resize, destroy } = makeCanvas(container, { pixelRatioCap: 1 });

  // Use a smaller simulation grid for performance
  const SIM = 128;
  let a = new Float32Array(SIM * SIM);
  let b = new Float32Array(SIM * SIM);
  let a2 = new Float32Array(SIM * SIM);
  let b2 = new Float32Array(SIM * SIM);

  // Fill with chemical A, seed chemical B in center
  a.fill(1);
  b.fill(0);
  for (let y = SIM / 2 - 8; y < SIM / 2 + 8; y++) {
    for (let x = SIM / 2 - 8; x < SIM / 2 + 8; x++) {
      b[y * SIM + x] = 1;
    }
  }
  // Random seeds for variety
  for (let i = 0; i < 12; i++) {
    const sx = Math.floor(Math.random() * (SIM - 20)) + 10;
    const sy = Math.floor(Math.random() * (SIM - 20)) + 10;
    for (let dy = -3; dy <= 3; dy++) {
      for (let dx = -3; dx <= 3; dx++) {
        b[(sy + dy) * SIM + (sx + dx)] = 1;
      }
    }
  }

  const dA = 1.0, dB = 0.5;
  const feed = 0.055, kill = 0.062;

  function laplacian(grid, x, y) {
    const i = y * SIM + x;
    const up = ((y - 1 + SIM) % SIM) * SIM + x;
    const dn = ((y + 1) % SIM) * SIM + x;
    const lt = y * SIM + ((x - 1 + SIM) % SIM);
    const rt = y * SIM + ((x + 1) % SIM);
    return grid[up] + grid[dn] + grid[lt] + grid[rt] - 4 * grid[i];
  }

  function step() {
    for (let y = 0; y < SIM; y++) {
      for (let x = 0; x < SIM; x++) {
        const i = y * SIM + x;
        const av = a[i], bv = b[i];
        const abb = av * bv * bv;
        a2[i] = av + (dA * laplacian(a, x, y) - abb + feed * (1 - av));
        b2[i] = bv + (dB * laplacian(b, x, y) + abb - (kill + feed) * bv);
        a2[i] = Math.max(0, Math.min(1, a2[i]));
        b2[i] = Math.max(0, Math.min(1, b2[i]));
      }
    }
    [a, a2] = [a2, a];
    [b, b2] = [b2, b];
  }

  let W = 0, H = 0;
  function onResize() {
    const s = resize();
    W = s.width; H = s.height;
  }
  onResize();

  const stop = rafLoop(() => {
    onResize();

    // Multiple simulation steps per frame
    for (let s = 0; s < 8; s++) step();

    // Render to canvas
    const img = ctx.createImageData(SIM, SIM);
    for (let i = 0; i < SIM * SIM; i++) {
      const v = Math.floor((1 - b[i]) * 255);
      const warm = Math.floor(b[i] * 80);
      img.data[i * 4 + 0] = Math.min(255, v + warm);
      img.data[i * 4 + 1] = v;
      img.data[i * 4 + 2] = Math.max(0, v - warm * 0.5);
      img.data[i * 4 + 3] = 255;
    }

    // Scale up to fill canvas
    const offscreen = new OffscreenCanvas(SIM, SIM);
    const offCtx = offscreen.getContext('2d');
    offCtx.putImageData(img, 0, 0);

    ctx.imageSmoothingEnabled = true;
    ctx.drawImage(offscreen, 0, 0, W, H);
  });

  return () => { stop(); destroy(); };
}
