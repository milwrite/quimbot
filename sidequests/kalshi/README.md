# Kalshi Trading Bot

Systematic prediction market trading on Kalshi. Two strategies — weather and CPI — using free public data sources. Up to 5 trades per day at scheduled windows.

## Structure

```
kalshi/
├── core/
│   ├── auth.py        # RSA-PSS signing, Kalshi API key auth
│   ├── client.py      # REST client: markets, orderbook, orders, positions
│   └── logger.py      # JSONL trade + signal logging
├── strategies/
│   ├── weather.py     # Open-Meteo forecast vs Kalshi high-temp markets
│   └── cpi.py         # Cleveland Fed nowcast vs Kalshi CPI markets
├── logs/              # trades.jsonl, signals.jsonl, runner.log (gitignored)
├── runner.py          # Scheduler + CLI
├── .env.example       # Config template
└── requirements.txt
```

## Setup

```bash
cd /home/milwrite/kalshi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# fill in KALSHI_API_KEY_ID + KALSHI_PRIVATE_KEY_PATH in .env
```

## Kalshi Account Setup (morning)

1. Sign up at kalshi.com
2. Account & Security → API Keys → Create Key
3. Download the `.key` file → save as `kalshi-key.key` in this dir
4. Copy the API Key ID into `.env`
5. Set `KALSHI_USE_DEMO=true` to test against demo first

## Usage

```bash
# Test signals without placing orders
python runner.py --dry-run --now

# Run both strategies now (live)
python runner.py --now

# Run only weather strategy
python runner.py --strategy weather --now

# Run CPI strategy, ignore timing gate
python runner.py --strategy cpi --now --force-cpi

# Start scheduled 5x/day loop
python runner.py
```

## Schedule (ET)

| Time  | Strategies      | Rationale |
|-------|-----------------|-----------|
| 07:45 | Weather         | Pre-open scan before markets reprice morning forecast |
| 08:25 | CPI             | Pre-release window (BLS drops 8:30 AM on release days) |
| 10:30 | Weather         | Intraday forecast update lag |
| 13:00 | Weather + CPI   | Afternoon sweep |
| 15:45 | Weather         | EOD — markets close, expiration approaching |

## Strategies

### Weather
- Source: Open-Meteo API (no key) + NWS fallback
- Markets: Kalshi high-temperature contracts (e.g. "NYC high > 75°F today")
- Edge: forecast divergence from market-implied probability
- Minimum edge: 6% after fees

### CPI
- Source: Cleveland Fed Inflation Nowcast + BLS API
- Markets: Kalshi "CPI MoM > X%" contracts
- Window: 8:00–8:30 AM ET on BLS release days only
- Minimum edge: 7% after fees

## Trade Log

All signals and orders are written to `logs/`:
- `signals.jsonl` — every signal considered (including below-edge)
- `trades.jsonl` — orders placed + close events
- `runner.log` — full run log

## Risk

- Hard cap: 5 orders/day (`MAX_DAILY_TRADES` in `.env`)
- Maker-only limit orders (no market orders)
- All positions logged with expected close for manual review
- Kalshi is a CFTC-regulated exchange; real money at risk
