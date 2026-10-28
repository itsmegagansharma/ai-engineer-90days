"""
Day 38 · Task 3 · Practice: Problems: Kth Largest Element & Daily Temperatures

Solve both in the starter file, then run it: every assert must pass. Heaps and stacks.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Kth Largest Element ----------------
import heapq


def kth_largest(nums: list[int], k: int) -> int:
    """Keep a min-heap of size k with heapq."""
    pass


# ---------------- Daily Temperatures ----------------
def daily_temperatures(temps: list[int]) -> list[int]:
    """Days to wait for a warmer day (0 if never). Use a stack of indices."""
    pass


if __name__ == "__main__":
    # Kth Largest Element
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    # Daily Temperatures
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    print("All tests passed!")
