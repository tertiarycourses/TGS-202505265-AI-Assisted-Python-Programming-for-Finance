# Lab 12 — Sets and Operators — Common Holdings Across Portfolios

**Topic 2: Data Types and Operators**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO2: Apply the set data type and arithmetic, compound, comparison, membership and logical operators to compare portfolios and encode financial rules.

## Goal

Mirroring the reference notebook activities, the learner uses set intersection, union and difference to find overlapping and unique holdings across two SGX portfolios and to de-duplicate a ticker list, then works through the full operator families — arithmetic, compound assignment, comparison, membership and logical — applied to a portfolio concentration and eligibility rule.

## What you'll build

A script `portfolio_sets.py` that reports common, unique and combined holdings across two portfolios plus an operator-driven eligibility check.

**Tools:** uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

## Step-by-step

1. Create the project.

   ```bash
   uv init lab-12-sets-operators && cd lab-12-sets-operators
   ```

2. Create portfolio_sets.py with two portfolios as sets of SGX tickers.

   ```bash
   set_a = {'D05.SI','U11.SI','O39.SI','Z74.SI','V03.SI'}; set_b = {'Z74.SI','C38U.SI','D05.SI','A17U.SI','S68.SI'}
   ```

3. Find the overlap with intersection — these are the concentrated positions a risk officer cares about.

   ```bash
   print(f'Common: {set_a.intersection(set_b)}')
   ```

4. Find the combined universe with union and the fund-specific holdings with difference.

   ```bash
   print(set_a.union(set_b)); print(set_a.difference(set_b)); print(set_b.difference(set_a))
   ```

5. Add a ticker, then de-duplicate a messy list of tickers by converting it through a set.

   ```bash
   unique = list(set(['D05.SI','U11.SI','D05.SI','O39.SI','U11.SI'])); print(unique)
   ```

6. Work the operators: use compound assignment to accumulate a running portfolio value, and membership to test whether a ticker is held.

   ```bash
   total = 0.0; total += 2000 * 35.90; print('D05.SI' in set_a)
   ```

7. Combine comparison and logical operators into a real eligibility rule: a stock qualifies if ROE is above 10% AND the PE ratio is below 20, OR it is held in both portfolios.

   ```bash
   eligible = (roe > 10 and pe < 20) or (ticker in set_a.intersection(set_b))
   ```

8. Run the script and check each operator's result against your expectation before trusting it.

   ```bash
   uv run python portfolio_sets.py
   ```

9. PROMPT THE AI ASSISTANT with: 'Extend portfolio_sets.py so it prints a reconciliation report between the two portfolios: the count and list of common tickers, tickers only in Fund A, tickers only in Fund B, the total combined universe size, and the overlap percentage computed as the intersection size divided by the union size. Then add a screen that uses comparison, membership and logical operators to classify each ticker in the union as BUY, HOLD or REVIEW from a dictionary of ROE and PE values, treating a missing ROE or PE as REVIEW.' Apply the code.
10. REVIEW the AI output: confirm the overlap percentage uses the union and not the sum of the two sets, that the missing-data branch is checked before the comparison operators run, and that the classifications are mutually exclusive.
11. Run the reconciliation and the screen.

   ```bash
   uv run python portfolio_sets.py
   ```

12. Test the edge cases: two identical portfolios (overlap should be 100%), two disjoint portfolios (0%), and a ticker whose PE is missing.

   ```bash
   uv run python portfolio_sets.py
   ```


## Test it

The reconciliation reports D05.SI and Z74.SI as the common tickers, an overlap of 25% across a combined universe of eight tickers, and every ticker in the union is classified as exactly one of BUY, HOLD or REVIEW with missing data landing in REVIEW.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
