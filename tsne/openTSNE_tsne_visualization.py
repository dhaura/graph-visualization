import argparse
from time import time

from openTSNE import TSNE

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter

from sklearn import manifold
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import gzip

def load_images(path):
    print(f"Loading images from {path}")
    with gzip.open(path, 'rb') as f:
        _ = int.from_bytes(f.read(4), 'big')
        n = int.from_bytes(f.read(4), 'big')
        rows = int.from_bytes(f.read(4), 'big')
        cols = int.from_bytes(f.read(4), 'big')
        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data.reshape(n, rows * cols)

def load_labels(path):
    print(f"Loading labels from {path}")
    with gzip.open(path, 'rb') as f:
        _ = int.from_bytes(f.read(4), 'big')
        n = int.from_bytes(f.read(4), 'big')
        return np.frombuffer(f.read(), dtype=np.uint8)


# Argument parser for command line arguments.
parser = argparse.ArgumentParser()

parser.add_argument("-input", required=True)
parser.add_argument("-labels", required=True)
parser.add_argument("-output", required=True)
parser.add_argument("-n_jobs", required=True, type=int)
parser.add_argument("-perplexity", required=True, type=int)
parser.add_argument("-n_neighbors", required=True, type=int)

args = parser.parse_args()

# Load data.
images = load_images(args.input)
labels = load_labels(args.labels)

X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Setting up the TSNE model with specified parameters.
t0 = time()
tsne = TSNE(
    perplexity=args.perplexity,
    metric="euclidean",
    n_jobs=args.n_jobs,
    random_state=42,
    verbose=True,
)

# Fitting the model on the training set and transforming the test set.
Y_train = tsne.fit(X_train)
Y_test = Y_train.transform(X_test)
t1 = time()

print(f"t-SNE completed in {t1 - t0:.4f} seconds with perplexity={args.perplexity}, "
      f"n_jobs={args.n_jobs}")

# Calculate KNNG classifier accuracy.
t2 = time()
knn = KNeighborsClassifier(n_neighbors=args.n_neighbors, n_jobs=args.n_jobs)
knn.fit(Y_train, y_train)
t3 = time()

y_pred = knn.predict(Y_test)
acc = accuracy_score(y_test, y_pred)

print(f"KNNG Classifier Accuracy: {acc:.4f} in {t3 - t2:.4f} seconds with n_neighbors={args.n_neighbors}")

X = np.concatenate([X_train, X_test])
y = np.concatenate([y_train, y_test])
Y = np.concatenate([Y_train, Y_test])

# Plot the t-SNE embeddings.
plt.figure(figsize=(8, 6))
scatter = plt.scatter(Y[:, 0], Y[:, 1], c=y, cmap='tab10', s=10, alpha=0.7)
# plt.legend(*scatter.legend_elements(), title="Classes", loc='best')
# plt.title("t-SNE Visualization")
# plt.xlabel("Dim 1")
# plt.ylabel("Dim 2")
plt.xticks([])
plt.yticks([])
plt.box(False)
plt.tight_layout()

plt.savefig(args.output, dpi=300)
