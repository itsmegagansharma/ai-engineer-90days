"""
Day 21 · Task 1: Feature engineering

Encode categories, scale numbers, create 2 new features.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd

df = pd.read_csv("day20/titanic.csv")

# TODO: create 2 new features, for example:
#   FamilySize = SibSp + Parch + 1
#   IsAlone = FamilySize == 1
#   Title extracted from Name ("Mr", "Mrs", "Miss"...)
