# Kalshi Trading Bot

Information-edge trading on Kalshi weather and CPI contracts.

## Strategy

The edge is data speed: HRRR forecasts update hourly, NWS station observations
are near-realtime, and BLS CPI drops at 8:30 AM sharp. Kalshi markets often
price off stale consensus. When your model disagrees with the market by more
than the fee hurdle, you trade.

## Structure

```
kalshi/
├── core/
│   ├── auth.py            # RSA-PSS signing, Kalshi API key auth
│   ├── client.py          # REST client: markets, orderbook, orders, positions
│   ├── logger.py          # JSONL trade + signal logging
│   └── position_manager.py
├── strategies/
│   ├── weather.py         # HRRR forecast + live NWS obs vs Kalshi high-temp markets
│   └── cpi.py             # Cleveland Fed nowcast vs Kalshi CPI contracts
├── logs/                  # trades.jsonl, signals.jsonl, runner.log (gitignored)
├── runner.py              # Continuous scanner + CLI
├── .env.example           # Config template
└── requirements.txt
```

## Setup

```bash
cd sidequests/kalshi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# fill in KALSHI_API_KEY_ID + KALSHI_PRIVATE_KEY_PATH in .env
```

## Kalshi Account Setup

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

# Run only weather
python runner.py --strategy weather --now

# Run CPI only, skip timing gate
python runner.py --strategy cpi --now --force-cpi

# Start continuous scan loop (60s interval)
python runner.py

# Print today's P&L + positions
python runner.py --status
```

## Strategies

### Weather (HRRR + live obs)
- **Forecast source:** Open-Meteo with `models=hrrr_conus` — actual HRRR runs,
  updated every ~1 hour
- **Live observations:** NWS `observations/latest` endpoint per city — current
  station temp, not forecast
- **Signal:** blended probability weights obs more heavily as market close
  approaches (obs weight ~0.2 at 12h out, ~0.75 at 2h out)
- **Cities:** NYC, CHI, LA, MIA, DAL, ATL, HOU, PHX, SEA, BOS
- **Minimum edge:** 6% after fees

### CPI
- **Source:** Cleveland Fed Inflation Nowcast + BLS API fallback
- **Window:** 8:00–8:30 AM ET on BLS release days only
- **Minimum edge:** 7% after fees

## Risk Controls

All configured via `.env`:

| Variable | Default | Description |
|---|---|---|
| `MAX_DAILY_TRADES` | 200 | Hard cap on orders per day |
| `MAX_OPEN_POSITIONS` | 50 | Max concurrent open contracts |
| `MAX_DAILY_LOSS_CENTS` | 5000 | Halt if down $50 on the day |
| `ORDER_CONTRACTS` | 1 | Contracts per order (start small) |
| `SCAN_INTERVAL_SEC` | 60 | Seconds between full scans |
| `WEATHER_EDGE_THRESHOLD` | 0.06 | Minimum edge to trade (weather) |
| `CPI_EDGE_THRESHOLD` | 0.07 | Minimum edge to trade (CPI) |

## Ticker Format

The series prefixes (`KXHIGHNYCTEMP`, `KXCPI`, etc.) are placeholder guesses.
Run `--dry-run --now` after adding credentials and check what the market scan
returns — update `CITIES[*]["series"]` in `weather.py` and `CPI_SERIES_PREFIX`
in `cpi.py` to match real Kalshi tickers before going live.

## Trade Log

All signals and orders go to `logs/`:
- `signals.jsonl` — every signal evaluated (including below-edge)
- `trades.jsonl` — orders placed + close events
- `runner.log` — full run log

## Risks

- Kalshi is a CFTC-regulated exchange. Real money is at risk.
- Maker-only limit orders — no market orders.
- Ticker format must be confirmed before live trading.
- Edge thresholds assume ~1% fee per side. Verify current Kalshi fee structure.
