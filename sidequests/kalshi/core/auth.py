"""
Kalshi API v2 - RSA-PSS authentication helper.
Reads KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH from env at call time.

Env load order (first match wins per var):
  1. Already-set environment variables (e.g. from shell or cron set -a source)
  2. ~/kalshi/.env  (canonical credentials location)
  3. local .env in the kalshi project dir (overrides)
"""

import os
import base64
import datetime
from pathlib import Path
from urllib.parse import urlparse

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# ── env loading ───────────────────────────────────────────────────────────────
try:
    from dotenv import load_dotenv
    # Load ~/kalshi/.env first (canonical creds), then local .env (overrides)
    # override=False so already-exported env vars are never clobbered
    _home_env = Path.home() / "kalshi" / ".env"
    _local_env = Path(__file__).parent.parent / ".env"
    if _home_env.exists():
        load_dotenv(_home_env, override=False)
    if _local_env.exists():
        load_dotenv(_local_env, override=True)
except ImportError:
    pass

DEMO_BASE = "https://demo-api.kalshi.co/trade-api/v2"
PROD_BASE = "https://api.elections.kalshi.com/trade-api/v2"


def _base_url() -> str:
    use_demo = os.getenv("KALSHI_USE_DEMO", "true").lower() == "true"
    return DEMO_BASE if use_demo else PROD_BASE


# Expose BASE_URL as a property-like helper (read at call time)
BASE_URL = property(lambda self: _base_url())


def _get_api_key_id() -> str:
    return os.getenv("KALSHI_API_KEY_ID", "")


def _get_private_key_path() -> str:
    return os.getenv("KALSHI_PRIVATE_KEY_PATH", "")


def get_base_url() -> str:
    return _base_url()


def _load_private_key():
    path = _get_private_key_path()
    if not path:
        raise EnvironmentError("KALSHI_PRIVATE_KEY_PATH not set")
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())


def sign_headers(method: str, path: str) -> dict:
    """Return the three Kalshi auth headers for a given method + path."""
    api_key_id = _get_api_key_id()
    if not api_key_id:
        raise EnvironmentError("KALSHI_API_KEY_ID not set")

    ts = str(int(datetime.datetime.now().timestamp() * 1000))
    # Strip query string before signing
    clean_path = urlparse(path).path
    message = f"{ts}{method.upper()}{clean_path}".encode()

    key = _load_private_key()
    sig = key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.DIGEST_LENGTH,
        ),
        hashes.SHA256(),
    )

    return {
        "KALSHI-ACCESS-KEY":       api_key_id,
        "KALSHI-ACCESS-TIMESTAMP": ts,
        "KALSHI-ACCESS-SIGNATURE": base64.b64encode(sig).decode(),
        "Content-Type":            "application/json",
    }


# Module-level BASE_URL compat: read at import time but also refreshable
BASE_URL = get_base_url()
