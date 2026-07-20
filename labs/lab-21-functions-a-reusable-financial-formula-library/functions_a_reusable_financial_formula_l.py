"""Lab 21 — Functions — A Reusable Financial Formula Library

Topic 4: Scripting with Function and Lambda
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO3: Construct reusable functions that turn a business requirement into a named, testable unit computing standard financial metrics.

Goal: You build your first reusable module: three named functions covering Compound Annual Growth Rate, simple interest and break-even units. Each gets a docstring stating the formula, because in a regulated environment the formula must be auditable from the code. You then see the difference between a function that returns a value and one that only prints, and why the returning version is the only one you can test.

You will build: finance_formulas.py — a module of documented, reusable financial functions (CAGR, simple interest, break-even units) with a demonstration block.
Tools: uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python functions_a_reusable_financial_formula_l.py
"""


def main():
    print("Lab 21: Functions — A Reusable Financial Formula Library")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project for your formula library.
    #   $ uv init lab-21-finance-formulas && cd lab-21-finance-formulas
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # In finance_formulas.py define calculate_cagr(beginning_value,
    # ending_value, years) returning ((ending_value / beginning_value) ** (1 /
    # years)) - 1, with a one-line docstring naming the metric.
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Define calculate_simple_interest(principal, rate, time) returning
    # principal * (rate / 100) * time — note the rate is passed as a whole
    # number of percent, and say so in the docstring.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Define break_even_units(fixed_costs, price_per_unit,
    # variable_cost_per_unit) returning fixed_costs / (price_per_unit -
    # variable_cost_per_unit).
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Call all three with the worked examples — CAGR from 10000 to 15000 over 5
    # years, simple interest on 5000 at 4.5% for 2 years, break-even on 20000
    # fixed costs at a $50 price and $30 variable cost — and print each result
    # with the right format specifier ({:.2%} for CAGR, ${:.2f} for interest,
    # whole units for break-even).
    #   $ uv run python finance_formulas.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # CONTRAST: write a fourth function that prints the CAGR instead of
    # returning it. Try to use its output in a further calculation and observe
    # that you get None. Write a comment recording why 'return' beats 'print' in
    # a library.
    #   $ uv run python finance_formulas.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Add input validation to these three
    # financial functions. calculate_cagr must reject a zero or negative
    # beginning value and zero years; break_even_units must reject a
    # contribution margin of zero or below because that means the product never
    # breaks even (ZeroDivisionError). Raise ValueError with a message naming
    # the offending argument." Review the exceptions it chose.
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Apply the validated version and test each failure path: CAGR with
    # beginning_value = 0, CAGR with years = 0, and break-even where the
    # variable cost exceeds the price.
    #   $ uv run python finance_formulas.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Add a `if __name__ == '__main__':` guard around the demonstration block so
    # the module can be imported by later labs without running the demo.
    #   $ uv run python finance_formulas.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Prove the guard works by importing the module and calling one function
    # from a one-liner.
    #   $ uv run python -c "from finance_formulas import calculate_cagr; print(f'{calculate_cagr(10000, 15000, 5):.2%}')"
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Discuss: what does the CAGR figure hide about the year-by-year path an
    # investment took, and why does that matter to a client conversation?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python finance_formulas.py`. CAGR must print 8.45%, simple
    # interest $450.00, and break-even 1000 units. The import one-liner must
    # print 8.45% with no demonstration output, proving the __main__ guard
    # works. All three invalid-input tests must raise a ValueError naming the
    # bad argument.


if __name__ == "__main__":
    main()
