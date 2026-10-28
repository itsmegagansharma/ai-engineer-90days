"""
Day 22 · Task 1: SVM

Train SVC with linear and RBF kernels. Scale features first.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Reuse the Titanic features from day 21
for kernel in ["linear", "rbf"]:
    model = make_pipeline(StandardScaler(), SVC(kernel=kernel))
    # TODO: fit and print test accuracy
