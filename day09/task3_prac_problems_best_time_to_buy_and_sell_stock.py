"""
Day 09 · Task 3 · Practice: Problems: Best Time to Buy and Sell Stock & Move Zeroes

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Best Time to Buy and Sell Stock ----------------
def max_profit(prices: list[int]) -> int:
    """Max profit from one buy then one later sell (0 if none). One pass, track the lowest price."""
    pass


# ---------------- Move Zeroes ----------------
def move_zeroes(nums: list[int]) -> list[int]:
    """Move all 0s to the end, keeping the order of the others. Modify in place and return nums."""
    pass


if __name__ == "__main__":
    # Best Time to Buy and Sell Stock
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    # Move Zeroes
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    print("All tests passed!")
