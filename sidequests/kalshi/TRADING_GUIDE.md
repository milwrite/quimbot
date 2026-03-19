# Kalshi Trading Guide

Research synthesis from CEPR, Laikal Labs, fee schedule analysis, and practitioner sources.

---

## The Core Problem

Kalshi is a real-money prediction market. Your goal: find contracts whose market price deviates from the true probability far enough to profit after fees. That gap is your edge. No edge, no profit.

Most traders lose. Research on 300,000+ contracts shows:
- Makers (who set prices) average ~10% losses
- Takers (who accept prices) average ~32% losses

The game is hard. The edge sources are well-defined though.

---

## The Favourite-Longshot Bias

The single most documented inefficiency on Kalshi:

**Cheap contracts (5–15¢) dramatically underperform.** A 5¢ contract should win ~5% of the time. It wins ~2%. That's a 60% loss rate on entry price.

**Expensive contracts (80–95¢) slightly outperform.** They're close to resolution anyway.

Implication:
- Never buy cheap lottery tickets on uncertain outcomes hoping for a big payout
- If anything, sell cheap contracts (YES at 5¢ → sell, or equivalently buy NO at 95¢)
- The market systematically overprices small-probability events because retail overestimates them

---

## Maker vs. Taker: The Most Important Rule

Kalshi's fee structure:

| Role | Fee formula | ~Impact at 50/50 odds |
|------|------------|----------------------|
| Maker | `0.035 × contracts × price × (1-price)` | ~$0.88/contract |
| Taker | `0.07 × contracts × price × (1-price)` | ~$1.75/contract |

**Maker fees are half the taker fees.** This isn't minor — at $0.50 per contract, takers pay 3.5¢/contract; makers pay 1.75¢.

**Rule: Always use limit orders. Never use market orders.**

Place your bid slightly below the ask or your offer slightly above the bid. You may not fill immediately, but you capture the fee advantage and often a better price. Taking is only justified when:
1. You have an urgent time-sensitive edge (economic release in 5 minutes)
2. The market is about to move against you
3. Position size is small enough the fee difference is trivial

---

## The Three Edge Categories

### 1. Data Edges (CPI, NFP, Weather)

The best bot-friendly opportunities. You have an external data signal; the market doesn't fully price it yet.

**How it works:**
- Kalshi offers "Will CPI be above X%" for multiple thresholds
- Cleveland Fed publishes a real-time CPI nowcast before the release
- If the nowcast says 0.35% MoM and the market is pricing the 0.3% threshold at 45¢ (too cheap), buy YES
- Your true probability estimate says it should be 70¢ → edge of 25¢ minus fees

**Key window:** 8:00–8:30 AM ET on BLS release days. Liquidity drops before the print; mispricings are largest.

**For weather:** NOAA gridded forecast data (GFS/NAM) is more accurate than market prices for short-range temperature/precipitation contracts. The market uses stale consensus; you can use 6-hour update cycles.

**Key discipline:** Only trade when `|your_estimate - market_price| > fee_cost + buffer`. If your edge is 3% and fees are 2%, skip it.

### 2. Structural Inefficiency Edges

Some contracts are badly designed:
- Bundled risks (a "tariff" market correlated with election odds)
- Ambiguous resolution criteria
- Round-number thresholds with consensus clustered right above or below them

These are harder to bot. They require judgment about contract design. Watch for markets where the resolution language is genuinely ambiguous — the market prices a simple outcome, but resolution could go either way. Those often get resolved in favor of the more literal reading, creating exploitable bias.

### 3. Momentum/Flow Edges

During live events (election night, Fed decisions), prices whipsaw. Fast traders buy dips when prices overshoot their fair value downward, then exit before resolution.

**Rule:** Only enter momentum trades as a taker if your edge is large. The fee drag on round-trips doubles your cost.

---

## Fee Math: Know Your Break-Even

For a 50-cent contract:
- Taker fee: ~$0.035/contract (3.5% of $1.00 payout)
- Round-trip (enter + exit): ~7% drag

You need a 7%+ edge just to break even on a round-trip taker trade at 50¢.

As a maker, that drops to ~3.5%.

For a 10-cent contract (low probability):
- Taker fee: ~$0.007/contract (0.7%)
- Round-trip: ~1.4%

Cheaper contracts have lower absolute fees but you're buying into the longshot bias. The fee math looks OK but the probability mispricing is killing you.

**General rule:** You need a minimum 5–8% edge to trade profitably as a taker after accounting for fees, slippage, and model error. As a maker, 3–4%.

