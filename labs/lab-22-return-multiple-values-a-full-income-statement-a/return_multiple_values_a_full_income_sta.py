"""Lab 22 — Return Multiple Values — A Full Income Statement Analysis in One Call

Topic 4: Scripting with Function and Lambda
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO3: Construct a function that returns multiple values so a single call delivers a complete set of financial ratios, and unpack them cleanly.

Goal: A single call should be able to hand back a whole analysis. You build analyze_income_statement(revenue, cogs, operating_expenses) which returns gross profit, net income and profit margin as a tuple, then unpack all three in one assignment. You compare tuple return against dictionary return, learn why the tuple's ORDER is a silent trap when a caller unpacks it wrongly, and finish with a named-tuple version that removes the trap.

You will build: income_analysis.py — an income statement analyser returning gross profit, net income and margin, in tuple, dict and namedtuple variants.
Tools: uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python return_multiple_values_a_full_income_sta.py
"""


def main():
    print("Lab 22: Return Multiple Values — A Full Income Statement Analysis in One Call")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project.
    #   $ uv init lab-22-income-analysis && cd lab-22-income-analysis
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # In income_analysis.py define analyze_income_statement(revenue, cogs,
    # operating_expenses). Compute gross_profit = revenue - cogs, net_income =
    # gross_profit - operating_expenses, and profit_margin = (net_income /
    # revenue) * 100 if revenue != 0 else 0.
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Return all three as a tuple: `return gross_profit, net_income,
    # profit_margin`. Note in the docstring that this is a tuple return even
    # though there are no parentheses.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Call it with revenue 500000, COGS 200000 and operating expenses 150000,
    # unpacking with `gp, ni, pm = analyze_income_statement(...)`.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Print a formatted mini income statement: Revenue, Gross Profit and Net
    # Income with thousands separators, and Profit Margin to 2 decimals with a
    # percent sign.
    #   $ uv run python income_analysis.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # SEE THE TRAP: deliberately unpack in the wrong order as `pm, ni, gp = ...`
    # and re-run. Nothing errors, but the report is nonsense. Restore the
    # correct order and comment on the risk.
    #   $ uv run python income_analysis.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Confirm the zero-revenue guard: call the function with revenue = 0 and
    # check the margin comes back as 0 rather than raising ZeroDivisionError.
    #   $ uv run python income_analysis.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Rewrite this function to return a
    # dictionary with keys gross_profit, net_income and profit_margin instead of
    # a positional tuple, and then a third version using collections.namedtuple.
    # Explain which of the three is safest for a financial reporting system
    # where callers are written by different teams." Read the trade-off
    # argument.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Add both AI variants to the file as analyze_income_statement_dict and
    # analyze_income_statement_nt, and call all three on the same inputs to
    # confirm identical numbers.
    #   $ uv run python income_analysis.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Extend the analysis: add operating margin ((gross_profit -
    # operating_expenses) / revenue * 100) and a cost ratio (cogs / revenue *
    # 100) to the dict version, so one call now returns five metrics.
    #   $ uv run python income_analysis.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Run the analyser over three mock companies held in a list of tuples,
    # printing one comparison row per company in an aligned table.
    #   $ uv run python income_analysis.py
    # TODO: implement this step

    # ---- Step 12 ----------------------------------------------------------
    # Discuss: the tuple version is faster to write and the dict version is
    # safer to consume. At what team size does that trade-off flip?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python income_analysis.py`. For revenue 500000 / COGS 200000 /
    # OpEx 150000 it must report Gross Profit $300,000, Net Income $150,000 and
    # Profit Margin 30.00%. The dict and namedtuple versions must return the
    # same three numbers, revenue = 0 must return a margin of 0 without a
    # traceback, and the three-company comparison table must print three aligned
    # rows.


if __name__ == "__main__":
    main()
