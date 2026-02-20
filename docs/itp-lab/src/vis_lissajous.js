import { makeCanvas, rafLoop } from './util_canvas.js';

// Lissajous curves — parametric harmony made visible.
export function lissajous(container) {
  container.innerHTML = '';
  const { ctx, resize, destroy } = makeCanvas(container);

  let { width, height } = resize();
  let t = 0;
  const trails = [];
  let freqA = 3, freqB = 2, phase = Math.PI / 4;
  let hue = 0;

  // Slowly drift parameters for variety
  let driftA = 0.00003;
  let driftB = 0.00005;
  let driftP = 0.0007;

  const stop = rafLoop((ts) => {
    ({ width, height } = resize());
    const cx = width / 2;
    const cy = height / 2;
    const scale = Math.min(width, height) * 0.38;

    // Evolve parameters
    freqA += driftA;
    freqB += driftB;
    phase += driftP;
    hue = (hue + 0.3) % 360;

    // Compute current point
    const x = cx + Math.sin(freqA * t + phase) * scale;
    const y = cy + Math.sin(freqB * t) * scale;
    trails.push({ x, y, h: hue });

    // Keep trail length bounded
    if (trails.length > 2000) trails.splice(0, trails.length - 2000);

    // Clear
    ctx.fillStyle = 'rgba(5, 5, 15, 0.06)';
    ctx.fillRect(0, 0, width, height);

    // Draw trail
    ctx.lineWidth = 1.5;
    ctx.lineCap = 'round';
    for (let i = 1; i < trails.length; i++) {
      const a = trails[i - 1];
      const b = trails[i];
      const alpha = i / trails.length;
      ctx.strokeStyle = `hsla(${b.h}, 80%, 60%, ${alpha * 0.8})`;
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.stroke();
    }

    // Bright dot at head
    if (trails.length > 0) {
      const head = trails[trails.length - 1];
      ctx.fillStyle = `hsl(${head.h}, 90%, 80%)`;
      ctx.beginPath();
      ctx.arc(head.x, head.y, 3, 0, Math.PI * 2);
      ctx.fill();
    }

    t += 0.015;
  });

  return () => { stop(); destroy(); };
}
