# Data Visualization with Matplotlib & Seaborn

This project is part of the **InternCircle Data Science & AI** internship (Project 2).

The objective is to create clear, honest charts from a real dataset using Matplotlib and Seaborn, following best data visualization practices (sensible chart types, honest axes, colorblind-friendly colors, and a clear one-line takeaway for every chart).

---

## 📊 Overview Dashboard (2x2 Grid)

![Tips Overview Dashboard](tips_overview.png)

---

## ❓ Questions & Chart Takeaways

| # | Question | Chart Type | One-Line Takeaway |
|:---:|:---|:---|:---|
| **1** | How are bills distributed? | **Histogram (KDE)** | Most bills are between \$10 and \$25 (median \$17.80), with a right skew due to infrequent large parties. |
| **2** | Do tips differ by day? | **Box Plot** | Median tips are consistent across days (~$2.75–$3.00), but weekends show higher variance and outlier tips up to \$10. |
| **3** | Does a bigger bill mean a bigger tip? | **Scatter Plot** | Bigger bills consistently bring bigger tips across both lunch and dinner sittings. |
| **4** | Which numbers move together? | **Correlation Heatmap** | Total bill and tip share the strongest positive correlation (r = 0.68), followed by party size and bill (r = 0.60). |
| **5** | Which day has the highest average bill? | **Bar Chart** *(Honest zero baseline)* | Sunday has the highest average bill (\$21.41), followed by Saturday (\$20.44), while Thursday and Friday are lower. |

---

## 📁 Project Structure

```text
├── data_visualization.ipynb      # Main Jupyter Notebook with code, plots, and takeaways
├── visualize.py                  # Python script to generate all figures
├── tips.csv                      # Dataset (244 dining records)
├── tips_overview.png             # 2x2 combined overview dashboard (150 DPI)
├── project-2-guide.pdf           # Task requirements guide
└── figures/                      # Individual saved figures
    ├── 01_bill_distribution.png
    ├── 02_tips_by_day.png
    ├── 03_bill_vs_tip.png
    ├── 04_correlation_heatmap.png
    └── 05_average_bill_by_day.png
```

---

## 🛠️ How to Run

1. **Install requirements:**
   ```bash
   pip install pandas seaborn matplotlib numpy
   ```

2. **Generate the charts:**
   ```bash
   python visualize.py
   ```

3. **Open the notebook:**
   ```bash
   jupyter notebook data_visualization.ipynb
   ```

---

## ✅ Best Practices Followed
- [x] Each chart type matches its question (Histogram for distribution, Box plot for spread/outliers, Scatter for 2 continuous variables, Heatmap for correlation matrix, Bar chart for category means).
- [x] Chart titles state findings directly rather than generic variable names.
- [x] Zero line is strictly preserved on the bar chart.
- [x] Colorblind-friendly palette used (Blue/Orange tones; no red-green clashes).
- [x] `plt.tight_layout()` applied to avoid cut-off labels.
- [x] Saved 2x2 dashboard at 150 DPI (`tips_overview.png`).
