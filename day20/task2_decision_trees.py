"""
Day 20 · Task 2: Decision trees

Train DecisionTreeClassifier, try max_depth values, plot the tree.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Reuse the Titanic X_train/X_test/y_train/y_test from task1
for depth in [2, 4, 8, None]:
    # TODO: fit DecisionTreeClassifier(max_depth=depth), print train and test accuracy
    pass

# TODO: plot the depth-3 tree with plot_tree(model, feature_names=X.columns, filled=True); save as day20/tree.png
# Comment: which depth overfits? How can you tell?
