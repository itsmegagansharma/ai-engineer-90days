"""
Day 10 · Task 1 · Engineering: Inheritance, dunder methods & dataclasses

SavingsAccount(BankAccount) adds interest. Call super().__init__. Then: Add __repr__ and __eq__ so objects print nicely and compare. Then: Rewrite Expense as a dataclass with type hints.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Inheritance and super() =====
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.04):
        # TODO: call super().__init__(owner, balance), then store rate
        pass

    def add_interest(self) -> None:
        # TODO: increase balance by balance * rate
        pass


s = SavingsAccount("Gagan", 1000)
s.add_interest()
print(s.balance)   # 1040.0


# ===== Part 2: Dunder methods =====
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: __repr__ so print(Point(1, 2)) shows Point(x=1, y=2)

    # TODO: __eq__ so Point(1, 2) == Point(1, 2) is True

    # TODO (stretch): __add__ so Point(1, 2) + Point(3, 4) == Point(4, 6)


print(Point(1, 2))
print(Point(1, 2) == Point(1, 2))


# ===== Part 3: @dataclass =====
from dataclasses import dataclass, field
from datetime import date


# TODO: turn this into a dataclass with type hints:
#   amount: float, category: str, spent_on: date = today, tags: list[str] = empty list
#   (hint: field(default_factory=list) for lists)
class Expense:
    pass


# Then refactor day06/expense_tracker.py to use Expense objects instead of dicts.
