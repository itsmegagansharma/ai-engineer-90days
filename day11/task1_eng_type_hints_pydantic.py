"""
Day 11 · Task 1 · Engineering: Type hints & Pydantic

Annotate all functions: def add(a: float, b: float) -> float. Try list[str], dict[str, int], str | None. Then: pip install pydantic. Make class Expense(BaseModel) with amount: float, category: str. Then: Pass bad data and catch ValidationError. Add a Field(gt=0) constraint.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Type hints =====
# Add type hints to every function. Then run: pip install mypy && mypy day11/task1_type_hints.py

def average(nums):
    return sum(nums) / len(nums)

def find_user(users, name):
    for u in users:
        if u["name"] == name:
            return u
    return None          # hint: return type is dict | None

def tag_counts(tags):
    counts = {}
    for t in tags:
        counts[t] = counts.get(t, 0) + 1
    return counts


# ===== Part 2: Pydantic models =====
# pip install pydantic
from pydantic import BaseModel, Field


class Expense(BaseModel):
    # TODO: amount (float, must be > 0), category (str), note (str, optional, default "")
    pass


e = Expense(amount=250, category="food")
print(e)
print(e.model_dump())      # dict
print(e.model_dump_json()) # JSON string


# ===== Part 3: Validation errors =====
from pydantic import BaseModel, Field, ValidationError


class Expense(BaseModel):
    amount: float = Field(gt=0)
    category: str


bad_inputs = [
    {"amount": -5, "category": "food"},
    {"amount": "abc", "category": "food"},
    {"category": "food"},
]

for data in bad_inputs:
    # TODO: try Expense(**data); catch ValidationError and print e.errors()[0]["msg"]
    pass
