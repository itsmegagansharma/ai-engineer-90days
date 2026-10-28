"""
Day 55 · Task 3 · Practice: Problems: Retry Decorator & TTL Cache

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Retry Decorator ----------------
import functools
import time


def retry(times: int = 3, delay: float = 0.0, exceptions=(Exception,)):
    """Decorator: call the function again (up to `times`) when it raises one of `exceptions`."""
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            pass
        return wrapper
    return deco


# ---------------- TTL Cache ----------------
import time


class TTLCache:
    """get/set where entries expire after ttl seconds. Good for caching LLM answers."""

    def __init__(self, ttl: float):
        pass

    def set(self, key, value, now: float | None = None) -> None:
        pass

    def get(self, key, now: float | None = None):
        """Return the value, or None if missing or expired."""
        pass


if __name__ == "__main__":
    # Retry Decorator
    calls = {"n": 0}
    
    @retry(times=3)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise ValueError("not yet")
        return "ok"
    
    assert flaky() == "ok" and calls["n"] == 3
    # TTL Cache
    c = TTLCache(10); c.set("q", "a", now=0)
    assert c.get("q", now=5) == "a" and c.get("q", now=11) is None
    print("All tests passed!")
