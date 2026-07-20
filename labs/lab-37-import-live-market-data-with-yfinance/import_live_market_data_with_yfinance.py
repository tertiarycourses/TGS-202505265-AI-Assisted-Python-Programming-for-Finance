"""Lab 37 — Import Live Market Data with yfinance

Topic 6: Import and Process Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO5: Download multi-ticker market data with yfinance and reshape the result into an analysis-ready DataFrame.

Goal: The learner downloads three years of daily data for a small multi-market portfolio with yfinance and immediately meets its awkward output shape: a MultiIndex column frame when several tickers are requested, and a flat frame when only one is. The learner writes a loader that normalises both cases into a tidy long-format DataFrame with Date, Ticker and Close, caches it to CSV so the rest of the course is not dependent on the network, and wraps the download in the try/except pattern learned in Topic 5.

You will build: A uv project `lab-37-yfinance-import` with load_market.py producing a tidy long-format DataFrame and a cached market_data.csv covering three years and at least four tickers.
Tools: uv, yfinance, pandas, AI coding assistant

Run this lab with uv:
    uv run python import_live_market_data_with_yfinance.py
"""


def main():
    print("Lab 37: Import Live Market Data with yfinance")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add the data dependencies.
    #   $ uv init lab-37-yfinance-import && cd lab-37-yfinance-import && uv add yfinance pandas
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Download three years of daily data for a single ticker and inspect the
    # shape of what comes back.
    #   $ uv run python -c "import yfinance as yf; d=yf.download('AAPL', period='3y'); print(d.columns); print(d.head())"
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Now download four tickers at once — AAPL, MSFT, D05.SI, O39.SI — and print
    # the columns again to see the MultiIndex.
    #   $ uv run python load_market.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Discuss: with one ticker the columns are flat; with several they are a
    # (field, ticker) MultiIndex. Code written against one shape breaks against
    # the other — a very common production bug.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # In load_market.py write fetch(tickers, period) that always returns a tidy
    # long frame with columns Date, Ticker, Open, High, Low, Close, Volume,
    # using .stack() to flatten the MultiIndex case and adding a Ticker column
    # in the single case.
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Wrap the download in try/except (Topic 5 pattern) so a failed or empty
    # ticker is reported and skipped rather than aborting the whole fetch.
    #   $ uv run python load_market.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Cache the tidy frame to market_data.csv and add a guard so the script
    # reads the cache when it exists and only hits the network otherwise.
    #   $ uv run python load_market.py && wc -l market_data.csv
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # AI STEP — prompt your AI assistant: "yf.download returns a MultiIndex
    # column DataFrame for multiple tickers and a flat one for a single ticker.
    # Write a function that normalises both into a long-format DataFrame with
    # columns Date, Ticker, Open, High, Low, Close, Volume. Handle auto_adjust
    # and explain what Adj Close means for a dividend-paying stock."
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Test the AI's normaliser with a one-ticker call AND a four-ticker call and
    # confirm both produce identical column layouts.
    #   $ uv run python load_market.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Discuss the AI's explanation of adjusted close: why backtesting on
    # unadjusted close overstates losses around ex-dividend dates.
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Print a summary — the date range, the row count per ticker, and the number
    # of trading days captured.
    #   $ uv run python load_market.py
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # market_data.csv exists, covers roughly three years, contains all four
    # tickers in long format with one row per ticker per trading day, and the
    # loader returns the same column layout whether called with one ticker or
    # four.


if __name__ == "__main__":
    main()
