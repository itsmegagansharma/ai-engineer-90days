"""
Day 09 · Task 3: @dataclass

Rewrite Expense as a dataclass with type hints.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from dataclasses import dataclass, field
from datetime import date


# TODO: turn this into a dataclass with type hints:
#   amount: float, category: str, spent_on: date = today, tags: list[str] = empty list
#   (hint: field(default_factory=list) for lists)
class Expense:
    pass


# Then refactor day07/expense_tracker.py to use Expense objects instead of dicts.
