import argparse
from time import time
from sklearn import manifold
import numpy as np
from scipy.spatial import procrustes
from sklearn.neighbors import NearestNeighbors


def knn_overlap(orig_neighbors, emb_neighbors):
    overlaps = []
    for i in range(len(orig_neighbors)):
        orig_set = set(orig_neighbors[i])
        emb_set = set(emb_neighbors[i])
        overlap = len(orig_set & emb_set) / len(orig_set)
        overlaps.append(overlap)
    return np.mean(overlaps)

# Argument parser for command line arguments.
parser = argparse.ArgumentParser()

parser.add_argument("-input", required=True, type=str)
parser.add_argument("-n_jobs", required=True, type=int)
parser.add_argument("-perplexity", required=True, type=int)
parser.add_argument("-n_components", required=True, type=int)
parser.add_argument("-max_iter", required=True, type=int)

args = parser.parse_args()

# Load data.
X = np.loadtxt(args.input, dtype=float, delimiter=' ')

# Run t-SNE on the loaded data.
t0 = time()
tsne_1 = manifold.TSNE(
    n_components=args.n_components,
    init="random",
    random_state=0,
    perplexity=args.perplexity,
    max_iter=args.max_iter,
    n_jobs=args.n_jobs
)
Y_1 = tsne_1.fit_transform(X)
t1 = time()

t2 = time()
tsne_2 = manifold.TSNE(
    n_components=args.n_components,
    init="random",
    random_state=42,
    perplexity=args.perplexity,
    max_iter=args.max_iter,
    n_jobs=args.n_jobs
)
Y_2 = tsne_2.fit_transform(X)
t3 = time()

# Calculate average time taken for t-SNE.
avg_time = (t1 - t0 + t3 - t2) / 2
print(f"t-SNE completed in {avg_time:.4f} seconds with perplexity={args.perplexity}, "
      f"n_components={args.n_components}, max_iter={args.max_iter}, n_jobs={args.n_jobs}")

# Calculate Procrustes MSE for embedding stability.
_, tsne_1_aligned, tsne_2_aligned = procrustes(Y_1, Y_2)
mse = np.mean((tsne_1_aligned - tsne_2_aligned)**2)
print(f"Embedding stability (Procrustes MSE): {mse:.4e}")

# Calculate KNN overlap for link prediction.
k = 10

# Original space KNN.
knn_orig = NearestNeighbors(n_neighbors=k).fit(X)
orig_neighbors = knn_orig.kneighbors(return_distance=False)

# Embedding space KNN.
knn_emb = NearestNeighbors(n_neighbors=k).fit(Y_1)
emb_neighbors = knn_emb.kneighbors(return_distance=False)

link_pred_score = knn_overlap(orig_neighbors, emb_neighbors)
print(f"Link prediction score (KNN overlap): {link_pred_score:.4f}")
