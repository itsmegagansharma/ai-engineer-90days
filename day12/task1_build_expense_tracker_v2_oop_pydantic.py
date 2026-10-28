"""
Day 12 · Task 1 · Build: expense tracker v2 (OOP + Pydantic)

Rebuild day 6's tracker: an Expense Pydantic model, an ExpenseStore class that loads/saves JSON, and a summary by category.

Complete every TODO, run the file, then tick this task on the tracker.
"""
"""Expense tracker v2: classes + Pydantic + JSON."""
import json
from datetime import date
from pathlib import Path

from pydantic import BaseModel, Field


class Expense(BaseModel):
    amount: float = Field(gt=0)
    category: str
    spent_on: date = Field(default_factory=date.today)
    note: str = ""


class ExpenseStore:
    def __init__(self, path: Path):
        self.path = path
        self.items: list[Expense] = []

    def load(self) -> None:
        # TODO: read JSON if the file exists; build Expense objects with Expense.model_validate(...)
        pass

    def save(self) -> None:
        # TODO: write [e.model_dump(mode="json") for e in self.items]
        pass

    def add(self, expense: Expense) -> None:
        # TODO
        pass

    def summary(self) -> dict[str, float]:
        # TODO: total per category
        pass


if __name__ == "__main__":
    store = ExpenseStore(Path(__file__).parent / "expenses.json")
    store.load()
    # TODO: a small menu loop like v1, but using the store
