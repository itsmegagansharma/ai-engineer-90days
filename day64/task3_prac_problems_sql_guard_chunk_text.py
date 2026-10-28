"""
Day 64 · Task 3 · Practice: Problems: SQL Guard & Chunk Text

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- SQL Guard ----------------
import re


def is_safe_select(sql: str) -> bool:
    """Allow a single SELECT statement only. Reject INSERT/UPDATE/DELETE/DROP/ALTER, comments and
    multiple statements. Your text-to-SQL agent must never run anything else."""
    pass


# ---------------- Chunk Text ----------------
def chunk(text: str, size: int, overlap: int) -> list[str]:
    """Split into chunks of `size` characters where each chunk starts `size - overlap` after the last."""
    pass


if __name__ == "__main__":
    # SQL Guard
    assert is_safe_select("SELECT name FROM users WHERE id = 3")
    assert not is_safe_select("DROP TABLE users")
    assert not is_safe_select("SELECT 1; DELETE FROM users")
    # Chunk Text
    assert chunk("abcdefghij", 4, 1) == ["abcd", "defg", "ghij"]
    assert chunk("abc", 5, 1) == ["abc"]
    print("All tests passed!")
