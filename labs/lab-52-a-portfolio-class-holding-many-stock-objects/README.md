# Lab 52 — A Portfolio Class Holding Many Stock Objects

**Topic 8: Object Oriented Programming**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO7: Compose objects — a Portfolio class that aggregates many Stock instances and reports book-level metrics.

## Goal

The learner builds a Portfolio class that holds a list of Stock objects (composition). Methods include add_holding(), total_value(), total_pnl(), weights() returning each holding's share of the book, sector_allocation() aggregating by sector, and top_holdings(n). The lab demonstrates why the Portfolio should never duplicate price data — it delegates to each Stock's own methods.

## What you'll build

A portfolio.py module defining Portfolio, importing Stock from lab 51, with a demo book of six holdings.

**Tools:** uv, Python 3.12, pandas, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project and add pandas.

   ```bash
   uv init lab-52-portfolio-class && cd lab-52-portfolio-class && uv add pandas
   ```

2. Copy stock.py from lab 51 so Portfolio can import it.

   ```bash
   cp ../lab-51-stock-class/stock.py .
   ```

3. Prompt your AI assistant: "Write a Python class Portfolio that holds a list of Stock objects. __init__ takes an owner name and an optional list of holdings. Add add_holding(stock), total_value() summing each holding's market_value(), total_cost(), total_pnl(), weights() returning a dict of ticker to percentage of total_value, sector_allocation() returning a dict of sector to total market value, and top_holdings(n=3) returning the n largest holdings by market value. The Portfolio must call the Stock methods rather than recomputing prices itself."
4. Save as portfolio.py and review — confirm total_value() calls h.market_value() and does not re-implement shares * price.
5. Build a six-stock demo book across at least three sectors.
6. Print the book-level totals.

   ```bash
   uv run python -c "from portfolio import build_demo; p=build_demo(); print(p.total_value(), p.total_pnl())"
   ```

7. Check the weights sum to 100%.

   ```bash
   uv run python -c "from portfolio import build_demo; p=build_demo(); print(round(sum(p.weights().values()),6))"
   ```

8. Confirm sector_allocation() totals equal total_value().

   ```bash
   uv run python portfolio.py
   ```

9. Update one Stock's current_price and re-run total_value() — the Portfolio total must change with no Portfolio code touched. This is the payoff of delegation.
10. Discuss: composition (a Portfolio HAS Stocks) versus inheritance (an Equity IS an Instrument) — why is Portfolio the wrong place to use inheritance?

## Test it

weights() sums to 100.0; sum(sector_allocation().values()) equals total_value(); changing one Stock's current_price changes the Portfolio total without editing portfolio.py.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
