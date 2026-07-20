"""Lab 58 — Lambda versus Named Functions in .apply()

Topic 9: Analyze Finance Data
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO8: Choose between lambda and named functions in apply, and assess code to identify readability and testability gaps.

Goal: The learner takes the same classification logic and writes it three ways: a one-line lambda, a named function passed by reference, and a vectorised alternative using np.select. Each is benchmarked and, critically, assessed for testability — a named function can be unit-tested in isolation, a lambda buried in an apply cannot. The learner writes pytest cases for the named function, including the boundary values that the lambda version silently gets wrong.

You will build: A classify.py module with three implementations plus test_classify.py containing passing boundary-value tests.
Tools: uv, pandas, NumPy, pytest, VS Code / Cursor AI assistant

Run this lab with uv:
    uv run python lambda_versus_named_functions_in_apply.py
"""


def main():
    print("Lab 58: Lambda versus Named Functions in .apply()")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project and add the libraries including pytest.
    #   $ uv init lab-58-lambda-vs-function && cd lab-58-lambda-vs-function && uv add pandas numpy pytest
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Copy df_scored.csv from lab 57.
    #   $ cp ../lab-57-credit-risk-apply/df_scored.csv .
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Write version A by hand: a lambda inside .apply() banding
    # Calculated_Risk_Score into High/Medium/Low.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Prompt your AI assistant: "Refactor this pandas lambda apply into a named
    # function classify_risk(score) with an explicit docstring stating the
    # boundary behaviour at exactly 30 and exactly 60, and a third vectorised
    # version using numpy.select with the same conditions. All three must
    # produce identical output on the same column. Then write pytest tests for
    # classify_risk covering scores of 0, 30, 30.01, 60, 60.01 and 100, plus a
    # None input."
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Save the three implementations in classify.py and the tests in
    # test_classify.py.
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Assess the code for gaps: does the lambda handle a NaN score? Does it
    # define whether exactly 60 is High or Medium? Note every ambiguity you
    # find.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Run the tests — expect the boundary cases to expose the ambiguity.
    #   $ uv run pytest test_classify.py -v
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Fix classify_risk so the documented boundary behaviour and the tests
    # agree, then re-run until green.
    #   $ uv run pytest test_classify.py -v
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Prove all three versions agree on the real data.
    #   $ uv run python -c "import pandas as pd; from classify import apply_lambda, apply_named, apply_vectorised; d=pd.read_csv('df_scored.csv'); a,b,c = apply_lambda(d), apply_named(d), apply_vectorised(d); print((a==b).all(), (b==c).all())"
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Time the three approaches on the 500-row frame and again on a 500,000-row
    # frame to see where vectorisation wins.
    #   $ uv run python classify.py --benchmark
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Discuss: when is a lambda the right choice, and why does a risk model that
    # will face an auditor belong in a named, tested function?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # All pytest boundary tests pass; the lambda, named and vectorised outputs
    # are element-wise identical on df_scored.csv; the benchmark shows np.select
    # fastest at scale.


if __name__ == "__main__":
    main()
