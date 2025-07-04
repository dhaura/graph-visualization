import argparse
from time import time
from sklearn import manifold
import numpy as np
from scipy.spatial import procrustes
from sklearn.neighbors import NearestNeighbors

# Argument parser for command line arguments.
parser = argparse.ArgumentParser()

parser.add_argument("-input", required=True, type=str)
parser.add_argument("-output", required=True, type=str)
parser.add_argument("-n_jobs", required=True, type=int)
parser.add_argument("-perplexity", required=True, type=int)
parser.add_argument("-n_components", required=True, type=int)
parser.add_argument("-max_iter", required=True, type=int)

args = parser.parse_args()

# Load data.
X = np.loadtxt(args.input, dtype=float, delimiter=' ')

# Run t-SNE on the loaded data.
t0 = time()
tsne = manifold.TSNE(
    n_components=args.n_components,
    init="random",
    random_state=0,
    perplexity=args.perplexity,
    max_iter=args.max_iter,
    n_jobs=args.n_jobs
)
Y = tsne.fit_transform(X)
t1 = time()

print(f"t-SNE completed in {t1 - t0:.4f} seconds with perplexity={args.perplexity}, "
      f"n_components={args.n_components}, max_iter={args.max_iter}, n_jobs={args.n_jobs}")

def save_embeddings_txt(embeddings, filename):
    num_nodes, dim = embeddings.shape
    with open(filename, 'w') as f:  
        f.write(f"{num_nodes} {dim}\n")
        for i, emb in enumerate(embeddings):
            emb_str = ' '.join(map(str, emb))
            f.write(f"{i+1} {emb_str}\n")

save_embeddings_txt(Y, args.output)
