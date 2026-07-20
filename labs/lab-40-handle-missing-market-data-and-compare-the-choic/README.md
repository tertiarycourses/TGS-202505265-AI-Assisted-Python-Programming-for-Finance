# Lab 40 — Handle Missing Market Data and Compare the Choices

**Topic 6: Import and Process Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO5: Detect missing market data with isna, and compare dropna, fillna and forward-fill, quantifying how each choice changes the analytical result.

## Goal

The central judgement lab of Topic 6. Market data has gaps: public holidays that differ between SGX and NASDAQ, trading suspensions, and vendor errors. The learner injects and detects gaps, then applies three treatments — dropna, fillna with the mean, and forward-fill — to the SAME series, computes total return and volatility under each, and puts the three answers side by side. The point is that the numbers genuinely differ, so the cleaning choice is an analytical decision that must be documented, not a formatting step.

## What you'll build

A uv project `lab-40-missing-data` with clean_compare.py printing a comparison table of total return, mean daily return and annualised volatility under each of the four treatments, plus a written recommendation.

**Tools:** uv, pandas, numpy, AI coding assistant

## Step-by-step

1. Create the project and add the dependencies.

   ```bash
   uv init lab-40-missing-data && cd lab-40-missing-data && uv add pandas numpy && cp ../lab-37-yfinance-import/market_data.csv .
   ```

2. Reindex a single ticker's Close series onto a full business-day calendar so every non-trading gap becomes an explicit NaN, then count them with .isna().sum().

   ```bash
   uv run python clean_compare.py
   ```

3. Print the specific dates that are missing and identify which are public holidays versus genuine data gaps.

   ```bash
   uv run python clean_compare.py
   ```

4. Treatment A — dropna(): drop the missing rows, then compute total return, mean daily return and annualised volatility.

   ```bash
   uv run python clean_compare.py
   ```

5. Treatment B — fillna(series.mean()): fill every gap with the series mean and recompute the same three metrics.

   ```bash
   uv run python clean_compare.py
   ```

6. Treatment C — ffill(): forward-fill the last traded price across the gap, which is the standard convention for a non-trading day, and recompute.

   ```bash
   uv run python clean_compare.py
   ```

7. Treatment D — interpolate(method='time'): linearly interpolate across the gap and recompute.

   ```bash
   uv run python clean_compare.py
   ```

8. Print all four sets of metrics in one comparison table and identify the largest discrepancy between treatments.

   ```bash
   uv run python clean_compare.py
   ```

9. DISCUSS — the key judgement of this topic: filling with the series mean injects a huge artificial price jump and inflates volatility; dropna understates the number of periods; forward-fill correctly implies zero return on a non-trading day but suppresses volatility if used across a long suspension. Which treatment would you defend to an auditor, and for which kind of gap?
10. AI STEP — prompt your AI assistant: "I have a daily stock Close series with NaNs from public holidays and one three-week trading suspension. Compare dropna, fillna(mean), ffill and time interpolation for computing daily returns and annualised volatility. For each, state the assumption it makes about what happened during the gap and when it biases the volatility estimate up or down."
11. Check the AI's reasoning against your own measured numbers from the comparison table — does its claimed direction of bias match what you actually observed?

   ```bash
   uv run python clean_compare.py
   ```

12. Write your recommendation as a comment block: which treatment for a holiday, which for a suspension, and which you would never use.

## Test it

The comparison table prints four rows of metrics that visibly differ, the missing dates are listed by date, and the file ends with a written, justified recommendation naming a treatment per gap type.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
