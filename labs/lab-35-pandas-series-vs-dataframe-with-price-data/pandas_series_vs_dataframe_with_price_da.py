"""Lab 35 — Pandas Series vs DataFrame with Price Data

Topic 6: Import and Process Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO5: Construct and distinguish a pandas Series and a DataFrame, and index both with financial labels.

Goal: The learner builds a Series of closing prices indexed by date, then a DataFrame holding open, high, low, close and volume for several tickers. Working with both side by side makes the distinction concrete: a Series is one labelled column — a single instrument's price history — while a DataFrame is a labelled table where a column selection returns a Series again. The learner also compares `.loc` label-based access against `.iloc` position-based access, the source of most beginner indexing bugs in finance code.

You will build: A uv project `lab-35-series-dataframe` with series_vs_frame.py demonstrating Series construction, DataFrame construction, column and row selection, and a printed comparison of .loc versus .iloc.
Tools: uv, pandas, AI coding assistant

Run this lab with uv:
    uv run python pandas_series_vs_dataframe_with_price_da.py
"""


def main():
    print("Lab 35: Pandas Series vs DataFrame with Price Data")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add pandas.
    #   $ uv init lab-35-series-dataframe && cd lab-35-series-dataframe && uv add pandas
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # In series_vs_frame.py build a Series of 10 daily closing prices for D05.SI
    # indexed by a pd.date_range of business days, and print it with its .index,
    # .dtype and .name.
    #   $ touch series_vs_frame.py
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Print series.mean(), series.max() and series.pct_change() and note that a
    # Series carries its index through every operation.
    #   $ uv run python series_vs_frame.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Build a DataFrame with columns Open, High, Low, Close and Volume over the
    # same dates, and print df.shape, df.columns and df.dtypes.
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Select a single column with df['Close'] and confirm with type() that it is
    # a Series, not a DataFrame; then select df[['Close', 'Volume']] and confirm
    # that a list of columns returns a DataFrame.
    #   $ uv run python series_vs_frame.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Discuss: the single-bracket versus double-bracket distinction. Passing a
    # Series where a DataFrame is expected is a very common error in financial
    # pipelines.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Compare label and position indexing: df.loc['2024-03-05'] against
    # df.iloc[2], and df.loc['2024-03-04':'2024-03-08'] against df.iloc[1:4].
    # Note that .loc slices are INCLUSIVE of the endpoint while .iloc slices are
    # not.
    #   $ uv run python series_vs_frame.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # AI STEP — prompt your AI assistant: "Explain the difference between a
    # pandas Series and a DataFrame using a stock price example, and give me
    # three short code snippets showing when .loc silently returns different
    # rows than .iloc on a date-indexed price table. Include the off-by-one trap
    # on slice endpoints."
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Run the AI's snippets yourself and verify each claim against your own
    # DataFrame — do not accept the endpoint behaviour on trust.
    #   $ uv run python series_vs_frame.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Add a multi-ticker DataFrame with a two-level column index (ticker, field)
    # and select just the Close columns for all tickers.
    #   $ uv run python series_vs_frame.py
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # The script prints the Series with its DatetimeIndex, confirms
    # type(df['Close']) is Series and type(df[['Close']]) is DataFrame, and
    # shows .loc and .iloc returning the expected rows with the
    # inclusive/exclusive endpoint difference clearly labelled.


if __name__ == "__main__":
    main()
