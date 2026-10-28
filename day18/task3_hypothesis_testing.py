"""
Day 18 · Task 3: Hypothesis testing

Run a t-test with scipy.stats.ttest_ind and explain the p-value in one sentence.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd
from scipy import stats

df = pd.read_csv("day16/clean.csv")

# Example with Titanic: do survivors have a higher average fare?
# group_a = df[df["Survived"] == 1]["Fare"]
# group_b = df[df["Survived"] == 0]["Fare"]

# TODO: run stats.ttest_ind(group_a, group_b) and print the p-value
# TODO: one sentence: what does this p-value mean?
