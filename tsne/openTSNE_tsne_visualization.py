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

def load_images_from_ubyte(path):
    print(f"Loading images from {path}")
    if not path.endswith('.gz'):
        with open(path, 'rb') as f:
            _ = int.from_bytes(f.read(4), 'big')
            n = int.from_bytes(f.read(4), 'big')
            rows = int.from_bytes(f.read(4), 'big')
            cols = int.from_bytes(f.read(4), 'big')
            data = np.frombuffer(f.read(), dtype=np.uint8)
            return data.reshape(n, rows * cols)
    
    with gzip.open(path, 'rb') as f:
        _ = int.from_bytes(f.read(4), 'big')
        n = int.from_bytes(f.read(4), 'big')
        rows = int.from_bytes(f.read(4), 'big')
        cols = int.from_bytes(f.read(4), 'big')
        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data.reshape(n, rows * cols)

def load_labels_from_ubyte(path):
    print(f"Loading labels from {path}")
    if not path.endswith('.gz'):
        with open(path, 'rb') as f:
            _ = int.from_bytes(f.read(4), 'big')
            n = int.from_bytes(f.read(4), 'big')
            return np.frombuffer(f.read(), dtype=np.uint8)
    
    with gzip.open(path, 'rb') as f:
        _ = int.from_bytes(f.read(4), 'big')
        n = int.from_bytes(f.read(4), 'big')
        return np.frombuffer(f.read(), dtype=np.uint8)


# Argument parser for command line arguments.
parser = argparse.ArgumentParser()

parser.add_argument("-input", required=True, type=str)
parser.add_argument("-labels", required=True, type=str)
parser.add_argument("-input_type", required=True, type=int, default=0)
parser.add_argument("-output", required=True, type=str)
parser.add_argument("-n_jobs", required=True, type=int)
parser.add_argument("-perplexity", required=True, type=int)

args = parser.parse_args()

# Load data.
if (args.input_type == 0):
    images = load_images_from_ubyte(args.input)
    labels = load_labels_from_ubyte(args.labels)
elif (args.input_type == 1):
    images = load_images_from_ubyte(args.input)
    labels = np.loadtxt(args.labels, dtype=int, usecols=1)
elif (args.input_type == 2):
    images = np.loadtxt(args.input, dtype=float, delimiter=' ')
    labels = np.loadtxt(args.labels, dtype=int, usecols=1)

print(f"Loaded {images.shape[0]} samples with {images.shape[1]} features each.")

X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")

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

print(f"t-SNE visualization saved to {args.output}")

# Calculate KNNG classifier accuracy.
for n_neighbors in [10, 20, 50, 100]:
    t2 = time()
    knn = KNeighborsClassifier(n_neighbors=n_neighbors, n_jobs=args.n_jobs)
    knn.fit(Y_train, y_train)
    t3 = time()

    y_pred = knn.predict(Y_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"KNNG Classifier Accuracy: {acc:.4f} in {t3 - t2:.4f} seconds with n_neighbors={n_neighbors}")
