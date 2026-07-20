# Lab 39 — Filter and Slice by Date, Sector and Ticker

**Topic 6: Import and Process Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO5: Select subsets of financial data with boolean masks, date-range slicing and multi-condition filters.

## Goal

The learner attaches a sector mapping to the price data and then answers a series of real screening questions with boolean masks: all bank stocks in Q1, every day AAPL closed above its own 200-day average, the intersection of a date window and a ticker list. The lab covers the operator-precedence trap unique to pandas — `&` and `|` with parentheses, never `and`/`or` — plus .isin(), .between(), .query() and .loc date slicing on a DatetimeIndex.

## What you'll build

A uv project `lab-39-filter-slice` with screen.py answering five stated screening questions, each as a documented boolean mask.

**Tools:** uv, pandas, AI coding assistant

## Step-by-step

1. Create the project, add pandas and copy in the market data.

   ```bash
   uv init lab-39-filter-slice && cd lab-39-filter-slice && uv add pandas && cp ../lab-37-yfinance-import/market_data.csv .
   ```

2. Add a SECTORS dict mapping each ticker to a sector — AAPL and MSFT to Technology, D05.SI and O39.SI to Financials — and map it into a new Sector column.

   ```bash
   touch screen.py
   ```

3. Question 1: slice the last full calendar year using .loc with a date range on the DatetimeIndex, and print the row count.

   ```bash
   uv run python screen.py
   ```

4. Question 2: select only the Financials rows with a boolean mask df['Sector'] == 'Financials', and print the tickers it contains to verify.

   ```bash
   uv run python screen.py
   ```

5. Question 3: combine two conditions — Financials AND Close above 30 — using & with parentheses around each condition. Then deliberately try it with `and` and read the resulting ValueError.

   ```bash
   uv run python screen.py
   ```

6. Discuss: pandas cannot evaluate the truth of a whole Series, which is why `and` fails and `&` is required. Forgetting the parentheses gives a wrong answer silently because of operator precedence.
7. Question 4: use .isin(['AAPL', 'D05.SI']) to select a ticker subset, and .between() on Close to select a price band, and combine both.

   ```bash
   uv run python screen.py
   ```

8. Question 5: rewrite the most complex mask using .query() and compare readability with the bracket form; time both on the full dataset.

   ```bash
   uv run python screen.py
   ```

9. AI STEP — prompt your AI assistant: "Using a pandas DataFrame with columns Date (DatetimeIndex), Ticker, Sector, Close and Volume, write filters for: all Financials rows in 2024 where Close rose more than 2 percent from the prior day, and the 10 highest-volume days for any Technology stock. Use boolean masks with correct parentheses and explain why `and` would fail."
10. Run the AI's filters and verify the row counts by cross-checking a couple of rows manually — an incorrect mask usually returns a plausible but wrong number of rows.

   ```bash
   uv run python screen.py
   ```

11. Save each screened subset to its own CSV for use in the next lab.

   ```bash
   uv run python screen.py && ls *.csv
   ```


## Test it

All five screening questions print a result with its row count, the `and` version raises the expected ValueError with an explanatory printed note, and the .query() result is identical to the bracket-mask result.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
