"""
Kalshi API v2 - RSA-PSS authentication helper.
Reads KALSHI_API_KEY_ID and KALSHI_PRIVATE_KEY_PATH from env / .env file.
"""

import os
import base64
import datetime
from pathlib import Path
from urllib.parse import urlparse

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# ── env ──────────────────────────────────────────────────────────────────────
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

DEMO_BASE   = "https://demo-api.kalshi.co/trade-api/v2"
PROD_BASE   = "https://trading-api.kalshi.com/trade-api/v2"

USE_DEMO    = os.getenv("KALSHI_USE_DEMO", "true").lower() == "true"
BASE_URL    = DEMO_BASE if USE_DEMO else PROD_BASE

API_KEY_ID       = os.getenv("KALSHI_API_KEY_ID", "")
PRIVATE_KEY_PATH = os.getenv("KALSHI_PRIVATE_KEY_PATH", "")


def _load_private_key():
    if not PRIVATE_KEY_PATH:
        raise EnvironmentError("KALSHI_PRIVATE_KEY_PATH not set")
    with open(PRIVATE_KEY_PATH, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())


def sign_headers(method: str, path: str) -> dict:
    """Return the three Kalshi auth headers for a given method + path."""
    if not API_KEY_ID:
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
        "KALSHI-ACCESS-KEY":       API_KEY_ID,
        "KALSHI-ACCESS-TIMESTAMP": ts,
        "KALSHI-ACCESS-SIGNATURE": base64.b64encode(sig).decode(),
        "Content-Type":            "application/json",
    }
