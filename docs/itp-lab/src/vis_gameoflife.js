import { makeCanvas, rafLoop } from './util_canvas.js';

// Conway's Game of Life — emergent complexity from four rules.
export function gameOfLife(container) {
  container.innerHTML = '';
  const { ctx, resize, destroy } = makeCanvas(container);

  let { width, height } = resize();
  const CELL = 6;
  let cols, rows, grid, next;
  let frameCount = 0;
  let generation = 0;
  let hueShift = 0;

  function init() {
    ({ width, height } = resize());
    cols = Math.floor(width / CELL) || 1;
    rows = Math.floor(height / CELL) || 1;
    grid = new Uint8Array(cols * rows);
    next = new Uint8Array(cols * rows);
    // Random seed ~30% density
    for (let i = 0; i < grid.length; i++) {
      grid[i] = Math.random() < 0.3 ? 1 : 0;
    }
    generation = 0;
  }

  init();

  function idx(x, y) {
    return ((y % rows) + rows) % rows * cols + ((x % cols) + cols) % cols;
  }

  function neighbors(x, y) {
    let count = 0;
    for (let dy = -1; dy <= 1; dy++) {
      for (let dx = -1; dx <= 1; dx++) {
        if (dx === 0 && dy === 0) continue;
        count += grid[idx(x + dx, y + dy)];
      }
    }
    return count;
  }

  function step() {
    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < cols; x++) {
        const i = y * cols + x;
        const n = neighbors(x, y);
        const alive = grid[i];
        next[i] = alive ? (n === 2 || n === 3 ? 1 : 0) : (n === 3 ? 1 : 0);
      }
    }
    [grid, next] = [next, grid];
    generation++;
  }

  function draw() {
    ctx.fillStyle = '#0a0a14';
    ctx.fillRect(0, 0, width, height);

    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < cols; x++) {
        if (grid[y * cols + x]) {
          const h = (hueShift + x * 0.5 + y * 0.3) % 360;
          ctx.fillStyle = `hsl(${h}, 70%, 55%)`;
          ctx.fillRect(x * CELL, y * CELL, CELL - 1, CELL - 1);
        }
      }
    }

    // Generation counter
    ctx.fillStyle = 'rgba(255,255,255,0.3)';
    ctx.font = '11px monospace';
    ctx.fillText(`gen ${generation}`, 6, height - 8);
  }

  // Re-seed if population dies or stagnates
  let lastPop = 0;
  let staleCount = 0;

  const stop = rafLoop(() => {
    ({ width, height } = resize());
    const neededCols = Math.floor(width / CELL) || 1;
    const neededRows = Math.floor(height / CELL) || 1;
    if (neededCols !== cols || neededRows !== rows) init();

    frameCount++;
    if (frameCount % 3 === 0) {
      step();
      hueShift = (hueShift + 0.2) % 360;

      // Check for stagnation
      let pop = 0;
      for (let i = 0; i < grid.length; i++) pop += grid[i];
      if (pop === lastPop) staleCount++;
      else staleCount = 0;
      lastPop = pop;

      if (pop === 0 || staleCount > 60) init();
    }
    draw();
  });

  return () => { stop(); destroy(); };
}
