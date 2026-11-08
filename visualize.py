"""
Project 2: Data Visualization with Matplotlib & Seaborn
Dataset: Tips Dataset

This script generates:
- Individual plots for each analytical question in 'figures/'
- Combined 2x2 overview dashboard ('tips_overview.png')
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set matplotlib cache directory to temp
os.environ['MPLCONFIGDIR'] = os.environ.get('TEMP', '.')

# Directory paths
base_dir = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(base_dir, "figures")
os.makedirs(figures_dir, exist_ok=True)

# Load data
csv_path = os.path.join(base_dir, "tips.csv")
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
elif os.path.exists("tips.csv"):
    df = pd.read_csv("tips.csv")
else:
    df = sns.load_dataset("tips")

# Set theme
sns.set_theme(style="whitegrid", palette="colorblind")
plt.rcParams['font.sans-serif'] = 'Arial'

day_order = ["Thur", "Fri", "Sat", "Sun"]

# -----------------------------------------------------------
# Chart 1: Histogram - Total Bill Distribution
# -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5))
sns.histplot(df["total_bill"], bins=20, kde=True, ax=ax, color="#1f77b4")
median_val = df["total_bill"].median()
ax.axvline(median_val, color="red", linestyle="--", label=f"Median (${median_val:.2f})")
ax.set_title("Most Bills Are Between $10 and $25", fontsize=13, fontweight="bold")
ax.set_xlabel("Total Bill (USD)", fontsize=11)
ax.set_ylabel("Number of Meals", fontsize=11)
ax.set_xlim(left=0)
ax.legend()
plt.tight_layout()
fig.savefig(os.path.join(figures_dir, "01_bill_distribution.png"), dpi=150)
plt.close(fig)

# -----------------------------------------------------------
# Chart 2: Box Plot - Tips by Day
# -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x="day", y="tip", hue="day", legend=False, order=day_order, palette="Blues", ax=ax)
ax.set_title("Tips by Day: Weekends Show Greater Spread", fontsize=13, fontweight="bold")
ax.set_xlabel("Day of the Week", fontsize=11)
ax.set_ylabel("Tip (USD)", fontsize=11)
ax.set_ylim(bottom=0)
plt.tight_layout()
fig.savefig(os.path.join(figures_dir, "02_tips_by_day.png"), dpi=150)
plt.close(fig)

# -----------------------------------------------------------
# Chart 3: Scatter Plot - Total Bill vs Tip
# -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time",
    palette={"Lunch": "#1f77b4", "Dinner": "#ff7f0e"},
    alpha=0.8,
    s=60,
    ax=ax
)
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    scatter=False,
    color="gray",
    line_kws={"linestyle": "--", "linewidth": 1.5},
    ax=ax
)
ax.set_title("Bigger Bills Bring Bigger Tips", fontsize=13, fontweight="bold")
ax.set_xlabel("Total Bill (USD)", fontsize=11)
ax.set_ylabel("Tip (USD)", fontsize=11)
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.legend(title="Time")
plt.tight_layout()
fig.savefig(os.path.join(figures_dir, "03_bill_vs_tip.png"), dpi=150)
plt.close(fig)

# -----------------------------------------------------------
# Chart 4: Correlation Heatmap
# -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 5))
corr = df.select_dtypes("number").corr()
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", linewidths=1, ax=ax)
ax.set_title("Total Bill and Tip Have Strongest Correlation (0.68)", fontsize=12, fontweight="bold")
plt.tight_layout()
fig.savefig(os.path.join(figures_dir, "04_correlation_heatmap.png"), dpi=150)
plt.close(fig)

# -----------------------------------------------------------
# Chart 5: Bar Chart - Average Bill by Day
# -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(data=df, x="day", y="total_bill", hue="day", legend=False, order=day_order, palette="Blues_d", errorbar=None, ax=ax)
ax.set_title("Average Total Bill by Day: Sunday Is Highest", fontsize=13, fontweight="bold")
ax.set_xlabel("Day of the Week", fontsize=11)
ax.set_ylabel("Average Total Bill (USD)", fontsize=11)
ax.set_ylim(bottom=0)
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f"${height:.2f}",
                xy=(p.get_x() + p.get_width() / 2, height),
                xytext=(0, 4),
                textcoords="offset points",
                ha="center", va="bottom", fontsize=10, fontweight="bold")
plt.tight_layout()
fig.savefig(os.path.join(figures_dir, "05_average_bill_by_day.png"), dpi=150)
plt.close(fig)

# -----------------------------------------------------------
# Combined 2x2 Dashboard Figure
# -----------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Chart 1: Histplot
sns.histplot(df["total_bill"], bins=20, ax=axes[0, 0], color="#1f77b4")
axes[0, 0].set_title(r"Most Bills Are Between \$10 and \$25", fontsize=12, fontweight="bold")
axes[0, 0].set_xlabel("Total Bill (USD)")
axes[0, 0].set_ylabel("Number of Meals")
axes[0, 0].set_xlim(left=0)

# Chart 2: Boxplot
sns.boxplot(data=df, x="day", y="tip", hue="day", legend=False, order=day_order, palette="Blues", ax=axes[0, 1])
axes[0, 1].set_title("Tips by Day: Weekends Show Greater Spread", fontsize=12, fontweight="bold")
axes[0, 1].set_xlabel("Day")
axes[0, 1].set_ylabel("Tip (USD)")
axes[0, 1].set_ylim(bottom=0)

# Chart 3: Scatterplot
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time",
    palette={"Lunch": "#1f77b4", "Dinner": "#ff7f0e"},
    alpha=0.8,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Bigger Bills Bring Bigger Tips", fontsize=12, fontweight="bold")
axes[1, 0].set_xlabel("Total Bill (USD)")
axes[1, 0].set_ylabel("Tip (USD)")
axes[1, 0].set_xlim(left=0)
axes[1, 0].set_ylim(bottom=0)

# Chart 4: Heatmap
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", linewidths=1, ax=axes[1, 1])
axes[1, 1].set_title("Total Bill and Tip Have Strongest Correlation (0.68)", fontsize=12, fontweight="bold")

plt.tight_layout()
overview_path = os.path.join(base_dir, "tips_overview.png")
fig.savefig(overview_path, dpi=150)
plt.close(fig)

print("Dashboard and figures updated successfully.")
