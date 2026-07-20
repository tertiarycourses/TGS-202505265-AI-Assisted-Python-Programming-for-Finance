# Lab 60 — Descriptive Statistics, Correlation and Tracking Change Over Time

**Topic 9: Analyze Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO8: Apply descriptive statistics to summarise risk and return, and track trend, volatility and drawdown over time.

## Goal

Two halves. First, cross-sectional statistics on the loan book: .describe(), mean, median, standard deviation and a correlation matrix of Credit_Score, Debt_to_Income_Ratio, Annual_Income and Calculated_Risk_Score, with the median-versus-mean gap exposing income skew. Second, time-series tracking on a price history: daily returns, a rolling 20-day annualised volatility, the cumulative return trend and the maximum drawdown computed from the running peak — the three numbers an investment committee asks for.

## What you'll build

A stats_analysis.py script producing the loan-book statistics and correlation matrix, plus a drawdown/volatility report and chart.

**Tools:** uv, pandas, NumPy, matplotlib, yfinance, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project and add the libraries.

   ```bash
   uv init lab-60-statistics-and-trend && cd lab-60-statistics-and-trend && uv add pandas numpy matplotlib yfinance
   ```

2. Copy df_scored.csv from lab 57.

   ```bash
   cp ../lab-57-credit-risk-apply/df_scored.csv .
   ```

3. Produce the baseline descriptive statistics for the numeric loan columns.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_scored.csv'); print(d[['Annual_Income','Credit_Score','Debt_to_Income_Ratio','Calculated_Risk_Score']].describe().round(2))"
   ```

4. Compare mean against median for Annual_Income and explain the gap — which one belongs in a board report on a skewed distribution?
5. Compute the correlation matrix and identify the strongest driver of the risk score.

   ```bash
   uv run python -c "import pandas as pd; d=pd.read_csv('df_scored.csv'); print(d[['Annual_Income','Credit_Score','Debt_to_Income_Ratio','Missed_Payments_Last_2Y','Calculated_Risk_Score']].corr().round(3))"
   ```

6. Prompt your AI assistant: "Write a Python script that downloads 2 years of daily prices for a ticker with yfinance and computes: daily returns from the close, annualised return, annualised volatility as the standard deviation of daily returns times the square root of 252, a rolling 20-day annualised volatility series, the cumulative return series, and the maximum drawdown computed as the minimum of (cumulative / cumulative.cummax() - 1) together with the peak and trough dates. Plot the cumulative return with the drawdown shaded underneath in a second matplotlib panel and save to PNG. Print all headline statistics."
7. Save as stats_analysis.py and check the volatility annualisation uses sqrt(252) on DAILY returns, a very common AI-generated error.
8. Run the analysis.

   ```bash
   uv run python stats_analysis.py
   ```

9. Sanity-check the drawdown: it must be negative or zero, never positive, and the trough date must fall on or after the peak date.
10. Verify the correlation matrix is symmetric with a unit diagonal.
11. Discuss: a portfolio with the same annualised return but half the maximum drawdown — why does the risk committee prefer it, and which statistic alone would have hidden that difference?

## Test it

The correlation matrix is symmetric with 1.0 on the diagonal; maximum drawdown is <= 0 with trough_date >= peak_date; the rolling volatility series has exactly 19 leading NaN values for a 20-day window.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
