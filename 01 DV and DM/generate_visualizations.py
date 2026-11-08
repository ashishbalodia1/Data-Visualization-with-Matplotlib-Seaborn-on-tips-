"""
Project 02: Data Visualization with Matplotlib & Seaborn
InternCircle Data Science & AI Project

This script loads the tips dataset, performs exploratory data analysis,
and creates publication-ready, honest visualizations with Seaborn and Matplotlib.
It produces:
1. Individual high-resolution plots in 'figures/'
2. Combined 2x2 dashboard images ('tips_overview.png' and 'tips_dashboard.png')
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set Matplotlib temp directory to avoid permission warnings
os.environ['MPLCONFIGDIR'] = os.environ.get('TEMP', '.')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# 1. Load Dataset
data_path = os.path.join(SCRIPT_DIR, 'tips.csv')
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    df = sns.load_dataset('tips')
    df.to_csv(data_path, index=False)

print(f"Loaded tips dataset: {len(df)} rows, {len(df.columns)} columns.")

# 2. Global Styling & Theme Configuration
sns.set_theme(style="whitegrid", font="sans-serif")
plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
    'axes.labelweight': 'semibold',
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.titlesize': 16,
    'figure.titleweight': 'bold',
})

# Accessible, color-blind friendly palette
accessible_palette = sns.color_palette("colorblind")
primary_blue = accessible_palette[0]
warm_amber = accessible_palette[1]
subtle_teal = accessible_palette[2]
day_order = ['Thur', 'Fri', 'Sat', 'Sun']

figures_dir = os.path.join(SCRIPT_DIR, 'figures')
os.makedirs(figures_dir, exist_ok=True)

# -------------------------------------------------------------
# Chart 1: Histogram - Bill Distribution
# Question: How are total meal bills distributed among dining parties?
# Takeaway: Most bills cluster between $10 and $25, with a pronounced right skew toward higher spending.
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 5.5))
sns.histplot(
    data=df,
    x="total_bill",
    bins=24,
    kde=True,
    color=primary_blue,
    edgecolor="white",
    alpha=0.75,
    ax=ax
)
median_val = df['total_bill'].median()
mean_val = df['total_bill'].mean()
ax.axvline(median_val, color='#d95f02', linestyle='--', linewidth=2,
           label=f"Median Bill: ${median_val:.2f}")
ax.axvline(mean_val, color='#1b9e77', linestyle=':', linewidth=2,
           label=f"Mean Bill: ${mean_val:.2f}")

ax.set_title("Distribution of Total Bills: Peak Concentration Between $10 and $25", pad=12)
ax.set_xlabel("Total Bill (USD)", labelpad=8)
ax.set_ylabel("Number of Dining Parties", labelpad=8)
ax.set_xlim(left=0, right=55)
ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper right')

# Add explicit takeaway annotation under the chart
fig.text(0.5, 0.01, "Takeaway: Most bills cluster between $10 and $25, with a pronounced right skew toward higher spending.",
         ha='center', fontsize=10, style='italic', color='#2b2b2b')

plt.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(os.path.join(figures_dir, '01_bill_distribution_histogram.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Chart 2: Box Plot - Tips by Day of Week
# Question: Do tipping amounts and variability differ across days of the week?
# Takeaway: Weekend meals feature wider tip variance and the highest top-end tips compared to weekdays.
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 5.5))
sns.boxplot(
    data=df,
    x="day",
    y="tip",
    hue="day",
    legend=False,
    order=day_order,
    palette="Blues",
    boxprops=dict(alpha=0.85),
    flierprops=dict(marker='o', markersize=6, markerfacecolor='#e7298a', markeredgecolor='black', alpha=0.8),
    ax=ax
)
ax.set_title("Tips by Day: Weekend Dining Yields Greater Spread and Top Outliers", pad=12)
ax.set_xlabel("Day of the Week", labelpad=8)
ax.set_ylabel("Tip Amount (USD)", labelpad=8)
ax.set_ylim(bottom=0, top=11)

fig.text(0.5, 0.01, "Takeaway: Weekend tips exhibit wider variance and reach higher peak amounts (up to $10) than weekday tips.",
         ha='center', fontsize=10, style='italic', color='#2b2b2b')

plt.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(os.path.join(figures_dir, '02_tips_by_day_boxplot.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Chart 3: Scatter Plot - Total Bill vs Tip
# Question: Does a bigger bill mean a bigger tip, and does time of day alter this pattern?
# Takeaway: Tips increase reliably with total bill size across both lunch and dinner sittings.
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 5.5))
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time",
    palette={'Lunch': primary_blue, 'Dinner': warm_amber},
    style="time",
    s=75,
    alpha=0.85,
    edgecolor="black",
    linewidth=0.5,
    ax=ax
)
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    scatter=False,
    color="#2c3e50",
    line_kws={"linestyle": "--", "linewidth": 1.8, "alpha": 0.8, "label": "Linear Fit"},
    ax=ax
)
ax.set_title("Bill Size vs. Tip: Strong Positive Linear Relationship Across Dining Times", pad=12)
ax.set_xlabel("Total Bill (USD)", labelpad=8)
ax.set_ylabel("Tip Amount (USD)", labelpad=8)
ax.set_xlim(left=0, right=55)
ax.set_ylim(bottom=0, top=11)
ax.legend(title="Dining Time", frameon=True, facecolor='white', framealpha=0.9, loc='upper left')

fig.text(0.5, 0.01, "Takeaway: Larger bills consistently bring larger tips, maintaining an approximate 15-18% reward rate across meal times.",
         ha='center', fontsize=10, style='italic', color='#2b2b2b')

plt.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(os.path.join(figures_dir, '03_bill_vs_tip_scatterplot.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Chart 4: Correlation Heatmap - Numerical Features
# Question: Which numerical metrics move together most strongly in the dataset?
# Takeaway: Total bill and tip share the strongest correlation (r = 0.68), while party size has moderate influence.
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 6))
numeric_df = df.select_dtypes(include=['number'])
corr = numeric_df.corr()
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="YlGnBu",
    vmin=0,
    vmax=1,
    cbar_kws={'label': 'Pearson Correlation (r)'},
    linewidths=2,
    linecolor='white',
    annot_kws={"size": 13, "weight": "bold"},
    ax=ax
)
ax.set_title("Correlation Matrix: Bill and Tip Display the Strongest Association (r = 0.68)", pad=14)

fig.text(0.5, 0.01, "Takeaway: Bill size is the strongest predictor of tip amount (r = 0.68), followed by party size and bill (r = 0.60).",
         ha='center', fontsize=10, style='italic', color='#2b2b2b')

plt.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(os.path.join(figures_dir, '04_correlation_heatmap.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Chart 5: Bar Chart - Average Spend by Day (Honest Zero Baseline)
# Question: Which day generates the highest average meal spend per party?
# Takeaway: Average customer spend peaks on Sunday ($21.41) and Saturday ($20.44), surpassing weekdays.
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 5.5))
day_spend = df.groupby('day', observed=False)['total_bill'].mean().reindex(day_order)
day_sem = df.groupby('day', observed=False)['total_bill'].sem().reindex(day_order)

sns.barplot(
    data=df,
    x="day",
    y="total_bill",
    hue="day",
    legend=False,
    order=day_order,
    palette="Blues_d",
    errorbar='se',
    capsize=0.12,
    edgecolor="black",
    linewidth=0.8,
    ax=ax
)
# Ensure honest zero baseline
ax.set_ylim(bottom=0, top=26)
for i, v in enumerate(day_spend):
    err = day_sem[i]
    ax.text(i, v + err + 0.8, f"${v:.2f}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1a1a1a')

ax.set_title("Average Spend by Day: Weekend Parties Spend Significantly More Than Weekday Diners", pad=12)
ax.set_xlabel("Day of the Week", labelpad=8)
ax.set_ylabel("Mean Total Bill (USD)", labelpad=8)

fig.text(0.5, 0.01, "Takeaway: Weekend parties generate higher average checks ($20.44 - $21.41) compared to Thursday ($17.68) and Friday ($17.15).",
         ha='center', fontsize=10, style='italic', color='#2b2b2b')

plt.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(os.path.join(figures_dir, '05_average_bill_by_day_barchart.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Combined 2x2 Dashboard Figure
# Fits all 4 required question archetypes into a clean presentation image
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10.5))

# Top-Left: Histogram
sns.histplot(
    data=df,
    x="total_bill",
    bins=20,
    kde=True,
    color=primary_blue,
    edgecolor="white",
    alpha=0.75,
    ax=axes[0, 0]
)
axes[0, 0].axvline(median_val, color='#d95f02', linestyle='--', linewidth=1.8,
                   label=f"Median (${median_val:.2f})")
axes[0, 0].set_title("A. Total Bill Distribution: Most Bills Are Under $25", pad=8)
axes[0, 0].set_xlabel("Total Bill (USD)", labelpad=6)
axes[0, 0].set_ylabel("Number of Meals", labelpad=6)
axes[0, 0].set_xlim(left=0)
axes[0, 0].legend(loc="upper right", frameon=True)

# Top-Right: Boxplot
sns.boxplot(
    data=df,
    x="day",
    y="tip",
    hue="day",
    legend=False,
    order=day_order,
    palette="Blues",
    boxprops=dict(alpha=0.85),
    flierprops=dict(marker='o', markersize=5, markerfacecolor='#e7298a', markeredgecolor='black', alpha=0.7),
    ax=axes[0, 1]
)
axes[0, 1].set_title("B. Tips by Day: Weekend Dining Shows Wider Tip Variance", pad=8)
axes[0, 1].set_xlabel("Day of the Week", labelpad=6)
axes[0, 1].set_ylabel("Tip Amount (USD)", labelpad=6)
axes[0, 1].set_ylim(bottom=0)

# Bottom-Left: Scatterplot
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time",
    palette={'Lunch': primary_blue, 'Dinner': warm_amber},
    s=55,
    alpha=0.8,
    edgecolor="black",
    linewidth=0.5,
    ax=axes[1, 0]
)
sns.regplot(
    data=df,
    x="total_bill",
    y="tip",
    scatter=False,
    color="#2c3e50",
    line_kws={"linestyle": "--", "linewidth": 1.5, "alpha": 0.8},
    ax=axes[1, 0]
)
axes[1, 0].set_title("C. Bill vs. Tip: Bigger Bills Bring Bigger Tips", pad=8)
axes[1, 0].set_xlabel("Total Bill (USD)", labelpad=6)
axes[1, 0].set_ylabel("Tip Amount (USD)", labelpad=6)
axes[1, 0].set_xlim(left=0)
axes[1, 0].set_ylim(bottom=0)
axes[1, 0].legend(title="Meal Time", loc="upper left", frameon=True)

# Bottom-Right: Correlation Heatmap
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="YlGnBu",
    vmin=0,
    vmax=1,
    cbar_kws={'label': 'Pearson Correlation (r)'},
    linewidths=1.2,
    linecolor='white',
    annot_kws={"size": 11, "weight": "bold"},
    ax=axes[1, 1]
)
axes[1, 1].set_title("D. Correlation Heatmap: Bill and Tip Move Together Strongest (r = 0.68)", pad=8)

fig.suptitle("Exploratory Restaurant Dining Analysis: Spending, Tipping, and Timing Patterns",
             fontsize=16, fontweight='bold', y=0.99)

plt.tight_layout(rect=[0, 0.03, 1, 0.97])

# Bottom annotation banner with concise takeaways
takeaways_banner = (
    "Key Takeaways: [A] Customer bills peak between $10-$25 (median $17.80) with a right skew. "
    "[B] Weekend tips have wider variance and the highest outliers.\n"
    "[C] Tips increase steadily with bill size across both Lunch and Dinner. "
    "[D] Total bill and tip share the strongest linear correlation (r = 0.68)."
)
fig.text(0.5, 0.008, takeaways_banner, ha='center', fontsize=10, style='italic', color='#1a1a1a', linespacing=1.4)

# Save both tips_dashboard.png and tips_overview.png (matching assignment example name)
dashboard_path = os.path.join(SCRIPT_DIR, 'tips_dashboard.png')
overview_path = os.path.join(SCRIPT_DIR, 'tips_overview.png')
fig.savefig(dashboard_path, dpi=200, bbox_inches='tight')
fig.savefig(overview_path, dpi=150, bbox_inches='tight')
plt.close(fig)

print("Saved refined individual figures in 'figures/'")
print(f"Saved refined dashboard to {dashboard_path} and {overview_path}")
