"""Lab 53 — Dunder Methods — __str__, __repr__, __len__ and __add__ to Combine Portfolios

Topic 8: Object Oriented Programming
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO7: Apply method overloading through dunder methods so financial objects print, size and merge naturally.

Goal: The learner adds Python's special (dunder) methods to Stock and Portfolio: __str__ for a human-readable holding line, __repr__ for the debugger-friendly form, __len__ so len(portfolio) returns the number of holdings, __getitem__ so a portfolio can be indexed and iterated, __eq__ to compare by ticker, and __add__ so two portfolios can be merged with the + operator — combining shares where the same ticker appears in both. This is operator overloading applied to a real fund-merger scenario.

You will build: Enhanced stock.py and portfolio.py with six dunder methods, supporting print(), len(), iteration and portfolio_a + portfolio_b.
Tools: uv, Python 3.12, VS Code / Cursor AI assistant

Run this lab with uv:
    uv run python dunder_methods_str_repr_len_and_add_to_c.py
"""


def main():
    print("Lab 53: Dunder Methods — __str__, __repr__, __len__ and __add__ to Combine Portfolios")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and copy the lab 52 modules.
    #   $ uv init lab-53-dunder-methods && cd lab-53-dunder-methods && cp ../lab-52-portfolio-class/*.py .
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Observe the default behaviour first: print a Stock object and note the
    # unhelpful <stock.Stock object at 0x...> output.
    #   $ uv run python -c "from stock import Stock; print(Stock('D05','DBS','Banking',500,32.10,38.40))"
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Prompt your AI assistant: "Add dunder methods to these Stock and Portfolio
    # classes. Stock gets __str__ returning 'D05 | DBS Group | 500 sh @ SGD
    # 38.40 | MV 19,200.00 | P&L +3,150.00', __repr__ returning
    # Stock(ticker='D05', shares=500), and __eq__ comparing by ticker. Portfolio
    # gets __len__ returning the number of holdings, __getitem__ so it can be
    # indexed and iterated, __str__ returning a multi-line table of holdings
    # with the total, and __add__ that merges two Portfolios into a new one,
    # summing shares and recomputing a weighted average buy_price when the same
    # ticker appears in both."
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Apply the generated dunder methods and read the __add__ implementation
    # carefully — confirm it returns a NEW Portfolio and does not mutate either
    # operand.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Test __str__ and __repr__.
    #   $ uv run python -c "from stock import Stock; s=Stock('D05','DBS Group','Banking',500,32.10,38.40); print(str(s)); print(repr(s))"
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Test __len__ and iteration.
    #   $ uv run python -c "from portfolio import build_demo; p=build_demo(); print(len(p)); [print(h.ticker) for h in p]"
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Build two portfolios that share at least one ticker and merge them with
    # the + operator.
    #   $ uv run python merge_demo.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Verify the merge conserves value: (a + b).total_value() must equal
    # a.total_value() + b.total_value().
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Verify neither operand was mutated — len(a) and len(b) are unchanged after
    # the merge.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Discuss: when is operator overloading good design, and when does a + on a
    # domain object become misleading to the next developer?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # print(stock) shows the formatted line; len(portfolio) returns the holding
    # count; (a + b).total_value() equals a.total_value() + b.total_value() and
    # both a and b are unchanged.


if __name__ == "__main__":
    main()
