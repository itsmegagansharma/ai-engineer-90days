"""
Day 11 · Task 2: Fixtures and parametrize

Use @pytest.mark.parametrize for many inputs, a fixture for a temp file.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pytest
from calculator import add


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
