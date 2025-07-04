from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from scipy.io import mmwrite
import argparse
import numpy as np
import os

def build_knn_graph(data, k=10):
    nbrs = NearestNeighbors(n_neighbors=k+1, algorithm='auto').fit(data)
    distances, indices = nbrs.kneighbors(data)
    
    rows, cols, vals = [], [], []
    for i in range(len(indices)):
        for j in range(1, k+1):  # skip self-loop at j=0
            rows.append(i)
            cols.append(indices[i][j])
            vals.append(distances[i][j])

    adj_matrix = csr_matrix((vals, (rows, cols)), shape=(len(data), len(data)))
    return adj_matrix

parser = argparse.ArgumentParser(description="Generate k-NN graph from dataset.")
parser.add_argument("-input", required=True, type=str, help="Path to the input dataset directory.")
parser.add_argument("-output", required=True, type=str, help="Directory to save the output adjacency matrix.")
parser.add_argument("-dataset", required=True, type=str, help="Name of the dataset.")
parser.add_argument("-size", type=int, help="Size of the dataset subset to process.")
args = parser.parse_args()

size = args.size
subset = np.loadtxt(os.path.join(args.input, f"{args.dataset}_subset_{size}.txt"), dtype=np.float32)
print(f"Loaded subset of size {size} from {args.input}/{args.dataset}_subset_{size}.txt")
adj = build_knn_graph(subset, k=10)
print(f"Generated k-NN graph for {args.dataset} with size {size}.")
mmwrite(os.path.join(args.output, f"{args.dataset}_size_{size}_adjacency.mtx"), adj)
print(f"Saved adjacency matrix to {args.output}/{args.dataset}_size_{size}_adjacency.mtx\n")
