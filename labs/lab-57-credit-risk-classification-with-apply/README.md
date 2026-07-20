# Lab 57 — Credit Risk Classification with .apply()

**Topic 9: Analyze Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO8: Use .apply() with axis=1 to run a multi-column risk calculation across every row of a finance DataFrame.

## Goal

This is the reference slide 152 activity. The learner defines determine_loan_risk(row) computing a risk score as (Debt_to_Income_Ratio * 50) + (Missed_Payments_Last_2Y * 10) - (Credit_Score / 100), applies it with axis=1 to create Calculated_Risk_Score, then applies a lambda to that score to create a Risk_Profile column labelling scores above 60 as High, above 30 as Medium and the rest as Low. The lab contrasts .apply() with a manual for loop and shows why row-wise calculations that span several columns need axis=1.

## What you'll build

A risk_apply.py script adding Calculated_Risk_Score and Risk_Profile columns to df_finance and exporting df_scored.csv.

**Tools:** uv, pandas, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project and add pandas.

   ```bash
   uv init lab-57-credit-risk-apply && cd lab-57-credit-risk-apply && uv add pandas
   ```

2. Copy df_finance.csv from lab 43.

   ```bash
   cp ../lab-43-mock-loan-data/df_finance.csv .
   ```

3. Prompt your AI assistant with the slide-152 brief: "Write a pandas script demonstrating .apply() on a financial DataFrame named df_finance containing Credit_Score, Debt_to_Income_Ratio and Missed_Payments_Last_2Y. Define a function determine_loan_risk(row) returning (Debt_to_Income_Ratio * 50) + (Missed_Payments_Last_2Y * 10) - (Credit_Score / 100). Use .apply() with axis=1 to create a Calculated_Risk_Score column. Then use .apply() with a lambda on that new column to create a Risk_Profile column labelling scores above 60 as High, above 30 as Medium and the rest as Low. Display the first ten rows and the Risk_Profile value counts."
4. Save as risk_apply.py and confirm axis=1 is present on the first apply — without it pandas would pass columns, not rows.
5. Run the script.

   ```bash
   uv run python risk_apply.py
   ```

6. Verify the score by hand for row 0 and compare against the column value.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_scored.csv'); r=d.iloc[0]; print(round(r.Debt_to_Income_Ratio*50 + r.Missed_Payments_Last_2Y*10 - r.Credit_Score/100, 6), round(r.Calculated_Risk_Score, 6))"
   ```

7. Check the banding boundaries: no High row may have a score at or below 60, and no Low row may exceed 30.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_scored.csv'); print(d.groupby('Risk_Profile')['Calculated_Risk_Score'].agg(['min','max','count']).round(2))"
   ```

8. Write the equivalent logic as a manual for loop with iterrows() and time both approaches to see the difference.
9. Cross-tabulate Risk_Profile against Loan_Status — does the bank's actual approval decision agree with the model's risk band?

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_scored.csv'); print(pd.crosstab(d['Risk_Profile'], d['Loan_Status']))"
   ```

10. Discuss: this score is a linear rule with hard-coded weights. What must a credit-risk team document before such a model is used in a lending decision?

## Test it

Every row's Calculated_Risk_Score matches the formula recomputed by hand; the Risk_Profile bands are mutually exclusive with min/max values that respect the 30 and 60 thresholds; the value counts sum to 500.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
