# HEARTBEAT.md

## Nightly Gallery Mobile Optimization (11 PM ET)

If current time is between 22:30 and 23:30 ET:

1. Read all `vis_*.js` files in `/home/milwrite/.openclaw/workspace/docs/itp-lab/src/`
2. Audit each for mobile issues:
   - Missing touch/pointer event handlers
   - No responsive canvas resize
   - Hardcoded pixel dimensions
   - OffscreenCanvas usage (unsupported on some mobile browsers)
   - Font sizes too small on mobile
   - Canvas not filling container properly
3. Pick the 1-2 most broken visualizations and fix them
4. Commit and push fixes to `milwrite/quimbot`
5. Post summary to #orchestra tagging Petrarch (`<@1464098720340508776>`) with:
   - What you fixed
   - What still needs work
   - So Petrarch can pick up the next round

## Morning Gallery Creation (9 AM ET)

If current time is between 08:30 and 09:30 ET:

1. Check r/CreativeCoding for trending ideas
2. Build 1-2 new visualizations for the gallery
3. Register in `registry.js`, commit, push
4. Post to #orchestra with descriptions

## Gateway Token Check

If gateway commands fail with token mismatch, flag it to milwrite. Don't silently skip tasks.
