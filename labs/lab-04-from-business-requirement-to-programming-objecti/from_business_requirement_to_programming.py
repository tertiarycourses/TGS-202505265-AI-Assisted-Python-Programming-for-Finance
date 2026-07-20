"""Lab 4 — From Business Requirement to Programming Objective — SGX Price Fetcher

Topic 1: Introduction to Python Programming
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO1: Translate a financial services business requirement into a programming objective and set up an AI-assisted Python environment that fetches live SGX market data.

Goal: The learner practises the requirement-to-objective translation that opens every real project: a written business requirement from a wealth desk is decomposed into inputs, processing, outputs and acceptance criteria, then implemented as a first live market-data script using yfinance against the SGX tickers used throughout the course.

You will build: A requirements note plus `sgx_prices.py`, which fetches and prints the latest close for DBS, UOB, OCBC, Singtel and CapitaLand.
Tools: uv, Python 3.12, yfinance, VS Code / Cursor / Google Colab, Gemini or Copilot

Run this lab with uv:
    uv run python from_business_requirement_to_programming.py
"""


def main():
    print("Lab 4: From Business Requirement to Programming Objective — SGX Price Fetcher")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add the market-data dependency.
    #   $ uv init lab-04-sgx-prices && cd lab-04-sgx-prices && uv add yfinance
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Read the business requirement aloud: 'Each morning the wealth desk needs
    # the previous close of our five core SGX holdings, in SGD, on one screen,
    # so advisers can brief clients before the market opens.'
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Decompose it in a plain-text file requirements.md under four headings —
    # INPUTS (the five tickers), PROCESSING (fetch last close), OUTPUTS (ticker,
    # name, close price), ACCEPTANCE CRITERIA (all five print, two decimals, no
    # crash if one ticker fails).
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Define the watchlist in Python as the programming objective's input.
    #   $ tickers = ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'C38U.SI']
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Fetch one ticker manually first to see the shape of the data before
    # automating.
    #   $ uv run python -c "import yfinance as yf; print(yf.Ticker('D05.SI').history(period='5d')['Close'])"
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # PROMPT THE AI ASSISTANT with: 'Write sgx_prices.py. For each ticker in
    # D05.SI, U11.SI, O39.SI, Z74.SI, C38U.SI use yfinance to fetch the most
    # recent closing price and the short name. Print one aligned row per ticker
    # showing the ticker, the company name and the close formatted as SGD with
    # two decimals. If a ticker returns no data, print NO DATA for that row and
    # continue to the next ticker.' Save the result.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # REVIEW the AI output against your acceptance criteria: does it handle the
    # empty-data case, does it continue after a failure, and does it format to
    # two decimals?
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Run the script.
    #   $ uv run python sgx_prices.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Introduce a deliberately invalid ticker such as 'ZZZZ.SI' into the list
    # and re-run to prove the acceptance criterion about failure is genuinely
    # met.
    #   $ uv run python sgx_prices.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Discuss: which of your four headings did the AI get right without being
    # told, and which did you have to specify? This is the difference between a
    # prompt and a requirement.
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # `uv run python sgx_prices.py` prints five aligned rows with company names
    # and SGD closing prices to two decimal places, and prints NO DATA rather
    # than crashing when the invalid ticker is included.


if __name__ == "__main__":
    main()
