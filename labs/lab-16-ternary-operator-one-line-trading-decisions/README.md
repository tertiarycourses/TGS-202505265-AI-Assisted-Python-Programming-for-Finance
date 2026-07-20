# Lab 16 — Ternary Operator — One-Line Trading Decisions

**Topic 3: Problem Solving with Control Structures**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO2: Apply the ternary conditional expression to write compact, readable one-line financial decision rules.

## Goal

The ternary operator collapses a four-line if-else into one expression: value_if_true if condition else value_if_false. You use it for a price-versus-target buy/wait decision, a margin-call check, a dividend-yield flag and a safe division that returns 0 instead of raising ZeroDivisionError. You then meet its limit — a nested ternary that is technically correct but unreadable — and learn when to go back to if-elif.

## What you'll build

ternary_decisions.py — a set of one-line ternary rules covering buy/wait, margin call, yield flagging and zero-safe division.

**Tools:** uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

## Step-by-step

1. Create the uv project.

   ```bash
   uv init lab-16-ternary-decisions && cd lab-16-ternary-decisions
   ```

2. Create ternary_decisions.py. Set current_price = 145.50 and target_price = 150.00, then write decision = 'Buy' if current_price < target_price else 'Wait'.
3. Print the current price, target price and decision, all formatted to 2 decimals.

   ```bash
   uv run python ternary_decisions.py
   ```

4. Write the same rule the long way as a four-line if-else, print both results, and confirm they agree. Keep both in the file as a side-by-side comparison.

   ```bash
   uv run python ternary_decisions.py
   ```

5. Add a margin-call ternary: given account_equity = 18000 and maintenance_margin = 20000, set status = 'MARGIN CALL' if account_equity < maintenance_margin else 'OK'.
6. Add a zero-safe ternary — the pattern you will reuse all course: margin = (net_income / revenue) * 100 if revenue != 0 else 0. Test it with revenue = 0 and confirm no ZeroDivisionError.

   ```bash
   uv run python ternary_decisions.py
   ```

7. Use a ternary inside an f-string to flag high-yield stocks: for a dividend yield of 5.8%, print a line ending in 'HIGH YIELD' if the yield exceeds 4 else 'STANDARD'.

   ```bash
   uv run python ternary_decisions.py
   ```

8. AI-ASSIST: prompt your AI tool with: "Convert this PE-ratio if-elif-else ladder with three branches (Undervalued / Fairly Valued / Overvalued) into a nested ternary expression, then tell me honestly whether the nested version is more readable and when I should NOT use a ternary." Read the answer critically.
9. Paste the nested ternary in, run it against PE values of 12, 20 and 30, and confirm it matches Lab 13's output. Then write a one-line comment recording your own judgement on readability.

   ```bash
   uv run python ternary_decisions.py
   ```

10. Apply the ternary across a small portfolio: loop over the list [('D05.SI', 35.50), ('U11.SI', 28.40), ('O39.SI', 13.10)] with a target of 30.00 and print a Buy/Wait decision per ticker in an aligned table.

   ```bash
   uv run python ternary_decisions.py
   ```

11. Discuss: a ternary always evaluates to a value, so it can sit inside a list comprehension or a function argument — where an if statement cannot. Name one place in your own code where that matters.

## Test it

Run `uv run python ternary_decisions.py`. The buy/wait decision must be 'Buy' (145.50 < 150.00), the margin status must be 'MARGIN CALL', the zero-revenue margin must print 0 with no traceback, and the portfolio table must show one Buy/Wait decision per ticker.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
