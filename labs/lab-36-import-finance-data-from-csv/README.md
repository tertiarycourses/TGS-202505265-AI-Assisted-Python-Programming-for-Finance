# Lab 36 — Import Finance Data from CSV

**Topic 6: Import and Process Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO5: Import a financial CSV into pandas with correct date parsing, index and dtypes.

## Goal

The learner imports a historical prices CSV and confronts the three defects that make most real finance CSVs unusable on the first read: dates loaded as strings, numbers loaded as objects because of thousands separators or currency symbols, and an unnamed index column. The learner fixes each with read_csv parameters — parse_dates, index_col, thousands, dtype and na_values — rather than by post-processing, and confirms the fix with .dtypes.

## What you'll build

A uv project `lab-36-csv-import` containing prices.csv, load_csv.py with a correctly parameterised read_csv call, and a printed dtype report proving Close is float64 and the index is a DatetimeIndex.

**Tools:** uv, pandas, AI coding assistant

## Step-by-step

1. Create the project and add pandas.

   ```bash
   uv init lab-36-csv-import && cd lab-36-csv-import && uv add pandas
   ```

2. Create prices.csv with columns Date, Ticker, Open, Close, Volume — deliberately writing volumes with thousands commas like '1,204,300', a few cells as 'N/A', and dates in DD/MM/YYYY form.

   ```bash
   touch prices.csv
   ```

3. Load it with a naive pd.read_csv('prices.csv') and print df.dtypes and df.head().

   ```bash
   uv run python load_csv.py
   ```

4. Discuss: Date came in as object, Volume came in as object because of the commas, and 'N/A' was not recognised as missing. Every downstream calculation on these columns would either fail or be silently wrong.
5. Re-import with parse_dates=['Date'], dayfirst=True, index_col='Date', thousands=',' and na_values=['N/A', '', '-'], then reprint df.dtypes.

   ```bash
   uv run python load_csv.py
   ```

6. Verify the index with df.index.dtype and confirm df.index.is_monotonic_increasing; sort the index if it is not.

   ```bash
   uv run python load_csv.py
   ```

7. AI STEP — prompt your AI assistant: "Here are the first five rows of my stock price CSV <paste rows>. Write the single pd.read_csv call that parses the DD/MM/YYYY dates into a DatetimeIndex, strips thousands separators from Volume, treats 'N/A' and '-' as missing, and forces Close to float64. Explain each parameter you used."
8. Compare the AI's read_csv call with your own. Check specifically that it set dayfirst correctly — a wrong dayfirst silently swaps day and month for the first twelve days of each month and is nearly invisible.
9. Prove the parse is right by printing the rows for a date after the 12th of a month and checking it against the raw CSV text.

   ```bash
   uv run python load_csv.py
   ```

10. Save the cleaned frame back out and confirm the round trip is stable.

   ```bash
   uv run python load_csv.py && head -3 prices_clean.csv
   ```


## Test it

df.dtypes shows Close and Open as float64, Volume as int64 or float64, and df.index is a DatetimeIndex sorted ascending. The 'N/A' cells appear as NaN, and a spot-checked date after the 12th matches the raw CSV.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
