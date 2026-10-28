"""
Day 20 · Task 1: Logistic regression

Train on Titanic. Predict survival.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("day20/titanic.csv")
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Age"] = df["Age"].fillna(df["Age"].median())

X = df[["Pclass", "Sex", "Age", "Fare"]]
y = df["Survived"]

# TODO: split, fit LogisticRegression(max_iter=1000), print accuracy on the test set
