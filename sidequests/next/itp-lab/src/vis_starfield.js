import { makeCanvas, rafLoop } from './util_canvas.js';

// Slide 11/12 artifact: starfield w/ pointer parallax (vibe-coding example).
export function starfield(container) {
  container.innerHTML = '';
  const { ctx, resize, destroy } = makeCanvas(container);
  // Prevent scroll-on-drag on mobile so the parallax gesture works cleanly.
  container.style.touchAction = 'none';

  let mouse = { x: 0.5, y: 0.5 };
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
    mouse.x = 0.5; mouse.y = 0.5;
  };
  container.addEventListener('pointermove', onMove);
  container.addEventListener('pointerdown', onDown);
  container.addEventListener('pointerup', onUp);

  // Device orientation fallback for mobile (tilt-to-parallax).
  // iOS 13+ gates this event behind an explicit user-gesture permission prompt.
  // We request on first pointerdown so the call happens inside a user gesture.
  let orientListening = false;
  const onOrient = (e) => {
    if (touching) return; // touch takes priority
    const gamma = (e.gamma || 0) / 45; // left-right tilt, [-1, 1]
    const beta = ((e.beta || 0) - 45) / 45; // front-back tilt, [-1, 1]
    mouse.x = 0.5 + Math.max(-0.5, Math.min(0.5, gamma));
    mouse.y = 0.5 + Math.max(-0.5, Math.min(0.5, beta));
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

  const stop = rafLoop(() => {
    ({ width, height } = resize());

    // Redistribute stars on orientation change or resize — avoids sparse/clustered fields.
    if (Math.floor(width) !== lastW || Math.floor(height) !== lastH) {
      reset(width, height);
    }

    ctx.fillStyle = 'rgba(0,0,0,0.25)';
    ctx.fillRect(0, 0, width, height);

    const mx = (mouse.x - 0.5) * width;
    const my = (mouse.y - 0.5) * height;

    for (const s of stars) {
      ctx.fillStyle = `rgba(255,255,255,${s.z / 3})`;
      ctx.fillRect(s.x, s.y, s.z, s.z);
      s.x += mx * 0.0009 * s.z;
      s.y += my * 0.0009 * s.z;
      // wrap
      if (s.x < 0) s.x += width;
      if (s.x > width) s.x -= width;
      if (s.y < 0) s.y += height;
      if (s.y > height) s.y -= height;
    }
  });

  return () => {
    stop();
    container.removeEventListener('pointermove', onMove);
    container.removeEventListener('pointerdown', onDown);
    container.removeEventListener('pointerup', onUp);
    if (orientListening) window.removeEventListener('deviceorientation', onOrient);
    destroy();
  };
}
