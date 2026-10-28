"""
Day 20 · Task 2 · AI & ML: Linear regression

Fit LinearRegression on a house-price dataset. Check MAE and RMSE.

Complete every TODO, run the file, then tick this task on the tracker.
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from sklearn.model_selection import train_test_split

# Use a house-price CSV from Kaggle, saved as day19/houses.csv
df = pd.read_csv("day19/houses.csv")
X = df[[...]]        # TODO: choose 3-5 numeric feature columns
y = df[...]          # TODO: the price column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TODO: fit LinearRegression, predict on X_test, print MAE and RMSE
