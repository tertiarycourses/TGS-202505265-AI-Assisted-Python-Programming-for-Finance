# Lab 49 — Streamlit Capstone Part 1 — Portfolio & Loan Analytics App Shell

**Topic 7: Aggregate and Visualize Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO6: Publish an aggregation as an interactive Streamlit application with sidebar filters and KPI metric cards.

## Goal

The Streamlit capstone STARTS here. The learner creates the app project, writes app.py, and builds the shell of the 'Portfolio & Loan Analytics' dashboard: page config, a cached data loader for df_finance.csv, a sidebar with multiselect filters for Employment_Sector, Region and Loan_Status, and a row of four KPI metric cards (Total Applications, Approval Rate, Average Annual Income, Average Debt-to-Income Ratio) that all recompute live as the filters change. This same app.py is extended in labs 50, 61 and 62.

## What you'll build

A Streamlit project with app.py serving the filtered KPI dashboard at localhost:8501.

**Tools:** uv, Streamlit, pandas, VS Code / Cursor AI assistant

## Step-by-step

1. Create the capstone project — keep this folder, labs 50, 61 and 62 all extend it.

   ```bash
   uv init loan-analytics-app && cd loan-analytics-app
   ```

2. Add Streamlit and the data libraries.

   ```bash
   uv add streamlit pandas matplotlib
   ```

3. Copy df_finance.csv from lab 43 into the app folder.

   ```bash
   cp ../lab-43-mock-loan-data/df_finance.csv .
   ```

4. Prompt your AI assistant: "Write a Streamlit app.py titled 'Portfolio & Loan Analytics'. Use st.set_page_config with a wide layout. Add a load_data() function decorated with @st.cache_data that reads df_finance.csv. In the sidebar add three st.multiselect filters for Employment_Sector, Region and Loan_Status, each defaulting to all values. Filter the DataFrame by all three selections, then display four st.metric cards in st.columns(4): Total Applications, Approval Rate as a percentage, Average Annual Income formatted as SGD with thousands separators, and Average Debt-to-Income Ratio to 3 decimals. Show the filtered table below with st.dataframe."
5. Save the answer as app.py — this is THE file every remaining capstone lab edits. Read it and confirm @st.cache_data is on the loader and the filter is applied before the metrics are computed.
6. Run the app.

   ```bash
   uv run streamlit run app.py
   ```

7. Open http://localhost:8501 and change one sidebar filter — verify all four metric cards update.
8. Set the Loan_Status filter to Approved only and confirm the Approval Rate card reads 100%.
9. Clear all values from one filter and confirm the app shows a friendly empty-state message rather than crashing; add an if filtered.empty: st.warning(...) guard if it does not.
10. Commit or note the file structure — labs 50, 61 and 62 add to this exact app.py.

   ```bash
   ls -la app.py df_finance.csv pyproject.toml
   ```


## Test it

The app loads at localhost:8501; selecting a single Employment_Sector changes Total Applications to that sector's row count, and clearing a filter shows a warning instead of a traceback.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
