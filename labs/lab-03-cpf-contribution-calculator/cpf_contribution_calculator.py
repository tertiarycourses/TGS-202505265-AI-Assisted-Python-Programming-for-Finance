"""Lab 3 — CPF Contribution Calculator

Topic 1: Introduction to Python Programming
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO1: Translate the CPF contribution business rules into a Python programming objective and implement them as a working script.

Goal: Mirroring the reference notebook activity, the learner builds a CPF calculator that applies the age-banded employee and employer contribution rates against the Ordinary Wage ceiling, then hardens it with input validation and a formatted contribution breakdown suitable for a payroll report.

You will build: A script `cpf_calculator.py` that takes a monthly salary and age and prints the employee, employer and total CPF contribution with the wage ceiling applied.
Tools: uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

Run this lab with uv:
    uv run python cpf_contribution_calculator.py
"""


def main():
    print("Lab 3: CPF Contribution Calculator")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project.
    #   $ uv init lab-03-cpf-calculator && cd lab-03-cpf-calculator
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Write the business rules in plain English first: rates are banded by age
    # (55 and below, 56–60, 61–65, 66–70, above 70); the Ordinary Wage ceiling
    # caps the contributable salary at $6,800.
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Create cpf_calculator.py and define the function signature and the age
    # bands.
    #   $ def calculate_cpf(salary, age):
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Implement the age-banded rates with if/elif — employee and employer rate
    # as a pair.
    #   $ if age <= 55: emp_rate, emr_rate = 0.20, 0.17
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Apply the Ordinary Wage ceiling before computing any contribution.
    #   $ capped_salary = min(salary, 6800)
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Return the three figures the payroll report needs.
    #   $ return capped_salary * emp_rate, capped_salary * emr_rate, capped_salary * (emp_rate + emr_rate)
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Collect the inputs and print the breakdown to two decimal places.
    #   $ sal = float(input('Enter monthly salary: ')); age = int(input('Enter age: '))
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Run it with a salary of 5000 and age 30, then with 9000 and age 30 to see
    # the ceiling bite.
    #   $ uv run python cpf_calculator.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # PROMPT THE AI ASSISTANT with: 'Harden cpf_calculator.py. Reject a negative
    # or non-numeric salary and an age below 16 or above 100 with a clear
    # message instead of a traceback. Print the capped salary alongside the raw
    # salary so the user can see when the $6,800 Ordinary Wage ceiling was
    # applied, and format every amount as $x,xxx.xx. Keep calculate_cpf a pure
    # function that returns three values.' Apply the generated code.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # REVIEW the AI output: verify the rate bands were not altered, that
    # min(salary, 6800) is still applied before the rate, and that the totals
    # still equal employee + employer.
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Test the edge cases: salary 0, salary 20000, age 56, age 71, and a
    # non-numeric salary such as 'abc'.
    #   $ uv run python cpf_calculator.py
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # A salary of 9000 at age 30 returns an employee contribution of $1,360.00,
    # an employer contribution of $1,156.00 and a total of $2,516.00 — proving
    # the $6,800 ceiling was applied. Entering 'abc' as the salary prints a
    # friendly message, not a traceback.


if __name__ == "__main__":
    main()
