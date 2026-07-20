# Lab 62 — Streamlit Capstone Finale — Test, Polish and Deploy the Analytics App

**Topic 9: Analyze Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO8: Assess the completed application to identify gaps, test the results, and deploy the finished capstone.

## Goal

The course finale. The learner completes the SAME app.py: adds an executive summary header with the headline KPIs, caching on every expensive computation, a data-refresh control, error guards on every empty-data path, and an About page documenting the data source, the risk-model formula and its limitations — the model-transparency the earlier labs argued for. The app is then assessed against a gap checklist, its outputs are regression-tested against the lab 47, 48 and 57 numbers, and it is deployed either locally on the network or to Streamlit Community Cloud.

## What you'll build

The finished, tested and deployed Portfolio & Loan Analytics application with a README and a passing test suite.

**Tools:** uv, Streamlit, pandas, pytest, Git, Streamlit Community Cloud, VS Code / Cursor AI assistant

## Step-by-step

1. Return to the capstone app folder — this is the final edit of the same app.py.

   ```bash
   cd loan-analytics-app
   ```

2. Assess the app against a gap checklist and write down every failure: does every page handle an empty filtered frame? Is every expensive call cached? Does any number appear without units or a currency? Is the risk formula documented anywhere in the UI?
3. Prompt your AI assistant: "Review and complete this Streamlit app. Add an executive summary banner at the top of every page showing total applications, approval rate and total risk-adjusted exposure. Add @st.cache_data to every expensive computation with a Refresh Data button calling st.cache_data.clear(). Add an 'About & Methodology' page documenting the data source, the exact risk-score formula, the Risk_Profile band thresholds, the SMA and RSI parameters and a plain-English limitations section. Add empty-state guards so every chart shows an informative message instead of raising when the filtered DataFrame is empty. Finally write a requirements.txt and a README.md with run instructions."
4. Apply the changes, then write regression tests asserting the app's helper functions reproduce the known numbers from labs 47, 48 and 57.
5. Run the regression suite.

   ```bash
   uv run pytest -v
   ```

6. Run the app and click through all four pages under three different filter combinations, including one that yields zero rows.

   ```bash
   uv run streamlit run app.py
   ```

7. Confirm the zero-row case shows informative messages on every page with no traceback in the terminal.
8. Serve the app on the local network so a colleague can open it from their own machine.

   ```bash
   uv run streamlit run app.py --server.address 0.0.0.0 --server.port 8501
   ```

9. Export the dependency list and initialise a Git repository for deployment.

   ```bash
   uv export --no-hashes --format requirements-txt > requirements.txt && git init && git add . && git commit -m 'Portfolio & Loan Analytics capstone'
   ```

10. Deploy: push to GitHub and connect the repository at share.streamlit.io, selecting app.py as the entry point, then open the public URL and verify every page works in the cloud.
11. Present your app: walk through one business question — for example 'which employment sector carries our highest risk-adjusted exposure?' — and answer it live using only the dashboard, without touching Python.

## Test it

pytest passes; all four pages render under every filter combination including the empty case; the deployed URL loads and reproduces the same KPI values as the local app; a non-programmer can answer a business question using only the UI.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
