# Lab 46 — Loan Application Counts by Status and Type

**Topic 7: Aggregate and Visualize Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO6: Aggregate categorical loan data into counts and approval rates with groupby and crosstab.

## Goal

The learner counts loan applications by Loan_Status and Loan_Type using groupby().size(), value_counts() and pd.crosstab(), then converts the raw counts into approval rates per loan product with normalize. The output answers a real credit-operations question: which product line has the weakest approval rate and the largest pending backlog?

## What you'll build

A loan_counts.py script producing a Loan_Type x Loan_Status count table plus an approval-rate table.

**Tools:** uv, pandas, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project and add pandas.

   ```bash
   uv init lab-46-loan-counts && cd lab-46-loan-counts && uv add pandas
   ```

2. Copy in df_finance.csv.

   ```bash
   cp ../lab-43-mock-loan-data/df_finance.csv .
   ```

3. Count applications per Loan_Status.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d['Loan_Status'].value_counts())"
   ```

4. Count applications per Loan_Type and Loan_Status with groupby().size().

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby(['Loan_Type','Loan_Status']).size())"
   ```

5. Build the same table as a cross-tab with margins (row and column totals).

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(pd.crosstab(d['Loan_Type'], d['Loan_Status'], margins=True))"
   ```

6. Prompt your AI assistant: "Using pandas, build a crosstab of Loan_Type against Loan_Status from df_finance, then produce a second table normalised by row so each cell is the percentage of that loan type's applications in that status, rounded to 1 decimal. Print which Loan_Type has the lowest Approved percentage and which has the highest Pending percentage."
7. Save it as loan_counts.py, review the normalize='index' argument, and confirm each row sums to 100%.
8. Run the script.

   ```bash
   uv run python loan_counts.py
   ```

9. Verify the totals: the crosstab grand total must equal len(df_finance).
10. Discuss: why is an approval rate a more actionable KPI for a credit committee than a raw approval count?

## Test it

Every row of the normalised table sums to 100.0 (+/- 0.1) and the crosstab margin total equals the DataFrame row count.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
