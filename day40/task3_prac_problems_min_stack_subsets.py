"""
Day 40 · Task 3 · Practice: Problems: Min Stack & Subsets

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Min Stack ----------------
class MinStack:
    """push, pop, top and get_min, all O(1). Hint: store (value, current_min) pairs."""

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass


# ---------------- Subsets ----------------
def subsets(nums: list[int]) -> list[list[int]]:
    """All possible subsets (backtracking, or build up from [[]])."""
    pass


if __name__ == "__main__":
    # Min Stack
    s = MinStack(); s.push(-2); s.push(0); s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0 and s.get_min() == -2
    # Subsets
    assert sorted(map(sorted, subsets([1, 2, 3]))) == sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    print("All tests passed!")
