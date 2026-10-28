"""
Day 52 · Task 3 · Practice: Problems: Rate Limiter & Flatten JSON

Solve both in the starter file, then run it: every assert must pass. Two practical problems you'll meet in LLM apps.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Rate Limiter ----------------
import time
from collections import deque


class RateLimiter:
    """Allow at most `limit` calls per `window` seconds (sliding window of timestamps).
    APIs like LLM providers enforce exactly this."""

    def __init__(self, limit: int, window: float):
        pass

    def allow(self, now: float | None = None) -> bool:
        pass


# ---------------- Flatten JSON ----------------
def flatten(d: dict, prefix: str = "") -> dict:
    """{"a": {"b": 1}, "c": 2} -> {"a.b": 1, "c": 2}. Useful for logging LLM outputs."""
    pass


if __name__ == "__main__":
    # Rate Limiter
    r = RateLimiter(2, 1.0)
    assert r.allow(0.0) and r.allow(0.1) and not r.allow(0.2) and r.allow(1.05)
    # Flatten JSON
    assert flatten({"a": {"b": 1, "c": {"d": 2}}, "e": 3}) == {"a.b": 1, "a.c.d": 2, "e": 3}
    print("All tests passed!")
