"""
Day 03 · Task 1: if / elif / else

Write a grade calculator: 90+ A, 75+ B, etc.

Complete every TODO, run the file, and tick this task on the tracker.
"""
def grade(score: int) -> str:
    """Return A (90+), B (75+), C (60+), D (40+) or F."""
    # TODO: use if / elif / else
    pass


if __name__ == "__main__":
    for s in [95, 80, 61, 45, 10]:
        print(s, grade(s))   # expected: A B C D F
