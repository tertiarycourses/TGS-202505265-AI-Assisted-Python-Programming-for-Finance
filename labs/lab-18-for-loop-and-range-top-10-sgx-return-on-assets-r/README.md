# Lab 18 — For Loop and Range — Top 10 SGX Return on Assets (ROA) Ranking

**Topic 3: Problem Solving with Control Structures**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO2: Apply for loops and the range function to iterate a portfolio of tickers, compute Return on Assets for each, and rank the results.

## Goal

You iterate a list of ten major SGX tickers — DBS, UOB, OCBC, SingTel, Jardine, Keppel, Venture, CapitaLand Integrated, Ascendas REIT and City Developments — fetching Net Income and Total Assets for each and computing ROA = Net Income / Total Assets * 100. You then sort the results and print a ranked league table. Along the way you use range for a compound-growth projection and learn why a per-ticker try/except keeps a ten-stock scan alive when one ticker's data is missing.

## What you'll build

roa_ranking.py — fetches fundamentals for 10 SGX tickers in a for loop and prints a sorted Top 10 ROA league table.

**Tools:** uv, yfinance, pandas, Google Colab / Cursor, Gemini or Copilot

## Step-by-step

1. Create the uv project and add market-data dependencies.

   ```bash
   uv init lab-18-roa-ranking && cd lab-18-roa-ranking && uv add yfinance pandas
   ```

2. Warm up with range: in roa_ranking.py project a $1,000 principal at 5% for 10 years using `for year in range(1, years + 1)` and the formula principal * (1 + rate) ** year, printing each year-end balance.

   ```bash
   uv run python roa_ranking.py
   ```

3. Define the ticker list: sgx_tickers = ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'J36.SI', 'BN4.SI', 'V03.SI', 'C38U.SI', 'A17U.SI', 'C07.SI'].
4. Write the main for loop: for each ticker build a yf.Ticker object, read stock.financials and stock.balance_sheet, extract Net Income and Total Assets with .loc[...].iloc[0], compute ROA, and append a dict {'name', 'ticker', 'roa'} to a results list.
5. Wrap the body of the loop in try/except so a single failing ticker prints a skip message and the loop continues to the next one instead of aborting the whole scan.

   ```bash
   uv run python roa_ranking.py
   ```

6. Pull a readable company name with stock.info.get('shortName', ticker) — the .get default means a missing name falls back to the ticker rather than raising KeyError.
7. Sort the results descending by ROA using sorted(results, key=lambda x: x['roa'], reverse=True).
8. Print a ranked table with aligned columns: use enumerate(..., 1) for the rank number and f-string width specifiers such as {name:<28} {ticker:<10} {roa:>8.2f}, under a header row and a separator line.

   ```bash
   uv run python roa_ranking.py
   ```

9. AI-ASSIST: prompt your AI tool with: "This loop makes one network call per ticker and re-fetches on every run. Add a simple check that skips a ticker whose Total Assets is zero or missing to avoid ZeroDivisionError, count how many tickers succeeded versus were skipped, and print that summary at the end. Do not add any external caching library." Review the changes before applying.
10. Apply the AI version and deliberately insert an invalid ticker such as 'XXXX.SI' in the middle of the list. Confirm the scan completes all ten, reports the skip, and the summary counts are correct.

   ```bash
   uv run python roa_ranking.py
   ```

11. Add a range-based slice of the league table: use `for i in range(3)` to print only the top three performers under a 'BEST IN CLASS' heading.

   ```bash
   uv run python roa_ranking.py
   ```

12. Discuss: ROA and ROE tell different stories for a bank, which is highly leveraged. Which of the two is more comparable across a bank and a REIT, and why?

## Test it

Run `uv run python roa_ranking.py`. You should see the 10-year compound projection, then a ranked ROA table with up to 10 rows sorted highest ROA first, a BEST IN CLASS top-three block, and a final summary line counting successes and skips. Inserting 'XXXX.SI' must not stop the scan.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
