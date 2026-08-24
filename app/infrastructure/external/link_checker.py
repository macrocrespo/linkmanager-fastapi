import httpx

async def check_link_is_alive(url: str) -> None:
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.head(url)
            print(f"[link-check] {url} -> {response.status_code}")
    except httpx.HTTPError as exc:
        print(f"[link-check] {url} -> error: {exc}")