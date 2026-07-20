"""Lab 11 — Dictionaries — Company Stock Values and Market Cap Lookup

Topic 2: Data Types and Operators
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply the dictionary data type to map financial instrument keys to values and build a fast lookup for portfolio reporting.

Goal: Mirroring the reference notebook activity, the learner builds a dictionary of stock attributes, practises access, update, membership testing, pop and iteration, then constructs a ticker-to-market-cap dictionary with a comprehension and uses .get() with a default to make the lookup safe for a missing ticker.

You will build: A script `stock_dict.py` holding a ticker-to-market-cap dictionary with a safe lookup and a formatted portfolio valuation.
Tools: uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

Run this lab with uv:
    uv run python dictionaries_company_stock_values_and_ma.py
"""


def main():
    print("Lab 11: Dictionaries — Company Stock Values and Market Cap Lookup")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project.
    #   $ uv init lab-11-dictionaries && cd lab-11-dictionaries
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Create stock_dict.py with a dictionary describing one holding, and read a
    # value by key.
    #   $ stock_info = {'ticker': 'D05.SI', 'name': 'DBS Group Holdings', 'price': 35.50}; print(stock_info['name'])
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Add a new key and update an existing one — the two operations that make
    # dictionaries the right structure for a mutable position record.
    #   $ stock_info['currency'] = 'SGD'; stock_info['price'] = 36.20
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Test membership before access, then pop a key and iterate the remaining
    # items.
    #   $ if 'ticker' in stock_info: print(stock_info['ticker'])
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Iterate keys and values for a printed position record.
    #   $ for key, value in stock_info.items(): print(f'{key}: {value}')
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Build the ticker-to-market-cap dictionary with a dict comprehension over a
    # list of company records.
    #   $ company_market_values = {item['ticker']: item['market_cap'] for item in top_10_data}
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Use .get() with a default so a delisted ticker returns a safe value
    # instead of raising KeyError.
    #   $ print(f"DBS market cap: ${company_market_values.get('D05.SI', 0):,.0f}")
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Compare .get() with direct bracket access on a missing ticker and observe
    # the KeyError.
    #   $ uv run python stock_dict.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # PROMPT THE AI ASSISTANT with: 'Extend stock_dict.py with a portfolio
    # dictionary mapping ticker to number of shares for D05.SI 2000, U11.SI
    # 1500, O39.SI 3000 and Z74.SI 10000, and a prices dictionary for the same
    # tickers. Compute each position value and the total portfolio value, print
    # a table of ticker, shares, price, value and weight as a percentage of the
    # portfolio sorted by value descending, and use .get() with a default of 0
    # so a ticker missing from prices reports a value of zero with a warning
    # line rather than crashing.' Apply the code.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # REVIEW the AI output: confirm the weights sum to 100%, that .get()
    # defaults are used on the prices lookup and not on the shares lookup, and
    # that the sort is descending by value.
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Delete Z74.SI from the prices dictionary and re-run to prove the warning
    # path works.
    #   $ uv run python stock_dict.py
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # The portfolio table prints four positions sorted by value with weights
    # summing to 100%; removing Singtel from the prices dictionary produces a
    # warning line and a zero-value row instead of a KeyError.


if __name__ == "__main__":
    main()
