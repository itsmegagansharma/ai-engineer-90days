"""
Day 20 · Task 1 · Engineering: SQL from Python

Load a CSV into SQLite with pandas.to_sql, then query it with sqlite3 and pandas.read_sql.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import sqlite3
import pandas as pd

df = pd.read_csv("day11/clean.csv")
conn = sqlite3.connect("day19/data.db")
df.to_sql("records", conn, if_exists="replace", index=False)

questions = {
    "How many rows are there?": "SELECT COUNT(*) FROM records",
    # TODO: add 9 more questions with their SQL (use WHERE, GROUP BY, ORDER BY, AVG, etc.)
}

for q, sql in questions.items():
    print(q)
    print(pd.read_sql(sql, conn), "\n")
