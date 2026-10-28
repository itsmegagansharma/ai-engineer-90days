"""
Day 20 · Task 3 · Practice: Problems: Product of Array Except Self & Maximum Subarray

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Product of Array Except Self ----------------
def product_except_self(nums: list[int]) -> list[int]:
    """Without division: prefix products from the left, then multiply by suffix products from the right."""
    pass


# ---------------- Maximum Subarray ----------------
def max_subarray(nums: list[int]) -> int:
    """Largest sum of a contiguous subarray (Kadane's algorithm)."""
    pass


if __name__ == "__main__":
    # Product of Array Except Self
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    # Maximum Subarray
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("All tests passed!")
