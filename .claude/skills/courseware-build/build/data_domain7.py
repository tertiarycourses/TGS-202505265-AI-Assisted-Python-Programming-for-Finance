"""
Topic 7 — Aggregate and Visualize Finance Data (labs 43-50).

Maps to LO6: aggregate and visualise financial data with groupby, pivot tables and
charts, and publish the results as an interactive Streamlit application.

Labs 43-48 build the aggregation and charting toolkit on a mock credit-loan
dataset (df_finance). Labs 49-50 START the Streamlit capstone — the
"Portfolio & Loan Analytics" dashboard that Topic 9 (labs 61-62) completes.
All labs use uv, never pip/venv.
"""

DOMAIN7 = [
    dict(
        num=43,
        topic=7,
        title="Generate Mock Credit-Loan Data with df_finance",
        objective="LO6: Aggregate and visualise financial data — build the credit-loan dataset that every Topic 7 lab aggregates.",
        desc=(
            "The learner creates a uv project and generates a reproducible mock credit-loan "
            "portfolio of 500 applicants as a pandas DataFrame named df_finance, with the columns "
            "used throughout Topics 7 and 9: Applicant_ID, Gender, Region, Employment_Sector, "
            "Annual_Income, Credit_Score, Years_at_Job, Loan_Type, Loan_Status, "
            "Loan_Amount_Requested, Debt_to_Income_Ratio, Missed_Payments_Last_2Y, Education and "
            "Marital_Status. An AI prompt drafts the generator; the learner reviews the ranges for "
            "financial realism before accepting the code."
        ),
        build="A uv project containing generate_data.py and a saved df_finance.csv of 500 mock loan applicants.",
        services="uv, Python 3.12, pandas, NumPy, VS Code / Cursor AI assistant",
        steps=[
            ("Create and enter the uv project for this lab.", "uv init lab-43-mock-loan-data && cd lab-43-mock-loan-data"),
            ("Add the data libraries to the project.", "uv add pandas numpy"),
            ("Prompt your AI assistant with this exact text: \"Write a Python function generate_finance_data(n=500, seed=42) that returns a pandas DataFrame df_finance of mock credit-loan applicants with columns Applicant_ID, Gender (Male/Female), Region (North/South/East/West/Central), Employment_Sector (Banking/Technology/Healthcare/Manufacturing/Retail/Government), Annual_Income (lognormal, 30000-250000 SGD), Credit_Score (300-850), Years_at_Job (0-35), Loan_Type (Personal/Mortgage/Auto/Education), Loan_Status (Approved/Rejected/Pending), Loan_Amount_Requested, Debt_to_Income_Ratio (0.05-0.75), Missed_Payments_Last_2Y (0-6), Education and Marital_Status. Use numpy with a fixed seed so results are reproducible.\"", ""),
            ("Save the generated code as generate_data.py and read every line — confirm the income and credit-score ranges are financially plausible and that the seed is fixed.", ""),
            ("Add a line at the end that writes the frame to CSV: df_finance.to_csv('df_finance.csv', index=False).", ""),
            ("Run the generator.", "uv run python generate_data.py"),
            ("Inspect the shape, dtypes and first rows in a REPL to confirm the schema.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.shape); print(d.dtypes); print(d.head())\""),
            ("Check the categorical spread — every Region, Loan_Status and Employment_Sector must be represented.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); [print(c, d[c].value_counts().to_dict()) for c in ['Region','Loan_Status','Employment_Sector']]\""),
            ("Discuss: why does a fixed random seed matter when a model output will be reviewed by a risk committee or an auditor?", ""),
        ],
        test="df_finance.csv exists with 500 rows and 14 columns; re-running generate_data.py produces a byte-identical file, proving reproducibility.",
    ),
    dict(
        num=44,
        topic=7,
        title="Join Finance Datasets with concat, append and merge",
        objective="LO6: Combine prices, fundamentals and customer records into one analysis-ready frame using concat and merge.",
        desc=(
            "The learner combines the loan book with two extra sources: a second branch's loan file "
            "(stacked vertically with pd.concat) and a regional risk-rating reference table (joined "
            "horizontally with pd.merge on Region). The lab contrasts inner, left and outer joins and "
            "shows what a mismatched key silently does to a loan book — the classic cause of "
            "disappearing applicants in a reconciliation."
        ),
        build="A join_data.py script producing df_all — the combined multi-branch loan book enriched with regional risk ratings.",
        services="uv, pandas, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add pandas.", "uv init lab-44-join-finance-data && cd lab-44-join-finance-data && uv add pandas numpy"),
            ("Copy df_finance.csv from lab 43 into this project.", "cp ../lab-43-mock-loan-data/df_finance.csv ."),
            ("Create a second branch file by regenerating with a different seed and an offset Applicant_ID, saving it as df_branch2.csv.", ""),
            ("Stack the two branches vertically and reset the index.", "uv run python -c \"import pandas as pd; a=pd.read_csv('df_finance.csv'); b=pd.read_csv('df_branch2.csv'); df=pd.concat([a,b], ignore_index=True); print(len(a), len(b), len(df))\""),
            ("Prompt your AI assistant: \"Given a pandas DataFrame df of loan applicants with a Region column, build a small reference DataFrame df_risk with one row per Region and columns Regional_Risk_Rating (A/B/C) and Base_Interest_Rate. Then merge it into df on Region using a left join, and print how many rows have a null Regional_Risk_Rating after the merge.\"", ""),
            ("Review the generated merge — confirm it uses how='left' so no applicant is dropped, and that the null check is present.", ""),
            ("Deliberately break one Region value (e.g. 'central' lower-case) and re-run the merge to see the applicant lose its rating.", ""),
            ("Compare the row counts of an inner, left and outer merge on the broken key.", "uv run python join_data.py"),
            ("Discuss: in a loan reconciliation, which join type is safest and why must the post-merge row count always be asserted?", ""),
            ("Save the final combined frame.", "uv run python -c \"import pandas as pd; print('df_all saved')\""),
        ],
        test="df_all has exactly len(branch1) + len(branch2) rows after the left merge — no applicant is silently lost — and zero null Regional_Risk_Rating values once the key is fixed.",
    ),
    dict(
        num=45,
        topic=7,
        title="Groupby: Annual Income by Gender and Region",
        objective="LO6: Aggregate financial data with groupby across one and multiple grouping keys.",
        desc=(
            "The learner uses df.groupby() to compute average and median Annual_Income by Gender, "
            "then by Region, then by both keys together to produce a MultiIndex result. The lab covers "
            "unstack() to turn the MultiIndex into a readable Gender x Region matrix, and interprets "
            "the income gaps as a fair-lending analyst would."
        ),
        build="A groupby_income.py script printing income statistics by Gender, by Region and by the Gender x Region cross-section.",
        services="uv, pandas, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add pandas.", "uv init lab-45-groupby-income && cd lab-45-groupby-income && uv add pandas"),
            ("Copy in df_finance.csv from lab 43.", "cp ../lab-43-mock-loan-data/df_finance.csv ."),
            ("Compute mean Annual_Income by Gender.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby('Gender')['Annual_Income'].mean().round(2))\""),
            ("Compute mean and median Annual_Income by Region and sort descending by the mean.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby('Region')['Annual_Income'].agg(['mean','median']).round(2).sort_values('mean', ascending=False))\""),
            ("Group by both keys to get a MultiIndex Series.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby(['Gender','Region'])['Annual_Income'].mean().round(2))\""),
            ("Prompt your AI assistant: \"Using a pandas DataFrame df_finance, group Annual_Income by Gender and Region, take the mean, then unstack Region into columns so the result is a Gender-by-Region matrix rounded to 2 decimals. Add a final column showing each gender's overall mean and a final row showing each region's overall mean.\"", ""),
            ("Save the generated code as groupby_income.py, read it, and confirm unstack() is applied to the correct level.", ""),
            ("Run the script and inspect the matrix.", "uv run python groupby_income.py"),
            ("Interpret the output: which Gender x Region cell has the widest gap from the overall mean?", ""),
            ("Discuss: groupby means say nothing about causation — what confounders (sector, tenure, education) would a fair-lending review demand before acting on this table?", ""),
        ],
        test="The unstacked matrix has one row per Gender and one column per Region, with the row/column totals matching the ungrouped overall mean to 2 decimal places.",
    ),
    dict(
        num=46,
        topic=7,
        title="Loan Application Counts by Status and Type",
        objective="LO6: Aggregate categorical loan data into counts and approval rates with groupby and crosstab.",
        desc=(
            "The learner counts loan applications by Loan_Status and Loan_Type using groupby().size(), "
            "value_counts() and pd.crosstab(), then converts the raw counts into approval rates per "
            "loan product with normalize. The output answers a real credit-operations question: which "
            "product line has the weakest approval rate and the largest pending backlog?"
        ),
        build="A loan_counts.py script producing a Loan_Type x Loan_Status count table plus an approval-rate table.",
        services="uv, pandas, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add pandas.", "uv init lab-46-loan-counts && cd lab-46-loan-counts && uv add pandas"),
            ("Copy in df_finance.csv.", "cp ../lab-43-mock-loan-data/df_finance.csv ."),
            ("Count applications per Loan_Status.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d['Loan_Status'].value_counts())\""),
            ("Count applications per Loan_Type and Loan_Status with groupby().size().", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby(['Loan_Type','Loan_Status']).size())\""),
            ("Build the same table as a cross-tab with margins (row and column totals).", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(pd.crosstab(d['Loan_Type'], d['Loan_Status'], margins=True))\""),
            ("Prompt your AI assistant: \"Using pandas, build a crosstab of Loan_Type against Loan_Status from df_finance, then produce a second table normalised by row so each cell is the percentage of that loan type's applications in that status, rounded to 1 decimal. Print which Loan_Type has the lowest Approved percentage and which has the highest Pending percentage.\"", ""),
            ("Save it as loan_counts.py, review the normalize='index' argument, and confirm each row sums to 100%.", ""),
            ("Run the script.", "uv run python loan_counts.py"),
            ("Verify the totals: the crosstab grand total must equal len(df_finance).", ""),
            ("Discuss: why is an approval rate a more actionable KPI for a credit committee than a raw approval count?", ""),
        ],
        test="Every row of the normalised table sums to 100.0 (+/- 0.1) and the crosstab margin total equals the DataFrame row count.",
    ),
    dict(
        num=47,
        topic=7,
        title="Multi-Metric Aggregation by Employment Sector with .agg()",
        objective="LO6: Perform multi-metric aggregation, flatten MultiIndex columns and produce a board-ready sector table.",
        desc=(
            "This is the reference slide 137 activity. The learner groups df_finance by "
            "Employment_Sector and passes a dictionary to .agg() to compute the mean, median and "
            "standard deviation of Annual_Income plus the mean Credit_Score and mean Years_at_Job in "
            "one pass. The resulting MultiIndex columns are flattened and renamed to Avg_Income, "
            "Median_Income, Income_Std_Dev, Avg_Credit_Score and Avg_Tenure_Years."
        ),
        build="A sector_agg.py script producing a flat, renamed one-row-per-sector summary table exported to sector_summary.csv.",
        services="uv, pandas, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add pandas.", "uv init lab-47-sector-aggregation && cd lab-47-sector-aggregation && uv add pandas"),
            ("Copy in df_finance.csv.", "cp ../lab-43-mock-loan-data/df_finance.csv ."),
            ("Run a single-metric baseline: mean Annual_Income by Employment_Sector.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d.groupby('Employment_Sector')['Annual_Income'].mean().round(2))\""),
            ("Prompt your AI assistant with the slide-137 brief: \"Using pandas on a DataFrame named df_finance, group the data by Employment_Sector and perform a multi-metric aggregation with .agg(): calculate the mean, median and standard deviation for Annual_Income, and the mean for Credit_Score and Years_at_Job. Flatten the resulting MultiIndex columns and rename them to Avg_Income, Median_Income, Income_Std_Dev, Avg_Credit_Score and Avg_Tenure_Years. Round to 2 decimals, sort by Avg_Income descending and export to sector_summary.csv.\"", ""),
            ("Save the answer as sector_agg.py and review the .agg() dictionary — confirm it maps each column to its list of functions.", ""),
            ("Inspect how the MultiIndex is flattened: it should join the tuple levels, e.g. ['_'.join(c) for c in df.columns].", ""),
            ("Run the script.", "uv run python sector_agg.py"),
            ("Verify the flattened column names are exactly the five required names.", "uv run python -c \"import pandas as pd; print(list(pd.read_csv('sector_summary.csv').columns))\""),
            ("Cross-check one cell by hand: recompute Income_Std_Dev for the Banking sector independently.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(d[d.Employment_Sector=='Banking']['Annual_Income'].std().round(2))\""),
            ("Discuss: why does a high Income_Std_Dev within a sector matter more to a lender than the sector's mean income?", ""),
        ],
        test="sector_summary.csv has one row per Employment_Sector, exactly the five renamed columns plus the sector key, and no MultiIndex or tuple-shaped headers remain.",
    ),
    dict(
        num=48,
        topic=7,
        title="Pivot Table of Debt-to-Income Ratio and Matplotlib Visualisation",
        objective="LO6: Cross-tabulate a risk metric with pivot_table and visualise aggregations as bar, line and distribution charts.",
        desc=(
            "The learner builds the reference slide 139 pivot table — average Debt_to_Income_Ratio "
            "indexed by Education with Marital_Status as columns, rounded to 3 decimals — then turns "
            "the Topic 7 aggregations into three matplotlib charts: a bar chart of average income by "
            "sector, a line chart of approval rate across credit-score bands, and a histogram of the "
            "Debt_to_Income_Ratio distribution. All charts are saved as PNG for the dashboard."
        ),
        build="A pivot_and_charts.py script writing dti_pivot.csv plus chart_income_by_sector.png, chart_approval_by_score.png and chart_dti_distribution.png.",
        services="uv, pandas, matplotlib, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add pandas and matplotlib.", "uv init lab-48-pivot-and-charts && cd lab-48-pivot-and-charts && uv add pandas matplotlib"),
            ("Copy in df_finance.csv.", "cp ../lab-43-mock-loan-data/df_finance.csv ."),
            ("Build the slide-139 pivot table.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_finance.csv'); print(pd.pivot_table(d, values='Debt_to_Income_Ratio', index='Education', columns='Marital_Status', aggfunc='mean').round(3))\""),
            ("Add margins=True to get the row and column averages, and confirm the grand mean matches d['Debt_to_Income_Ratio'].mean().", ""),
            ("Prompt your AI assistant: \"Using pandas and matplotlib on df_finance, produce three saved PNG charts: (1) a horizontal bar chart of mean Annual_Income by Employment_Sector sorted descending, (2) a line chart of the Approved rate across Credit_Score bands created with pd.cut into 50-point bins, and (3) a histogram with 30 bins of Debt_to_Income_Ratio with a vertical dashed line at the mean. Give every chart a title, axis labels with units, and use plt.tight_layout() before savefig at dpi=150.\"", ""),
            ("Save as pivot_and_charts.py and review: confirm matplotlib uses a non-interactive backend (matplotlib.use('Agg')) so it runs headless.", ""),
            ("Run the script.", "uv run python pivot_and_charts.py"),
            ("Confirm all four output files exist.", "ls -la dti_pivot.csv chart_*.png"),
            ("Open each PNG and check it is readable: are the axis labels present and is the sector bar chart actually sorted?", ""),
            ("Discuss: which of the three chart types best supports a credit-policy decision, and why is a distribution more honest than a single average?", ""),
        ],
        test="dti_pivot.csv contains one row per Education level and one column per Marital_Status with all values rounded to 3 decimals, and the three PNG files open with titles and labelled axes.",
    ),
    dict(
        num=49,
        topic=7,
        title="Streamlit Capstone Part 1 — Portfolio & Loan Analytics App Shell",
        objective="LO6: Publish an aggregation as an interactive Streamlit application with sidebar filters and KPI metric cards.",
        desc=(
            "The Streamlit capstone STARTS here. The learner creates the app project, writes app.py, "
            "and builds the shell of the 'Portfolio & Loan Analytics' dashboard: page config, a cached "
            "data loader for df_finance.csv, a sidebar with multiselect filters for Employment_Sector, "
            "Region and Loan_Status, and a row of four KPI metric cards (Total Applications, Approval "
            "Rate, Average Annual Income, Average Debt-to-Income Ratio) that all recompute live as the "
            "filters change. This same app.py is extended in labs 50, 61 and 62."
        ),
        build="A Streamlit project with app.py serving the filtered KPI dashboard at localhost:8501.",
        services="uv, Streamlit, pandas, VS Code / Cursor AI assistant",
        steps=[
            ("Create the capstone project — keep this folder, labs 50, 61 and 62 all extend it.", "uv init loan-analytics-app && cd loan-analytics-app"),
            ("Add Streamlit and the data libraries.", "uv add streamlit pandas matplotlib"),
            ("Copy df_finance.csv from lab 43 into the app folder.", "cp ../lab-43-mock-loan-data/df_finance.csv ."),
            ("Prompt your AI assistant: \"Write a Streamlit app.py titled 'Portfolio & Loan Analytics'. Use st.set_page_config with a wide layout. Add a load_data() function decorated with @st.cache_data that reads df_finance.csv. In the sidebar add three st.multiselect filters for Employment_Sector, Region and Loan_Status, each defaulting to all values. Filter the DataFrame by all three selections, then display four st.metric cards in st.columns(4): Total Applications, Approval Rate as a percentage, Average Annual Income formatted as SGD with thousands separators, and Average Debt-to-Income Ratio to 3 decimals. Show the filtered table below with st.dataframe.\"", ""),
            ("Save the answer as app.py — this is THE file every remaining capstone lab edits. Read it and confirm @st.cache_data is on the loader and the filter is applied before the metrics are computed.", ""),
            ("Run the app.", "uv run streamlit run app.py"),
            ("Open http://localhost:8501 and change one sidebar filter — verify all four metric cards update.", ""),
            ("Set the Loan_Status filter to Approved only and confirm the Approval Rate card reads 100%.", ""),
            ("Clear all values from one filter and confirm the app shows a friendly empty-state message rather than crashing; add an if filtered.empty: st.warning(...) guard if it does not.", ""),
            ("Commit or note the file structure — labs 50, 61 and 62 add to this exact app.py.", "ls -la app.py df_finance.csv pyproject.toml"),
        ],
        test="The app loads at localhost:8501; selecting a single Employment_Sector changes Total Applications to that sector's row count, and clearing a filter shows a warning instead of a traceback.",
    ),
    dict(
        num=50,
        topic=7,
        title="Streamlit Capstone Part 2 — Charts and Pivot Tab in the Dashboard",
        objective="LO6: Extend the Streamlit application with tabbed groupby charts and an interactive pivot table driven by user input.",
        desc=(
            "The learner EXTENDS the same app.py from lab 49, adding st.tabs with three tabs: "
            "'Sector Analysis' (bar chart of mean Annual_Income by Employment_Sector plus the .agg() "
            "sector summary table from lab 47), 'Loan Mix' (grouped bar chart of Loan_Type by "
            "Loan_Status counts), and 'Risk Pivot' (an interactive pivot table where the user chooses "
            "the index and column dimensions from selectboxes and sees average Debt_to_Income_Ratio, "
            "rendered with a background gradient). All charts respect the sidebar filters."
        ),
        build="An extended app.py with a three-tab analytics section: sector charts, loan mix, and a user-configurable risk pivot.",
        services="uv, Streamlit, pandas, matplotlib, VS Code / Cursor AI assistant",
        steps=[
            ("Return to the capstone app folder from lab 49 — do NOT create a new project.", "cd loan-analytics-app"),
            ("Confirm the lab 49 app still runs before changing anything.", "uv run streamlit run app.py"),
            ("Prompt your AI assistant: \"Extend this existing Streamlit app.py. Below the KPI metric cards add st.tabs(['Sector Analysis','Loan Mix','Risk Pivot']). In Sector Analysis, show a matplotlib horizontal bar chart of mean Annual_Income by Employment_Sector from the filtered DataFrame via st.pyplot, plus the multi-metric .agg() table with Avg_Income, Median_Income, Income_Std_Dev, Avg_Credit_Score, Avg_Tenure_Years. In Loan Mix, show a grouped bar chart of application counts by Loan_Type and Loan_Status. In Risk Pivot, add two st.selectbox controls letting the user pick the pivot index and columns from Education, Marital_Status, Region and Gender, then display pivot_table of mean Debt_to_Income_Ratio styled with a background gradient. Keep the existing sidebar filters and metric cards unchanged.\"", ""),
            ("Paste the generated tabs into app.py under the metric-card row. Verify the existing filter and KPI code is untouched.", ""),
            ("Re-run the app.", "uv run streamlit run app.py"),
            ("Click through all three tabs and confirm each renders without error.", ""),
            ("Change a sidebar filter and confirm the charts in every tab redraw with the filtered subset — this proves the filter is applied upstream of the tabs.", ""),
            ("In the Risk Pivot tab, set index=Education and columns=Marital_Status and check the numbers match dti_pivot.csv from lab 48.", ""),
            ("Guard against a pivot with an empty filtered frame — wrap the pivot in a try/except or an .empty check so the tab shows a message instead of an exception.", ""),
            ("Discuss: what does moving from a static PNG chart to a Streamlit app change about who in the bank can use this analysis?", ""),
        ],
        test="All three tabs render under any filter combination; the Risk Pivot values for Education x Marital_Status match the lab 48 pivot to 3 decimals when no filters are applied.",
    ),
]
