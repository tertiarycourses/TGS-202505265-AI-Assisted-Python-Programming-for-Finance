"""Lab 59 — Building a clean → enrich → score Pipeline with .pipe()

Topic 9: Analyze Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO8: Chain transformations into a readable, testable data pipeline using .pipe().

Goal: The reference slide 155 activity, extended into a full three-stage pipeline. The learner writes small single-purpose functions — clean_data (drop duplicates, coerce dtypes, handle missing income), enrich_data (add Risk_Adjusted_Loan as Loan_Amount_Requested * Credit_Score / 850, plus an income band and a tenure band), and score_data (attach the lab 58 risk classification) — then chains them with .pipe(). A summarize_by_sector step produces the final table of mean Annual_Income, total Risk_Adjusted_Loan and applicant count. The lab contrasts the pipe chain with the unreadable nested-call equivalent.

You will build: A pipeline.py module of four pipe-able functions and a single readable chained expression producing sector_pipeline_summary.csv.
Tools: uv, pandas, pytest, VS Code / Cursor AI assistant

Run this lab with uv:
    uv run python building_a_clean_enrich_score_pipeline_w.py
"""


def main():
    print("Lab 59: Building a clean → enrich → score Pipeline with .pipe()")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add the libraries.
    #   $ uv init lab-59-pipe-pipeline && cd lab-59-pipe-pipeline && uv add pandas pytest
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Copy df_finance.csv and the classify module from lab 58.
    #   $ cp ../lab-43-mock-loan-data/df_finance.csv . && cp ../lab-58-lambda-vs-function/classify.py .
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Write the nested version first, deliberately:
    # summarize_by_sector(score_data(enrich_data(clean_data(df)))). Note how you
    # must read it inside-out.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Prompt your AI assistant: "Using a pandas DataFrame named df_finance,
    # build a .pipe() pipeline. Define clean_data(df) that drops duplicate
    # Applicant_IDs, coerces numeric columns and fills missing Annual_Income
    # with the sector median. Define filter_by_region(df, region='Central') that
    # filters to a region. Define enrich_data(df) that adds Risk_Adjusted_Loan
    # as Loan_Amount_Requested multiplied by Credit_Score divided by 850, plus
    # Income_Band via pd.cut. Define score_data(df) that adds
    # Calculated_Risk_Score and Risk_Profile. Define summarize_by_sector(df)
    # aggregating by Employment_Sector into mean Annual_Income, total
    # Risk_Adjusted_Loan and applicant count. Chain them all with .pipe() in one
    # readable expression and round the final summary to 2 decimals. Every
    # function must take a DataFrame as its first argument, return a new
    # DataFrame, and never mutate its input."
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Save as pipeline.py and audit the no-mutation rule: each function must
    # start with df = df.copy() or use non-mutating operations.
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Prove immutability — run the pipeline and confirm the original df_finance
    # is byte-identical afterwards.
    #   $ uv run python -c "import pandas as pd; from pipeline import run_pipeline; d=pd.read_csv('df_finance.csv'); before=d.copy(); run_pipeline(d); print(d.equals(before))"
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Run the full chain.
    #   $ uv run python pipeline.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Show the parameterised pipe: pass a region argument through the chain with
    # .pipe(filter_by_region, region='North') and confirm the summary changes.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Test each stage in isolation — a pipeline's value is that every stage is
    # independently testable.
    #   $ uv run pytest test_pipeline.py -v
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Verify the pipeline is order-safe: score_data before enrich_data must fail
    # loudly rather than produce silent nulls. Add an assertion on the required
    # columns at the top of each stage.
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Discuss: compare the pipe chain against the nested version you wrote first
    # — which would you rather hand to a colleague reviewing a credit model, and
    # why?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # run_pipeline() leaves the input DataFrame unmodified; the sector summary
    # has one row per Employment_Sector with three rounded metric columns; every
    # stage passes its isolated pytest and mis-ordering the stages raises an
    # assertion instead of returning nulls.


if __name__ == "__main__":
    main()
