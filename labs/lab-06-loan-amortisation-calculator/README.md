# Lab 6 — Loan Amortisation Calculator

**Topic 2: Data Types and Operators**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO2: Apply numeric data types and arithmetic operators to solve a financial calculation problem — the monthly instalment on an amortising loan.

## Goal

Mirroring the reference notebook activity, the learner implements the standard amortisation formula P·[r(1+r)^n]/[(1+r)^n−1] for a Singapore housing loan, then extends it with total interest paid, the zero-interest edge case, and input validation so the tool is safe to hand to a relationship manager.

## What you'll build

A script `loan_calculator.py` that returns the monthly instalment, total repayment and total interest for a given principal, annual rate and tenor.

**Tools:** uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

## Step-by-step

1. Create the project.

   ```bash
   uv init lab-06-loan-calculator && cd lab-06-loan-calculator
   ```

2. Create loan_calculator.py and collect the three inputs a mortgage quote needs.

   ```bash
   principal = float(input('Enter loan amount: ')); annual_rate = float(input('Enter annual interest rate (e.g., 5 for 5%): ')); years = int(input('Enter loan term in years: '))
   ```

3. Convert the annual rate to a monthly rate and the tenor to a number of payments — the two conversions candidates most often get wrong.

   ```bash
   monthly_rate = annual_rate / 100 / 12; n = years * 12
   ```

4. Implement the amortisation formula using the exponent operator.

   ```bash
   monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)
   ```

5. Derive the total repayment and the total interest, then print all three formatted as SGD.

   ```bash
   total_payment = monthly_payment * n; print(f'Monthly: ${monthly_payment:,.2f} | Total: ${total_payment:,.2f} | Interest: ${total_payment - principal:,.2f}')
   ```

6. Run it for a typical Singapore HDB loan: principal 500000, rate 2.6, term 25 years.

   ```bash
   uv run python loan_calculator.py
   ```

7. Try a rate of 0 and observe the ZeroDivisionError — a real defect, because interest-free staff loans exist.

   ```bash
   uv run python loan_calculator.py
   ```

8. PROMPT THE AI ASSISTANT with: 'Refactor loan_calculator.py into a function monthly_instalment(principal, annual_rate_pct, years) that returns monthly payment, total repayment and total interest. Handle a zero interest rate by dividing the principal evenly across the months instead of using the amortisation formula. Reject a principal of zero or less, a negative rate and a term under one year with a clear message. Format all output as SGD with thousands separators.' Apply the code.
9. REVIEW the AI output: confirm the zero-rate branch is chosen before the formula runs, that the rate is still divided by both 100 and 12, and that the three returned values are consistent.
10. Re-run the zero-rate case and a private-property case: 1200000 at 3.5% over 30 years.

   ```bash
   uv run python loan_calculator.py
   ```

11. Compare your 500000 / 2.6% / 25-year answer with a bank's published mortgage calculator and record any difference in your lab notes.

## Test it

A loan of $500,000 at 2.6% over 25 years gives a monthly instalment of approximately $2,268.51 and total interest near $180,554. A rate of 0% returns principal/months with no ZeroDivisionError.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
