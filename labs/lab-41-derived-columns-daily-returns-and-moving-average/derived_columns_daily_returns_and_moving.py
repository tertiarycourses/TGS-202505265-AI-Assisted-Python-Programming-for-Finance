"""Lab 41 — Derived Columns — Daily Returns and Moving Averages

Topic 6: Import and Process Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO5: Create derived analytical columns — daily and cumulative returns, rolling moving averages and rolling volatility — with pct_change, shift and rolling.

Goal: The learner turns a price table into an analytics table. Daily simple returns come from pct_change(); log returns from np.log on a shift() ratio; cumulative growth from cumprod. Rolling windows produce the 20-day and 50-day simple moving averages and a 20-day rolling volatility. The lab emphasises correct grouping — every derived column must be computed per ticker with groupby, or the first return of each ticker will be contaminated by the last price of the previous one, a mistake that is easy to make and hard to see.

You will build: A uv project `lab-41-derived-columns` with features.py producing enriched_prices.csv containing daily_return, log_return, cum_return, sma_20, sma_50 and vol_20 per ticker.
Tools: uv, pandas, numpy, AI coding assistant

Run this lab with uv:
    uv run python derived_columns_daily_returns_and_moving.py
"""


def main():
    print("Lab 41: Derived Columns — Daily Returns and Moving Averages")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add the dependencies.
    #   $ uv init lab-41-derived-columns && cd lab-41-derived-columns && uv add pandas numpy && cp ../lab-37-yfinance-import/market_data.csv .
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Load the long-format data, sort by Ticker then Date, and add daily_return
    # using df.groupby('Ticker')['Close'].pct_change().
    #   $ uv run python features.py
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Deliberately compute the same column WITHOUT groupby and compare the first
    # row of each ticker between the two versions.
    #   $ uv run python features.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Discuss: without groupby the first row of MSFT was computed against the
    # last price of AAPL, producing a nonsense return. Nothing raised an error —
    # this is a silent correctness bug that survives all the way to a published
    # number.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Add log_return using np.log(close / close.shift(1)) within the groupby,
    # and explain when log returns are preferred (time-additivity for
    # multi-period aggregation).
    #   $ uv run python features.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Add cum_return as (1 + daily_return).cumprod() - 1 per ticker, and print
    # the three-year cumulative return for each instrument.
    #   $ uv run python features.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Add sma_20 and sma_50 with groupby + rolling(window).mean(), and confirm
    # the first 19 and 49 values respectively are NaN by design.
    #   $ uv run python features.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Add vol_20 as the 20-day rolling standard deviation of daily_return,
    # annualised by multiplying by the square root of 252.
    #   $ uv run python features.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # AI STEP — prompt your AI assistant: "Given a long-format pandas DataFrame
    # with columns Date, Ticker and Close, write vectorised code that adds daily
    # simple returns, log returns, cumulative return, a 20-day and 50-day SMA,
    # and 20-day annualised rolling volatility — all computed per ticker with
    # groupby so no value leaks across tickers. Explain why min_periods matters
    # on the rolling calls."
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Verify the AI's output on the boundary rows: check the first row of each
    # ticker is NaN for daily_return, and that no SMA value appears before its
    # window is full.
    #   $ uv run python features.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Write the enriched frame to enriched_prices.csv and print a per-ticker
    # summary of cumulative return and mean annualised volatility.
    #   $ uv run python features.py && head -3 enriched_prices.csv
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # enriched_prices.csv contains all six derived columns, the first row of
    # every ticker has NaN daily_return, sma_50 is NaN for exactly the first 49
    # rows of each ticker, and the per-ticker summary prints a plausible
    # cumulative return and volatility.


if __name__ == "__main__":
    main()
