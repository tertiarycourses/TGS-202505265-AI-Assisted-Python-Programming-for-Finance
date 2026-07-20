# Lab 43 — Generate Mock Credit-Loan Data with df_finance

**Topic 7: Aggregate and Visualize Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO6: Aggregate and visualise financial data — build the credit-loan dataset that every Topic 7 lab aggregates.

## Goal

The learner creates a uv project and generates a reproducible mock credit-loan portfolio of 500 applicants as a pandas DataFrame named df_finance, with the columns used throughout Topics 7 and 9: Applicant_ID, Gender, Region, Employment_Sector, Annual_Income, Credit_Score, Years_at_Job, Loan_Type, Loan_Status, Loan_Amount_Requested, Debt_to_Income_Ratio, Missed_Payments_Last_2Y, Education and Marital_Status. An AI prompt drafts the generator; the learner reviews the ranges for financial realism before accepting the code.

## What you'll build

A uv project containing generate_data.py and a saved df_finance.csv of 500 mock loan applicants.

**Tools:** uv, Python 3.12, pandas, NumPy, VS Code / Cursor AI assistant

## Step-by-step

1. Create and enter the uv project for this lab.

   ```bash
   uv init lab-43-mock-loan-data && cd lab-43-mock-loan-data
   ```

2. Add the data libraries to the project.

   ```bash
   uv add pandas numpy
   ```

3. Prompt your AI assistant with this exact text: "Write a Python function generate_finance_data(n=500, seed=42) that returns a pandas DataFrame df_finance of mock credit-loan applicants with columns Applicant_ID, Gender (Male/Female), Region (North/South/East/West/Central), Employment_Sector (Banking/Technology/Healthcare/Manufacturing/Retail/Government), Annual_Income (lognormal, 30000-250000 SGD), Credit_Score (300-850), Years_at_Job (0-35), Loan_Type (Personal/Mortgage/Auto/Education), Loan_Status (Approved/Rejected/Pending), Loan_Amount_Requested, Debt_to_Income_Ratio (0.05-0.75), Missed_Payments_Last_2Y (0-6), Education and Marital_Status. Use numpy with a fixed seed so results are reproducible."
4. Save the generated code as generate_data.py and read every line — confirm the income and credit-score ranges are financially plausible and that the seed is fixed.
5. Add a line at the end that writes the frame to CSV: df_finance.to_csv('df_finance.csv', index=False).
6. Run the generator.

   ```bash
   uv run python generate_data.py
   ```

7. Inspect the shape, dtypes and first rows in a REPL to confirm the schema.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.shape); print(d.dtypes); print(d.head())"
   ```

8. Check the categorical spread — every Region, Loan_Status and Employment_Sector must be represented.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_finance.csv'); [print(c, d[c].value_counts().to_dict()) for c in ['Region','Loan_Status','Employment_Sector']]"
   ```

9. Discuss: why does a fixed random seed matter when a model output will be reviewed by a risk committee or an auditor?

## Test it

df_finance.csv exists with 500 rows and 14 columns; re-running generate_data.py produces a byte-identical file, proving reproducibility.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
