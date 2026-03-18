"""
Trade logger — writes JSON lines to logs/trades.jsonl and logs/signals.jsonl.
"""

import json
import logging
import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

TRADES_FILE  = LOG_DIR / "trades.jsonl"
SIGNALS_FILE = LOG_DIR / "signals.jsonl"


def _append(path: Path, record: dict):
    record["ts"] = datetime.datetime.utcnow().isoformat() + "Z"
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")
    logging.getLogger("kalshi.log").info("%s → %s", path.name, record)


def log_signal(strategy: str, ticker: str, side: str, edge: float, data: dict):
    _append(SIGNALS_FILE, {
        "strategy": strategy,
        "ticker":   ticker,
        "side":     side,
        "edge_pct": round(edge, 4),
        "data":     data,
    })


def log_trade(strategy: str, ticker: str, side: str, price: int, count: int,
              order_id: str, status: str, raw: dict = None):
    _append(TRADES_FILE, {
        "strategy": strategy,
        "ticker":   ticker,
        "side":     side,
        "price_c":  price,
        "count":    count,
        "order_id": order_id,
        "status":   status,
        "raw":      raw or {},
    })


def log_close(ticker: str, order_id: str, pnl_cents: float = None):
    _append(TRADES_FILE, {
        "event":    "close",
        "ticker":   ticker,
        "order_id": order_id,
        "pnl_c":    pnl_cents,
    })
