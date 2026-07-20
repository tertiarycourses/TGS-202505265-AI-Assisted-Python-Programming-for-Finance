"""Lab 30 — Try/Except on a Failing Market-Data Fetch

Topic 5: Error Handling Using Exception
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO4: Wrap a live market-data call in try/except so a delisted or invalid ticker does not halt the pipeline.

Goal: The learner writes a market-data fetcher that downloads recent closing prices for a watchlist using yfinance. One entry in the watchlist is a delisted or misspelled ticker that returns an empty frame. The learner catches the failure per ticker so the remaining instruments are still processed, and separates a network/API exception from an empty-result condition — a distinction that matters when a batch job runs unattended overnight.

You will build: A uv project `lab-30-market-fetch` with fetch_prices.py that returns a summary dict of successful tickers and a separate list of failed tickers with the reason for each failure.
Tools: uv, yfinance, pandas, AI coding assistant

Run this lab with uv:
    uv run python try_except_on_a_failing_market_data_fetc.py
"""


def main():
    print("Lab 30: Try/Except on a Failing Market-Data Fetch")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project and add the market-data dependencies.
    #   $ uv init lab-30-market-fetch && cd lab-30-market-fetch && uv add yfinance pandas
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Write fetch_prices.py with WATCHLIST = ['AAPL', 'MSFT', 'ENRNQ', 'D05.SI']
    # — ENRNQ is a delisted ticker that will return no data.
    #   $ touch fetch_prices.py
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Write a naive loop with no error handling that calls yf.download(t,
    # period='5d') and prints the last close for each ticker. Run it and observe
    # the failure.
    #   $ uv run python fetch_prices.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Discuss: the delisted ticker produced an empty DataFrame, so
    # `df['Close'].iloc[-1]` raised IndexError and the loop died BEFORE reaching
    # D05.SI. One bad symbol silently cost you the rest of the watchlist.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Refactor the loop so each ticker is fetched inside its own try/except.
    # Catch IndexError and KeyError for empty data, and catch Exception as a
    # last resort for network/API faults, appending (ticker, reason) to a
    # failures list.
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Run the fixed script and confirm every good ticker is priced and the bad
    # one is reported.
    #   $ uv run python fetch_prices.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # AI STEP — prompt your AI assistant: "Review this Python function that
    # fetches prices with yfinance inside a try/except. Is catching bare
    # Exception acceptable here for an overnight batch job? Suggest more
    # specific exception types and show how to log the failing ticker with the
    # traceback so an analyst can debug it the next morning."
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Apply the AI's logging suggestion, but verify yourself that a genuine bug
    # (for example a typo in a column name) is still visible rather than
    # swallowed by the broad handler.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Add a summary print at the end: how many tickers succeeded, how many
    # failed, and the reason for each failure.
    #   $ uv run python fetch_prices.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Discuss: why the pipeline must record which tickers were skipped — a
    # portfolio valuation computed from three of four holdings is wrong, not
    # merely incomplete.
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # The script completes without crashing, prints a latest close for AAPL,
    # MSFT and D05.SI, and ends with a failure report naming ENRNQ and its
    # reason. Exit status is 0.


if __name__ == "__main__":
    main()
