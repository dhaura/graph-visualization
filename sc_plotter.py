import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("output/small_scale_results.csv")
df['K'] = df['K'].astype(int)
df['KNN Classifier Accuracy'] = df['KNN Classifier Accuracy'].astype(float)
df['Total Time'] = df['Total Time'].astype(float)
df = df.sort_values(by=["K", "Dataset", "Method"])
unique_ks = sorted(df['K'].unique())
n_rows = len(unique_ks)

sns.set(style="whitegrid", font_scale=0.9)

### ---------------- ACCURACY PLOT ---------------- ###
fig_acc, axes_acc = plt.subplots(nrows=n_rows, ncols=1, figsize=(10, 4 * n_rows))

# Handle single-row case
if n_rows == 1:
    axes_acc = [axes_acc]

for i, k in enumerate(unique_ks):
    df_k = df[df['K'] == k]
    ax = axes_acc[i]
    sns.barplot(data=df_k, x='Dataset', y='KNN Classifier Accuracy', hue='Method', ax=ax, errorbar=None)
    ax.set_title(f"K = {k} | Accuracy")
    ax.set_ylabel("Accuracy")
    ax.set_xlabel("Dataset")
    ax.tick_params(axis='x', rotation=30)
    ax.legend(loc='lower right')

fig_acc.suptitle("Small Scale KNN Classifier Accuracy Comparison", fontsize=16)
fig_acc.tight_layout(rect=[0, 0.03, 1, 0.95])
fig_acc.savefig("output/small_scale_acc_plot.png", dpi=500)
print("Saved: output/small_scale_acc_plot.png")

### ---------------- TIME PLOT ---------------- ###
fig_time, axes_time = plt.subplots(nrows=n_rows, ncols=1, figsize=(10, 4 * n_rows))

if n_rows == 1:
    axes_time = [axes_time]

for i, k in enumerate(unique_ks):
    df_k = df[df['K'] == k]
    ax = axes_time[i]
    sns.barplot(data=df_k, x='Dataset', y='Total Time', hue='Method', ax=ax, errorbar=None)
    ax.set_title(f"K = {k} | Total Time")
    ax.set_ylabel("Time (s)")
    ax.set_xlabel("Dataset")
    ax.tick_params(axis='x', rotation=30)
    ax.legend(loc='upper right')

fig_time.suptitle("Small Scale Total Time Comparison", fontsize=16)
fig_time.tight_layout(rect=[0, 0.03, 1, 0.95])
fig_time.savefig("output/small_scale_time_plot.png", dpi=500)
print("Saved: output/small_scale_time_plot.png")
