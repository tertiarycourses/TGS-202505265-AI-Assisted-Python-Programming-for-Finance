"""Lab 55 — Polymorphism — One .value() Call Across a Mixed Instrument Book

Topic 8: Object Oriented Programming
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO7: Apply polymorphism so a single valuation loop handles every instrument type correctly.

Goal: The learner adds a third subclass (a simple CashDeposit or FXForward), then builds a mixed book of Equity, Bond and Cash objects in one list and values the entire book with a single loop calling item.value() — Python dispatches to the correct override at runtime. The lab also adds a duck-typed report_book() function that works on any object exposing .value(), showing polymorphism does not require inheritance, and proves the open/closed principle by adding a fourth instrument type without editing the valuation loop.

You will build: A book.py script valuing a heterogeneous instrument book through one polymorphic loop, plus an asset-class breakdown.
Tools: uv, Python 3.12, pandas, VS Code / Cursor AI assistant

Run this lab with uv:
    uv run python polymorphism_one_value_call_across_a_mix.py
"""


def main():
    print("Lab 55: Polymorphism — One .value() Call Across a Mixed Instrument Book")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project, add pandas and copy the lab 54 hierarchy.
    #   $ uv init lab-55-polymorphism-book && cd lab-55-polymorphism-book && uv add pandas && cp ../lab-54-inheritance-instruments/instruments.py .
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Prompt your AI assistant: "Extend this instruments module with a
    # CashDeposit(Instrument) subclass holding a principal and an annual
    # interest rate, overriding value() as principal plus accrued interest and
    # income() as principal * rate. Then write a function value_book(items) that
    # takes a list of ANY Instrument subclasses and returns a pandas DataFrame
    # with columns Identifier, Asset_Class (the class name), Value and Income,
    # plus the book total — using a single loop that calls item.value() with no
    # isinstance checks and no if/elif on type."
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Save as book.py and audit the loop: if the generated code contains
    # isinstance() or a type check inside value_book(), that is NOT polymorphism
    # — rewrite it.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Build a mixed book of at least two Equities, two Bonds and one CashDeposit
    # in a single Python list.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Run the polymorphic valuation.
    #   $ uv run python book.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Confirm each row's Asset_Class is derived at runtime via
    # type(item).__name__ — the loop never knew the type in advance.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Group the book by Asset_Class to produce the allocation table.
    #   $ uv run python -c "from book import value_book, build_book; df=value_book(build_book()); print(df.groupby('Asset_Class')['Value'].sum().round(2))"
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Prove the open/closed principle: add a fourth subclass (e.g. FXForward)
    # with its own value(), append one to the book, and re-run WITHOUT changing
    # value_book().
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Verify the book total rose by exactly the new instrument's value.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Discuss: how does polymorphism reduce risk in a valuation engine compared
    # with a long if/elif chain on instrument type?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # value_book() contains no isinstance or type comparisons; adding a
    # brand-new Instrument subclass to the list changes the book total with zero
    # edits to value_book(), and the Asset_Class column names it correctly.


if __name__ == "__main__":
    main()
