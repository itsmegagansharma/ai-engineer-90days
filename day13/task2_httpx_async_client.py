"""
Day 13 · Task 2: httpx async client

Fetch 5 URLs concurrently with httpx.AsyncClient.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install httpx
import asyncio
import httpx

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]


async def fetch(client: httpx.AsyncClient, url: str) -> int:
    # TODO: r = await client.get(url, timeout=10); return r.status_code
    pass


async def main():
    async with httpx.AsyncClient() as client:
        # TODO: results = await asyncio.gather(*(fetch(client, u) for u in URLS))
        pass


asyncio.run(main())
