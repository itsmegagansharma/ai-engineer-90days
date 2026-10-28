"""
Day 22 · Task 2 · AI & ML: Logistic regression & decision trees

Train on Titanic. Predict survival. Then: Train DecisionTreeClassifier, try max_depth values, plot the tree.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: Logistic regression =====
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("day22/titanic.csv")
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Age"] = df["Age"].fillna(df["Age"].median())

X = df[["Pclass", "Sex", "Age", "Fare"]]
y = df["Survived"]

# TODO: split, fit LogisticRegression(max_iter=1000), print accuracy on the test set


# ===== Part 2: Decision trees =====
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Reuse the Titanic X_train/X_test/y_train/y_test from task1
for depth in [2, 4, 8, None]:
    # TODO: fit DecisionTreeClassifier(max_depth=depth), print train and test accuracy
    pass

# TODO: plot the depth-3 tree with plot_tree(model, feature_names=X.columns, filled=True); save as day22/tree.png
# Comment: which depth overfits? How can you tell?
