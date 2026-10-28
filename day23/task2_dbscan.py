"""
Day 23 · Task 2: DBSCAN

Try DBSCAN on the same data and compare.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

# TODO: try KMeans(n_clusters=2) and DBSCAN(eps=0.2, min_samples=5) on the moons
# TODO: plot both results side by side. Which one finds the moon shapes? Why?
