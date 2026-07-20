# Lab 25 — Variable Arguments — *args and **kwargs for Portfolios of Any Size

**Topic 4: Scripting with Function and Lambda**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO3: Construct functions accepting a variable number of arguments so one function handles a portfolio of any size or a metric set of any shape.

## Goal

A portfolio does not have a fixed number of holdings, so a fixed-arity function is the wrong shape. You rebuild calculate_portfolio_total with *stock_values so it sums three holdings or fifty, add a category-plus-amounts expense reporter, then move to **kwargs to accept an arbitrary named metric set. You finish with unpacking — passing an existing list into an *args function with the star operator, and a dict into a **kwargs function with double-star.

## What you'll build

variable_args.py — variable-argument portfolio, expense and metric functions using *args and **kwargs, plus argument unpacking from existing collections.

**Tools:** uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

## Step-by-step

1. Create the uv project.

   ```bash
   uv init lab-25-variable-args && cd lab-25-variable-args
   ```

2. In variable_args.py redefine calculate_portfolio_total(*stock_values) returning sum(stock_values). Call it with three values (1500.50, 2300.75, 850.00) and then five values (500, 1200, 450, 3000, 150) — same function, both work.

   ```bash
   uv run python variable_args.py
   ```

3. Print len(stock_values) inside the function to prove *args arrives as a tuple, and confirm the type with a print of type(stock_values).

   ```bash
   uv run python variable_args.py
   ```

4. Handle the empty case: call calculate_portfolio_total() with no arguments. sum(()) returns 0 — decide whether that is the right answer for an empty portfolio and note your reasoning in a comment.

   ```bash
   uv run python variable_args.py
   ```

5. Define list_expenses(category, *amounts) which prints the category name, the number of items, and the total formatted to 2 decimals. Call it for 'Trading Fees' with four amounts and for 'Custody' with one.

   ```bash
   uv run python variable_args.py
   ```

6. UNPACKING: given an existing list holdings = [1500.50, 2300.75, 850.00, 1200.00], call calculate_portfolio_total(*holdings) with the star operator. Then call it without the star and observe you get a TypeError or a single-tuple result.

   ```bash
   uv run python variable_args.py
   ```

7. Move to **kwargs: define report_metrics(ticker, **metrics) that prints the ticker then one aligned line per keyword metric. Call it as report_metrics('D05.SI', roe=15.8, roa=1.2, npm=42.5, pe=11.4).

   ```bash
   uv run python variable_args.py
   ```

8. Unpack a dict into it: build metrics_dict = {'roe': 12.1, 'roa': 0.9, 'pe': 9.8} and call report_metrics('O39.SI', **metrics_dict).

   ```bash
   uv run python variable_args.py
   ```

9. AI-ASSIST: prompt your AI tool with: "Write a function build_trade_order(ticker, quantity, *, order_type='LIMIT', **extras) that accepts required positional arguments, a keyword-only default, and arbitrary extra parameters. Show me the exact order the four argument categories must appear in a Python signature and what error I get if I put them in the wrong order." Test the wrong order yourself to see the SyntaxError.
10. Add the generated build_trade_order to your file, call it with and without extras, and print the resulting order dict.

   ```bash
   uv run python variable_args.py
   ```

11. Combine everything: write summarise_portfolio(name, *values, currency='SGD', **tags) printing the portfolio name, holding count, total in the given currency, and any tags supplied.

   ```bash
   uv run python variable_args.py
   ```

12. Discuss: *args and **kwargs make a function flexible but also make its contract invisible to a caller reading the signature. Where would you refuse to use them in a trading system?

## Test it

Run `uv run python variable_args.py`. The three-stock total must be $4,651.25 and the five-stock total $5,300.00 from the same function. The unpacked call with *holdings must total $5,851.25. report_metrics must print four aligned metric lines for D05.SI and three for O39.SI, and summarise_portfolio must print the name, count, currency-formatted total and every tag supplied.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
