"""Lab 26 — Activity: Max ROE Function — Finding the Best Performer in a Portfolio

Topic 4: Scripting with Function and Lambda
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO3: Construct a function that scans a list of financial records and returns the maximum value by a chosen metric, and compare it against Python's built-in max.

Goal: You fetch Return on Equity for ten SGX companies, then write find_max_roe(data_list) that walks the list of dicts and returns the single best entry — implementing the max algorithm by hand before replacing it with max(data_list, key=lambda x: x['roe']). Handling the empty list (return None, not an IndexError) is the point of the lab: a screener that finds nothing must say so calmly. You then generalise it to find_max_by(data_list, metric) so one function serves ROE, ROA and margin.

You will build: max_roe.py — fetches ROE for 10 SGX tickers and reports the top performer via a hand-written max function, a built-in max version and a generalised find_max_by.
Tools: uv, yfinance, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python activity_max_roe_function_finding_the_be.py
"""


def main():
    print("Lab 26: Activity: Max ROE Function — Finding the Best Performer in a Portfolio")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project and add yfinance.
    #   $ uv init lab-26-max-roe && cd lab-26-max-roe && uv add yfinance
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # In max_roe.py loop over the ten tickers ['D05.SI', 'U11.SI', 'O39.SI',
    # 'Z74.SI', 'J36.SI', 'BN4.SI', 'V03.SI', 'C38U.SI', 'A17U.SI', 'C07.SI'],
    # read stock.info.get('returnOnEquity'), and append {'ticker': ..., 'roe':
    # roe * 100} only when the value is not None.
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Wrap each fetch in try/except so one failing ticker does not abort the
    # scan, and print how many of the ten returned usable ROE data.
    #   $ uv run python max_roe.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Print the full ROE sequence as an aligned table before any ranking, so you
    # can verify the winner by eye.
    #   $ uv run python max_roe.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Write find_max_roe(data_list) by hand: return None immediately if the list
    # is empty, otherwise seed max_entry with data_list[0] and loop comparing
    # entry['roe'] against max_entry['roe'], reassigning on a higher value.
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Call it and print the winner: 'TOP PERFORMER: {ticker} with ROE
    # {roe:.2f}%'.
    #   $ uv run python max_roe.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Test the empty case: call find_max_roe([]) and confirm it returns None
    # rather than raising IndexError. Print a 'no qualifying stocks found'
    # message when it does.
    #   $ uv run python max_roe.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Replace the hand-written loop with the built-in: best = max(data_list,
    # key=lambda x: x['roe']) and confirm it names the same winner. Note that
    # max on an empty list raises ValueError unless you pass default=None.
    #   $ uv run python max_roe.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Generalise find_max_roe into
    # find_max_by(data_list, metric) that takes the metric name as a string so
    # the same function works for roe, roa or margin. Add a matching
    # find_min_by, handle the empty list and the case where the metric key is
    # missing from some records, and explain the trade-off versus just using max
    # with a key lambda." Review the missing-key handling especially.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Add the generalised functions, extend your fetch loop to also collect
    # returnOnAssets, and call find_max_by twice — once for 'roe' and once for
    # 'roa' — printing both winners.
    #   $ uv run python max_roe.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Add a top-three report using sorted(data_list, key=lambda x: x['roe'],
    # reverse=True)[:3] and print it as a ranked podium with enumerate.
    #   $ uv run python max_roe.py
    # TODO: implement this step

    # ---- Step 12 ----------------------------------------------------------
    # Discuss: the highest ROE in the list may be driven by high leverage rather
    # than operating strength. What second metric would you require before
    # acting on this screener's winner?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python max_roe.py`. It must print the count of tickers with
    # usable data, the full ROE table, a single TOP PERFORMER line, and
    # confirmation that the hand-written find_max_roe and the built-in max agree
    # on the same ticker. find_max_roe([]) must return None with a 'no
    # qualifying stocks' message, and find_max_by must report a winner for both
    # 'roe' and 'roa'.


if __name__ == "__main__":
    main()
