"""
Day 23 · Task 1: k-means

Cluster customers; choose k with the elbow method and silhouette score.

Complete every TODO, run the file, and tick this task on the tracker.
"""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# Practice data first; then try Kaggle "Mall Customers"
X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

inertias, silhouettes = [], []
for k in range(2, 9):
    # TODO: fit KMeans(n_clusters=k, n_init=10, random_state=42); store inertia_ and silhouette_score
    pass

# TODO: plot inertias (elbow) and pick k
