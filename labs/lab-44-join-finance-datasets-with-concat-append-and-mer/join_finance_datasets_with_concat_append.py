"""Lab 44 — Join Finance Datasets with concat, append and merge

Topic 7: Aggregate and Visualize Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO6: Combine prices, fundamentals and customer records into one analysis-ready frame using concat and merge.

Goal: The learner combines the loan book with two extra sources: a second branch's loan file (stacked vertically with pd.concat) and a regional risk-rating reference table (joined horizontally with pd.merge on Region). The lab contrasts inner, left and outer joins and shows what a mismatched key silently does to a loan book — the classic cause of disappearing applicants in a reconciliation.

You will build: A join_data.py script producing df_all — the combined multi-branch loan book enriched with regional risk ratings.
Tools: uv, pandas, VS Code / Cursor AI assistant

Run this lab with uv:
    uv run python join_finance_datasets_with_concat_append.py
"""


def main():
    print("Lab 44: Join Finance Datasets with concat, append and merge")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add pandas.
    #   $ uv init lab-44-join-finance-data && cd lab-44-join-finance-data && uv add pandas numpy
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Copy df_finance.csv from lab 43 into this project.
    #   $ cp ../lab-43-mock-loan-data/df_finance.csv .
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Create a second branch file by regenerating with a different seed and an
    # offset Applicant_ID, saving it as df_branch2.csv.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Stack the two branches vertically and reset the index.
    #   $ uv run python -c "import pandas as pd; a=pd.read_csv('df_finance.csv'); b=pd.read_csv('df_branch2.csv'); df=pd.concat([a,b], ignore_index=True); print(len(a), len(b), len(df))"
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Prompt your AI assistant: "Given a pandas DataFrame df of loan applicants
    # with a Region column, build a small reference DataFrame df_risk with one
    # row per Region and columns Regional_Risk_Rating (A/B/C) and
    # Base_Interest_Rate. Then merge it into df on Region using a left join, and
    # print how many rows have a null Regional_Risk_Rating after the merge."
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Review the generated merge — confirm it uses how='left' so no applicant is
    # dropped, and that the null check is present.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Deliberately break one Region value (e.g. 'central' lower-case) and re-run
    # the merge to see the applicant lose its rating.
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Compare the row counts of an inner, left and outer merge on the broken
    # key.
    #   $ uv run python join_data.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Discuss: in a loan reconciliation, which join type is safest and why must
    # the post-merge row count always be asserted?
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Save the final combined frame.
    #   $ uv run python -c "import pandas as pd; print('df_all saved')"
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # df_all has exactly len(branch1) + len(branch2) rows after the left merge —
    # no applicant is silently lost — and zero null Regional_Risk_Rating values
    # once the key is fixed.


if __name__ == "__main__":
    main()
