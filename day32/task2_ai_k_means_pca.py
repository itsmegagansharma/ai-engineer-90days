"""
Day 32 · Task 2 · AI & ML: k-means & PCA

Cluster customers; choose k with the elbow method and silhouette score. Then: Reduce to 2D and plot clusters.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ===== Part 1: k-means =====
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


# ===== Part 2: PCA =====
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

digits = load_digits()      # 64 features per image

# TODO: reduce to 2D with PCA(n_components=2).fit_transform(digits.data)
# TODO: scatter plot coloured by digits.target; save as day32/pca.png
# TODO: print explained_variance_ratio_
