import { makeCanvas, rafLoop } from './util_canvas.js';

// Lorenz attractor (Edward Lorenz, 1963).
// Deterministic chaos: three coupled ODEs produce the famous butterfly shape.
// Particles trace the attractor with fading trails.

export function lorenz(container) {
  const { ctx, resize, destroy } = makeCanvas(container, { pixelRatioCap: 2 });

  let W = 0, H = 0;
  function onResize() {
    const s = resize();
    W = s.width; H = s.height;
  }
  onResize();

  // Lorenz parameters (classic values).
  const sigma = 10;
  const rho = 28;
  const beta = 8 / 3;
  const dt = 0.005;

  // Multiple particles for visual richness.
  const N = 6;
  const particles = [];
  const trails = []; // each trail: array of {x, y, z} world coords
  const maxTrail = 600;

  const hues = [200, 260, 320, 40, 160, 80];

  function initParticles() {
    particles.length = 0;
    trails.length = 0;
    for (let i = 0; i < N; i++) {
      const p = {
        x: 0.1 + (Math.random() - 0.5) * 0.01,
        y: 0.0 + (Math.random() - 0.5) * 0.01,
        z: 25 + (Math.random() - 0.5) * 0.01,
      };
      particles.push(p);
      trails.push([{ x: p.x, y: p.y, z: p.z }]);
    }
  }
  initParticles();

  // Camera rotation.
  let angle = 0;
  let targetAngle = 0;
  let dragging = false;
  let dragStartX = 0;
  let dragStartAngle = 0;

  function onPointerDown(e) {
    dragging = true;
    dragStartX = e.clientX;
    dragStartAngle = targetAngle;
    container.setPointerCapture(e.pointerId);
  }
  function onPointerMove(e) {
    if (!dragging) return;
    targetAngle = dragStartAngle + (e.clientX - dragStartX) * 0.01;
  }
  function onPointerUp(e) {
    dragging = false;
    container.releasePointerCapture(e.pointerId);
  }
  function onDblClick() { initParticles(); }

  container.addEventListener('pointerdown', onPointerDown);
  container.addEventListener('pointermove', onPointerMove);
  container.addEventListener('pointerup', onPointerUp);
  container.addEventListener('dblclick', onDblClick);

  // Project 3D world coords to 2D screen, rotating around Y axis.
  function project(wx, wy, wz) {
    const cosA = Math.cos(angle);
    const sinA = Math.sin(angle);
    const px = wx * cosA + wz * sinA;
    const py = wy;
    const scale = Math.min(W, H) / 55;
    return {
      sx: W / 2 + px * scale,
      sy: H * 0.55 - py * scale,
    };
  }

  function integrate() {
    for (let i = 0; i < N; i++) {
      const p = particles[i];
      const dx = sigma * (p.y - p.x) * dt;
      const dy = (p.x * (rho - p.z) - p.y) * dt;
      const dz = (p.x * p.y - beta * p.z) * dt;
      p.x += dx;
      p.y += dy;
      p.z += dz;

      trails[i].push({ x: p.x, y: p.y, z: p.z });
      if (trails[i].length > maxTrail) trails[i].shift();
    }
  }

  const stop = rafLoop(() => {
    onResize();

    if (!dragging) targetAngle += 0.002;
    angle += (targetAngle - angle) * 0.08;

    // Multiple sub-steps per frame for trail density.
    for (let s = 0; s < 4; s++) integrate();

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#05070b';
    ctx.fillRect(0, 0, W, H);

    // Draw each particle's trail.
    for (let i = 0; i < N; i++) {
      const trail = trails[i];
      if (trail.length < 2) continue;
      const hue = hues[i % hues.length];

      ctx.lineWidth = 1.2;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';

      // Project all points this frame.
      let prev = project(trail[0].x, trail[0].y, trail[0].z);
      for (let j = 1; j < trail.length; j++) {
        const cur = project(trail[j].x, trail[j].y, trail[j].z);
        const alpha = (j / trail.length) * 0.85;
        ctx.strokeStyle = `hsla(${hue}, 80%, 65%, ${alpha})`;
        ctx.beginPath();
        ctx.moveTo(prev.sx, prev.sy);
        ctx.lineTo(cur.sx, cur.sy);
        ctx.stroke();
        prev = cur;
      }

      // Bright dot at head.
      const head = project(trail[trail.length - 1].x, trail[trail.length - 1].y, trail[trail.length - 1].z);
      ctx.fillStyle = `hsla(${hue}, 90%, 80%, 0.95)`;
      ctx.beginPath();
      ctx.arc(head.sx, head.sy, 2.5, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.fillStyle = 'rgba(255,255,255,0.55)';
    ctx.font = '12px ui-monospace, SFMono-Regular, Menlo, monospace';
    ctx.fillText('Lorenz attractor (1963) \u2022 drag to rotate \u2022 double-click to reseed', 14, 22);
  });

  return () => {
    stop();
    container.removeEventListener('pointerdown', onPointerDown);
    container.removeEventListener('pointermove', onPointerMove);
    container.removeEventListener('pointerup', onPointerUp);
    container.removeEventListener('dblclick', onDblClick);
    destroy();
  };
}
