"""
Day 16 · Task 2: Filter, sort, groupby

df[df.col > x], sort_values, groupby('cat').agg(...).

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd

df = pd.read_csv("day16/data.csv")

# TODO 1: filter rows where a numeric column is above its mean
# TODO 2: sort by that column, descending
# TODO 3: groupby a category column and compute mean + count with .agg(["mean", "count"])
