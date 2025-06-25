import numpy as np
import struct
import os
import argparse

def read_fbin(filename):
    with open(filename, 'rb') as f:
        n = struct.unpack('i', f.read(4))[0]
        d = struct.unpack('i', f.read(4))[0]
        print(f"Loading {n} vectors of dimension {d} from {filename}")
        data = np.fromfile(f, dtype=np.float32, count=n * d).reshape(n, d)
    return data

def save_as_text(data, filename):
    print(f"Saving {data.shape[0]} vectors to {filename}")
    np.savetxt(filename, data, fmt='%.6f')

def create_subsets(base_data, sizes, out_dir, dataset):
    os.makedirs(out_dir, exist_ok=True)
    for size in sizes:
        subset = base_data[:size]
        save_as_text(subset, os.path.join(out_dir, f"{dataset}_subset_{size}.txt"))

parser = argparse.ArgumentParser()

parser.add_argument("-input", required=True, type=str)
parser.add_argument("-output", required=True, type=str)
parser.add_argument("-dataset", required=True, type=str)

args = parser.parse_args()

input_path = args.input
subset_sizes = [20000, 40000, 80000, 160000, 320000, 640000, 1000000] 
output_dir = args.output

base = read_fbin(input_path)
create_subsets(base, subset_sizes, output_dir, args.dataset)
