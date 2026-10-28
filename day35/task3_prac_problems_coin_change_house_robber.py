"""
Day 35 · Task 3 · Practice: Problems: Coin Change & House Robber

Solve both in the starter file, then run it: every assert must pass. Your first dynamic programming problems.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Coin Change ----------------
def coin_change(coins: list[int], amount: int) -> int:
    """Fewest coins to make amount, or -1. Dynamic programming over amounts 0..amount."""
    pass


# ---------------- House Robber ----------------
def rob(nums: list[int]) -> int:
    """Max money without robbing two neighbours. dp[i] = max(dp[i-1], dp[i-2] + nums[i])."""
    pass


if __name__ == "__main__":
    # Coin Change
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    # House Robber
    assert rob([2, 7, 9, 3, 1]) == 12
    print("All tests passed!")
