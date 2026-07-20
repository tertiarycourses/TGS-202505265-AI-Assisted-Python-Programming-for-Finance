# Lab 4 — From Business Requirement to Programming Objective — SGX Price Fetcher

**Topic 1: Introduction to Python Programming**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO1: Translate a financial services business requirement into a programming objective and set up an AI-assisted Python environment that fetches live SGX market data.

## Goal

The learner practises the requirement-to-objective translation that opens every real project: a written business requirement from a wealth desk is decomposed into inputs, processing, outputs and acceptance criteria, then implemented as a first live market-data script using yfinance against the SGX tickers used throughout the course.

## What you'll build

A requirements note plus `sgx_prices.py`, which fetches and prints the latest close for DBS, UOB, OCBC, Singtel and CapitaLand.

**Tools:** uv, Python 3.12, yfinance, VS Code / Cursor / Google Colab, Gemini or Copilot

## Step-by-step

1. Create the project and add the market-data dependency.

   ```bash
   uv init lab-04-sgx-prices && cd lab-04-sgx-prices && uv add yfinance
   ```

2. Read the business requirement aloud: 'Each morning the wealth desk needs the previous close of our five core SGX holdings, in SGD, on one screen, so advisers can brief clients before the market opens.'
3. Decompose it in a plain-text file requirements.md under four headings — INPUTS (the five tickers), PROCESSING (fetch last close), OUTPUTS (ticker, name, close price), ACCEPTANCE CRITERIA (all five print, two decimals, no crash if one ticker fails).
4. Define the watchlist in Python as the programming objective's input.

   ```bash
   tickers = ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'C38U.SI']
   ```

5. Fetch one ticker manually first to see the shape of the data before automating.

   ```bash
   uv run python -c "import yfinance as yf; print(yf.Ticker('D05.SI').history(period='5d')['Close'])"
   ```

6. PROMPT THE AI ASSISTANT with: 'Write sgx_prices.py. For each ticker in D05.SI, U11.SI, O39.SI, Z74.SI, C38U.SI use yfinance to fetch the most recent closing price and the short name. Print one aligned row per ticker showing the ticker, the company name and the close formatted as SGD with two decimals. If a ticker returns no data, print NO DATA for that row and continue to the next ticker.' Save the result.
7. REVIEW the AI output against your acceptance criteria: does it handle the empty-data case, does it continue after a failure, and does it format to two decimals?
8. Run the script.

   ```bash
   uv run python sgx_prices.py
   ```

9. Introduce a deliberately invalid ticker such as 'ZZZZ.SI' into the list and re-run to prove the acceptance criterion about failure is genuinely met.

   ```bash
   uv run python sgx_prices.py
   ```

10. Discuss: which of your four headings did the AI get right without being told, and which did you have to specify? This is the difference between a prompt and a requirement.

## Test it

`uv run python sgx_prices.py` prints five aligned rows with company names and SGD closing prices to two decimal places, and prints NO DATA rather than crashing when the invalid ticker is included.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
