"""Lab 60 — Descriptive Statistics, Correlation and Tracking Change Over Time

Topic 9: Analyze Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO8: Apply descriptive statistics to summarise risk and return, and track trend, volatility and drawdown over time.

Goal: Two halves. First, cross-sectional statistics on the loan book: .describe(), mean, median, standard deviation and a correlation matrix of Credit_Score, Debt_to_Income_Ratio, Annual_Income and Calculated_Risk_Score, with the median-versus-mean gap exposing income skew. Second, time-series tracking on a price history: daily returns, a rolling 20-day annualised volatility, the cumulative return trend and the maximum drawdown computed from the running peak — the three numbers an investment committee asks for.

You will build: A stats_analysis.py script producing the loan-book statistics and correlation matrix, plus a drawdown/volatility report and chart.
Tools: uv, pandas, NumPy, matplotlib, yfinance, VS Code / Cursor AI assistant

Run this lab with uv:
    uv run python descriptive_statistics_correlation_and_t.py
"""


def main():
    print("Lab 60: Descriptive Statistics, Correlation and Tracking Change Over Time")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add the libraries.
    #   $ uv init lab-60-statistics-and-trend && cd lab-60-statistics-and-trend && uv add pandas numpy matplotlib yfinance
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Copy df_scored.csv from lab 57.
    #   $ cp ../lab-57-credit-risk-apply/df_scored.csv .
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Produce the baseline descriptive statistics for the numeric loan columns.
    #   $ uv run python -c "import pandas as pd; d=pd.read_csv('df_scored.csv'); print(d[['Annual_Income','Credit_Score','Debt_to_Income_Ratio','Calculated_Risk_Score']].describe().round(2))"
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Compare mean against median for Annual_Income and explain the gap — which
    # one belongs in a board report on a skewed distribution?
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Compute the correlation matrix and identify the strongest driver of the
    # risk score.
    #   $ uv run python -c "import pandas as pd; d=pd.read_csv('df_scored.csv'); print(d[['Annual_Income','Credit_Score','Debt_to_Income_Ratio','Missed_Payments_Last_2Y','Calculated_Risk_Score']].corr().round(3))"
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Prompt your AI assistant: "Write a Python script that downloads 2 years of
    # daily prices for a ticker with yfinance and computes: daily returns from
    # the close, annualised return, annualised volatility as the standard
    # deviation of daily returns times the square root of 252, a rolling 20-day
    # annualised volatility series, the cumulative return series, and the
    # maximum drawdown computed as the minimum of (cumulative /
    # cumulative.cummax() - 1) together with the peak and trough dates. Plot the
    # cumulative return with the drawdown shaded underneath in a second
    # matplotlib panel and save to PNG. Print all headline statistics."
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Save as stats_analysis.py and check the volatility annualisation uses
    # sqrt(252) on DAILY returns, a very common AI-generated error.
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Run the analysis.
    #   $ uv run python stats_analysis.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Sanity-check the drawdown: it must be negative or zero, never positive,
    # and the trough date must fall on or after the peak date.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Verify the correlation matrix is symmetric with a unit diagonal.
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Discuss: a portfolio with the same annualised return but half the maximum
    # drawdown — why does the risk committee prefer it, and which statistic
    # alone would have hidden that difference?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # The correlation matrix is symmetric with 1.0 on the diagonal; maximum
    # drawdown is <= 0 with trough_date >= peak_date; the rolling volatility
    # series has exactly 19 leading NaN values for a 20-day window.


if __name__ == "__main__":
    main()
