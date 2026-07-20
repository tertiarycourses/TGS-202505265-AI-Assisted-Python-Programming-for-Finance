# Lab 24 — Multiple, Default and Named Arguments — A Flexible Valuation Toolkit

**Topic 4: Scripting with Function and Lambda**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO3: Construct functions using multiple, default and named arguments so one function serves several business cases without duplication.

## Goal

You learn the three argument styles that stop a codebase filling up with near-duplicate functions. Multiple arguments give a fixed three-stock portfolio total; default arguments let calculate_net_salary assume a 15% tax rate while still accepting a custom one; named arguments make calculate_dividend_yield(stock_price=120.00, dividend_per_share=3.60) unambiguous regardless of order. You also meet the mutable-default-argument trap, one of Python's most notorious bugs.

## What you'll build

valuation_toolkit.py — portfolio total, net salary, investment projection, dividend yield and ROI functions demonstrating multiple, default and named arguments.

**Tools:** uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

## Step-by-step

1. Create the uv project.

   ```bash
   uv init lab-24-valuation-toolkit && cd lab-24-valuation-toolkit
   ```

2. MULTIPLE ARGUMENTS: define calculate_portfolio_total(stock1, stock2, stock3) returning their sum, and call it with 1500.50, 2300.75 and 850.00. Then call it with only two values and read the TypeError carefully.

   ```bash
   uv run python valuation_toolkit.py
   ```

3. DEFAULT ARGUMENTS: define calculate_net_salary(gross_salary, tax_rate=0.15) returning gross_salary minus the tax. Call it once on 5000 using the default and once with tax_rate=0.20, printing both.

   ```bash
   uv run python valuation_toolkit.py
   ```

4. Add estimate_investment_value(principal, years, annual_return=0.07) returning principal * (1 + annual_return) ** years. Call it as (1000, 5) with the default and as (1000, 5, 0.10) with a custom return.

   ```bash
   uv run python valuation_toolkit.py
   ```

5. NAMED ARGUMENTS: define calculate_dividend_yield(dividend_per_share, stock_price) returning (dps / price) * 100. Call it twice with the arguments in DIFFERENT orders using keywords, and confirm both give the right answer.

   ```bash
   uv run python valuation_toolkit.py
   ```

6. Now call the same function positionally with the arguments swapped — (50.00, 2.50) — and observe it returns a nonsense 2000% yield with no error. Write a comment: named arguments are a correctness control, not a style preference.

   ```bash
   uv run python valuation_toolkit.py
   ```

7. Add calculate_roi(initial_investment, final_value) returning ((final - initial) / initial) * 100 and call it with named arguments for clarity.

   ```bash
   uv run python valuation_toolkit.py
   ```

8. AI-ASSIST: prompt your AI tool with: "Show me the mutable default argument trap using a function like add_holding(ticker, portfolio=[]) that appends to a portfolio list. Demonstrate the bug by calling it three times, explain exactly why the list persists between calls, and give me the correct fix using portfolio=None." Run the buggy version first so you SEE the bug.
9. Add both the buggy and the fixed add_holding to your file, call each three times, and print the resulting portfolios side by side so the difference is undeniable.

   ```bash
   uv run python valuation_toolkit.py
   ```

10. Combine the styles: extend calculate_net_salary with a second default argument cpf_rate=0.20 and call it with only the keyword you want to override, leaving the other at its default.

   ```bash
   uv run python valuation_toolkit.py
   ```

11. Enforce clarity: place a bare `*` in a signature (def calculate_dividend_yield(*, dividend_per_share, stock_price)) to make both arguments keyword-only, then confirm the positional call now raises a TypeError instead of silently returning 2000%.

   ```bash
   uv run python valuation_toolkit.py
   ```

12. Discuss: a default value baked into a function is a policy decision. Who owns the 15% tax rate default, and what happens when the policy changes?

## Test it

Run `uv run python valuation_toolkit.py`. Portfolio total must be $4,651.25; net salary $4,250.00 at the default rate and $4,000.00 at 20%; investment value $1,402.55 at the default 7%; both dividend yield calls 5.00% and 3.00%. The buggy add_holding must show a growing shared list while the fixed one shows a fresh list each call, and the keyword-only version must raise TypeError on a positional call.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
