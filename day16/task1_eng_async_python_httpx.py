"""
Day 16 · Task 1 · Engineering: Async Python & httpx

Write two async functions with asyncio.sleep and run them with asyncio.gather. Then: Fetch 5 URLs concurrently with httpx.AsyncClient. Then: Time sync vs async versions and note the difference.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: async/await =====
import asyncio
import time


async def make_tea(name: str, seconds: int) -> str:
    await asyncio.sleep(seconds)
    return f"{name} ready"


async def main():
    start = time.perf_counter()
    # TODO 1: await make_tea("masala", 2) then make_tea("green", 2) one after another; time it
    # TODO 2: run both with asyncio.gather(...); time it. Why is it faster?
    pass


asyncio.run(main())


# ===== Part 2: httpx async client =====
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


# ===== Part 3: Measure =====
# ## Results
# | Version | Time for 5 requests |
# |---------|---------------------|
# | sync (requests, one by one) | |
# | async (httpx + gather) | |
#
# Why does this matter for LLM apps that call several tools or models?
# >
