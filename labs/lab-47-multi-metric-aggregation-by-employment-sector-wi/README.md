# Lab 47 — Multi-Metric Aggregation by Employment Sector with .agg()

**Topic 7: Aggregate and Visualize Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO6: Perform multi-metric aggregation, flatten MultiIndex columns and produce a board-ready sector table.

## Goal

This is the reference slide 137 activity. The learner groups df_finance by Employment_Sector and passes a dictionary to .agg() to compute the mean, median and standard deviation of Annual_Income plus the mean Credit_Score and mean Years_at_Job in one pass. The resulting MultiIndex columns are flattened and renamed to Avg_Income, Median_Income, Income_Std_Dev, Avg_Credit_Score and Avg_Tenure_Years.

## What you'll build

A sector_agg.py script producing a flat, renamed one-row-per-sector summary table exported to sector_summary.csv.

**Tools:** uv, pandas, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project and add pandas.

   ```bash
   uv init lab-47-sector-aggregation && cd lab-47-sector-aggregation && uv add pandas
   ```

2. Copy in df_finance.csv.

   ```bash
   cp ../lab-43-mock-loan-data/df_finance.csv .
   ```

3. Run a single-metric baseline: mean Annual_Income by Employment_Sector.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby('Employment_Sector')['Annual_Income'].mean().round(2))"
   ```

4. Prompt your AI assistant with the slide-137 brief: "Using pandas on a DataFrame named df_finance, group the data by Employment_Sector and perform a multi-metric aggregation with .agg(): calculate the mean, median and standard deviation for Annual_Income, and the mean for Credit_Score and Years_at_Job. Flatten the resulting MultiIndex columns and rename them to Avg_Income, Median_Income, Income_Std_Dev, Avg_Credit_Score and Avg_Tenure_Years. Round to 2 decimals, sort by Avg_Income descending and export to sector_summary.csv."
5. Save the answer as sector_agg.py and review the .agg() dictionary — confirm it maps each column to its list of functions.
6. Inspect how the MultiIndex is flattened: it should join the tuple levels, e.g. ['_'.join(c) for c in df.columns].
7. Run the script.

   ```bash
   uv run python sector_agg.py
   ```

8. Verify the flattened column names are exactly the five required names.

   ```bash
   uv run python -c "import pandas as pd; print(list(pd.read_csv('sector_summary.csv').columns))"
   ```

9. Cross-check one cell by hand: recompute Income_Std_Dev for the Banking sector independently.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d[d.Employment_Sector=='Banking']['Annual_Income'].std().round(2))"
   ```

10. Discuss: why does a high Income_Std_Dev within a sector matter more to a lender than the sector's mean income?

## Test it

sector_summary.csv has one row per Employment_Sector, exactly the five renamed columns plus the sector key, and no MultiIndex or tuple-shaped headers remain.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
