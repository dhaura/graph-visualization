from openTSNE import TSNE

import utils

import numpy as np
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


import gzip
import pickle

with gzip.open("data/macosko_2015.pkl.gz", "rb") as f:
    data = pickle.load(f)

x = data["pca_50"]
y = data["CellType1"].astype(str)

print("Data set contains %d samples with %d features" % x.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.33, random_state=42)

print("%d training samples" % x_train.shape[0])
print("%d test samples" % x_test.shape[0])

# Setting up the TSNE model with specified parameters.
tsne = TSNE(
    perplexity=30,
    metric="euclidean",
    n_jobs=16,
    random_state=42,
    verbose=True,
)

# Fitting the model on the training set and transforming the test set.
embedding_train = tsne.fit(x_train)
print("\nTraining set embedding shape:", embedding_train.shape , "\n")
embedding_test = embedding_train.transform(x_test)
print("\nTest set embedding shape:", embedding_test.shape , "\n")

# Plotting train and test sets separately.
utils.plot(embedding_train, y_train, colors=utils.MACOSKO_COLORS, output_path="output/macosko_train.png")
utils.plot(embedding_test, y_test, colors=utils.MACOSKO_COLORS, output_path="output/macosko_test.png")

# Plotting both train and test sets together.
fig, ax = plt.subplots(figsize=(8, 8))
utils.plot(embedding_train, y_train, colors=utils.MACOSKO_COLORS, alpha=0.25, ax=ax)
utils.plot(embedding_test, y_test, colors=utils.MACOSKO_COLORS, alpha=0.75, ax=ax, output_path="output/macosko_combined.png")
