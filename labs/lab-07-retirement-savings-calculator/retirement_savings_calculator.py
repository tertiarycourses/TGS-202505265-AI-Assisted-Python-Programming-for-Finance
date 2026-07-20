"""Lab 7 — Retirement Savings Calculator

Topic 2: Data Types and Operators
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply numeric data types, arithmetic operators and compound assignment to solve a retirement future-value calculation problem.

Goal: Mirroring the reference notebook activity, the learner computes the future value of a regular monthly savings plan using the annuity formula, then adds a CPF top-up scenario and a year-by-year projection table so a client can see the compounding effect rather than just a single number.

You will build: A script `retirement_calculator.py` that projects retirement savings from a monthly contribution, expected return and years to retirement.
Tools: uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

Run this lab with uv:
    uv run python retirement_savings_calculator.py
"""


def main():
    print("Lab 7: Retirement Savings Calculator")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project.
    #   $ uv init lab-07-retirement && cd lab-07-retirement
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Create retirement_calculator.py and collect the four planning inputs.
    #   $ current_age = int(input('Enter your current age: ')); retirement_age = int(input('Enter your target retirement age: ')); monthly_savings = float(input('Enter amount you save monthly: ')); annual_return_rate = float(input('Enter expected annual return rate (e.g., 5 for 5%): '))
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Derive the horizon in months and the monthly rate.
    #   $ months = (retirement_age - current_age) * 12; monthly_rate = annual_return_rate / 100 / 12
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Implement the future-value-of-an-annuity formula, guarding the zero-return
    # case with a conditional.
    #   $ total = monthly_savings * (((1 + monthly_rate) ** months - 1) / monthly_rate) if monthly_rate > 0 else monthly_savings * months
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Print the projection with thousands separators, and print the total
    # contributed so the client can see how much is growth rather than saving.
    #   $ print(f'Projected: ${total:,.2f} | Contributed: ${monthly_savings*months:,.2f} | Growth: ${total - monthly_savings*months:,.2f}')
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Run a realistic Singapore case: age 30 to 65, $1,000 a month, 5% expected
    # return.
    #   $ uv run python retirement_calculator.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # PROMPT THE AI ASSISTANT with: 'Extend retirement_calculator.py to also
    # print a year-by-year table with columns Age, Contributed To Date, Balance
    # and Growth, using a compound assignment (balance += ...) inside a loop
    # over the months and printing one row at each year boundary. Add a CPF
    # Special Account scenario at a fixed 4% return alongside the user rate, and
    # print both projected balances side by side. Reject a retirement age not
    # greater than the current age.' Apply the code.
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # REVIEW the AI output: check the loop applies the monthly return before
    # adding the contribution consistently, that the final loop balance agrees
    # with the closed-form formula to within a dollar, and that the validation
    # actually stops execution.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Run and verify the closed-form and the iterative balance agree.
    #   $ uv run python retirement_calculator.py
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Test sensitivity: re-run at 3%, 5% and 7% and note in your lab record how
    # much of the final balance is growth in each case.
    #   $ uv run python retirement_calculator.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Discuss: what does this model ignore — inflation, fees,
    # sequence-of-returns risk — and how would you disclose that to a client?
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Saving $1,000 a month from age 30 to 65 at 5% projects approximately
    # $1,136,000, with roughly $420,000 contributed and the remainder growth;
    # the year-by-year table's final row matches the closed-form figure.


if __name__ == "__main__":
    main()
