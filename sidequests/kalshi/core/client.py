"""
Thin Kalshi REST client — markets, orderbook, order lifecycle, positions.
"""

import requests
import json
import logging
from typing import Optional
from .auth import BASE_URL, sign_headers

log = logging.getLogger("kalshi.client")


class KalshiClient:
    def __init__(self, base_url: str = BASE_URL, timeout: int = 10):
        self.base = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    # ── internals ─────────────────────────────────────────────────────────────

    def _get(self, path: str, params: dict = None) -> dict:
        url = self.base + path
        # Signing requires the full path including /trade-api/v2 prefix
        full_path = "/trade-api/v2" + path
        headers = sign_headers("GET", full_path)
        r = self.session.get(url, headers=headers, params=params, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def _post(self, path: str, body: dict) -> dict:
        url = self.base + path
        full_path = "/trade-api/v2" + path
        headers = sign_headers("POST", full_path)
        r = self.session.post(url, headers=headers, json=body, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def _delete(self, path: str) -> dict:
        url = self.base + path
        full_path = "/trade-api/v2" + path
        headers = sign_headers("DELETE", full_path)
        r = self.session.delete(url, headers=headers, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    # ── markets ───────────────────────────────────────────────────────────────

    def get_markets(self, event_ticker: str = None, limit: int = 100) -> list:
        params = {"limit": limit}
        if event_ticker:
            params["event_ticker"] = event_ticker
        return self._get("/markets", params).get("markets", [])

    def get_market(self, ticker: str) -> dict:
        return self._get(f"/markets/{ticker}").get("market", {})

    def get_orderbook(self, ticker: str, depth: int = 10) -> dict:
        return self._get(f"/markets/{ticker}/orderbook", {"depth": depth})

    def get_market_history(self, ticker: str, limit: int = 100) -> list:
        return self._get(f"/markets/{ticker}/history", {"limit": limit}).get("history", [])

    # ── portfolio ─────────────────────────────────────────────────────────────

    def get_balance(self) -> dict:
        return self._get("/portfolio/balance")

    def get_positions(self) -> list:
        return self._get("/portfolio/positions").get("market_positions", [])

    def get_orders(self, status: str = None) -> list:
        params = {}
        if status:
            params["status"] = status
        return self._get("/portfolio/orders", params).get("orders", [])

    # ── order lifecycle ───────────────────────────────────────────────────────

    def place_order(
        self,
        ticker: str,
        side: str,           # "yes" | "no"
        action: str,         # "buy" | "sell"
        count: int,          # number of contracts
        price: int,          # cents (1–99)
        order_type: str = "limit",
        client_order_id: str = None,
    ) -> dict:
        body = {
            "ticker":     ticker,
            "side":       side,
            "action":     action,
            "count":      count,
            "type":       order_type,
            "yes_price":  price if side == "yes" else 100 - price,
            "no_price":   100 - price if side == "yes" else price,
        }
        if client_order_id:
            body["client_order_id"] = client_order_id
        log.info("Placing order: %s", json.dumps(body))
        return self._post("/portfolio/orders", body)

    def cancel_order(self, order_id: str) -> dict:
        log.info("Cancelling order %s", order_id)
        return self._delete(f"/portfolio/orders/{order_id}")

    def get_order(self, order_id: str) -> dict:
        return self._get(f"/portfolio/orders/{order_id}").get("order", {})
