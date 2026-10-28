"""
Day 20 · Task 3: Metrics

Confusion matrix, precision, recall, F1, ROC-AUC. Know when accuracy misleads.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Use your best model from task1 or task2
# TODO: print confusion_matrix(y_test, preds)
# TODO: print classification_report(y_test, preds)
# TODO: print roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
# Comment: when is accuracy misleading? (think: 99% of emails are not spam)
