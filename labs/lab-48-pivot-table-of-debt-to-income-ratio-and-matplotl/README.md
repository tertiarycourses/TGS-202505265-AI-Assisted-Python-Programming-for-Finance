# Lab 48 — Pivot Table of Debt-to-Income Ratio and Matplotlib Visualisation

**Topic 7: Aggregate and Visualize Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO6: Cross-tabulate a risk metric with pivot_table and visualise aggregations as bar, line and distribution charts.

## Goal

The learner builds the reference slide 139 pivot table — average Debt_to_Income_Ratio indexed by Education with Marital_Status as columns, rounded to 3 decimals — then turns the Topic 7 aggregations into three matplotlib charts: a bar chart of average income by sector, a line chart of approval rate across credit-score bands, and a histogram of the Debt_to_Income_Ratio distribution. All charts are saved as PNG for the dashboard.

## What you'll build

A pivot_and_charts.py script writing dti_pivot.csv plus chart_income_by_sector.png, chart_approval_by_score.png and chart_dti_distribution.png.

**Tools:** uv, pandas, matplotlib, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project and add pandas and matplotlib.

   ```bash
   uv init lab-48-pivot-and-charts && cd lab-48-pivot-and-charts && uv add pandas matplotlib
   ```

2. Copy in df_finance.csv.

   ```bash
   cp ../lab-43-mock-loan-data/df_finance.csv .
   ```

3. Build the slide-139 pivot table.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(pd.pivot_table(d, values='Debt_to_Income_Ratio', index='Education', columns='Marital_Status', aggfunc='mean').round(3))"
   ```

4. Add margins=True to get the row and column averages, and confirm the grand mean matches d['Debt_to_Income_Ratio'].mean().
5. Prompt your AI assistant: "Using pandas and matplotlib on df_finance, produce three saved PNG charts: (1) a horizontal bar chart of mean Annual_Income by Employment_Sector sorted descending, (2) a line chart of the Approved rate across Credit_Score bands created with pd.cut into 50-point bins, and (3) a histogram with 30 bins of Debt_to_Income_Ratio with a vertical dashed line at the mean. Give every chart a title, axis labels with units, and use plt.tight_layout() before savefig at dpi=150."
6. Save as pivot_and_charts.py and review: confirm matplotlib uses a non-interactive backend (matplotlib.use('Agg')) so it runs headless.
7. Run the script.

   ```bash
   uv run python pivot_and_charts.py
   ```

8. Confirm all four output files exist.

   ```bash
   ls -la dti_pivot.csv chart_*.png
   ```

9. Open each PNG and check it is readable: are the axis labels present and is the sector bar chart actually sorted?
10. Discuss: which of the three chart types best supports a credit-policy decision, and why is a distribution more honest than a single average?

## Test it

dti_pivot.csv contains one row per Education level and one column per Marital_Status with all values rounded to 3 decimals, and the three PNG files open with titles and labelled axes.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
