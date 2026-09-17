import pytest

@pytest.mark.asyncio
async def test_register_and_create_link(client, auth_token):
    response = await client.post(
        "/api/v1/links",
        json={"url": "https://example.com", "title": "Example", "tags": ["docs"]},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 201