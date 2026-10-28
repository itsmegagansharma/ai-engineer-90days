"""
Day 10 · Task 3: Validation errors

Pass bad data and catch ValidationError. Add a Field(gt=0) constraint.

Complete every TODO, run the file, and tick this task on the tracker.
"""
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
