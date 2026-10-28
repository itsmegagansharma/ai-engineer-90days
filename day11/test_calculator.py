"""
Day 11 · Task 1: First tests

pip install pytest. Write test_calculator.py with 5 assert tests. Run pytest -v.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# Run: pytest day11 -v
# Tests for day04's calculator. Copy calculator.py into day11/ or import it.

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5

# TODO: write 4 more tests: subtract, multiply, divide, and divide by zero returns None
