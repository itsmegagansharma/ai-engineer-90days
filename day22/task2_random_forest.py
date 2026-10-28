"""
Day 22 · Task 2: Random forest

RandomForestClassifier and feature_importances_.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# TODO: fit RandomForestClassifier(n_estimators=200, random_state=42)
# TODO: print test accuracy
# TODO: print feature importances sorted:
#   pd.Series(model.feature_importances_, index=X_train.columns).sort_values(ascending=False)
