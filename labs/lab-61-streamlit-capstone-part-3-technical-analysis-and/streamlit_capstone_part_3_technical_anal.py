"""Lab 61 — Streamlit Capstone Part 3 — Technical Analysis and Risk Scoring Pages

Topic 9: Analyze Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO8: Integrate the OOP analyzer and the apply/pipe pipeline into the Streamlit application as new interactive pages.

Goal: The capstone continues in the SAME loan-analytics-app/app.py from labs 49-50. The learner converts it to a multi-page app with an st.sidebar.radio navigation and adds two new pages. The Technical Analysis page imports StockTechnicalAnalyzer from lab 56, takes a ticker and period from user input, and renders the price/SMA and RSI charts plus the BUY/SELL signals table. The Risk Scoring page imports the lab 59 pipeline, runs clean → enrich → score on the filtered loan book, and shows the Risk_Profile distribution, the risk-versus-credit-score scatter and a downloadable scored CSV.

You will build: A multi-page app.py with Loan Analytics, Technical Analysis and Risk Scoring pages, importing analyzer.py and pipeline.py.
Tools: uv, Streamlit, pandas, matplotlib, yfinance, VS Code / Cursor AI assistant

Run this lab with uv:
    uv run python streamlit_capstone_part_3_technical_anal.py
"""


def main():
    print("Lab 61: Streamlit Capstone Part 3 — Technical Analysis and Risk Scoring Pages")

    # ---- Step 1 -----------------------------------------------------------
    # Return to the capstone app folder from labs 49-50 — do NOT create a new
    # project.
    #   $ cd loan-analytics-app
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Add the market-data dependency and copy in the Topic 8 and Topic 9 modules
    # the app will import.
    #   $ uv add yfinance && cp ../lab-56-stock-analyzer/analyzer.py . && cp ../lab-59-pipe-pipeline/pipeline.py . && cp ../lab-58-lambda-vs-function/classify.py .
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Prompt your AI assistant: "Convert this existing Streamlit app.py into a
    # multi-page app using an st.sidebar.radio navigation with three pages:
    # 'Loan Analytics', 'Technical Analysis' and 'Risk Scoring'. Move all the
    # current KPI cards, filters and tabs under 'Loan Analytics' unchanged. On
    # 'Technical Analysis', import StockTechnicalAnalyzer from analyzer.py, add
    # a st.text_input for the ticker and a st.selectbox for the period, run the
    # analysis on a button click inside a st.spinner, then render the
    # price-with-SMA chart, the RSI chart with 30/70 reference lines, and the
    # BUY/SELL signals table, showing st.error if fetch_data returns False. On
    # 'Risk Scoring', import run_pipeline from pipeline.py, run it on the
    # filtered loan book, and show the Risk_Profile distribution bar chart, a
    # scatter of Credit_Score against Calculated_Risk_Score coloured by
    # Risk_Profile, the sector summary table, and a st.download_button for the
    # scored CSV. Cache the yfinance call with @st.cache_data."
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Apply the changes to app.py and confirm the labs 49-50 Loan Analytics page
    # still works exactly as before — a regression here means the refactor broke
    # existing functionality.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Run the app.
    #   $ uv run streamlit run app.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Navigate to Technical Analysis, enter a valid ticker and confirm both
    # charts and the signals table render.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Enter an invalid ticker and confirm the page shows an st.error message
    # rather than a traceback — the Topic 5 error-handling discipline applied to
    # a UI.
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Navigate to Risk Scoring and confirm the Risk_Profile counts match the lab
    # 57 value counts when no sidebar filters are applied.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Change a sidebar filter and confirm the Risk Scoring page recomputes on
    # the filtered subset only.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Download the scored CSV from the app and verify it opens with the
    # Calculated_Risk_Score and Risk_Profile columns present.
    #   $ uv run python -c "import pandas as pd; print(pd.read_csv('~/Downloads/scored_loans.csv').columns.tolist())"
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # All three pages load from the sidebar radio; the Loan Analytics page is
    # unchanged from lab 50; an invalid ticker shows st.error not a traceback;
    # the unfiltered Risk_Profile counts match lab 57 exactly.


if __name__ == "__main__":
    main()
