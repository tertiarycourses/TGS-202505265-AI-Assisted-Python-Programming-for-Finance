"""Lab 15 — If-Elif Income Grouping and Credit Risk Banding

Topic 3: Problem Solving with Control Structures
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply a multi-branch if-elif-else ladder to classify bank customers into income bands and credit-risk categories.

Goal: Retail banking runs on segmentation. You build a classifier that maps annual income into Low (below $30,000), Middle (up to $80,000), High (up to $150,000) and Super High Income bands, then a second classifier that maps a 300-850 credit score into Excellent / Good / Fair / Poor with the bank's stated lending posture for each. You will see why the ORDER of elif branches is load-bearing: reverse two of them and customers land in the wrong band.

You will build: income_grouping.py — classifies annual income into four bands and a credit score into four risk categories, with range validation.
Tools: uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python if_elif_income_grouping_and_credit_risk.py
"""


def main():
    print("Lab 15: If-Elif Income Grouping and Credit Risk Banding")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project for the segmentation lab.
    #   $ uv init lab-15-income-grouping && cd lab-15-income-grouping
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Create income_grouping.py and read the customer's annual income with
    # float(input('Enter annual income: ')).
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Write the if-elif ladder: below 30000 is 'Low Income'; up to 80000 is
    # 'Middle Income'; up to 150000 is 'High Income'; else 'Super High Income'.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Print the result with formatting: income as ${:,.2f} and the
    # classification on its own line.
    #   $ uv run python income_grouping.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Test the band boundaries deliberately: 29999.99, 30000, 80000, 150000 and
    # 150000.01. Note which side of each boundary each value lands on.
    #   $ uv run python income_grouping.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # BREAK IT ON PURPOSE: move the 'income <= 150000' branch above the 'income
    # <= 80000' branch, re-run with 50000, and observe it now misclassifies as
    # High Income. Restore the correct order and write one sentence explaining
    # why elif order matters.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Add the second classifier in the same script: read a credit score with
    # int(input(...)) and band it — 800+ Excellent ('High probability of loan
    # approval at best rates'), 700+ Good ('Likely approved with standard
    # rates'), 600+ Fair ('May be approved with higher interest rates'), else
    # Poor ('High risk; loan approval unlikely').
    #   $ uv run python income_grouping.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Add input validation to this banking
    # classifier — reject a negative annual income, and reject any credit score
    # outside the valid 300 to 850 range with a specific message naming the
    # valid range. Use try/except to handle non-numeric input. Then refactor
    # both classifiers into a single reusable function each." Review the
    # generated functions before running them.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Run the AI-refactored script and test the invalid paths: income of -1000,
    # credit score of 250, credit score of 900, and the text 'seven hundred'.
    #   $ uv run python income_grouping.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Add a combined rule at the end: a customer in the High or Super High
    # income band AND with a credit score of 700 or above is flagged 'PRIORITY
    # WEALTH SEGMENT'. Use the logical `and` operator inside a single if.
    #   $ uv run python income_grouping.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Discuss: the bands here are hard-coded. What is the operational risk when
    # the bank's segmentation policy changes and this rule is duplicated across
    # five scripts?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python income_grouping.py` and enter income 25000 / 55000 /
    # 120000 / 250000 — you should get Low, Middle, High and Super High Income
    # respectively. A credit score of 810 must return Excellent; 250 and 900
    # must both be rejected with a range message. Income 160000 with score 750
    # must print PRIORITY WEALTH SEGMENT.


if __name__ == "__main__":
    main()
