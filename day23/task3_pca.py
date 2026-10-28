"""
Day 23 · Task 3: PCA

Reduce to 2D and plot clusters.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

digits = load_digits()      # 64 features per image

# TODO: reduce to 2D with PCA(n_components=2).fit_transform(digits.data)
# TODO: scatter plot coloured by digits.target; save as day23/pca.png
# TODO: print explained_variance_ratio_
