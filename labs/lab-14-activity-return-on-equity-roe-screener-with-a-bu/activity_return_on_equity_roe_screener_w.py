"""Lab 14 — Activity: Return on Equity (ROE) Screener with a BUY / SELL Threshold

Topic 3: Problem Solving with Control Structures
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply conditional logic to a real SGX fundamental metric, computing ROE from live financial statements and converting it into an investment decision.

Goal: You pull DBS Group Holdings (D05.SI) financials with yfinance, compute Return on Equity as Net Income divided by AVERAGE shareholders' equity, and apply a 15% threshold to generate a BUY or SELL signal. Using average equity (latest and prior year) rather than closing equity is the analyst convention, because net income is earned across the whole year. You also meet your first ZeroDivisionError risk: a company with zero or missing equity.

You will build: roe_screener.py — computes ROE for D05.SI from live yfinance statements and prints a threshold-based BUY/SELL recommendation.
Tools: uv, yfinance, pandas, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python activity_return_on_equity_roe_screener_w.py
"""


def main():
    print("Lab 14: Activity: Return on Equity (ROE) Screener with a BUY / SELL Threshold")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project and add the market-data dependencies.
    #   $ uv init lab-14-roe-screener && cd lab-14-roe-screener && uv add yfinance pandas
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Check that uv recorded yfinance and pandas in pyproject.toml.
    #   $ uv run python -c "import yfinance, pandas; print(yfinance.__version__, pandas.__version__)"
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Create roe_screener.py and fetch DBS: build a yf.Ticker('D05.SI') object,
    # then read stock.financials into income_stmt and stock.balance_sheet into
    # balance_sheet.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Inspect the raw statements once so you know the row labels you are about
    # to index — print income_stmt.index and balance_sheet.index.
    #   $ uv run python roe_screener.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Extract Net Income with income_stmt.loc['Net Income'].iloc[0] (iloc[0] is
    # the most recent year), and extract Stockholders Equity for both .iloc[0]
    # and .iloc[1].
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Compute avg_equity = (equity_latest + equity_prev) / 2, then roe =
    # (net_income / avg_equity) * 100.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Print a formatted report: company name and ticker, Net Income with
    # thousands separators (${:,.0f}), Average Shareholders Equity, and ROE to 2
    # decimals with a percent sign.
    #   $ uv run python roe_screener.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Add the decision rule with if-else: ROE above 15% prints 'STRONG —
    # Consider BUY', 10% to 15% prints 'MODERATE — HOLD', below 10% prints 'WEAK
    # — Consider SELL'.
    #   $ uv run python roe_screener.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "This script divides net income by
    # average shareholders equity. Add guards so it fails safely: raise or
    # report a clear message if average equity is zero (ZeroDivisionError), if
    # the 'Net Income' or 'Stockholders Equity' row is missing from the
    # statement (KeyError), or if only one year of balance sheet data exists
    # (IndexError). Do not swallow the error silently." Review the generated
    # guards.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Apply the guarded version and deliberately break it: change the ticker to
    # a nonsense symbol such as 'ZZZZ.SI' and confirm the script reports a clear
    # message rather than crashing with a traceback.
    #   $ uv run python roe_screener.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Wrap the whole calculation in a loop over three banks — D05.SI, U11.SI,
    # O39.SI — so one run screens all three and prints one recommendation line
    # each.
    #   $ uv run python roe_screener.py
    # TODO: implement this step

    # ---- Step 12 ----------------------------------------------------------
    # Discuss: why does using average equity instead of year-end equity matter
    # most for a company that raised a lot of capital mid-year?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python roe_screener.py`. You should see a Net Income figure,
    # an Average Shareholders Equity figure and an ROE percentage for each of
    # D05.SI, U11.SI and O39.SI, each followed by a BUY / HOLD / SELL line.
    # Substituting an invalid ticker must produce a readable message, never an
    # unhandled traceback.


if __name__ == "__main__":
    main()
