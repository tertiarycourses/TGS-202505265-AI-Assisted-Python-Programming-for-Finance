# Lab 31 — ZeroDivisionError in an ROE and Ratio Calculator

**Topic 5: Error Handling Using Exception**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO4: Handle ZeroDivisionError and TypeError in financial ratio calculations where the denominator can legitimately be zero.

## Goal

Return on Equity divides net income by shareholders' equity — and a distressed company can report zero or negative equity, which makes the ratio undefined rather than merely large. The learner builds a ratio calculator covering ROE, net profit margin and debt-to-equity, then hardens it against a zero denominator and against a None value arriving from an incomplete fundamentals feed. The lab makes the key point that returning 0.0 for an undefined ratio is a data-quality lie; returning None and flagging it is correct.

## What you'll build

A uv project `lab-31-roe-guard` with ratios.py exposing safe_roe(), safe_margin() and safe_debt_to_equity(), all returning None with a printed warning when the ratio is undefined.

**Tools:** uv, Python 3.12, AI coding assistant

## Step-by-step

1. Create the uv project for the ratio calculator.

   ```bash
   uv init lab-31-roe-guard && cd lab-31-roe-guard
   ```

2. Write ratios.py with an unguarded roe(net_income, equity) that simply returns net_income / equity, plus a COMPANIES list containing one firm with equity = 0 and one with equity = None.

   ```bash
   touch ratios.py
   ```

3. Run the script over the company list and observe it crash on the zero-equity firm.

   ```bash
   uv run python ratios.py
   ```

4. Discuss: ZeroDivisionError is not a bug in your code — it is the data telling you the ratio has no meaning. A company with zero book equity has an undefined ROE.
5. Rewrite roe() as safe_roe() with try/except catching ZeroDivisionError (return None, warn 'undefined: zero equity') and TypeError (return None, warn 'missing equity value').
6. Add safe_margin(net_income, revenue) and safe_debt_to_equity(debt, equity) using the same guarded pattern, and run over all companies.

   ```bash
   uv run python ratios.py
   ```

7. AI STEP — prompt your AI assistant: "I have three financial ratio functions that each repeat the same try/except for ZeroDivisionError and TypeError. Refactor them into one reusable safe_divide(numerator, denominator, label) helper that returns None and logs a warning, and rewrite the three ratios to use it. Keep the warning text specific to each ratio."
8. Test the AI's safe_divide against a negative-equity firm (equity = -500000). Decide as a class whether a negative denominator should return a number or a flag, and justify the choice in a comment.
9. Print a final table of every company with its three ratios, showing 'n/a' where the result is None.

   ```bash
   uv run python ratios.py
   ```

10. Discuss: why silently substituting 0.0 for an undefined ROE would corrupt a downstream screening model that ranks companies by ROE.

## Test it

`uv run python ratios.py` prints a ratio table for every company, shows 'n/a' for the zero-equity and None-equity firms with a warning line for each, and never raises.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
