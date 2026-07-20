# Lab 45 — Groupby: Annual Income by Gender and Region

**Topic 7: Aggregate and Visualize Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO6: Aggregate financial data with groupby across one and multiple grouping keys.

## Goal

The learner uses df.groupby() to compute average and median Annual_Income by Gender, then by Region, then by both keys together to produce a MultiIndex result. The lab covers unstack() to turn the MultiIndex into a readable Gender x Region matrix, and interprets the income gaps as a fair-lending analyst would.

## What you'll build

A groupby_income.py script printing income statistics by Gender, by Region and by the Gender x Region cross-section.

**Tools:** uv, pandas, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project and add pandas.

   ```bash
   uv init lab-45-groupby-income && cd lab-45-groupby-income && uv add pandas
   ```

2. Copy in df_finance.csv from lab 43.

   ```bash
   cp ../lab-43-mock-loan-data/df_finance.csv .
   ```

3. Compute mean Annual_Income by Gender.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby('Gender')['Annual_Income'].mean().round(2))"
   ```

4. Compute mean and median Annual_Income by Region and sort descending by the mean.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby('Region')['Annual_Income'].agg(['mean','median']).round(2).sort_values('mean', ascending=False))"
   ```

5. Group by both keys to get a MultiIndex Series.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby(['Gender','Region'])['Annual_Income'].mean().round(2))"
   ```

6. Prompt your AI assistant: "Using a pandas DataFrame df_finance, group Annual_Income by Gender and Region, take the mean, then unstack Region into columns so the result is a Gender-by-Region matrix rounded to 2 decimals. Add a final column showing each gender's overall mean and a final row showing each region's overall mean."
7. Save the generated code as groupby_income.py, read it, and confirm unstack() is applied to the correct level.
8. Run the script and inspect the matrix.

   ```bash
   uv run python groupby_income.py
   ```

9. Interpret the output: which Gender x Region cell has the widest gap from the overall mean?
10. Discuss: groupby means say nothing about causation — what confounders (sector, tenure, education) would a fair-lending review demand before acting on this table?

## Test it

The unstacked matrix has one row per Gender and one column per Region, with the row/column totals matching the ungrouped overall mean to 2 decimal places.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
