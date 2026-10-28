"""
Day 11 · Task 2 · AI & ML: Pandas: load, filter & group

read_csv, head, info, describe on a Kaggle dataset. Then: df[df.col > x], sort_values, groupby('cat').agg(...).

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Load and inspect =====
import pandas as pd

# Download any CSV from Kaggle (e.g. "Titanic") into day11/data.csv
df = pd.read_csv("day11/data.csv")

# TODO: print df.head(), df.info(), df.describe()
# TODO: print the column names and the number of rows


# ===== Part 2: Filter, sort, groupby =====
import pandas as pd

df = pd.read_csv("day11/data.csv")

# TODO 1: filter rows where a numeric column is above its mean
# TODO 2: sort by that column, descending
# TODO 3: groupby a category column and compute mean + count with .agg(["mean", "count"])
