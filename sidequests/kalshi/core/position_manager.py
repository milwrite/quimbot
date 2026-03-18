"""
Position manager — monitors open positions and handles auto-close logic.

Close triggers:
  - Position is at/above TARGET_PROFIT_PCT of max gain
  - Market closes in < CLOSE_BEFORE_EXPIRY_MIN minutes
  - Position has moved against us past STOP_LOSS_PCT

Run this as a separate thread or call manage() from the main scan loop.
"""

import os
import logging
import datetime
from zoneinfo import ZoneInfo

from .client import KalshiClient
from .logger import log_close, log_trade

log = logging.getLogger("kalshi.positions")

ET = ZoneInfo("America/New_York")

TARGET_PROFIT_PCT     = float(os.getenv("TARGET_PROFIT_PCT",    "0.60"))  # close at 60% of max gain
STOP_LOSS_PCT         = float(os.getenv("STOP_LOSS_PCT",        "0.40"))  # close if down 40% of cost
CLOSE_BEFORE_EXPIRY_M = int(os.getenv("CLOSE_BEFORE_EXPIRY_MIN", "15"))  # minutes before close


def _minutes_to_expiry(close_time_str: str) -> float:
    """Parse Kalshi close_time ISO string → minutes until expiry."""
    try:
        close_dt = datetime.datetime.fromisoformat(close_time_str.replace("Z", "+00:00"))
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        return (close_dt - now).total_seconds() / 60
    except Exception:
        return 9999.0


def manage(client: KalshiClient, dry_run: bool = False):
    """
    Check all open positions. Close any that hit a take-profit, stop-loss,
    or are within CLOSE_BEFORE_EXPIRY_MIN of expiry.
    """
    try:
        positions = client.get_positions()
    except Exception as e:
        log.warning("Could not fetch positions: %s", e)
        return

    for pos in positions:
        ticker   = pos.get("ticker", "")
        quantity = pos.get("position", 0)   # positive = YES, negative = NO
        if quantity == 0:
            continue

        side = "yes" if quantity > 0 else "no"
        qty  = abs(quantity)

        # Get current market price
        try:
            mkt = client.get_market(ticker)
        except Exception as e:
            log.warning("Market fetch failed %s: %s", ticker, e)
            continue

        yes_ask  = mkt.get("yes_ask", 50)
        yes_bid  = mkt.get("yes_bid", 50)
        close_time = mkt.get("close_time", "")
        status   = mkt.get("status", "open")

        if status != "open":
            continue

        current_price = yes_bid if side == "yes" else (100 - yes_ask)
        entry_price   = pos.get("average_yes_price", current_price)  # cents

        gain_pct  = (current_price - entry_price) / max(entry_price, 1)
        loss_pct  = (entry_price - current_price) / max(entry_price, 1)
        mins_left = _minutes_to_expiry(close_time)

        reason = None
        if gain_pct >= TARGET_PROFIT_PCT:
            reason = f"take_profit ({gain_pct:.0%} gain)"
        elif loss_pct >= STOP_LOSS_PCT:
            reason = f"stop_loss ({loss_pct:.0%} loss)"
        elif mins_left <= CLOSE_BEFORE_EXPIRY_M:
            reason = f"expiry_proximity ({mins_left:.1f}m left)"

        if reason:
            log.info("Closing %s %s x%d — %s", ticker, side, qty, reason)
            pnl = (current_price - entry_price) * qty

            if not dry_run:
                try:
                    # Sell the position (flip side)
                    close_side   = "no"  if side == "yes" else "yes"
                    close_price  = yes_ask if side == "yes" else (100 - yes_bid)
                    result = client.place_order(
                        ticker=ticker,
                        side=close_side,
                        action="sell",
                        count=qty,
                        price=close_price,
                        order_type="limit",
                    )
                    order_id = result.get("order", {}).get("order_id", "?")
                    log_close(ticker=ticker, order_id=order_id, pnl_cents=pnl)
                    log.info("Close order placed: %s (est. P&L: $%.2f)", order_id, pnl / 100)
                except Exception as e:
                    log.error("Close order failed %s: %s", ticker, e)
            else:
                log.info("[DRY RUN] Would close %s — %s (est. P&L: $%.2f)",
                         ticker, reason, pnl / 100)
