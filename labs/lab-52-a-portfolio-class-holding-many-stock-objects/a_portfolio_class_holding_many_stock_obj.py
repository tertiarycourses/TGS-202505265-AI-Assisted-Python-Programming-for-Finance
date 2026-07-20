"""Lab 52 — A Portfolio Class Holding Many Stock Objects

Topic 8: Object Oriented Programming
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO7: Compose objects — a Portfolio class that aggregates many Stock instances and reports book-level metrics.

Goal: The learner builds a Portfolio class that holds a list of Stock objects (composition). Methods include add_holding(), total_value(), total_pnl(), weights() returning each holding's share of the book, sector_allocation() aggregating by sector, and top_holdings(n). The lab demonstrates why the Portfolio should never duplicate price data — it delegates to each Stock's own methods.

You will build: A portfolio.py module defining Portfolio, importing Stock from lab 51, with a demo book of six holdings.
Tools: uv, Python 3.12, pandas, VS Code / Cursor AI assistant

Run this lab with uv:
    uv run python a_portfolio_class_holding_many_stock_obj.py
"""


def main():
    print("Lab 52: A Portfolio Class Holding Many Stock Objects")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add pandas.
    #   $ uv init lab-52-portfolio-class && cd lab-52-portfolio-class && uv add pandas
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Copy stock.py from lab 51 so Portfolio can import it.
    #   $ cp ../lab-51-stock-class/stock.py .
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Prompt your AI assistant: "Write a Python class Portfolio that holds a
    # list of Stock objects. __init__ takes an owner name and an optional list
    # of holdings. Add add_holding(stock), total_value() summing each holding's
    # market_value(), total_cost(), total_pnl(), weights() returning a dict of
    # ticker to percentage of total_value, sector_allocation() returning a dict
    # of sector to total market value, and top_holdings(n=3) returning the n
    # largest holdings by market value. The Portfolio must call the Stock
    # methods rather than recomputing prices itself."
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Save as portfolio.py and review — confirm total_value() calls
    # h.market_value() and does not re-implement shares * price.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Build a six-stock demo book across at least three sectors.
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Print the book-level totals.
    #   $ uv run python -c "from portfolio import build_demo; p=build_demo(); print(p.total_value(), p.total_pnl())"
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Check the weights sum to 100%.
    #   $ uv run python -c "from portfolio import build_demo; p=build_demo(); print(round(sum(p.weights().values()),6))"
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Confirm sector_allocation() totals equal total_value().
    #   $ uv run python portfolio.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Update one Stock's current_price and re-run total_value() — the Portfolio
    # total must change with no Portfolio code touched. This is the payoff of
    # delegation.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Discuss: composition (a Portfolio HAS Stocks) versus inheritance (an
    # Equity IS an Instrument) — why is Portfolio the wrong place to use
    # inheritance?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # weights() sums to 100.0; sum(sector_allocation().values()) equals
    # total_value(); changing one Stock's current_price changes the Portfolio
    # total without editing portfolio.py.


if __name__ == "__main__":
    main()
