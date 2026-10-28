"""
Day 10 · Task 2 · AI & ML: Distributions, correlation & hypothesis tests

Plot histograms; compute df.corr(). Correlation is not causation. Then: Run a t-test with scipy.stats.ttest_ind and explain the p-value in one sentence.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Distributions and correlation =====
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("day11/clean.csv")

# TODO 1: plot a histogram of one numeric column and save it as day09/hist.png
# TODO 2: print df.corr(numeric_only=True)
# TODO 3: comment: which two columns are most correlated? Does one cause the other?


# ===== Part 2: Hypothesis testing =====
import pandas as pd
from scipy import stats

df = pd.read_csv("day11/clean.csv")

# Example with Titanic: do survivors have a higher average fare?
# group_a = df[df["Survived"] == 1]["Fare"]
# group_b = df[df["Survived"] == 0]["Fare"]

# TODO: run stats.ttest_ind(group_a, group_b) and print the p-value
# TODO: one sentence: what does this p-value mean?
