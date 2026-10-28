"""
Day 04 · Task 3 · Practice: Problems: Two Sum & Contains Duplicate

Solve both in the starter file, then run it: every assert must pass. Both are classic dictionary/set problems.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Two Sum ----------------
def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of the two numbers that add up to target. Use a dict for O(n)."""
    pass


# ---------------- Contains Duplicate ----------------
def contains_duplicate(nums: list[int]) -> bool:
    """True if any value appears at least twice. Hint: a set."""
    pass


if __name__ == "__main__":
    # Two Sum
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    # Contains Duplicate
    assert contains_duplicate([1, 2, 3, 1])
    assert not contains_duplicate([1, 2, 3, 4])
    print("All tests passed!")
