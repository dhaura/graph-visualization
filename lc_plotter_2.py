import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("output/large_scale_results.csv")
df['Dataset Size'] = df['Dataset Size'].astype(int)
df['Link Prediction Accuracy'] = df['Link Prediction Accuracy'].astype(float)
df['Embedding Time'] = df['Embedding Time'].astype(float)
df = df.sort_values(by=["Dataset Size", "Dataset", "Method"])
unique_sizes = sorted(df['Dataset Size'].unique())
n_rows = len(unique_sizes)

sns.set(style="whitegrid", font_scale=0.9)

### ---------------- ACCURACY PLOT ---------------- ###
fig_acc, axes_acc = plt.subplots(nrows=n_rows, ncols=1, figsize=(10, 4 * n_rows))

# Handle single-row case
if n_rows == 1:
    axes_acc = [axes_acc]

for i, dataset_size in enumerate(unique_sizes):
    df_size = df[df['Dataset Size'] == dataset_size]
    ax = axes_acc[i]
    sns.barplot(data=df_size, x='Dataset', y='Link Prediction Accuracy', hue='Method', ax=ax, errorbar=None)
    ax.set_title(f"Dataset Size = {dataset_size} | Accuracy")
    ax.set_ylabel("Accuracy")
    ax.set_xlabel("Dataset")
    ax.tick_params(axis='x', rotation=30)
    ax.legend(loc='lower right')

fig_acc.suptitle("Large Scale Link Prediction Accuracy Comparison", fontsize=16)
fig_acc.tight_layout(rect=[0, 0.03, 1, 0.95])
fig_acc.savefig("output/large_scale_acc_plot_2.png", dpi=500)
print("Saved: output/large_scale_acc_plot_2.png")

### ---------------- TIME PLOT ---------------- ###
fig_time, axes_time = plt.subplots(nrows=n_rows, ncols=1, figsize=(10, 4 * n_rows))

if n_rows == 1:
    axes_time = [axes_time]

for i, dataset_size in enumerate(unique_sizes):
    df_size = df[df['Dataset Size'] == dataset_size]
    ax = axes_time[i]
    sns.barplot(data=df_size, x='Dataset', y='Embedding Time', hue='Method', ax=ax, errorbar=None)
    ax.set_title(f"Dataset Size = {dataset_size} | Embedding Time")
    ax.set_ylabel("Time (s)")
    ax.set_xlabel("Dataset")
    ax.tick_params(axis='x', rotation=30)
    ax.legend(loc='upper right')

fig_time.suptitle("Large Scale Embedding Time Comparison", fontsize=16)
fig_time.tight_layout(rect=[0, 0.03, 1, 0.95])
fig_time.savefig("output/large_scale_time_plot_2.png", dpi=500)
print("Saved: output/large_scale_time_plot_2.png")
