"""
Day 31 · Task 2 · AI & ML: SVM, random forest & XGBoost

Train SVC with linear and RBF kernels. Scale features first. Then: RandomForestClassifier and feature_importances_. Then: pip install xgboost; train XGBClassifier and compare all 4 models in a table.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: SVM =====
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Reuse the Titanic features from day 21
for kernel in ["linear", "rbf"]:
    model = make_pipeline(StandardScaler(), SVC(kernel=kernel))
    # TODO: fit and print test accuracy


# ===== Part 2: Random forest =====
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# TODO: fit RandomForestClassifier(n_estimators=200, random_state=42)
# TODO: print test accuracy
# TODO: print feature importances sorted:
#   pd.Series(model.feature_importances_, index=X_train.columns).sort_values(ascending=False)


# ===== Part 3: Gradient boosting =====
# pip install xgboost
from xgboost import XGBClassifier

results = {}
# TODO: train XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=4)
# TODO: fill results with test accuracy for: LogisticRegression, SVM, RandomForest, XGBoost
# TODO: print a comparison table: pd.Series(results).sort_values()
