"""
Day 16 · Task 3: Clean

Handle missing values (fillna/dropna), merge two tables, apply a function.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd

df = pd.read_csv("day16/data.csv")

# TODO 1: print missing values per column: df.isna().sum()
# TODO 2: fill numeric gaps with the median, drop rows missing a key column
# TODO 3: add a new column using .apply()
# TODO 4: save the cleaned data to day16/clean.csv