---

## Volume Discounts

Kalshi offers fee discounts at:
- 500+ contracts/month: tier 1 discount
- 5,000+/month: tier 2
- Higher tiers available for institutional

If the bot is running regularly, tracking toward a volume tier changes the edge math significantly.

---

## What the Best Traders Do

From practitioner sources:

1. **They don't predict events. They find mispricings.** The question isn't "will CPI be above 0.3%?" It's "does this contract deserve to be 30¢ or 55¢ right now, given what I know?"

2. **They're makers, not takers.** Limit orders, patient fills, half the fees.

3. **They avoid cheap lottery tickets.** The longshot bias is real and durable.

4. **They model round-trip costs before entry.** If you plan to exit before resolution, double your fee estimate.

5. **They exploit data advantages in narrow windows.** CPI, NFP, and weather contracts have defined pre-release windows where external data creates a real edge. Outside those windows, the market is efficiently priced.

6. **They watch for bundled-risk contracts.** If a "trade policy" contract moves with election odds, there's structural noise you can exploit by estimating the unbundled probabilities.

---

## Building the Bot: Priority Order

Based on this, here's the strategy stack in order of tractability:

| Priority | Strategy | Edge source | Difficulty |
|----------|----------|-------------|------------|
| 1 | CPI pre-release | Cleveland Fed nowcast vs market | Medium |
| 2 | Weather contracts | NOAA GFS vs market | Medium |
| 3 | NFP pre-release | ADP + Philly Fed vs market | Medium-Hard |
| 4 | Longshot fade | Statistical bias | Easy (passive) |
| 5 | Fed rate decisions | CME FedWatch vs Kalshi | Medium |
| 6 | Momentum | Live event price swings | Hard (speed) |

Start with CPI and weather — external data sources are clean, the trading windows are well-defined, and the edge has academic backing.

---

## Sources

- Whelan (2024), "The Economics of Kalshi" (CEPR/VoxEU) — favourite-longshot bias data, maker/taker performance analysis
- Kalshi fee schedule — fee formula
- Laikal Labs — practitioner synthesis
- fiftycentdollars.substack.com — structural inefficiency analysis
- Cleveland Fed Inflation Nowcasting — <https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting>
- NOAA GFS forecasts — <https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs>

---

## Known Failures (Dry Run Audit — 2026-03-18)

### Bug 1: B-ticker threshold parsing is broken (CRITICAL)

B-type contracts use format `KXHIGHNY-26MAR19-B49.5`. The parser is stripping the decimal and reading the threshold as 495°F instead of 49.5°F.

Evidence from log:
```
KXHIGHNY-26MAR19-B49.5 no @ $0.0600 edge=86.5% — NYC forecast=37.6°F vs threshold=495°F (NO)
KXHIGHNY-26MAR19-B47.5 no @ $0.1200 edge=80.5% — NYC forecast=37.6°F vs threshold=475°F (NO)
```

All B-type weather contract edge calculations are garbage. Do not go live until fixed.

**Fix:** Update `parse_threshold()` in `weather.py` to handle `B{float}` tickers correctly:
```python
# B-type: "KXHIGHNY-26MAR19-B49.5" → 49.5
m = re.search(r"-B(\d+\.?\d*)$", ticker)
if m: return float(m.group(1))
```

### Bug 2: Cleveland Fed nowcast scraper failing silently

Log: `CPI: using BLS trailing MoM: 0.267%`

The Cleveland Fed scraper fell back to last month's actual BLS CPI data. The bot is trading on a stale backward-looking number, not a forward nowcast estimate.

This is critical for CPI strategy — the whole edge depends on having the *forward* estimate, not last month's actual.

**Fix:** Add explicit log when nowcast fetch fails. Check if Cleveland Fed URL has changed or rate-limited. Consider parsing the JSON data endpoint directly instead of scraping HTML.

### Bug 3: Double-firing scheduler

Log shows two identical runs 42 seconds apart (11:53:01 and 11:53:43). The scheduler is triggering the same strategy twice in quick succession. With live orders this would double your position.

**Fix:** Add a run lock / debounce. Track last-run timestamp per strategy and skip if last run was < N minutes ago.

### What is working:
- RSA-PSS authentication: confirmed live
- Balance read: $6,282 confirmed
- Market fetching: all open markets loading
- T-type weather tickers: parsing correctly
- CPI T-type tickers: parsing correctly, edge calculation directionally sound
- Signal direction: LA at 92.9°F correctly identifies YES on 83°F / 89°F thresholds
