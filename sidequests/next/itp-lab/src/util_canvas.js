export function makeCanvas(container, { pixelRatioCap = 2 } = {}) {
  const c = document.createElement('canvas');
  c.style.width = '100%';
  c.style.height = '100%';
  c.style.display = 'block';
  container.appendChild(c);

  const ctx = c.getContext('2d');

  let _pw = 0, _ph = 0, _dpr = 0;

  function resize() {
    const r = container.getBoundingClientRect();
    const dpr = Math.min(window.devicePixelRatio || 1, pixelRatioCap);
    const pw = Math.max(1, Math.floor(r.width * dpr));
    const ph = Math.max(1, Math.floor(r.height * dpr));
    // Only touch canvas dimensions when they actually change.
    // Setting c.width/c.height clears the canvas per spec, which destroys
    // trail-based effects (flowfield, starfield) that rely on partial fade.
    if (pw !== _pw || ph !== _ph || dpr !== _dpr) {
      c.width = pw;
      c.height = ph;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      _pw = pw; _ph = ph; _dpr = dpr;
    }
    return { width: r.width, height: r.height, dpr };
  }

  const ro = new ResizeObserver(() => resize());
  ro.observe(container);
  const size = resize();

  return { canvas: c, ctx, resize, size, destroy: () => { ro.disconnect(); c.remove(); } };
}

export function rafLoop(step) {
  let raf = 0;
  let alive = true;
  function tick(t) {
    if (!alive) return;
    step(t);
    raf = requestAnimationFrame(tick);
  }
  raf = requestAnimationFrame(tick);
  return () => { alive = false; cancelAnimationFrame(raf); };
}
