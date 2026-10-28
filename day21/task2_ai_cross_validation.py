"""
Day 21 · Task 2 · AI & ML: Cross-validation

Use cross_val_score with 5 folds and compare to a single split.

Complete every TODO, run the file, then tick this task on the tracker.
"""
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Reuse X and y from task2
# TODO: scores = cross_val_score(LinearRegression(), X, y, cv=5, scoring="neg_mean_absolute_error")
# TODO: print each fold's MAE and the average. Is it close to your single split?
