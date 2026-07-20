# Lab 37 — Import Live Market Data with yfinance

**Topic 6: Import and Process Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO5: Download multi-ticker market data with yfinance and reshape the result into an analysis-ready DataFrame.

## Goal

The learner downloads three years of daily data for a small multi-market portfolio with yfinance and immediately meets its awkward output shape: a MultiIndex column frame when several tickers are requested, and a flat frame when only one is. The learner writes a loader that normalises both cases into a tidy long-format DataFrame with Date, Ticker and Close, caches it to CSV so the rest of the course is not dependent on the network, and wraps the download in the try/except pattern learned in Topic 5.

## What you'll build

A uv project `lab-37-yfinance-import` with load_market.py producing a tidy long-format DataFrame and a cached market_data.csv covering three years and at least four tickers.

**Tools:** uv, yfinance, pandas, AI coding assistant

## Step-by-step

1. Create the project and add the data dependencies.

   ```bash
   uv init lab-37-yfinance-import && cd lab-37-yfinance-import && uv add yfinance pandas
   ```

2. Download three years of daily data for a single ticker and inspect the shape of what comes back.

   ```bash
   uv run python -c "import yfinance as yf; d=yf.download('AAPL', period='3y'); print(d.columns); print(d.head())"
   ```

3. Now download four tickers at once — AAPL, MSFT, D05.SI, O39.SI — and print the columns again to see the MultiIndex.

   ```bash
   uv run python load_market.py
   ```

4. Discuss: with one ticker the columns are flat; with several they are a (field, ticker) MultiIndex. Code written against one shape breaks against the other — a very common production bug.
5. In load_market.py write fetch(tickers, period) that always returns a tidy long frame with columns Date, Ticker, Open, High, Low, Close, Volume, using .stack() to flatten the MultiIndex case and adding a Ticker column in the single case.
6. Wrap the download in try/except (Topic 5 pattern) so a failed or empty ticker is reported and skipped rather than aborting the whole fetch.

   ```bash
   uv run python load_market.py
   ```

7. Cache the tidy frame to market_data.csv and add a guard so the script reads the cache when it exists and only hits the network otherwise.

   ```bash
   uv run python load_market.py && wc -l market_data.csv
   ```

8. AI STEP — prompt your AI assistant: "yf.download returns a MultiIndex column DataFrame for multiple tickers and a flat one for a single ticker. Write a function that normalises both into a long-format DataFrame with columns Date, Ticker, Open, High, Low, Close, Volume. Handle auto_adjust and explain what Adj Close means for a dividend-paying stock."
9. Test the AI's normaliser with a one-ticker call AND a four-ticker call and confirm both produce identical column layouts.

   ```bash
   uv run python load_market.py
   ```

10. Discuss the AI's explanation of adjusted close: why backtesting on unadjusted close overstates losses around ex-dividend dates.
11. Print a summary — the date range, the row count per ticker, and the number of trading days captured.

   ```bash
   uv run python load_market.py
   ```


## Test it

market_data.csv exists, covers roughly three years, contains all four tickers in long format with one row per ticker per trading day, and the loader returns the same column layout whether called with one ticker or four.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
