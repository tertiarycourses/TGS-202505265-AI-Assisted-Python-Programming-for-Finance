# Lab 23 — Activity: Net Profit Margin Function with Zero-Revenue Handling

**Topic 4: Scripting with Function and Lambda**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO3: Construct a single-responsibility function computing net profit margin, and defend it against the zero and missing data cases found in real filings.

## Goal

This is the topic's core activity, built to production standard. calculate_net_profit_margin(net_income, revenue) returns (net_income / revenue) * 100, guarded so a revenue of zero returns 0 rather than raising ZeroDivisionError. You then apply it to live SGX filings, handle the negative-margin case (a loss-making company is not a bug), and write a small set of assertions that prove the function behaves — your first taste of testing.

## What you'll build

net_profit_margin.py — a validated net profit margin function with assertion-based tests, applied to live SGX financial statements.

**Tools:** uv, yfinance, pandas, Google Colab / Cursor, Gemini or Copilot

## Step-by-step

1. Create the uv project and add market-data dependencies.

   ```bash
   uv init lab-23-net-profit-margin && cd lab-23-net-profit-margin && uv add yfinance pandas
   ```

2. In net_profit_margin.py define calculate_net_profit_margin(net_income, revenue) with a docstring stating the formula (Net Income / Total Revenue) * 100. Return 0 if revenue is 0, otherwise the computed margin.
3. Test it with the sample figures from the reference: net income 1,000,000 on revenue 5,000,000. Print the result to 2 decimals with a percent sign.

   ```bash
   uv run python net_profit_margin.py
   ```

4. Test the loss case: net income of -250,000 on revenue 5,000,000 should return -5.00%. Confirm the function does NOT suppress the negative — a loss must stay visible.

   ```bash
   uv run python net_profit_margin.py
   ```

5. Test the guard: call it with revenue = 0 and confirm it returns 0 with no traceback. Add a comment on why returning 0 here is a design choice a reviewer might challenge.

   ```bash
   uv run python net_profit_margin.py
   ```

6. Wire it to live data: fetch D05.SI with yfinance, read Net Income and Total Revenue from stock.financials with .loc[...].iloc[0], and pass both into your function.

   ```bash
   uv run python net_profit_margin.py
   ```

7. Loop the live version over five SGX tickers ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'V03.SI'], printing a formatted margin table with a header row and a separator.

   ```bash
   uv run python net_profit_margin.py
   ```

8. AI-ASSIST: prompt your AI tool with: "Write five assert statements that test this net profit margin function: the normal case, a zero-revenue case, a negative net income case, a 100% margin case, and a case where revenue is negative. Then tell me whether returning 0 for zero revenue is better than raising an exception in a financial reporting context, and argue both sides." Review the tests and the argument.
9. Add the generated assertions to the bottom of the file under a run_tests() function and execute them — all five must pass silently.

   ```bash
   uv run python net_profit_margin.py
   ```

10. Add a classification wrapper on top: a margin above 20% is 'EXCELLENT', 10 to 20% is 'HEALTHY', 0 to 10% is 'THIN', below 0 is 'LOSS-MAKING'. Apply it to each row of the live table.

   ```bash
   uv run python net_profit_margin.py
   ```

11. Discuss: net profit margin is not comparable across sectors — a bank and a supermarket sit on completely different bases. What would you add to the output to stop a reader making that mistake?

## Test it

Run `uv run python net_profit_margin.py`. The sample case must report 20.00%, the loss case -5.00%, and the zero-revenue case 0 with no traceback. All five assertions must pass without output. The live table must show five SGX tickers each with a margin and one of the four classification labels.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
