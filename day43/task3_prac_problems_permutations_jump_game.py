"""
Day 43 · Task 3 · Practice: Problems: Permutations & Jump Game

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Permutations ----------------
def permutations(nums: list[int]) -> list[list[int]]:
    """All orderings. Backtracking: choose, explore, un-choose."""
    pass


# ---------------- Jump Game ----------------
def can_jump(nums: list[int]) -> bool:
    """nums[i] = max jump from i. Can you reach the end? Track the furthest reachable index."""
    pass


if __name__ == "__main__":
    # Permutations
    assert len(permutations([1, 2, 3])) == 6
    # Jump Game
    assert can_jump([2, 3, 1, 1, 4])
    assert not can_jump([3, 2, 1, 0, 4])
    print("All tests passed!")
