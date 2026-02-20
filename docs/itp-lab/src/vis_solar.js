import { makeCanvas, rafLoop } from './util_canvas.js';

// Solar system: gravitational dance around a pulsing sun.
// Each orbit traces its path with fading trails, creating
// a layered mandala effect over time.

export function solar(container) {
  const { ctx, resize, destroy } = makeCanvas(container, { pixelRatioCap: 2 });

  let W = 0, H = 0;
  function onResize() {
    const s = resize();
    W = s.width; H = s.height;
  }
  onResize();

  const bodies = [
    { r: 0.12, speed: 0.031, size: 3.5, hue: 45,  trail: [] },
    { r: 0.19, speed: 0.022, size: 3.0, hue: 200, trail: [] },
    { r: 0.27, speed: 0.015, size: 4.0, hue: 15,  trail: [] },
    { r: 0.36, speed: 0.009, size: 2.5, hue: 130, trail: [] },
    { r: 0.44, speed: 0.006, size: 5.5, hue: 30,  trail: [] },
  ];

  let t = 0;
  const trailMax = 300;

  const stop = rafLoop(() => {
    onResize();
    const cx = W / 2, cy = H / 2;
    const scale = Math.min(W, H) * 0.48;

    // Fade previous frame for trail effect
    ctx.fillStyle = 'rgba(5, 2, 10, 0.08)';
    ctx.fillRect(0, 0, W, H);

    // Sun glow
    const sunR = Math.min(W, H) * 0.04;
    const pulse = 1 + Math.sin(t * 0.04) * 0.15;
    const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, sunR * 4 * pulse);
    grad.addColorStop(0, 'rgba(255, 200, 50, 0.9)');
    grad.addColorStop(0.3, 'rgba(255, 140, 20, 0.4)');
    grad.addColorStop(0.7, 'rgba(255, 80, 10, 0.1)');
    grad.addColorStop(1, 'rgba(255, 50, 0, 0)');
    ctx.beginPath();
    ctx.arc(cx, cy, sunR * 4 * pulse, 0, Math.PI * 2);
    ctx.fillStyle = grad;
    ctx.fill();

    // Sun core
    ctx.beginPath();
    ctx.arc(cx, cy, sunR * pulse, 0, Math.PI * 2);
    ctx.fillStyle = '#ffe080';
    ctx.fill();

    // Orbit paths (faint)
    bodies.forEach(b => {
      ctx.beginPath();
      ctx.arc(cx, cy, b.r * scale, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
      ctx.lineWidth = 0.5;
      ctx.stroke();
    });

    // Bodies + trails
    bodies.forEach(b => {
      // Slight eccentricity for organic feel
      const ecc = 1 + 0.08 * Math.sin(t * b.speed * 0.7);
      const angle = t * b.speed;
      const x = cx + Math.cos(angle) * b.r * scale * ecc;
      const y = cy + Math.sin(angle) * b.r * scale;

      b.trail.push({ x, y });
      if (b.trail.length > trailMax) b.trail.shift();

      // Draw trail
      for (let i = 1; i < b.trail.length; i++) {
        const alpha = (i / b.trail.length) * 0.6;
        ctx.beginPath();
        ctx.moveTo(b.trail[i - 1].x, b.trail[i - 1].y);
        ctx.lineTo(b.trail[i].x, b.trail[i].y);
        ctx.strokeStyle = `hsla(${b.hue}, 70%, 60%, ${alpha})`;
        ctx.lineWidth = 1;
        ctx.stroke();
      }

      // Planet
      ctx.beginPath();
      ctx.arc(x, y, b.size, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${b.hue}, 70%, 65%)`;
      ctx.fill();
      ctx.strokeStyle = `hsla(${b.hue}, 80%, 80%, 0.5)`;
      ctx.lineWidth = 1;
      ctx.stroke();
    });

    t++;
  });

  return () => { stop(); destroy(); };
}
