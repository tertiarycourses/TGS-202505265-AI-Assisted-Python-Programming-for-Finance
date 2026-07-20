"""Lab 27 — Lambda and Map — Gross Profit Margin and ROE Across a Portfolio

Topic 4: Scripting with Function and Lambda
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO3: Construct lambda expressions for one-off financial formulas and apply them across a sequence of stocks with map.

Goal: Lambda gives you a formula without the ceremony of def, and map applies it across a whole portfolio in one expression. You write lambdas for simple interest, currency conversion and percent change, then the topic's activity: a gross profit margin lambda ((Revenue - COGS) / Revenue * 100) with a zero-revenue ternary guard. You then use map with a lambda to compute ROE for a list of SGX companies from hard-coded net income and equity, and compare map against the equivalent list comprehension.

You will build: lambda_map.py — gross profit margin and ROE computed with lambda expressions and applied across a portfolio using map, benchmarked against a list comprehension.
Tools: uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python lambda_and_map_gross_profit_margin_and_r.py
"""


def main():
    print("Lab 27: Lambda and Map — Gross Profit Margin and ROE Across a Portfolio")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project.
    #   $ uv init lab-27-lambda-map && cd lab-27-lambda-map
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # In lambda_map.py write three lambdas: calculate_interest = lambda p, r, t:
    # p * (r / 100) * t; sgd_to_usd = lambda amount: amount * 0.74;
    # percent_change = lambda new, old: ((new - old) / old) * 100. Call each and
    # print the results.
    #   $ uv run python lambda_map.py
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # ACTIVITY — GROSS PROFIT MARGIN: write calculate_gross_margin = lambda
    # revenue, cogs: ((revenue - cogs) / revenue) * 100 if revenue != 0 else 0.
    # Call it with revenue 500000 and COGS 300000 and print revenue, COGS and
    # the margin.
    #   $ uv run python lambda_map.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Confirm the guard by calling calculate_gross_margin(0, 100) and checking
    # it returns 0 rather than raising ZeroDivisionError.
    #   $ uv run python lambda_map.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Introduce map with three quick examples: apply 9% GST to transactions
    # [100.0, 250.50, 45.0, 1200.0] with round(x * 1.09, 2); extract tickers
    # from a list of portfolio dicts; and normalise prices [35.50, 36.20, 34.80,
    # 37.00] against the first price.
    #   $ uv run python lambda_map.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Note that map returns a lazy iterator — print the map object itself before
    # wrapping it in list() so you see the difference, and comment on why the
    # list() call is required.
    #   $ uv run python lambda_map.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # ACTIVITY — ROE VIA MAP: define financial_data as a list of dicts for five
    # SGX companies with net_income and equity in SGD billions (D05.SI
    # 10.3/57.1, U11.SI 5.7/45.2, O39.SI 7.0/54.8, Z74.SI 1.9/26.5, V03.SI
    # 1.1/12.4).
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Write roe_calculator as a lambda returning {'ticker': x['ticker'], 'roe':
    # (x['net_income'] / x['equity']) * 100 if x['equity'] != 0 else 0}, then
    # apply it with roe_results = list(map(roe_calculator, financial_data)).
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Print the results as an aligned table with a header and separator, each
    # ROE to 2 decimals.
    #   $ uv run python lambda_map.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Rewrite this map plus lambda as a
    # list comprehension and as a named def function, then tell me which of the
    # three you would use in a financial codebase that other analysts must
    # maintain, and explain when a lambda is genuinely the better choice." Weigh
    # the answer against your own reading of the code.
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Add all three versions to the file, run them on the same data, and print a
    # PASS line confirming they produce identical output.
    #   $ uv run python lambda_map.py
    # TODO: implement this step

    # ---- Step 12 ----------------------------------------------------------
    # Apply the gross margin lambda across a portfolio with map: given a list of
    # (revenue, cogs) tuples for four companies, use map with a lambda taking
    # the tuple and print each company's gross margin.
    #   $ uv run python lambda_map.py
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python lambda_map.py`. Simple interest must be $100.00, $100
    # SGD must convert to $74.00, percent change must be 20.00%, and the gross
    # profit margin on 500000/300000 must be 40.00%. The map-based ROE table
    # must show five tickers with D05.SI at approximately 18.04% and V03.SI at
    # approximately 8.87%, and the final PASS line must confirm the map,
    # comprehension and def versions agree.


if __name__ == "__main__":
    main()
