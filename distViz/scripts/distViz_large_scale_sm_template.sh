#!/bin/bash
#SBATCH --qos=regular
#SBATCH --time=8:00:00
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=64
#SBATCH --constraint=cpu
#SBATCH --output=logs/%j.log


export OMP_NUM_THREADS=128

module load intel
srun -n 1 --cpu-bind=cores ~/repos/HipGraph/DistViz/build/bin/distviz -input $SCRATCH/datasets/graph-viz/BIG_ANN/BIG_ANN_subset_1000000.txt -output ~/repos/graph-visualization/distViz/output -data-set-size 1000000 -dimension 128  -ntrees 32  -nn 10  -locality 0 -data-file-format 4 -tree-depth-ratio 0.8 -generate-knng-output 1 -dropout-error-th 0.013  -lr 0.25 -sparse-input 0 -nsamples 5 -iterations 1200 
