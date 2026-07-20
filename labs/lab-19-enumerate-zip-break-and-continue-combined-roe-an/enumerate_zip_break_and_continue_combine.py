"""Lab 19 — Enumerate, Zip, Break and Continue — Combined ROE and ROA Scanner

Topic 3: Problem Solving with Control Structures
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply enumerate and zip to combine parallel financial series, and break and continue to control early exit and skipping while scanning market data.

Goal: Real screening code walks several parallel lists at once — tickers, ROE values and ROA values — and must decide row by row whether to include, skip or stop. You use zip to fuse the three series into one table, enumerate to rank it, continue to skip tickers with missing data or negative returns, and break to stop a budget-constrained buying loop the moment the cash limit would be breached. You also see the classic zip trap: zip stops silently at the SHORTEST list, so a mismatched length loses data without any error.

You will build: roe_roa_scanner.py — a combined ROE + ROA screening table built with zip and enumerate, with continue-based skipping and a break-controlled budget allocator.
Tools: uv, yfinance, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python enumerate_zip_break_and_continue_combine.py
"""


def main():
    print("Lab 19: Enumerate, Zip, Break and Continue — Combined ROE and ROA Scanner")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project and add yfinance.
    #   $ uv init lab-19-roe-roa-scanner && cd lab-19-roe-roa-scanner && uv add yfinance
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # In roe_roa_scanner.py, loop over sgx_tickers = ['D05.SI', 'U11.SI',
    # 'O39.SI', 'Z74.SI', 'V03.SI'], read stock.info, and append to three
    # parallel lists: tickers, roes (info.get('returnOnEquity', 0) * 100) and
    # roas (info.get('returnOnAssets', 0) * 100).
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Fuse the three lists with data = zip(tickers, roes, roas) and print a
    # header row plus one aligned line per stock using {t:<10} {roe:<10.2f}
    # {roa:<10.2f}.
    #   $ uv run python roe_roa_scanner.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # SEE THE ZIP TRAP: temporarily append one extra ticker to `tickers` only,
    # re-run, and confirm the extra row disappears with no error. Restore the
    # lists and add a comment recording the lesson.
    #   $ uv run python roe_roa_scanner.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Add enumerate to rank the table: `for rank, (t, roe, roa) in
    # enumerate(zip(tickers, roes, roas), 1)` and print the rank in the first
    # column. Note that start=1 gives human-readable ranks.
    #   $ uv run python roe_roa_scanner.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Use continue to skip rows with no usable data: inside the loop, if roe ==
    # 0 or roa == 0, print a 'no data — skipped' line and continue to the next
    # ticker.
    #   $ uv run python roe_roa_scanner.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Add a quality flag column computed with a ternary: 'QUALITY' when ROE > 10
    # and ROA > 1, otherwise 'REVIEW'.
    #   $ uv run python roe_roa_scanner.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Build the break demo — a budget allocator: with budget = 100000 and a list
    # of intended trade sizes [20000, 35000, 30000, 25000, 40000], accumulate
    # them in a for loop and break the moment the next trade would exceed the
    # budget, printing which trade was refused.
    #   $ uv run python roe_roa_scanner.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Add a second continue demo on a transaction feed: given [120.50, -50.00,
    # 300.25, -20.00, 150.00, 0, 45.75], skip every non-positive amount (refunds
    # and zeros) and total only genuine expenses.
    #   $ uv run python roe_roa_scanner.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Rewrite this scanner so the three
    # parallel lists become a single list of dictionaries, and explain why that
    # is safer than zipping three separate lists that must stay the same length.
    # Keep the enumerate ranking, the continue-based skipping and the identical
    # printed output." Compare the two designs side by side.
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Apply the AI refactor into a second file, run both, and confirm the
    # printed tables are byte-for-byte identical.
    #   $ uv run python roe_roa_scanner_v2.py
    # TODO: implement this step

    # ---- Step 12 ----------------------------------------------------------
    # Discuss: break exits the loop entirely while continue only skips the
    # current iteration. In a compliance scan of 5,000 transactions, which one
    # would you use to skip malformed records, and which to abort on a hard stop
    # rule?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python roe_roa_scanner.py`. The scanner must print a ranked
    # table with Rank, Ticker, ROE %, ROA % and a QUALITY/REVIEW flag for each
    # stock that returned data, skip lines for any that did not, a budget
    # allocator that stops before breaching $100,000, and a total-valid-expenses
    # figure of $616.50 from the transaction feed.


if __name__ == "__main__":
    main()
