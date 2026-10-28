"""
Day 27 · Task 3 · Practice: Problems: 3Sum & Merge Intervals

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- 3Sum ----------------
def three_sum(nums: list[int]) -> list[list[int]]:
    """All unique triplets that sum to 0. Sort first, then two pointers."""
    pass


# ---------------- Merge Intervals ----------------
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Sort by start, then merge overlaps."""
    pass


if __name__ == "__main__":
    # 3Sum
    assert sorted(three_sum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    # Merge Intervals
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    print("All tests passed!")
