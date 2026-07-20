"""Lab 20 — Comprehensions — Net Profit Margin for 10 Singapore Stocks in One Line

Topic 3: Problem Solving with Control Structures
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply list, set and dict comprehensions to compute and filter financial metrics across a portfolio in a single readable expression.

Goal: Comprehensions are the idiom that makes Python financial code short and reviewable. You build up from simple currency conversion and GST examples to the topic's headline activity: net profit margin (Net Income / Total Revenue * 100) computed across ten SGX tickers with a single list comprehension, plus a set comprehension that de-duplicates tickers from a transaction history and a dict comprehension that builds a ticker-to-margin lookup and filters it to the high-margin names. You finish by comparing the comprehension against the equivalent for loop.

You will build: margin_comprehensions.py — computes net profit margin for 10 SGX stocks with a list comprehension, plus set and dict comprehension utilities and a filtered high-margin lookup.
Tools: uv, yfinance, pandas, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python comprehensions_net_profit_margin_for_10.py
"""


def main():
    print("Lab 20: Comprehensions — Net Profit Margin for 10 Singapore Stocks in One Line")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project and add the dependencies.
    #   $ uv init lab-20-margin-comprehensions && cd lab-20-margin-comprehensions && uv add yfinance pandas
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Warm up with three list comprehensions in margin_comprehensions.py:
    # convert prices_sgd = [35.50, 28.40, 13.10, 5.20] to USD at 0.74; apply 9%
    # GST to subtotals [100, 250, 45] with round(amt * 1.09, 2); and select
    # tickers priced above $20 using [t for t, p in zip(tickers, prices) if p >
    # 20].
    #   $ uv run python margin_comprehensions.py
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Add a set comprehension over a transaction history list of dicts to
    # extract the unique tickers: {t['ticker'] for t in transactions}. Print the
    # set and its length to prove duplicates were removed.
    #   $ uv run python margin_comprehensions.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Add two dict comprehensions: build a market-cap lookup from parallel lists
    # with {t: c for t, c in zip(tickers, market_caps)}, then filter an existing
    # price dict to only stocks above $20 with {t: p for t, p in prices.items()
    # if p > 20}.
    #   $ uv run python margin_comprehensions.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Now the main activity. Define a helper function get_margin(ticker) that
    # fetches stock.financials, reads Net Income and Total Revenue with
    # .loc[...].iloc[0], and returns {'ticker': ticker, 'margin': (net_income /
    # revenue) * 100}, returning a margin of None inside an except block.
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Define the ten tickers ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'J36.SI',
    # 'BN4.SI', 'V03.SI', 'C38U.SI', 'A17U.SI', 'C07.SI'] and compute every
    # margin in ONE line: results = [get_margin(t) for t in sgx_tickers].
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Print the results as an aligned table with a header, handling the None
    # case in the f-string so a failed fetch shows 'N/A' rather than crashing on
    # format.
    #   $ uv run python margin_comprehensions.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Add a filtering comprehension on top of the results: high_margin = [r for
    # r in results if r['margin'] is not None and r['margin'] > 20] and print
    # how many of the ten cleared the 20% bar.
    #   $ uv run python margin_comprehensions.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Build the dict lookup with a dict comprehension: margin_lookup =
    # {r['ticker']: round(r['margin'], 2) for r in results if r['margin'] is not
    # None}, then query a single ticker from it.
    #   $ uv run python margin_comprehensions.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Rewrite this single-line list
    # comprehension as an explicit for loop with the same behaviour, then tell
    # me which version you would approve in a code review for a financial
    # reporting system and why. Also point out any case where the comprehension
    # silently hides an error that the for loop would surface." Read the
    # reasoning carefully.
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Add the AI's for-loop version alongside the comprehension, run both, and
    # assert they produce identical results with a simple equality check printed
    # as PASS or FAIL.
    #   $ uv run python margin_comprehensions.py
    # TODO: implement this step

    # ---- Step 12 ----------------------------------------------------------
    # Discuss: the bare `except:` inside get_margin catches everything,
    # including a typo in a row label. Replace it with `except (KeyError,
    # IndexError, ZeroDivisionError)` and re-run — does anything now fail loudly
    # that was silently returning None before?
    #   $ uv run python margin_comprehensions.py
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python margin_comprehensions.py`. It must print the USD
    # prices, GST totals and >$20 ticker list; a unique-ticker set of size 3; a
    # market-cap dict and a filtered high-value price dict; a 10-row net profit
    # margin table where any failed fetch shows N/A; a count of stocks above a
    # 20% margin; and a final PASS line confirming the comprehension and the
    # for-loop versions agree.


if __name__ == "__main__":
    main()
