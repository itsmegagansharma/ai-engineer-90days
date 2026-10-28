"""
Day 13 · Task 3 · Practice: Problems: Valid Parentheses & Roman to Integer

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Valid Parentheses ----------------
def is_valid(s: str) -> bool:
    """Brackets ()[]{} must close in the right order. Use a stack (list)."""
    pass


# ---------------- Roman to Integer ----------------
def roman_to_int(s: str) -> int:
    """'XIV' -> 14. If a smaller value comes before a larger one, subtract it."""
    pass


if __name__ == "__main__":
    # Valid Parentheses
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert is_valid("{[]}")
    # Roman to Integer
    assert roman_to_int("III") == 3
    assert roman_to_int("MCMXCIV") == 1994
    print("All tests passed!")
