# graph-visualization

## openTSNE

```bash
module load conda
conda create -n tsne-env python=3.8
conda activate tsne-env
conda install -c conda-forge opentsne

```

## scikit-learn

```bash
module load python/3.10
python3 -m venv venv
source venv/bin/activate
pip3 install matplotlib numpy scipy
pip3 install -U scikit-learn
```
