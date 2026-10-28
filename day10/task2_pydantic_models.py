"""
Day 10 · Task 2: Pydantic models

pip install pydantic. Make class Expense(BaseModel) with amount: float, category: str.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install pydantic
from pydantic import BaseModel, Field


class Expense(BaseModel):
    # TODO: amount (float, must be > 0), category (str), note (str, optional, default "")
    pass


e = Expense(amount=250, category="food")
print(e)
print(e.model_dump())      # dict
print(e.model_dump_json()) # JSON string
