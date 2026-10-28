"""
Day 22 · Task 3: Gradient boosting

pip install xgboost; train XGBClassifier and compare all 4 models in a table.

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install xgboost
from xgboost import XGBClassifier

results = {}
# TODO: train XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=4)
# TODO: fill results with test accuracy for: LogisticRegression, SVM, RandomForest, XGBoost
# TODO: print a comparison table: pd.Series(results).sort_values()
