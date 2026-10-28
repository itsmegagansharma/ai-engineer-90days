"""
Day 59 · Task 3 · Practice: Problems: Async Fetch with Limit & Producer Consumer Queue

Solve both in the starter file, then run it: every assert must pass. Agents run tools concurrently like this.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Async Fetch with Limit ----------------
import asyncio


async def run_limited(jobs: list, limit: int) -> list:
    """Run coroutine factories (functions returning coroutines) with at most `limit` running at once.
    Use asyncio.Semaphore. Keep results in input order."""
    pass


# ---------------- Producer Consumer Queue ----------------
import asyncio


async def pipeline(items: list[int]) -> list[int]:
    """A producer puts items on an asyncio.Queue; 2 consumers square them; return sorted results.
    This is how agent workers pull tasks."""
    pass


if __name__ == "__main__":
    # Async Fetch with Limit
    async def job(i):
        await asyncio.sleep(0.01)
        return i * 2
    
    assert asyncio.run(run_limited([lambda i=i: job(i) for i in range(5)], 2)) == [0, 2, 4, 6, 8]
    # Producer Consumer Queue
    assert asyncio.run(pipeline([1, 2, 3])) == [1, 4, 9]
    print("All tests passed!")
