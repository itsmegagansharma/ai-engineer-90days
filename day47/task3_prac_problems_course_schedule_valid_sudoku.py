"""
Day 47 · Task 3 · Practice: Problems: Course Schedule & Valid Sudoku

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Course Schedule ----------------
def can_finish(n: int, prereqs: list[list[int]]) -> bool:
    """Can you finish all courses? Detect a cycle in a directed graph (topological sort)."""
    pass


# ---------------- Valid Sudoku ----------------
def is_valid_sudoku(board: list[list[str]]) -> bool:
    """Only filled cells need checking: no repeats in any row, column or 3x3 box. Use sets."""
    pass


if __name__ == "__main__":
    # Course Schedule
    assert can_finish(2, [[1, 0]])
    assert not can_finish(2, [[1, 0], [0, 1]])
    # Valid Sudoku
    b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    assert is_valid_sudoku(b)
    print("All tests passed!")
