"""
Day 33 · Task 3 · Practice: Problems: Number of Islands & Climbing Stairs

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Number of Islands ----------------
def num_islands(grid: list[list[str]]) -> int:
    """Count groups of connected "1"s (up/down/left/right). DFS or BFS from each unvisited land cell."""
    pass


# ---------------- Climbing Stairs ----------------
def climb_stairs(n: int) -> int:
    """Ways to climb n steps taking 1 or 2 at a time. It's Fibonacci."""
    pass


if __name__ == "__main__":
    # Number of Islands
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(grid) == 3
    # Climbing Stairs
    assert climb_stairs(2) == 2
    assert climb_stairs(5) == 8
    print("All tests passed!")
