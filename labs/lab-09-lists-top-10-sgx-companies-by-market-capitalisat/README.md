# Lab 9 — Lists — Top 10 SGX Companies by Market Capitalisation

**Topic 2: Data Types and Operators**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO2: Apply the list data type, indexing, slicing and sorting to rank financial instruments by a business metric.

## Goal

The learner exercises list creation, indexing, slicing, index() and pop() on a price series, then mirrors the reference notebook activity by fetching market capitalisation for a basket of SGX tickers with yfinance and producing a ranked top-10 list of Singapore's largest listed companies.

## What you'll build

A script `top10_sgx.py` that fetches market caps for a basket of SGX tickers and prints the top 10 ranked by market capitalisation.

**Tools:** uv, Python 3.12, yfinance, VS Code / Cursor / Google Colab, Gemini or Copilot

## Step-by-step

1. Create the project and add the market-data dependency with uv (not pip).

   ```bash
   uv init lab-09-top10-sgx && cd lab-09-top10-sgx && uv add yfinance
   ```

2. Create lists_demo.py with a short closing-price series and practise indexing and slicing.

   ```bash
   prices = [35.20, 35.80, 36.10, 35.95, 36.40]; print(prices[0], prices[-1], prices[0:3])
   ```

3. Find the position of a value and pop the latest observation — the two list operations used most in a rolling window.

   ```bash
   print(prices.index(36.10)); print(prices.pop(), prices)
   ```

4. Create top10_sgx.py and define the SGX basket as a list of tickers.

   ```bash
   sgx_tickers = ['D05.SI','U11.SI','O39.SI','Z74.SI','J36.SI','BN4.SI','V03.SI','C38U.SI','A17U.SI','C07.SI','C31.SI','U96.SI','F34.SI','S68.SI','BS6.SI']
   ```

5. Loop the basket, pull marketCap and shortName from yfinance, and append a dict per company to a results list, skipping any ticker that fails.

   ```bash
   company_data.append({'name': name, 'ticker': ticker, 'market_cap': market_cap})
   ```

6. Sort descending by market cap and slice the top ten.

   ```bash
   top_10 = sorted(company_data, key=lambda x: x['market_cap'], reverse=True)[:10]
   ```

7. Run it and note how long the fetch takes — API latency is a design constraint in any production screen.

   ```bash
   uv run python top10_sgx.py
   ```

8. PROMPT THE AI ASSISTANT with: 'Improve top10_sgx.py. Skip any ticker whose marketCap is missing or zero instead of ranking it as zero. Print a numbered table with rank, company name, ticker and market cap formatted in SGD billions to two decimals, plus a final line giving the combined market cap of the top 10 and each company's percentage share of that total. Cache the fetched results to a local JSON file so a re-run does not hit the API again.' Apply the code.
9. REVIEW the AI output: confirm missing caps are filtered before the sort, that the percentage shares total 100%, and that the cache is read before the network call rather than after.
10. Run the improved script twice and confirm the second run is served from the cache.

   ```bash
   uv run python top10_sgx.py
   ```

11. Add a deliberately invalid ticker 'ZZZZ.SI' to the basket and re-run to prove the skip logic holds.

   ```bash
   uv run python top10_sgx.py
   ```


## Test it

The script prints a numbered top-10 table led by DBS (D05.SI) with market caps in SGD billions, the percentage shares sum to 100%, and the invalid ticker is silently skipped.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
