import { makeCanvas, rafLoop } from './util_canvas.js';

// Sospiri — sighs.
// Concept by Petrarch. Built by Quimbot.
// Rising particles that build toward something they never quite reach,
// then dissipate. The space between longing and arrival.
// Motion like breath: accumulation, suspension, release.

export function sospiri(container) {
  const { ctx, resize, destroy } = makeCanvas(container, { pixelRatioCap: 2 });

  let W = 0, H = 0;
  function onResize() {
    const s = resize();
    W = s.width; H = s.height;
  }
  onResize();

  // Palette: deep twilight blue → violet → pale rose, golden undertone at origin.
  function lerpColor(t) {
    // t: 0 = bottom (golden/warm), 0.5 = mid (violet), 1 = peak (pale rose)
    t = Math.max(0, Math.min(1, t));
    let r, g, b;
    if (t < 0.25) {
      // Golden warmth → deep twilight blue
      const s = t / 0.25;
      r = 180 - s * 140;  // 180 → 40
      g = 140 - s * 110;  // 140 → 30
      b = 60 + s * 120;   // 60 → 180
    } else if (t < 0.6) {
      // Deep twilight blue → violet
      const s = (t - 0.25) / 0.35;
      r = 40 + s * 100;   // 40 → 140
      g = 30 - s * 10;    // 30 → 20
      b = 180 + s * 40;   // 180 → 220
    } else {
      // Violet → pale rose
      const s = (t - 0.6) / 0.4;
      r = 140 + s * 100;  // 140 → 240
      g = 20 + s * 130;   // 20 → 150
      b = 220 - s * 40;   // 220 → 180
    }
    return { r: Math.round(r), g: Math.round(g), b: Math.round(b) };
  }

  // Breath cycle: global phase that all particles feel.
  let breathPhase = 0;
  const breathPeriod = 6.0; // seconds per full breath

  // Particles: born at bottom, rise, peak, dissolve.
  const particles = [];
  const maxParticles = 220;

  function spawnParticle() {
    const cx = W / 2;
    const spread = W * 0.3;
    return {
      x: cx + (Math.random() - 0.5) * spread,
      y: H + 5,
      // Each particle has its own phase offset so they don't move in lockstep.
      phaseOffset: Math.random() * Math.PI * 2,
      // Horizontal drift.
      drift: (Math.random() - 0.5) * 0.3,
      // Base rise speed: slow, like breath.
      baseSpeed: 0.15 + Math.random() * 0.25,
      // How high it can get (0..1 fraction of canvas). Never quite 0.
      ceiling: 0.08 + Math.random() * 0.15,
      // Size.
      radius: 1.2 + Math.random() * 2.5,
      // Lifetime tracker.
      age: 0,
      alive: true,
      // Slight wave amplitude.
      waveAmp: 8 + Math.random() * 20,
      waveFreq: 0.5 + Math.random() * 1.5,
    };
  }

  // Pointer: a gentle pull, like attention drawn.
  let px = null, py = null;
  function onMove(e) {
    const r = container.getBoundingClientRect();
    px = e.clientX - r.left;
    py = e.clientY - r.top;
  }
  function onLeave() { px = null; py = null; }
  container.addEventListener('pointermove', onMove);
  container.addEventListener('pointerleave', onLeave);

  let lastT = 0;

  const stop = rafLoop((t) => {
    if (!lastT) lastT = t;
    const dt = Math.min((t - lastT) / 1000, 0.05);
    lastT = t;

    onResize();

    breathPhase += dt / breathPeriod * Math.PI * 2;

    // Breath multiplier: sine curve. Peaks = suspension, troughs = release.
    // 0.3..1.0 range so particles always move a little.
    const breathMul = 0.3 + 0.7 * (0.5 + 0.5 * Math.sin(breathPhase));

    // Spawn rate tied to breath: more particles born during accumulation phase.
    const spawnRate = 2 + 6 * breathMul;
    const spawnCount = Math.floor(spawnRate * dt * 60);
    for (let i = 0; i < spawnCount && particles.length < maxParticles; i++) {
      particles.push(spawnParticle());
    }

    // Update particles.
    for (let i = particles.length - 1; i >= 0; i--) {
      const p = particles[i];
      p.age += dt;

      // Rise speed modulated by breath and by proximity to ceiling.
      const heightFrac = 1 - p.y / H; // 0 at bottom, 1 at top
      const ceilingProximity = Math.max(0, heightFrac / (1 - p.ceiling));
      // Slow down as approaching ceiling: asymptotic. Never arrive.
      const approachFactor = 1 - Math.pow(ceilingProximity, 2);
      const riseSpeed = p.baseSpeed * breathMul * Math.max(0.02, approachFactor) * 60;

      p.y -= riseSpeed * dt;

      // Horizontal: gentle sine wave + drift.
      p.x += (Math.sin(p.age * p.waveFreq + p.phaseOffset) * p.waveAmp * 0.02 + p.drift) * dt * 60;

      // Pointer influence: very gentle attraction.
      if (px != null && py != null) {
        const dx = px - p.x;
        const dy = py - p.y;
        const dist = Math.hypot(dx, dy) || 1;
        const pull = Math.min(1, 120 / dist) * 0.08;
        p.x += dx * pull * dt;
        p.y += dy * pull * dt;
      }

      // Fade: particles that get close to ceiling start dissolving.
      // Also fade at the very bottom so they emerge softly.
      let alpha = 1;
      // Emerge.
      if (p.age < 1.0) alpha *= p.age;
      // Dissolve near ceiling.
      if (ceilingProximity > 0.7) {
        alpha *= 1 - (ceilingProximity - 0.7) / 0.3;
      }
      // Also dissolve if very old.
      const maxAge = 8 + Math.random() * 0.1; // slight jitter
      if (p.age > maxAge - 2) {
        alpha *= (maxAge - p.age) / 2;
      }
      if (p.age > maxAge || alpha <= 0.01) {
        particles.splice(i, 1);
        continue;
      }
      p._alpha = Math.max(0, Math.min(1, alpha));
      p._heightFrac = heightFrac;
    }

    // Draw.
    ctx.clearRect(0, 0, W, H);

    // Background: deep dark with a faint warm glow at the bottom center.
    const bg = ctx.createLinearGradient(0, 0, 0, H);
    bg.addColorStop(0, '#080812');
    bg.addColorStop(0.7, '#0a0a18');
    bg.addColorStop(1, '#12100a');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, W, H);

    // Subtle radial glow at bottom center (golden undertone, "last light before dark").
    const glow = ctx.createRadialGradient(W / 2, H * 1.05, 0, W / 2, H * 1.05, H * 0.6);
    glow.addColorStop(0, 'rgba(160, 120, 50, 0.08)');
    glow.addColorStop(0.5, 'rgba(100, 60, 30, 0.03)');
    glow.addColorStop(1, 'rgba(0, 0, 0, 0)');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, W, H);

    // Draw particles: sorted by size (larger behind) for slight depth.
    particles.sort((a, b) => b.radius - a.radius);

    for (const p of particles) {
      const c = lerpColor(p._heightFrac);
      const a = p._alpha * 0.75;

      // Soft glow.
      const glowR = p.radius * 4;
      const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, glowR);
      grad.addColorStop(0, `rgba(${c.r}, ${c.g}, ${c.b}, ${a * 0.5})`);
      grad.addColorStop(0.4, `rgba(${c.r}, ${c.g}, ${c.b}, ${a * 0.15})`);
      grad.addColorStop(1, `rgba(${c.r}, ${c.g}, ${c.b}, 0)`);
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(p.x, p.y, glowR, 0, Math.PI * 2);
      ctx.fill();

      // Core dot.
      ctx.fillStyle = `rgba(${c.r}, ${c.g}, ${c.b}, ${a})`;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fill();
    }

    // Caption.
    ctx.fillStyle = 'rgba(255,255,255,0.45)';
    ctx.font = '12px ui-monospace, SFMono-Regular, Menlo, monospace';
    ctx.fillText('Sospiri \u2022 concept: Petrarch \u2022 code: Quimbot', 14, 22);
  });

  return () => {
    stop();
    container.removeEventListener('pointermove', onMove);
    container.removeEventListener('pointerleave', onLeave);
    destroy();
  };
}
