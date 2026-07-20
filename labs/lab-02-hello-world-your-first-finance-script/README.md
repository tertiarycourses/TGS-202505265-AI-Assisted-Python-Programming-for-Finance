# Lab 2 — Hello World — Your First Finance Script

**Topic 1: Introduction to Python Programming**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO1: Translate a simple business requirement in financial services into a Python programming objective and execute the resulting script.

## Goal

The learner writes and runs the classic first program, then immediately upgrades it into a finance-relevant script: a trading-desk banner that prints the desk name, the reporting currency, the valuation date and a formatted portfolio value. The lab establishes the prompt-review-test cycle used for every later lab.

## What you'll build

A script `hello_finance.py` that prints a formatted trading-desk banner with a currency-formatted portfolio value.

**Tools:** uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

## Step-by-step

1. Create and enter the project for this lab.

   ```bash
   uv init lab-02-hello-world && cd lab-02-hello-world
   ```

2. Create hello_finance.py containing the single classic line, then run it to prove the toolchain works end to end.

   ```bash
   print('hello world')
   ```

3. Execute the script with uv.

   ```bash
   uv run python hello_finance.py
   ```

4. Now state the business requirement: the SGD equities desk wants every report to open with a banner showing the desk name, base currency, valuation date and total portfolio value in SGD to two decimal places with thousands separators.
5. Add the variables by hand so you understand what the AI will later generate.

   ```bash
   desk = 'SGD Equities Desk'; base_ccy = 'SGD'; portfolio_value = 12487650.75
   ```

6. Print the banner using an f-string with currency formatting.

   ```bash
   print(f'{desk} | {base_ccy} | Portfolio Value: ${portfolio_value:,.2f}')
   ```

7. PROMPT THE AI ASSISTANT with: 'Refactor hello_finance.py so it prints a bordered banner 60 characters wide. The banner must show the desk name, base currency SGD, today's valuation date from datetime, and the portfolio value formatted with a dollar sign, thousands separators and two decimals. Use only the standard library.' Apply the generated code.
8. REVIEW the AI output: confirm it uses datetime.date.today() rather than a hard-coded date, that the currency format is ,.2f and not .2f, and that no third-party import was added.
9. Run the refactored script and check the alignment of the banner.

   ```bash
   uv run python hello_finance.py
   ```

10. Change portfolio_value to 0.0 and to 1234567890.12 and re-run — confirm the formatting holds at both extremes.

   ```bash
   uv run python hello_finance.py
   ```


## Test it

The script prints a bordered banner showing the desk name, SGD, today's date and the portfolio value as $12,487,650.75 — with the comma separators and exactly two decimal places.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
