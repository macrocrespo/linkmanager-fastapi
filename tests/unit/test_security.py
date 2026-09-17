from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import get_settings
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token,
)

def test_hash_and_verify_password_roundtrip():
    hashed = hash_password("secret123")

    assert verify_password("secret123", hashed) is True
    assert verify_password("wrong-pass", hashed) is False

def test_decode_access_token_invalid_returns_none():
    assert decode_access_token("not-a-jwt") is None

def test_decode_access_token_expired_returns_none():
    settings = get_settings()
    expired_payload = {
        "sub": "42",
        "exp": datetime.now(timezone.utc) - timedelta(minutes=1),
    }
    token = jwt.encode(expired_payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)

    assert decode_access_token(token) is None

def test_create_access_token_roundtrip():
    token = create_access_token(subject="42")

    assert decode_access_token(token) == "42"
