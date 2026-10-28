"""
Day 55 · Task 1 · Engineering: Retries, backoff & fallbacks

Retry with backoff; fall back to a cheaper model or simpler path.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import random
import time


def flaky_api() -> str:
    if random.random() < 0.6:
        raise ConnectionError("temporary failure")
    return "ok"


def with_retry(fn, attempts: int = 4, base_delay: float = 0.5):
    # TODO: retry with exponential backoff (0.5s, 1s, 2s...). Re-raise after the last attempt.
    pass


def with_fallback(primary, fallback):
    # TODO: try primary(); on any exception log it and return fallback()
    pass
