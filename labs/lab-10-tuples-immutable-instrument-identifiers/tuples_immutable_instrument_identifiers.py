"""Lab 10 — Tuples — Immutable Instrument Identifiers

Topic 2: Data Types and Operators
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply the tuple data type and unpacking to represent fixed financial identifiers that must not change during processing.

Goal: The learner creates tuples of SGX tickers and OHLC records, practises indexing, slicing, length and unpacking, and proves immutability by attempting a write. The lab then applies tuples where they genuinely belong in finance: as fixed instrument identifiers, as multiple return values from a ratio function, and as dictionary keys.

You will build: A script `tuples_demo.py` demonstrating tuple unpacking of OHLC records and a function returning a tuple of financial ratios.
Tools: uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

Run this lab with uv:
    uv run python tuples_immutable_instrument_identifiers.py
"""


def main():
    print("Lab 10: Tuples — Immutable Instrument Identifiers")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project.
    #   $ uv init lab-10-tuples && cd lab-10-tuples
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Create tuples_demo.py with the core bank tickers as an immutable tuple,
    # and index and slice it.
    #   $ stock_tuple = ('D05.SI', 'U11.SI', 'O39.SI'); print(stock_tuple[0], stock_tuple[0:2], len(stock_tuple))
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Unpack the tuple into three named variables in one statement.
    #   $ ticker1, ticker2, ticker3 = stock_tuple; print(ticker1, ticker2, ticker3)
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Prove immutability: uncomment the assignment and observe the TypeError,
    # then discuss why an approved instrument list should be immutable.
    #   $ stock_tuple[0] = 'S68.SI'
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Build a list of OHLC tuples for one trading day and unpack each in a loop.
    #   $ bars = [('D05.SI', 35.20, 36.10, 35.05, 35.90), ('U11.SI', 32.10, 32.80, 31.95, 32.60)]
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Iterate with tuple unpacking directly in the for statement.
    #   $ for tkr, o, h, l, c in bars: print(f'{tkr}: range {h-l:.2f}, change {c-o:+.2f}')
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # PROMPT THE AI ASSISTANT with: 'Add a function ratios(net_profit, revenue,
    # equity, assets) to tuples_demo.py that returns a tuple of net profit
    # margin, ROE and ROA as percentages. Call it for DBS with net profit
    # 11290000000, revenue 20180000000, equity 62400000000 and assets
    # 739000000000, unpack the returned tuple into three variables and print
    # each to two decimals with a percent sign. Then build a dictionary keyed by
    # the tuple (ticker, financial_year) holding those ratios for two years and
    # print it.' Apply the code.
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # REVIEW the AI output: confirm the function returns a tuple rather than a
    # list, that each ratio is multiplied by 100 exactly once, and that the
    # tuple key is valid because it is immutable.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Run the script.
    #   $ uv run python tuples_demo.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Try to use a list as the dictionary key instead of the tuple and observe
    # the TypeError — this is the practical reason tuples exist.
    #   $ uv run python tuples_demo.py
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # The OHLC loop prints the day range and change for each bank, ratios()
    # returns a three-element tuple giving a DBS net margin near 55.95%, ROE
    # near 18.09% and ROA near 1.53%, and the tuple-keyed dictionary prints
    # without error.


if __name__ == "__main__":
    main()
