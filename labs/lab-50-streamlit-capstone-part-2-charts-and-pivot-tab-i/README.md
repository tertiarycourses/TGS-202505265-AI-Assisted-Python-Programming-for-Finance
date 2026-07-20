# Lab 50 — Streamlit Capstone Part 2 — Charts and Pivot Tab in the Dashboard

**Topic 7: Aggregate and Visualize Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO6: Extend the Streamlit application with tabbed groupby charts and an interactive pivot table driven by user input.

## Goal

The learner EXTENDS the same app.py from lab 49, adding st.tabs with three tabs: 'Sector Analysis' (bar chart of mean Annual_Income by Employment_Sector plus the .agg() sector summary table from lab 47), 'Loan Mix' (grouped bar chart of Loan_Type by Loan_Status counts), and 'Risk Pivot' (an interactive pivot table where the user chooses the index and column dimensions from selectboxes and sees average Debt_to_Income_Ratio, rendered with a background gradient). All charts respect the sidebar filters.

## What you'll build

An extended app.py with a three-tab analytics section: sector charts, loan mix, and a user-configurable risk pivot.

**Tools:** uv, Streamlit, pandas, matplotlib, VS Code / Cursor AI assistant

## Step-by-step

1. Return to the capstone app folder from lab 49 — do NOT create a new project.

   ```bash
   cd loan-analytics-app
   ```

2. Confirm the lab 49 app still runs before changing anything.

   ```bash
   uv run streamlit run app.py
   ```

3. Prompt your AI assistant: "Extend this existing Streamlit app.py. Below the KPI metric cards add st.tabs(['Sector Analysis','Loan Mix','Risk Pivot']). In Sector Analysis, show a matplotlib horizontal bar chart of mean Annual_Income by Employment_Sector from the filtered DataFrame via st.pyplot, plus the multi-metric .agg() table with Avg_Income, Median_Income, Income_Std_Dev, Avg_Credit_Score, Avg_Tenure_Years. In Loan Mix, show a grouped bar chart of application counts by Loan_Type and Loan_Status. In Risk Pivot, add two st.selectbox controls letting the user pick the pivot index and columns from Education, Marital_Status, Region and Gender, then display pivot_table of mean Debt_to_Income_Ratio styled with a background gradient. Keep the existing sidebar filters and metric cards unchanged."
4. Paste the generated tabs into app.py under the metric-card row. Verify the existing filter and KPI code is untouched.
5. Re-run the app.

   ```bash
   uv run streamlit run app.py
   ```

6. Click through all three tabs and confirm each renders without error.
7. Change a sidebar filter and confirm the charts in every tab redraw with the filtered subset — this proves the filter is applied upstream of the tabs.
8. In the Risk Pivot tab, set index=Education and columns=Marital_Status and check the numbers match dti_pivot.csv from lab 48.
9. Guard against a pivot with an empty filtered frame — wrap the pivot in a try/except or an .empty check so the tab shows a message instead of an exception.
10. Discuss: what does moving from a static PNG chart to a Streamlit app change about who in the bank can use this analysis?

## Test it

All three tabs render under any filter combination; the Risk Pivot values for Education x Marital_Status match the lab 48 pivot to 3 decimals when no filters are applied.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
