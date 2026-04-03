import { makeCanvas, rafLoop } from './util_canvas.js';

// Slide 11/12 artifact: starfield w/ pointer parallax (vibe-coding example).
export function starfield(container) {
  container.innerHTML = '';
  const { ctx, resize, destroy } = makeCanvas(container);
  // Use 'manipulation' (not 'none') so mobile users can still scroll past
  // the starfield. Tilt-to-parallax via deviceorientation is the primary
  // mobile input; pointer drag is a desktop nicety, not worth blocking scroll.
  container.style.touchAction = 'manipulation';

  let mouse = { x: 0.5, y: 0.5 };
  // Smoothed orientation target — raw gyro data is jittery on mobile.
  // Store the target separately and lerp mouse toward it each frame.
  let orientTarget = { x: 0.5, y: 0.5 };
  let touching = false;

  function updateMouse(e) {
    const r = container.getBoundingClientRect();
    mouse.x = (e.clientX - r.left) / r.width;
    mouse.y = (e.clientY - r.top) / r.height;
  }
  const onMove = (e) => { updateMouse(e); };
  const onDown = (e) => { touching = true; updateMouse(e); requestOrientPermission(); };
  const onUp = () => {
    touching = false;
    // Drift back to center so the field settles.
    orientTarget.x = 0.5; orientTarget.y = 0.5;
  };
  container.addEventListener('pointermove', onMove);
  container.addEventListener('pointerdown', onDown);
  container.addEventListener('pointerup', onUp);
  container.addEventListener('pointercancel', onUp); // mobile: cancel resets parallax

  // Device orientation fallback for mobile (tilt-to-parallax).
  // iOS 13+ gates this event behind an explicit user-gesture permission prompt.
  // We request on first pointerdown so the call happens inside a user gesture.
  let orientListening = false;
  const onOrient = (e) => {
    if (touching) return; // touch takes priority
    const gamma = (e.gamma || 0) / 45; // left-right tilt, [-1, 1]
    const beta = ((e.beta || 0) - 45) / 45; // front-back tilt, [-1, 1]
    // Write to target; the render loop lerps mouse toward this for smooth parallax.
    orientTarget.x = 0.5 + Math.max(-0.5, Math.min(0.5, gamma));
    orientTarget.y = 0.5 + Math.max(-0.5, Math.min(0.5, beta));
  };

  function requestOrientPermission() {
    if (orientListening) return;
    if (
      typeof DeviceOrientationEvent !== 'undefined' &&
      typeof DeviceOrientationEvent.requestPermission === 'function'
    ) {
      // iOS 13+: requires user-gesture context — called from onDown.
      DeviceOrientationEvent.requestPermission()
        .then(state => {
          if (state === 'granted') {
            window.addEventListener('deviceorientation', onOrient);
            orientListening = true;
          }
        })
        .catch(() => {});
    } else {
      // Android, desktop, iOS < 13 — no permission needed.
      window.addEventListener('deviceorientation', onOrient);
      orientListening = true;
    }
  }

  let stars = [];
  let lastW = 0, lastH = 0;
  let prevT = 0;

  function reset(width, height) {
    lastW = Math.floor(width);
    lastH = Math.floor(height);
    // Scale star count to viewport area — fewer on small/mobile screens.
    const area = width * height;
    const count = Math.max(80, Math.min(360, Math.floor(area / 1800)));
    stars = Array.from({ length: count }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      z: Math.random() * 3 + 0.5,
    }));
  }

  let { width, height } = resize();
  reset(width, height);

  // On Android (and desktop), DeviceOrientationEvent does not need a permission
  // prompt. Register immediately so tilt-to-parallax works on first load without
  // waiting for a tap.  iOS 13+ still gates on user gesture — handled in onDown.
  requestOrientPermission();

  const stop = rafLoop((t) => {
    ({ width, height } = resize());

    // Redistribute stars on orientation change or resize — avoids sparse/clustered fields.
    if (Math.floor(width) !== lastW || Math.floor(height) !== lastH) {
      reset(width, height);
    }

    // Smooth gyroscope input: lerp mouse toward orientTarget each frame.
    // Factor 0.08 gives ~120 ms settling time at 60 fps — fast enough to feel
    // responsive, slow enough to filter gyro jitter on mobile.
    if (!touching) {
      mouse.x += (orientTarget.x - mouse.x) * 0.08;
      mouse.y += (orientTarget.y - mouse.y) * 0.08;
    }

    // Frame-rate-independent fade: target the same visual trail length at any
    // refresh rate (60 Hz, 90 Hz, 120 Hz ProMotion, etc.).  We want the
    // equivalent of alpha 0.25 at 60 fps (~16.67 ms).  Using exponential decay:
    //   alpha = 1 - (1 - 0.25)^(dt / 16.667)
    const dt = Math.min(50, t - prevT) || 16.667;
    prevT = t;
    const fadeAlpha = 1 - Math.pow(0.75, dt / 16.667);
    ctx.fillStyle = `rgba(0,0,0,${fadeAlpha.toFixed(4)})`;
    ctx.fillRect(0, 0, width, height);

    const mx = (mouse.x - 0.5) * width;
    const my = (mouse.y - 0.5) * height;

    // Minimum star size so sub-pixel stars stay visible on mobile screens.
    const minStar = Math.max(1, Math.min(width, height) * 0.003);

    for (const s of stars) {
      const sz = Math.max(minStar, s.z);
      ctx.fillStyle = `rgba(255,255,255,${s.z / 3})`;
      ctx.fillRect(s.x, s.y, sz, sz);
      s.x += mx * 0.0009 * s.z;
      s.y += my * 0.0009 * s.z;
      // wrap
      if (s.x < 0) s.x += width;
      if (s.x > width) s.x -= width;
      if (s.y < 0) s.y += height;
      if (s.y > height) s.y -= height;
    }

    // Interaction hint — responsive font size.
    const hintPx = Math.max(11, Math.min(14, Math.floor(Math.min(width, height) * 0.032)));
    ctx.fillStyle = 'rgba(255,255,255,0.45)';
    ctx.font = `${hintPx}px ui-monospace, SFMono-Regular, Menlo, monospace`;
    const hintText = width < 480 ? 'Drag or tilt to shift' : 'Drag or tilt device to shift parallax';
    ctx.fillText(hintText, 14, height - Math.max(14, hintPx + 4));
  });

  return () => {
    stop();
    container.removeEventListener('pointermove', onMove);
    container.removeEventListener('pointerdown', onDown);
    container.removeEventListener('pointerup', onUp);
    container.removeEventListener('pointercancel', onUp);
    if (orientListening) window.removeEventListener('deviceorientation', onOrient);
    destroy();
  };
}
