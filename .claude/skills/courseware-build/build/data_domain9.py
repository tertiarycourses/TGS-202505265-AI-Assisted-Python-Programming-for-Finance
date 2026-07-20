"""
Topic 9 — Analyze Finance Data (labs 57-62).

Maps to LO8: analyse financial data using apply and pipe pipelines, assess code
to identify gaps, and test the results.

Labs 57-60 build the analysis layer: .apply() for row-wise credit-risk scoring,
lambda versus named functions, .pipe() for a clean -> enrich -> score pipeline,
and descriptive statistics plus trend/volatility/drawdown tracking.
Labs 61-62 COMPLETE the Streamlit capstone started in labs 49-50 — the same
loan-analytics-app/app.py gains a Technical Analysis page (the Topic 8
StockTechnicalAnalyzer) and a Risk Scoring page (the apply/pipe pipeline), then
is tested and deployed. This is the course finale.
All labs use uv, never pip/venv.
"""

DOMAIN9 = [
    dict(
        num=57,
        topic=9,
        title="Credit Risk Classification with .apply()",
        objective="LO8: Use .apply() with axis=1 to run a multi-column risk calculation across every row of a finance DataFrame.",
        desc=(
            "This is the reference slide 152 activity. The learner defines "
            "determine_loan_risk(row) computing a risk score as "
            "(Debt_to_Income_Ratio * 50) + (Missed_Payments_Last_2Y * 10) - (Credit_Score / 100), "
            "applies it with axis=1 to create Calculated_Risk_Score, then applies a lambda to that "
            "score to create a Risk_Profile column labelling scores above 60 as High, above 30 as "
            "Medium and the rest as Low. The lab contrasts .apply() with a manual for loop and shows "
            "why row-wise calculations that span several columns need axis=1."
        ),
        build="A risk_apply.py script adding Calculated_Risk_Score and Risk_Profile columns to df_finance and exporting df_scored.csv.",
        services="uv, pandas, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add pandas.", "uv init lab-57-credit-risk-apply && cd lab-57-credit-risk-apply && uv add pandas"),
            ("Copy df_finance.csv from lab 43.", "cp ../lab-43-mock-loan-data/df_finance.csv ."),
            ("Prompt your AI assistant with the slide-152 brief: \"Write a pandas script demonstrating .apply() on a financial DataFrame named df_finance containing Credit_Score, Debt_to_Income_Ratio and Missed_Payments_Last_2Y. Define a function determine_loan_risk(row) returning (Debt_to_Income_Ratio * 50) + (Missed_Payments_Last_2Y * 10) - (Credit_Score / 100). Use .apply() with axis=1 to create a Calculated_Risk_Score column. Then use .apply() with a lambda on that new column to create a Risk_Profile column labelling scores above 60 as High, above 30 as Medium and the rest as Low. Display the first ten rows and the Risk_Profile value counts.\"", ""),
            ("Save as risk_apply.py and confirm axis=1 is present on the first apply — without it pandas would pass columns, not rows.", ""),
            ("Run the script.", "uv run python risk_apply.py"),
            ("Verify the score by hand for row 0 and compare against the column value.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_scored.csv'); r=d.iloc[0]; print(round(r.Debt_to_Income_Ratio*50 + r.Missed_Payments_Last_2Y*10 - r.Credit_Score/100, 6), round(r.Calculated_Risk_Score, 6))\""),
            ("Check the banding boundaries: no High row may have a score at or below 60, and no Low row may exceed 30.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_scored.csv'); print(d.groupby('Risk_Profile')['Calculated_Risk_Score'].agg(['min','max','count']).round(2))\""),
            ("Write the equivalent logic as a manual for loop with iterrows() and time both approaches to see the difference.", ""),
            ("Cross-tabulate Risk_Profile against Loan_Status — does the bank's actual approval decision agree with the model's risk band?", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_scored.csv'); print(pd.crosstab(d['Risk_Profile'], d['Loan_Status']))\""),
            ("Discuss: this score is a linear rule with hard-coded weights. What must a credit-risk team document before such a model is used in a lending decision?", ""),
        ],
        test="Every row's Calculated_Risk_Score matches the formula recomputed by hand; the Risk_Profile bands are mutually exclusive with min/max values that respect the 30 and 60 thresholds; the value counts sum to 500.",
    ),
    dict(
        num=58,
        topic=9,
        title="Lambda versus Named Functions in .apply()",
        objective="LO8: Choose between lambda and named functions in apply, and assess code to identify readability and testability gaps.",
        desc=(
            "The learner takes the same classification logic and writes it three ways: a one-line "
            "lambda, a named function passed by reference, and a vectorised alternative using "
            "np.select. Each is benchmarked and, critically, assessed for testability — a named "
            "function can be unit-tested in isolation, a lambda buried in an apply cannot. The learner "
            "writes pytest cases for the named function, including the boundary values that the "
            "lambda version silently gets wrong."
        ),
        build="A classify.py module with three implementations plus test_classify.py containing passing boundary-value tests.",
        services="uv, pandas, NumPy, pytest, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add the libraries including pytest.", "uv init lab-58-lambda-vs-function && cd lab-58-lambda-vs-function && uv add pandas numpy pytest"),
            ("Copy df_scored.csv from lab 57.", "cp ../lab-57-credit-risk-apply/df_scored.csv ."),
            ("Write version A by hand: a lambda inside .apply() banding Calculated_Risk_Score into High/Medium/Low.", ""),
            ("Prompt your AI assistant: \"Refactor this pandas lambda apply into a named function classify_risk(score) with an explicit docstring stating the boundary behaviour at exactly 30 and exactly 60, and a third vectorised version using numpy.select with the same conditions. All three must produce identical output on the same column. Then write pytest tests for classify_risk covering scores of 0, 30, 30.01, 60, 60.01 and 100, plus a None input.\"", ""),
            ("Save the three implementations in classify.py and the tests in test_classify.py.", ""),
            ("Assess the code for gaps: does the lambda handle a NaN score? Does it define whether exactly 60 is High or Medium? Note every ambiguity you find.", ""),
            ("Run the tests — expect the boundary cases to expose the ambiguity.", "uv run pytest test_classify.py -v"),
            ("Fix classify_risk so the documented boundary behaviour and the tests agree, then re-run until green.", "uv run pytest test_classify.py -v"),
            ("Prove all three versions agree on the real data.", "uv run python -c \"import pandas as pd; from classify import apply_lambda, apply_named, apply_vectorised; d=pd.read_csv('df_scored.csv'); a,b,c = apply_lambda(d), apply_named(d), apply_vectorised(d); print((a==b).all(), (b==c).all())\""),
            ("Time the three approaches on the 500-row frame and again on a 500,000-row frame to see where vectorisation wins.", "uv run python classify.py --benchmark"),
            ("Discuss: when is a lambda the right choice, and why does a risk model that will face an auditor belong in a named, tested function?", ""),
        ],
        test="All pytest boundary tests pass; the lambda, named and vectorised outputs are element-wise identical on df_scored.csv; the benchmark shows np.select fastest at scale.",
    ),
    dict(
        num=59,
        topic=9,
        title="Building a clean → enrich → score Pipeline with .pipe()",
        objective="LO8: Chain transformations into a readable, testable data pipeline using .pipe().",
        desc=(
            "The reference slide 155 activity, extended into a full three-stage pipeline. The learner "
            "writes small single-purpose functions — clean_data (drop duplicates, coerce dtypes, "
            "handle missing income), enrich_data (add Risk_Adjusted_Loan as Loan_Amount_Requested * "
            "Credit_Score / 850, plus an income band and a tenure band), and score_data (attach the "
            "lab 58 risk classification) — then chains them with .pipe(). A summarize_by_sector step "
            "produces the final table of mean Annual_Income, total Risk_Adjusted_Loan and applicant "
            "count. The lab contrasts the pipe chain with the unreadable nested-call equivalent."
        ),
        build="A pipeline.py module of four pipe-able functions and a single readable chained expression producing sector_pipeline_summary.csv.",
        services="uv, pandas, pytest, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add the libraries.", "uv init lab-59-pipe-pipeline && cd lab-59-pipe-pipeline && uv add pandas pytest"),
            ("Copy df_finance.csv and the classify module from lab 58.", "cp ../lab-43-mock-loan-data/df_finance.csv . && cp ../lab-58-lambda-vs-function/classify.py ."),
            ("Write the nested version first, deliberately: summarize_by_sector(score_data(enrich_data(clean_data(df)))). Note how you must read it inside-out.", ""),
            ("Prompt your AI assistant: \"Using a pandas DataFrame named df_finance, build a .pipe() pipeline. Define clean_data(df) that drops duplicate Applicant_IDs, coerces numeric columns and fills missing Annual_Income with the sector median. Define filter_by_region(df, region='Central') that filters to a region. Define enrich_data(df) that adds Risk_Adjusted_Loan as Loan_Amount_Requested multiplied by Credit_Score divided by 850, plus Income_Band via pd.cut. Define score_data(df) that adds Calculated_Risk_Score and Risk_Profile. Define summarize_by_sector(df) aggregating by Employment_Sector into mean Annual_Income, total Risk_Adjusted_Loan and applicant count. Chain them all with .pipe() in one readable expression and round the final summary to 2 decimals. Every function must take a DataFrame as its first argument, return a new DataFrame, and never mutate its input.\"", ""),
            ("Save as pipeline.py and audit the no-mutation rule: each function must start with df = df.copy() or use non-mutating operations.", ""),
            ("Prove immutability — run the pipeline and confirm the original df_finance is byte-identical afterwards.", "uv run python -c \"import pandas as pd; from pipeline import run_pipeline; d=pd.read_csv('df_finance.csv'); before=d.copy(); run_pipeline(d); print(d.equals(before))\""),
            ("Run the full chain.", "uv run python pipeline.py"),
            ("Show the parameterised pipe: pass a region argument through the chain with .pipe(filter_by_region, region='North') and confirm the summary changes.", ""),
            ("Test each stage in isolation — a pipeline's value is that every stage is independently testable.", "uv run pytest test_pipeline.py -v"),
            ("Verify the pipeline is order-safe: score_data before enrich_data must fail loudly rather than produce silent nulls. Add an assertion on the required columns at the top of each stage.", ""),
            ("Discuss: compare the pipe chain against the nested version you wrote first — which would you rather hand to a colleague reviewing a credit model, and why?", ""),
        ],
        test="run_pipeline() leaves the input DataFrame unmodified; the sector summary has one row per Employment_Sector with three rounded metric columns; every stage passes its isolated pytest and mis-ordering the stages raises an assertion instead of returning nulls.",
    ),
    dict(
        num=60,
        topic=9,
        title="Descriptive Statistics, Correlation and Tracking Change Over Time",
        objective="LO8: Apply descriptive statistics to summarise risk and return, and track trend, volatility and drawdown over time.",
        desc=(
            "Two halves. First, cross-sectional statistics on the loan book: .describe(), mean, "
            "median, standard deviation and a correlation matrix of Credit_Score, "
            "Debt_to_Income_Ratio, Annual_Income and Calculated_Risk_Score, with the median-versus-"
            "mean gap exposing income skew. Second, time-series tracking on a price history: daily "
            "returns, a rolling 20-day annualised volatility, the cumulative return trend and the "
            "maximum drawdown computed from the running peak — the three numbers an investment "
            "committee asks for."
        ),
        build="A stats_analysis.py script producing the loan-book statistics and correlation matrix, plus a drawdown/volatility report and chart.",
        services="uv, pandas, NumPy, matplotlib, yfinance, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add the libraries.", "uv init lab-60-statistics-and-trend && cd lab-60-statistics-and-trend && uv add pandas numpy matplotlib yfinance"),
            ("Copy df_scored.csv from lab 57.", "cp ../lab-57-credit-risk-apply/df_scored.csv ."),
            ("Produce the baseline descriptive statistics for the numeric loan columns.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_scored.csv'); print(d[['Annual_Income','Credit_Score','Debt_to_Income_Ratio','Calculated_Risk_Score']].describe().round(2))\""),
            ("Compare mean against median for Annual_Income and explain the gap — which one belongs in a board report on a skewed distribution?", ""),
            ("Compute the correlation matrix and identify the strongest driver of the risk score.", "uv run python -c \"import pandas as pd; d=pd.read_csv('df_scored.csv'); print(d[['Annual_Income','Credit_Score','Debt_to_Income_Ratio','Missed_Payments_Last_2Y','Calculated_Risk_Score']].corr().round(3))\""),
            ("Prompt your AI assistant: \"Write a Python script that downloads 2 years of daily prices for a ticker with yfinance and computes: daily returns from the close, annualised return, annualised volatility as the standard deviation of daily returns times the square root of 252, a rolling 20-day annualised volatility series, the cumulative return series, and the maximum drawdown computed as the minimum of (cumulative / cumulative.cummax() - 1) together with the peak and trough dates. Plot the cumulative return with the drawdown shaded underneath in a second matplotlib panel and save to PNG. Print all headline statistics.\"", ""),
            ("Save as stats_analysis.py and check the volatility annualisation uses sqrt(252) on DAILY returns, a very common AI-generated error.", ""),
            ("Run the analysis.", "uv run python stats_analysis.py"),
            ("Sanity-check the drawdown: it must be negative or zero, never positive, and the trough date must fall on or after the peak date.", ""),
            ("Verify the correlation matrix is symmetric with a unit diagonal.", ""),
            ("Discuss: a portfolio with the same annualised return but half the maximum drawdown — why does the risk committee prefer it, and which statistic alone would have hidden that difference?", ""),
        ],
        test="The correlation matrix is symmetric with 1.0 on the diagonal; maximum drawdown is <= 0 with trough_date >= peak_date; the rolling volatility series has exactly 19 leading NaN values for a 20-day window.",
    ),
    dict(
        num=61,
        topic=9,
        title="Streamlit Capstone Part 3 — Technical Analysis and Risk Scoring Pages",
        objective="LO8: Integrate the OOP analyzer and the apply/pipe pipeline into the Streamlit application as new interactive pages.",
        desc=(
            "The capstone continues in the SAME loan-analytics-app/app.py from labs 49-50. The "
            "learner converts it to a multi-page app with an st.sidebar.radio navigation and adds two "
            "new pages. The Technical Analysis page imports StockTechnicalAnalyzer from lab 56, takes "
            "a ticker and period from user input, and renders the price/SMA and RSI charts plus the "
            "BUY/SELL signals table. The Risk Scoring page imports the lab 59 pipeline, runs "
            "clean → enrich → score on the filtered loan book, and shows the Risk_Profile "
            "distribution, the risk-versus-credit-score scatter and a downloadable scored CSV."
        ),
        build="A multi-page app.py with Loan Analytics, Technical Analysis and Risk Scoring pages, importing analyzer.py and pipeline.py.",
        services="uv, Streamlit, pandas, matplotlib, yfinance, VS Code / Cursor AI assistant",
        steps=[
            ("Return to the capstone app folder from labs 49-50 — do NOT create a new project.", "cd loan-analytics-app"),
            ("Add the market-data dependency and copy in the Topic 8 and Topic 9 modules the app will import.", "uv add yfinance && cp ../lab-56-stock-analyzer/analyzer.py . && cp ../lab-59-pipe-pipeline/pipeline.py . && cp ../lab-58-lambda-vs-function/classify.py ."),
            ("Prompt your AI assistant: \"Convert this existing Streamlit app.py into a multi-page app using an st.sidebar.radio navigation with three pages: 'Loan Analytics', 'Technical Analysis' and 'Risk Scoring'. Move all the current KPI cards, filters and tabs under 'Loan Analytics' unchanged. On 'Technical Analysis', import StockTechnicalAnalyzer from analyzer.py, add a st.text_input for the ticker and a st.selectbox for the period, run the analysis on a button click inside a st.spinner, then render the price-with-SMA chart, the RSI chart with 30/70 reference lines, and the BUY/SELL signals table, showing st.error if fetch_data returns False. On 'Risk Scoring', import run_pipeline from pipeline.py, run it on the filtered loan book, and show the Risk_Profile distribution bar chart, a scatter of Credit_Score against Calculated_Risk_Score coloured by Risk_Profile, the sector summary table, and a st.download_button for the scored CSV. Cache the yfinance call with @st.cache_data.\"", ""),
            ("Apply the changes to app.py and confirm the labs 49-50 Loan Analytics page still works exactly as before — a regression here means the refactor broke existing functionality.", ""),
            ("Run the app.", "uv run streamlit run app.py"),
            ("Navigate to Technical Analysis, enter a valid ticker and confirm both charts and the signals table render.", ""),
            ("Enter an invalid ticker and confirm the page shows an st.error message rather than a traceback — the Topic 5 error-handling discipline applied to a UI.", ""),
            ("Navigate to Risk Scoring and confirm the Risk_Profile counts match the lab 57 value counts when no sidebar filters are applied.", ""),
            ("Change a sidebar filter and confirm the Risk Scoring page recomputes on the filtered subset only.", ""),
            ("Download the scored CSV from the app and verify it opens with the Calculated_Risk_Score and Risk_Profile columns present.", "uv run python -c \"import pandas as pd; print(pd.read_csv('~/Downloads/scored_loans.csv').columns.tolist())\""),
        ],
        test="All three pages load from the sidebar radio; the Loan Analytics page is unchanged from lab 50; an invalid ticker shows st.error not a traceback; the unfiltered Risk_Profile counts match lab 57 exactly.",
    ),
    dict(
        num=62,
        topic=9,
        title="Streamlit Capstone Finale — Test, Polish and Deploy the Analytics App",
        objective="LO8: Assess the completed application to identify gaps, test the results, and deploy the finished capstone.",
        desc=(
            "The course finale. The learner completes the SAME app.py: adds an executive summary "
            "header with the headline KPIs, caching on every expensive computation, a data-refresh "
            "control, error guards on every empty-data path, and an About page documenting the data "
            "source, the risk-model formula and its limitations — the model-transparency the earlier "
            "labs argued for. The app is then assessed against a gap checklist, its outputs are "
            "regression-tested against the lab 47, 48 and 57 numbers, and it is deployed either "
            "locally on the network or to Streamlit Community Cloud."
        ),
        build="The finished, tested and deployed Portfolio & Loan Analytics application with a README and a passing test suite.",
        services="uv, Streamlit, pandas, pytest, Git, Streamlit Community Cloud, VS Code / Cursor AI assistant",
        steps=[
            ("Return to the capstone app folder — this is the final edit of the same app.py.", "cd loan-analytics-app"),
            ("Assess the app against a gap checklist and write down every failure: does every page handle an empty filtered frame? Is every expensive call cached? Does any number appear without units or a currency? Is the risk formula documented anywhere in the UI?", ""),
            ("Prompt your AI assistant: \"Review and complete this Streamlit app. Add an executive summary banner at the top of every page showing total applications, approval rate and total risk-adjusted exposure. Add @st.cache_data to every expensive computation with a Refresh Data button calling st.cache_data.clear(). Add an 'About & Methodology' page documenting the data source, the exact risk-score formula, the Risk_Profile band thresholds, the SMA and RSI parameters and a plain-English limitations section. Add empty-state guards so every chart shows an informative message instead of raising when the filtered DataFrame is empty. Finally write a requirements.txt and a README.md with run instructions.\"", ""),
            ("Apply the changes, then write regression tests asserting the app's helper functions reproduce the known numbers from labs 47, 48 and 57.", ""),
            ("Run the regression suite.", "uv run pytest -v"),
            ("Run the app and click through all four pages under three different filter combinations, including one that yields zero rows.", "uv run streamlit run app.py"),
            ("Confirm the zero-row case shows informative messages on every page with no traceback in the terminal.", ""),
            ("Serve the app on the local network so a colleague can open it from their own machine.", "uv run streamlit run app.py --server.address 0.0.0.0 --server.port 8501"),
            ("Export the dependency list and initialise a Git repository for deployment.", "uv export --no-hashes --format requirements-txt > requirements.txt && git init && git add . && git commit -m 'Portfolio & Loan Analytics capstone'"),
            ("Deploy: push to GitHub and connect the repository at share.streamlit.io, selecting app.py as the entry point, then open the public URL and verify every page works in the cloud.", ""),
            ("Present your app: walk through one business question — for example 'which employment sector carries our highest risk-adjusted exposure?' — and answer it live using only the dashboard, without touching Python.", ""),
        ],
        test="pytest passes; all four pages render under every filter combination including the empty case; the deployed URL loads and reproduces the same KPI values as the local app; a non-programmer can answer a business question using only the UI.",
    ),
]
