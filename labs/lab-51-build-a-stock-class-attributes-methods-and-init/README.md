# Lab 51 — Build a Stock Class — Attributes, Methods and __init__

**Topic 8: Object Oriented Programming**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO7: Model a financial instrument as a class with attributes and behaviour, initialised through __init__.

## Goal

The learner writes the first finance class: Stock. Instance attributes (ticker, name, sector, shares, buy_price, current_price) are set in the __init__ initializer, and methods add behaviour — market_value(), cost_basis(), unrealised_pnl() and pnl_percent(). The lab contrasts a class attribute (a shared CURRENCY = 'SGD') with instance attributes, and shows why every holding needs its own state.

## What you'll build

A stock.py module defining the Stock class with four financial methods, plus a demo creating three holdings.

**Tools:** uv, Python 3.12, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project.

   ```bash
   uv init lab-51-stock-class && cd lab-51-stock-class
   ```

2. Write a minimal class by hand first — class Stock with a class attribute CURRENCY = 'SGD' and a method describe() — to see the blueprint-versus-instance distinction before adding __init__.
3. Prompt your AI assistant: "Write a Python class Stock for a portfolio holding. The __init__ initializer takes ticker, name, sector, shares, buy_price and current_price and stores them as instance attributes, with a class attribute CURRENCY = 'SGD'. Add methods market_value() returning shares * current_price, cost_basis() returning shares * buy_price, unrealised_pnl() returning market_value minus cost_basis, and pnl_percent() returning the P&L as a percentage of cost basis guarding against a zero cost basis. Add a describe() method printing a formatted one-line summary with the currency."
4. Save the answer as stock.py. Read it and confirm every method takes self as its first parameter and reads attributes via self.
5. Create three objects — instances of the same class with different state.

   ```bash
   uv run python -c "from stock import Stock; s=Stock('D05','DBS Group','Banking',500,32.10,38.40); print(s.market_value(), s.unrealised_pnl(), round(s.pnl_percent(),2))"
   ```

6. Prove instance independence: create two Stock objects, change current_price on one, and confirm the other is unaffected.
7. Prove the class attribute is shared: print Stock.CURRENCY and s.CURRENCY and confirm they are the same object.
8. Test the zero-cost-basis guard by creating a Stock with buy_price=0 and calling pnl_percent().

   ```bash
   uv run python -c "from stock import Stock; s=Stock('X','Test','Tech',10,0,5); print(s.pnl_percent())"
   ```

9. Write a demo block under if __name__ == '__main__': that builds three holdings and prints each describe() line.

   ```bash
   uv run python stock.py
   ```

10. Discuss: what did wrapping price and shares in a class buy us over keeping parallel lists of tickers and prices?

## Test it

Three Stock objects report independent market values; pnl_percent() returns 0.0 (not a ZeroDivisionError) when buy_price is 0; Stock.CURRENCY is visible from every instance.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
