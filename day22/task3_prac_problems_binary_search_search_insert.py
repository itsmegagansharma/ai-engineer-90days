"""
Day 22 · Task 3 · Practice: Problems: Binary Search & Search Insert Position

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Binary Search ----------------
def binary_search(nums: list[int], target: int) -> int:
    """Index of target in sorted nums, or -1. O(log n)."""
    pass


# ---------------- Search Insert Position ----------------
def search_insert(nums: list[int], target: int) -> int:
    """Index where target is, or where it would be inserted to keep order."""
    pass


if __name__ == "__main__":
    # Binary Search
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    # Search Insert Position
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    print("All tests passed!")
