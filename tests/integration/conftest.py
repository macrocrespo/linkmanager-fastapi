import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

@pytest.fixture
async def auth_token(client):
    await client.post("/api/v1/auth/register", json={"email": "a@a.com", "password": "password123"})
    login = await client.post("/api/v1/auth/login", data={"username": "a@a.com", "password": "password123"})
    return login.json()["access_token"]