"""
Day 13 · Task 1 · Engineering: Testing with pytest

pip install pytest. Write test_calculator.py with 5 assert tests. Run pytest -v. Then: Use @pytest.mark.parametrize for many inputs, a fixture for a temp file.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: First tests =====
# Run: pytest day13 -v
# Tests for day05's calculator. Copy calculator.py into day13/ or import it.

from task1_eng_functions_arguments_docstrings import add, subtract, multiply, divide  # from day 5: copy task1_eng_functions_arguments_docstrings.py from day05/ into this folder


def test_add():
    assert add(2, 3) == 5

# TODO: write 4 more tests: subtract, multiply, divide, and divide by zero returns None


# ===== Part 2: Fixtures and parametrize =====
import pytest
from task1_eng_functions_arguments_docstrings import add  # from day 5: copy task1_eng_functions_arguments_docstrings.py from day05/ into this folder


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    # TODO: add 3 more cases, including floats
])
def test_add_many(a, b, expected):
    assert add(a, b) == expected


@pytest.fixture
def notes_file(tmp_path):
    path = tmp_path / "notes.json"
    path.write_text("[]")
    return path


def test_starts_empty(notes_file):
    # TODO: load the JSON from notes_file and assert it's an empty list
    pass
