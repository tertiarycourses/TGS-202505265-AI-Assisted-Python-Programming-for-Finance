"""Lab 1 — Set Up an AI-Assisted Python Environment with uv

Topic 1: Introduction to Python Programming
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO1: Set up an AI-assisted Python development environment and translate a finance business requirement into a programming objective.

Goal: The learner installs uv, creates the first finance project, adds the market-data and analysis dependencies used throughout the course, and confirms that the AI assistant in Google Colab / VS Code / Cursor can generate and explain Python code. The learner then writes the environment check as a short finance script that prints the SGX tickers the course will analyse.

You will build: A working uv project `lab-01-hello-finance` with yfinance and pandas installed, and an environment-check script that prints the course SGX watchlist.
Tools: uv, Python 3.12, yfinance, pandas, VS Code / Cursor / Google Colab, Gemini or Copilot

Run this lab with uv:
    uv run python set_up_an_ai_assisted_python_environment.py
"""


def main():
    print("Lab 1: Set Up an AI-Assisted Python Environment with uv")

    # ---- Step 1 -----------------------------------------------------------
    # Discuss the business requirement: a Singapore bank's analyst team needs a
    # repeatable Python environment so that every desk runs the same library
    # versions when valuing SGX equities. Write the requirement as one
    # programming objective.
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Install uv, the fast Python package and project manager used for every lab
    # in this course.
    #   $ curl -LsSf https://astral.sh/uv/install.sh | sh
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Confirm uv is on the PATH and note the version for your lab record.
    #   $ uv --version
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Create the first project for this topic.
    #   $ uv init lab-01-hello-finance
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Move into the project and pin the Python version the course standardises
    # on.
    #   $ cd lab-01-hello-finance && uv python pin 3.12
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Add the market-data and analysis dependencies. uv resolves and locks them
    # into pyproject.toml and uv.lock.
    #   $ uv add yfinance pandas
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Inspect the locked dependency tree — reproducibility is an audit
    # requirement in financial services.
    #   $ uv tree
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # PROMPT THE AI ASSISTANT (Colab Gemini / Cursor / Copilot chat) with:
    # 'Write a Python script named env_check.py that prints the Python version,
    # the installed yfinance and pandas versions, and then prints a numbered
    # watchlist of these SGX tickers with their company names: D05.SI DBS,
    # U11.SI UOB, O39.SI OCBC, Z74.SI Singtel, C38U.SI CapitaLand Integrated
    # Commercial Trust. Use f-strings and no external API calls.' Save the
    # generated code as env_check.py.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # REVIEW the AI output before running it: check that it imports only
    # yfinance and pandas, makes no network call, and that all five tickers
    # carry the correct .SI suffix. Correct anything the assistant got wrong.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Run the script inside the uv-managed environment.
    #   $ uv run python env_check.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Record in your lab notes one thing the AI assistant got wrong or left out
    # — this habit of verification is the core discipline of AI-assisted
    # development in a regulated environment.
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # `uv run python env_check.py` prints the Python version, the yfinance and
    # pandas versions, and all five SGX tickers with their company names, with
    # no traceback.


if __name__ == "__main__":
    main()
