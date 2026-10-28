"""
Day 06 · Task 1 · Build: CLI expense tracker v1

Commands: add (amount, category, date), list, summary by category. Save to JSON.

Complete every TODO, run the file, then tick this task on the tracker.
"""
"""Expense tracker (CLI). Run: python day06/expense_tracker.py"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def load() -> list[dict]:
    # TODO: return the list from DATA_FILE, or [] if the file doesn't exist
    pass


def save(expenses: list[dict]) -> None:
    # TODO: write expenses to DATA_FILE as JSON
    pass


def add(expenses, amount: float, category: str, date: str) -> None:
    # TODO: append {"amount": ..., "category": ..., "date": ...} and save
    pass


def summary(expenses) -> dict[str, float]:
    # TODO: return total spent per category, e.g. {"food": 450.0, "travel": 120.0}
    pass


def main():
    expenses = load()
    while True:
        cmd = input("add / list / summary / quit > ").strip().lower()
        if cmd == "quit":
            break
        elif cmd == "add":
            # TODO: ask for amount, category and date, then call add()
            pass
        elif cmd == "list":
            # TODO: print each expense on one line
            pass
        elif cmd == "summary":
            # TODO: print summary(expenses)
            pass
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
