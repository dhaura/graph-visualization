import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
df = pd.read_csv("output/large_scale_results.csv")

# Type casting
df['Dataset Size'] = df['Dataset Size'].astype(int)
df['Embedding Time'] = df['Embedding Time'].astype(float)
df['Link Prediction Accuracy'] = df['Link Prediction Accuracy'].astype(float)
df = df.sort_values(by=["Dataset", "Dataset Size", "Method"])

datasets = df['Dataset'].unique()
n_rows = len(datasets)

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

sns.set(style="whitegrid", font_scale=0.9)

# ---- Accuracy ----
fig_acc, axes_acc = plt.subplots(nrows=n_rows, ncols=1, figsize=(10, 4 * n_rows))
if n_rows == 1:
    axes_acc = [axes_acc]

for i, dataset in enumerate(datasets):
    df_d = df[df['Dataset'] == dataset]
    ax = axes_acc[i]
    sns.barplot(data=df_d, x="Dataset Size", y="Link Prediction Accuracy", hue="Method", ax=ax, errorbar=None)
    ax.set_title(f"{dataset} | Accuracy")
    ax.set_ylabel("Accuracy")
    ax.set_xlabel("Dataset Size")

fig_acc.suptitle("Large Scale Link Prediction Accuracy by Dataset Size", fontsize=16)
fig_acc.tight_layout(rect=[0, 0.03, 1, 0.95])
fig_acc.savefig("output/large_scale_acc_plot.png", dpi=500)
print("Saved: output/large_scale_acc_plot.png")

# ---- Embedding Time ----
fig_time, axes_time = plt.subplots(nrows=n_rows, ncols=1, figsize=(10, 4 * n_rows))
if n_rows == 1:
    axes_time = [axes_time]

for i, dataset in enumerate(datasets):
    df_d = df[df['Dataset'] == dataset]
    ax = axes_time[i]
    sns.barplot(data=df_d, x="Dataset Size", y="Embedding Time", hue="Method", ax=ax, errorbar=None)
    ax.set_title(f"{dataset} | Embedding Time")
    ax.set_ylabel("Time (s)")
    ax.set_xlabel("Dataset Size")

fig_time.suptitle("Large Scale Embedding Time by Dataset Size", fontsize=16)
fig_time.tight_layout(rect=[0, 0.03, 1, 0.95])
fig_time.savefig("output/large_scale_time_plot.png", dpi=500)
print("Saved: output/large_scale_time_plot.png")
