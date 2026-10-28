"""
Day 33 · Task 2 · AI & ML: DBSCAN & anomaly detection

Try DBSCAN on the same data and compare. Then: Detect outliers in a credit-card transactions dataset (Kaggle). Then: Flag z-score > 3 points and compare with Isolation Forest.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: DBSCAN =====
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

# TODO: try KMeans(n_clusters=2) and DBSCAN(eps=0.2, min_samples=5) on the moons
# TODO: plot both results side by side. Which one finds the moon shapes? Why?


# ===== Part 2: Isolation Forest =====
import pandas as pd
from sklearn.ensemble import IsolationForest

# Kaggle "Credit Card Fraud Detection" -> day33/creditcard.csv (big file: keep it out of git!)
df = pd.read_csv("day33/creditcard.csv").sample(20000, random_state=42)
X = df.drop(columns=["Class"])

# TODO: fit IsolationForest(contamination=0.002, random_state=42)
# TODO: preds = model.predict(X)  (-1 = anomaly)
# TODO: how many flagged anomalies are real frauds (Class == 1)?


# ===== Part 3: Statistical methods =====
import numpy as np

amounts = df["Amount"]
# TODO: z = (amounts - amounts.mean()) / amounts.std()
# TODO: flag rows where abs(z) > 3; compare with IsolationForest's flags
