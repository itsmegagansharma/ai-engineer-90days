"""
Day 24 · Task 1: Isolation Forest

Detect outliers in a credit-card transactions dataset (Kaggle).

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd
from sklearn.ensemble import IsolationForest

# Kaggle "Credit Card Fraud Detection" -> day24/creditcard.csv (big file: keep it out of git!)
df = pd.read_csv("day24/creditcard.csv").sample(20000, random_state=42)
X = df.drop(columns=["Class"])

# TODO: fit IsolationForest(contamination=0.002, random_state=42)
# TODO: preds = model.predict(X)  (-1 = anomaly)
# TODO: how many flagged anomalies are real frauds (Class == 1)?
