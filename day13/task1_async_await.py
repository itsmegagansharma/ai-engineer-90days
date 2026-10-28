"""
Day 13 · Task 1: async/await

Write two async functions with asyncio.sleep and run them with asyncio.gather.

Complete every TODO, run the file, and tick this task on the tracker.
"""
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
