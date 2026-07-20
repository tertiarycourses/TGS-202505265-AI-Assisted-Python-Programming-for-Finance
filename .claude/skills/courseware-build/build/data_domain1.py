"""
Topic 1 — Introduction to Python Programming (labs 1–4).

Hands-on activities for domain 1, mirroring the reference notebook
(Hello World finance script, CPF Calculator) and extended with two further
finance labs. All labs are managed with uv (`uv init`, `uv add`, `uv run`)
and every lab contains at least one AI-prompting step.
"""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Set Up an AI-Assisted Python Environment with uv",
        objective="LO1: Set up an AI-assisted Python development environment and translate a finance business requirement into a programming objective.",
        desc=(
            "The learner installs uv, creates the first finance project, adds the market-data and "
            "analysis dependencies used throughout the course, and confirms that the AI assistant in "
            "Google Colab / VS Code / Cursor can generate and explain Python code. The learner then "
            "writes the environment check as a short finance script that prints the SGX tickers the "
            "course will analyse."
        ),
        build="A working uv project `lab-01-hello-finance` with yfinance and pandas installed, and an environment-check script that prints the course SGX watchlist.",
        services="uv, Python 3.12, yfinance, pandas, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Discuss the business requirement: a Singapore bank's analyst team needs a repeatable Python environment so that every desk runs the same library versions when valuing SGX equities. Write the requirement as one programming objective.", ""),
            ("Install uv, the fast Python package and project manager used for every lab in this course.", "curl -LsSf https://astral.sh/uv/install.sh | sh"),
            ("Confirm uv is on the PATH and note the version for your lab record.", "uv --version"),
            ("Create the first project for this topic.", "uv init lab-01-hello-finance"),
            ("Move into the project and pin the Python version the course standardises on.", "cd lab-01-hello-finance && uv python pin 3.12"),
            ("Add the market-data and analysis dependencies. uv resolves and locks them into pyproject.toml and uv.lock.", "uv add yfinance pandas"),
            ("Inspect the locked dependency tree — reproducibility is an audit requirement in financial services.", "uv tree"),
            ("PROMPT THE AI ASSISTANT (Colab Gemini / Cursor / Copilot chat) with: 'Write a Python script named env_check.py that prints the Python version, the installed yfinance and pandas versions, and then prints a numbered watchlist of these SGX tickers with their company names: D05.SI DBS, U11.SI UOB, O39.SI OCBC, Z74.SI Singtel, C38U.SI CapitaLand Integrated Commercial Trust. Use f-strings and no external API calls.' Save the generated code as env_check.py.", ""),
            ("REVIEW the AI output before running it: check that it imports only yfinance and pandas, makes no network call, and that all five tickers carry the correct .SI suffix. Correct anything the assistant got wrong.", ""),
            ("Run the script inside the uv-managed environment.", "uv run python env_check.py"),
            ("Record in your lab notes one thing the AI assistant got wrong or left out — this habit of verification is the core discipline of AI-assisted development in a regulated environment.", ""),
        ],
        test="`uv run python env_check.py` prints the Python version, the yfinance and pandas versions, and all five SGX tickers with their company names, with no traceback.",
    ),
    dict(
        num=2,
        topic=1,
        title="Hello World — Your First Finance Script",
        objective="LO1: Translate a simple business requirement in financial services into a Python programming objective and execute the resulting script.",
        desc=(
            "The learner writes and runs the classic first program, then immediately upgrades it into a "
            "finance-relevant script: a trading-desk banner that prints the desk name, the reporting "
            "currency, the valuation date and a formatted portfolio value. The lab establishes the "
            "prompt-review-test cycle used for every later lab."
        ),
        build="A script `hello_finance.py` that prints a formatted trading-desk banner with a currency-formatted portfolio value.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create and enter the project for this lab.", "uv init lab-02-hello-world && cd lab-02-hello-world"),
            ("Create hello_finance.py containing the single classic line, then run it to prove the toolchain works end to end.", "print('hello world')"),
            ("Execute the script with uv.", "uv run python hello_finance.py"),
            ("Now state the business requirement: the SGD equities desk wants every report to open with a banner showing the desk name, base currency, valuation date and total portfolio value in SGD to two decimal places with thousands separators.", ""),
            ("Add the variables by hand so you understand what the AI will later generate.", "desk = 'SGD Equities Desk'; base_ccy = 'SGD'; portfolio_value = 12487650.75"),
            ("Print the banner using an f-string with currency formatting.", "print(f'{desk} | {base_ccy} | Portfolio Value: ${portfolio_value:,.2f}')"),
            ("PROMPT THE AI ASSISTANT with: 'Refactor hello_finance.py so it prints a bordered banner 60 characters wide. The banner must show the desk name, base currency SGD, today's valuation date from datetime, and the portfolio value formatted with a dollar sign, thousands separators and two decimals. Use only the standard library.' Apply the generated code.", ""),
            ("REVIEW the AI output: confirm it uses datetime.date.today() rather than a hard-coded date, that the currency format is ,.2f and not .2f, and that no third-party import was added.", ""),
            ("Run the refactored script and check the alignment of the banner.", "uv run python hello_finance.py"),
            ("Change portfolio_value to 0.0 and to 1234567890.12 and re-run — confirm the formatting holds at both extremes.", "uv run python hello_finance.py"),
        ],
        test="The script prints a bordered banner showing the desk name, SGD, today's date and the portfolio value as $12,487,650.75 — with the comma separators and exactly two decimal places.",
    ),
    dict(
        num=3,
        topic=1,
        title="CPF Contribution Calculator",
        objective="LO1: Translate the CPF contribution business rules into a Python programming objective and implement them as a working script.",
        desc=(
            "Mirroring the reference notebook activity, the learner builds a CPF calculator that applies "
            "the age-banded employee and employer contribution rates against the Ordinary Wage ceiling, "
            "then hardens it with input validation and a formatted contribution breakdown suitable for a "
            "payroll report."
        ),
        build="A script `cpf_calculator.py` that takes a monthly salary and age and prints the employee, employer and total CPF contribution with the wage ceiling applied.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project.", "uv init lab-03-cpf-calculator && cd lab-03-cpf-calculator"),
            ("Write the business rules in plain English first: rates are banded by age (55 and below, 56–60, 61–65, 66–70, above 70); the Ordinary Wage ceiling caps the contributable salary at $6,800.", ""),
            ("Create cpf_calculator.py and define the function signature and the age bands.", "def calculate_cpf(salary, age):"),
            ("Implement the age-banded rates with if/elif — employee and employer rate as a pair.", "if age <= 55: emp_rate, emr_rate = 0.20, 0.17"),
            ("Apply the Ordinary Wage ceiling before computing any contribution.", "capped_salary = min(salary, 6800)"),
            ("Return the three figures the payroll report needs.", "return capped_salary * emp_rate, capped_salary * emr_rate, capped_salary * (emp_rate + emr_rate)"),
            ("Collect the inputs and print the breakdown to two decimal places.", "sal = float(input('Enter monthly salary: ')); age = int(input('Enter age: '))"),
            ("Run it with a salary of 5000 and age 30, then with 9000 and age 30 to see the ceiling bite.", "uv run python cpf_calculator.py"),
            ("PROMPT THE AI ASSISTANT with: 'Harden cpf_calculator.py. Reject a negative or non-numeric salary and an age below 16 or above 100 with a clear message instead of a traceback. Print the capped salary alongside the raw salary so the user can see when the $6,800 Ordinary Wage ceiling was applied, and format every amount as $x,xxx.xx. Keep calculate_cpf a pure function that returns three values.' Apply the generated code.", ""),
            ("REVIEW the AI output: verify the rate bands were not altered, that min(salary, 6800) is still applied before the rate, and that the totals still equal employee + employer.", ""),
            ("Test the edge cases: salary 0, salary 20000, age 56, age 71, and a non-numeric salary such as 'abc'.", "uv run python cpf_calculator.py"),
        ],
        test="A salary of 9000 at age 30 returns an employee contribution of $1,360.00, an employer contribution of $1,156.00 and a total of $2,516.00 — proving the $6,800 ceiling was applied. Entering 'abc' as the salary prints a friendly message, not a traceback.",
    ),
    dict(
        num=4,
        topic=1,
        title="From Business Requirement to Programming Objective — SGX Price Fetcher",
        objective="LO1: Translate a financial services business requirement into a programming objective and set up an AI-assisted Python environment that fetches live SGX market data.",
        desc=(
            "The learner practises the requirement-to-objective translation that opens every real project: "
            "a written business requirement from a wealth desk is decomposed into inputs, processing, "
            "outputs and acceptance criteria, then implemented as a first live market-data script using "
            "yfinance against the SGX tickers used throughout the course."
        ),
        build="A requirements note plus `sgx_prices.py`, which fetches and prints the latest close for DBS, UOB, OCBC, Singtel and CapitaLand.",
        services="uv, Python 3.12, yfinance, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project and add the market-data dependency.", "uv init lab-04-sgx-prices && cd lab-04-sgx-prices && uv add yfinance"),
            ("Read the business requirement aloud: 'Each morning the wealth desk needs the previous close of our five core SGX holdings, in SGD, on one screen, so advisers can brief clients before the market opens.'", ""),
            ("Decompose it in a plain-text file requirements.md under four headings — INPUTS (the five tickers), PROCESSING (fetch last close), OUTPUTS (ticker, name, close price), ACCEPTANCE CRITERIA (all five print, two decimals, no crash if one ticker fails).", ""),
            ("Define the watchlist in Python as the programming objective's input.", "tickers = ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'C38U.SI']"),
            ("Fetch one ticker manually first to see the shape of the data before automating.", "uv run python -c \"import yfinance as yf; print(yf.Ticker('D05.SI').history(period='5d')['Close'])\""),
            ("PROMPT THE AI ASSISTANT with: 'Write sgx_prices.py. For each ticker in D05.SI, U11.SI, O39.SI, Z74.SI, C38U.SI use yfinance to fetch the most recent closing price and the short name. Print one aligned row per ticker showing the ticker, the company name and the close formatted as SGD with two decimals. If a ticker returns no data, print NO DATA for that row and continue to the next ticker.' Save the result.", ""),
            ("REVIEW the AI output against your acceptance criteria: does it handle the empty-data case, does it continue after a failure, and does it format to two decimals?", ""),
            ("Run the script.", "uv run python sgx_prices.py"),
            ("Introduce a deliberately invalid ticker such as 'ZZZZ.SI' into the list and re-run to prove the acceptance criterion about failure is genuinely met.", "uv run python sgx_prices.py"),
            ("Discuss: which of your four headings did the AI get right without being told, and which did you have to specify? This is the difference between a prompt and a requirement.", ""),
        ],
        test="`uv run python sgx_prices.py` prints five aligned rows with company names and SGD closing prices to two decimal places, and prints NO DATA rather than crashing when the invalid ticker is included.",
    ),
]
