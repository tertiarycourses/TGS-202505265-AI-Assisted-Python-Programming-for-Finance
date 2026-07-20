"""Lab 32 — KeyError and ValueError in a Portfolio Input Handler

Topic 5: Error Handling Using Exception
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO4: Catch KeyError for a missing portfolio holding and ValueError for malformed user input, using multiple except branches.

Goal: The learner builds an interactive portfolio lookup and loan-amount entry tool. Querying a ticker that is not in the holdings dictionary raises KeyError; typing '1,000,000' or 'fifty thousand' into a loan-amount prompt raises ValueError from int(). The learner writes a single try block with multiple except branches, then adds an input-validation loop that re-prompts until the value is usable — the standard pattern for any customer-facing finance form.

You will build: A uv project `lab-32-portfolio-input` with portfolio_tool.py providing a resilient ticker lookup and a validated loan-amount prompt that never crashes on bad input.
Tools: uv, Python 3.12, AI coding assistant

Run this lab with uv:
    uv run python keyerror_and_valueerror_in_a_portfolio_i.py
"""


def main():
    print("Lab 32: KeyError and ValueError in a Portfolio Input Handler")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project.
    #   $ uv init lab-32-portfolio-input && cd lab-32-portfolio-input
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Write portfolio_tool.py with PORTFOLIO = {'AAPL': 120, 'MSFT': 80,
    # 'D05.SI': 500} and an unguarded lookup that prints PORTFOLIO[ticker] for a
    # ticker typed by the user.
    #   $ touch portfolio_tool.py
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Run it and enter 'TSLA', a ticker you do not hold, to trigger KeyError.
    #   $ uv run python portfolio_tool.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Add a second unguarded prompt: amount = int(input('Loan amount: ')). Run
    # it and enter '1,000,000' to trigger ValueError.
    #   $ uv run python portfolio_tool.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Discuss: KeyError says the key is absent from the mapping; ValueError says
    # the type is right but the content is not convertible. They need different
    # messages to the user.
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Wrap the lookup in try/except KeyError, printing 'You do not hold TSLA —
    # holdings are: AAPL, MSFT, D05.SI' and continuing. Verify with a held and
    # an unheld ticker.
    #   $ uv run python portfolio_tool.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Wrap the loan prompt in a while True loop with try/except ValueError that
    # re-prompts until a valid positive integer is entered, and also rejects
    # zero or negative amounts.
    #   $ uv run python portfolio_tool.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # AI STEP — prompt your AI assistant: "Here is my Python input handler for a
    # loan application form. Rewrite it so it accepts amounts typed with commas
    # or a currency symbol like 'S$250,000', still raises ValueError for
    # genuinely invalid text, and caps the number of retries at three before
    # exiting with a clear message."
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # Test the AI-generated parser against the awkward cases yourself: '250000',
    # 'S$250,000', '-5000', '0', 'abc' and an empty string. Fix anything the AI
    # got wrong.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Discuss: why `.get(ticker, default)` is often better than try/except
    # KeyError for a dictionary, and when the explicit exception is still the
    # clearer choice.
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # The tool survives every input in the test set: unknown tickers produce a
    # helpful holdings list, malformed amounts re-prompt, and a valid amount is
    # echoed back formatted as currency. The script never terminates with a
    # traceback.


if __name__ == "__main__":
    main()
