"""Lab 38 — Inspect a Dataset with head, info and describe

Topic 6: Import and Process Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO5: Profile a financial dataset with head, tail, info, describe and value_counts to identify data-quality problems before analysis.

Goal: Before any calculation, an analyst profiles the data. The learner runs the standard inspection sequence over the cached market data and reads each output as a finance question: does info() show fewer non-null Closes than rows, meaning gaps? Does describe() show a minimum price of zero or a negative volume, meaning corrupt records? Does value_counts() over Ticker show one instrument with far fewer rows, meaning a late listing or a suspension? The learner writes a reusable profiling function that answers all of them.

You will build: A uv project `lab-38-inspect-data` with profile.py printing a full data-quality report and a written list of every anomaly found in the dataset.
Tools: uv, pandas, AI coding assistant

Run this lab with uv:
    uv run python inspect_a_dataset_with_head_info_and_des.py
"""


def main():
    print("Lab 38: Inspect a Dataset with head, info and describe")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project, add pandas, and copy in market_data.csv from lab 37.
    #   $ uv init lab-38-inspect-data && cd lab-38-inspect-data && uv add pandas && cp ../lab-37-yfinance-import/market_data.csv .
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Load the CSV with proper date parsing and print df.head(10) and
    # df.tail(10) to see the start and end of the series.
    #   $ uv run python profile.py
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Print df.info() and read it as a finance question: compare the non-null
    # count of Close against the total row count to find missing prices.
    #   $ uv run python profile.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Print df.describe() and inspect the min, max and quartiles of Close and
    # Volume for impossible values — a zero price, a negative volume, or a max
    # thousands of times the median.
    #   $ uv run python profile.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Print df['Ticker'].value_counts() and check every ticker has a similar row
    # count; investigate any that does not.
    #   $ uv run python profile.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Discuss: the three anomalies you found and what each would do to a
    # portfolio return calculation if left uncorrected.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Write profile_dataset(df) that packages the whole sequence — shape,
    # dtypes, null counts per column, describe, per-ticker row counts and date
    # coverage — into one printed report.
    #   $ uv run python profile.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # AI STEP — prompt your AI assistant: "Write a pandas data-quality report
    # function for a long-format stock price DataFrame with columns Date,
    # Ticker, Close, Volume. It must report: missing values per column,
    # duplicate (Date, Ticker) rows, non-positive prices, gaps of more than 5
    # calendar days in each ticker's date coverage, and any date that is not a
    # business day. Print it as a readable table."
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Run the AI's report on your data and verify each finding by hand against
    # the raw CSV before trusting it.
    #   $ uv run python profile.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Record the confirmed anomalies as a comment block at the top of profile.py
    # — this is the data-quality note that must accompany any published
    # analysis.
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # profile.py prints shape, dtypes, per-column null counts, describe output,
    # per-ticker row counts and date coverage, plus a list of duplicate or
    # non-positive-price rows. The learner can name at least two concrete
    # data-quality issues found in their own dataset.


if __name__ == "__main__":
    main()
