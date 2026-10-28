"""
Day 09 · Task 2 · AI & ML: Descriptive statistics

Mean, median, std, percentiles on yesterday's data.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import pandas as pd

df = pd.read_csv("day11/clean.csv")
col = df.select_dtypes("number").columns[0]   # TODO: pick a column that interests you

# TODO: print mean, median, std, and the 25th/75th percentiles of df[col]
# TODO: in a comment, explain why mean and median differ (if they do)
