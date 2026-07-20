"""
Topic 5 — Error Handling Using Exception.

Hands-on activities (labs 29-34) for domain 5 of "AI Assisted Python Programming
for Finance". Every lab is finance-oriented and maps to LO4: implement error
handling to build robust financial programs that survive missing, zero or
malformed market data.

Tooling: uv (uv init / uv add / uv run) — never pip or venv.
"""

DOMAIN5 = [
    dict(
        num=29,
        topic=5,
        title="Exceptions vs Syntax Errors in a Price Loader",
        objective="LO4: Distinguish an exception from a syntax error and read a Python traceback for a financial script.",
        desc=(
            "The learner builds a small closing-price loader that contains, in turn, a deliberate "
            "syntax error and a deliberate runtime exception. By running both versions under uv the "
            "learner sees that a syntax error stops the interpreter before a single line executes, "
            "while an exception occurs mid-flight and leaves a traceback pointing at the failing line. "
            "The learner then pastes the traceback into an AI assistant and asks it to explain and fix "
            "the fault, comparing the AI's diagnosis with their own reading of the traceback."
        ),
        build=(
            "A uv project `lab-29-exception-basics` containing price_loader.py, a captured traceback "
            "file traceback.txt, and a short written comparison of syntax errors versus exceptions."
        ),
        services="uv, Python 3.12, VS Code / Cursor, AI coding assistant",
        steps=[
            ("Create and enter the uv project for this lab.",
             "uv init lab-29-exception-basics && cd lab-29-exception-basics"),
            ("Create price_loader.py holding a dict of closing prices for AAPL, MSFT and DBS, and a "
             "function get_price(ticker) that returns prices[ticker].",
             "touch price_loader.py"),
            ("Introduce a deliberate SYNTAX error — remove the colon from the `def get_price(ticker)` "
             "line — then run the script and record what Python reports.",
             "uv run python price_loader.py"),
            ("Discuss: the interpreter printed `SyntaxError: expected ':'` and NO other output ran. A "
             "syntax error is found at parse time, so the program never starts. Nothing can catch it.",
             ""),
            ("Restore the colon, then trigger a RUNTIME exception by calling get_price('LEHMAN') for a "
             "ticker that is not in the dict. Run again and capture the full traceback to a file.",
             "uv run python price_loader.py 2> traceback.txt; cat traceback.txt"),
            ("Discuss: this time the earlier print statements DID run before the KeyError appeared. An "
             "exception happens during execution, is raised at a specific line, and can be caught.",
             ""),
            ("AI STEP — paste the captured traceback into your AI assistant with this prompt: "
             "\"Here is a Python traceback from my stock price loader: <paste traceback.txt>. Explain "
             "in plain English what KeyError means here, which line raised it, and show me the "
             "smallest correct fix using try/except that returns None for an unknown ticker.\"",
             ""),
            ("Review the AI's answer critically: check that it catches KeyError specifically and NOT a "
             "bare `except:`, then apply the fix to price_loader.py.",
             ""),
            ("Re-run the fixed script and confirm the unknown ticker is now reported gracefully while "
             "the known tickers still print their prices.",
             "uv run python price_loader.py"),
            ("Write a three-line comment block at the top of price_loader.py summarising the difference "
             "between a syntax error and an exception in your own words.",
             ""),
        ],
        test=(
            "Running `uv run python price_loader.py` exits with status 0, prints prices for AAPL, MSFT "
            "and DBS, and prints a friendly 'ticker LEHMAN not found' message instead of crashing. "
            "traceback.txt contains the original KeyError trace for reference."
        ),
    ),
    dict(
        num=30,
        topic=5,
        title="Try/Except on a Failing Market-Data Fetch",
        objective="LO4: Wrap a live market-data call in try/except so a delisted or invalid ticker does not halt the pipeline.",
        desc=(
            "The learner writes a market-data fetcher that downloads recent closing prices for a "
            "watchlist using yfinance. One entry in the watchlist is a delisted or misspelled ticker "
            "that returns an empty frame. The learner catches the failure per ticker so the remaining "
            "instruments are still processed, and separates a network/API exception from an "
            "empty-result condition — a distinction that matters when a batch job runs unattended "
            "overnight."
        ),
        build=(
            "A uv project `lab-30-market-fetch` with fetch_prices.py that returns a summary dict of "
            "successful tickers and a separate list of failed tickers with the reason for each failure."
        ),
        services="uv, yfinance, pandas, AI coding assistant",
        steps=[
            ("Create the uv project and add the market-data dependencies.",
             "uv init lab-30-market-fetch && cd lab-30-market-fetch && uv add yfinance pandas"),
            ("Write fetch_prices.py with WATCHLIST = ['AAPL', 'MSFT', 'ENRNQ', 'D05.SI'] — ENRNQ is a "
             "delisted ticker that will return no data.",
             "touch fetch_prices.py"),
            ("Write a naive loop with no error handling that calls yf.download(t, period='5d') and "
             "prints the last close for each ticker. Run it and observe the failure.",
             "uv run python fetch_prices.py"),
            ("Discuss: the delisted ticker produced an empty DataFrame, so `df['Close'].iloc[-1]` "
             "raised IndexError and the loop died BEFORE reaching D05.SI. One bad symbol silently cost "
             "you the rest of the watchlist.",
             ""),
            ("Refactor the loop so each ticker is fetched inside its own try/except. Catch IndexError "
             "and KeyError for empty data, and catch Exception as a last resort for network/API faults, "
             "appending (ticker, reason) to a failures list.",
             ""),
            ("Run the fixed script and confirm every good ticker is priced and the bad one is reported.",
             "uv run python fetch_prices.py"),
            ("AI STEP — prompt your AI assistant: \"Review this Python function that fetches prices "
             "with yfinance inside a try/except. Is catching bare Exception acceptable here for an "
             "overnight batch job? Suggest more specific exception types and show how to log the "
             "failing ticker with the traceback so an analyst can debug it the next morning.\"",
             ""),
            ("Apply the AI's logging suggestion, but verify yourself that a genuine bug (for example a "
             "typo in a column name) is still visible rather than swallowed by the broad handler.",
             ""),
            ("Add a summary print at the end: how many tickers succeeded, how many failed, and the "
             "reason for each failure.",
             "uv run python fetch_prices.py"),
            ("Discuss: why the pipeline must record which tickers were skipped — a portfolio valuation "
             "computed from three of four holdings is wrong, not merely incomplete.",
             ""),
        ],
        test=(
            "The script completes without crashing, prints a latest close for AAPL, MSFT and D05.SI, "
            "and ends with a failure report naming ENRNQ and its reason. Exit status is 0."
        ),
    ),
    dict(
        num=31,
        topic=5,
        title="ZeroDivisionError in an ROE and Ratio Calculator",
        objective="LO4: Handle ZeroDivisionError and TypeError in financial ratio calculations where the denominator can legitimately be zero.",
        desc=(
            "Return on Equity divides net income by shareholders' equity — and a distressed company can "
            "report zero or negative equity, which makes the ratio undefined rather than merely large. "
            "The learner builds a ratio calculator covering ROE, net profit margin and debt-to-equity, "
            "then hardens it against a zero denominator and against a None value arriving from an "
            "incomplete fundamentals feed. The lab makes the key point that returning 0.0 for an "
            "undefined ratio is a data-quality lie; returning None and flagging it is correct."
        ),
        build=(
            "A uv project `lab-31-roe-guard` with ratios.py exposing safe_roe(), safe_margin() and "
            "safe_debt_to_equity(), all returning None with a printed warning when the ratio is undefined."
        ),
        services="uv, Python 3.12, AI coding assistant",
        steps=[
            ("Create the uv project for the ratio calculator.",
             "uv init lab-31-roe-guard && cd lab-31-roe-guard"),
            ("Write ratios.py with an unguarded roe(net_income, equity) that simply returns "
             "net_income / equity, plus a COMPANIES list containing one firm with equity = 0 and one "
             "with equity = None.",
             "touch ratios.py"),
            ("Run the script over the company list and observe it crash on the zero-equity firm.",
             "uv run python ratios.py"),
            ("Discuss: ZeroDivisionError is not a bug in your code — it is the data telling you the "
             "ratio has no meaning. A company with zero book equity has an undefined ROE.",
             ""),
            ("Rewrite roe() as safe_roe() with try/except catching ZeroDivisionError (return None, warn "
             "'undefined: zero equity') and TypeError (return None, warn 'missing equity value').",
             ""),
            ("Add safe_margin(net_income, revenue) and safe_debt_to_equity(debt, equity) using the same "
             "guarded pattern, and run over all companies.",
             "uv run python ratios.py"),
            ("AI STEP — prompt your AI assistant: \"I have three financial ratio functions that each "
             "repeat the same try/except for ZeroDivisionError and TypeError. Refactor them into one "
             "reusable safe_divide(numerator, denominator, label) helper that returns None and logs a "
             "warning, and rewrite the three ratios to use it. Keep the warning text specific to each "
             "ratio.\"",
             ""),
            ("Test the AI's safe_divide against a negative-equity firm (equity = -500000). Decide as a "
             "class whether a negative denominator should return a number or a flag, and justify the "
             "choice in a comment.",
             ""),
            ("Print a final table of every company with its three ratios, showing 'n/a' where the "
             "result is None.",
             "uv run python ratios.py"),
            ("Discuss: why silently substituting 0.0 for an undefined ROE would corrupt a downstream "
             "screening model that ranks companies by ROE.",
             ""),
        ],
        test=(
            "`uv run python ratios.py` prints a ratio table for every company, shows 'n/a' for the "
            "zero-equity and None-equity firms with a warning line for each, and never raises."
        ),
    ),
    dict(
        num=32,
        topic=5,
        title="KeyError and ValueError in a Portfolio Input Handler",
        objective="LO4: Catch KeyError for a missing portfolio holding and ValueError for malformed user input, using multiple except branches.",
        desc=(
            "The learner builds an interactive portfolio lookup and loan-amount entry tool. Querying a "
            "ticker that is not in the holdings dictionary raises KeyError; typing '1,000,000' or "
            "'fifty thousand' into a loan-amount prompt raises ValueError from int(). The learner "
            "writes a single try block with multiple except branches, then adds an input-validation "
            "loop that re-prompts until the value is usable — the standard pattern for any "
            "customer-facing finance form."
        ),
        build=(
            "A uv project `lab-32-portfolio-input` with portfolio_tool.py providing a resilient ticker "
            "lookup and a validated loan-amount prompt that never crashes on bad input."
        ),
        services="uv, Python 3.12, AI coding assistant",
        steps=[
            ("Create the uv project.",
             "uv init lab-32-portfolio-input && cd lab-32-portfolio-input"),
            ("Write portfolio_tool.py with PORTFOLIO = {'AAPL': 120, 'MSFT': 80, 'D05.SI': 500} and an "
             "unguarded lookup that prints PORTFOLIO[ticker] for a ticker typed by the user.",
             "touch portfolio_tool.py"),
            ("Run it and enter 'TSLA', a ticker you do not hold, to trigger KeyError.",
             "uv run python portfolio_tool.py"),
            ("Add a second unguarded prompt: amount = int(input('Loan amount: ')). Run it and enter "
             "'1,000,000' to trigger ValueError.",
             "uv run python portfolio_tool.py"),
            ("Discuss: KeyError says the key is absent from the mapping; ValueError says the type is "
             "right but the content is not convertible. They need different messages to the user.",
             ""),
            ("Wrap the lookup in try/except KeyError, printing 'You do not hold TSLA — holdings are: "
             "AAPL, MSFT, D05.SI' and continuing. Verify with a held and an unheld ticker.",
             "uv run python portfolio_tool.py"),
            ("Wrap the loan prompt in a while True loop with try/except ValueError that re-prompts "
             "until a valid positive integer is entered, and also rejects zero or negative amounts.",
             "uv run python portfolio_tool.py"),
            ("AI STEP — prompt your AI assistant: \"Here is my Python input handler for a loan "
             "application form. Rewrite it so it accepts amounts typed with commas or a currency "
             "symbol like 'S$250,000', still raises ValueError for genuinely invalid text, and caps "
             "the number of retries at three before exiting with a clear message.\"",
             ""),
            ("Test the AI-generated parser against the awkward cases yourself: '250000', 'S$250,000', "
             "'-5000', '0', 'abc' and an empty string. Fix anything the AI got wrong.",
             ""),
            ("Discuss: why `.get(ticker, default)` is often better than try/except KeyError for a "
             "dictionary, and when the explicit exception is still the clearer choice.",
             ""),
        ],
        test=(
            "The tool survives every input in the test set: unknown tickers produce a helpful holdings "
            "list, malformed amounts re-prompt, and a valid amount is echoed back formatted as currency. "
            "The script never terminates with a traceback."
        ),
    ),
    dict(
        num=33,
        topic=5,
        title="Else, Finally and a Custom InsufficientDataError for a Risk Model",
        objective="LO4: Use the else and finally clauses and raise a custom exception to enforce a data-sufficiency rule in a risk model.",
        desc=(
            "A volatility model computed from four price observations is not a risk estimate — it is "
            "noise. The learner defines a custom InsufficientDataError, raises it when a price history "
            "is shorter than the model's minimum window, and structures the calculation with the full "
            "try / except / else / finally form: else runs the downstream risk write-up only when no "
            "exception occurred, and finally always closes the simulated API connection and appends a "
            "line to an audit log — the behaviour a regulator expects to see evidenced."
        ),
        build=(
            "A uv project `lab-33-risk-guard` with risk_model.py defining InsufficientDataError, a "
            "guarded compute_volatility(), and audit.log recording every run whether it succeeded or failed."
        ),
        services="uv, pandas, numpy, AI coding assistant",
        steps=[
            ("Create the project and add the numeric dependencies.",
             "uv init lab-33-risk-guard && cd lab-33-risk-guard && uv add pandas numpy"),
            ("In risk_model.py define `class InsufficientDataError(Exception)` with a docstring stating "
             "it is raised when a price history is too short for a reliable risk estimate.",
             "touch risk_model.py"),
            ("Write compute_volatility(prices, min_obs=30) that raises InsufficientDataError with a "
             "message naming the actual and required observation counts when len(prices) < min_obs, "
             "and otherwise returns the annualised standard deviation of daily returns.",
             ""),
            ("Write a fake connection object with open() and close() methods that print their action, "
             "to stand in for a market-data API session.",
             ""),
            ("Assemble the full structure: try (open connection, compute volatility) / except "
             "InsufficientDataError (print the reason, mark the run FAILED) / else (print the "
             "volatility and the risk band, mark the run OK) / finally (close the connection and append "
             "a timestamped line to audit.log).",
             ""),
            ("Run the model against a 250-day series and confirm the else branch executes.",
             "uv run python risk_model.py"),
            ("Run it again against a 12-day series and confirm the custom exception is caught, the else "
             "branch is skipped, and the connection is STILL closed.",
             "uv run python risk_model.py --short"),
            ("Inspect the audit log and confirm both runs are recorded with their outcome.",
             "cat audit.log"),
            ("Discuss: finally ran in both the success and failure paths. Without it, a failed model run "
             "would leak the API session and leave no audit trail — the failure that is invisible is "
             "the one that gets you sanctioned.",
             ""),
            ("AI STEP — prompt your AI assistant: \"Review this Python risk model. I use a custom "
             "InsufficientDataError plus try/except/else/finally. Suggest two more domain-specific "
             "exceptions a volatility model should raise (for example on stale or non-numeric prices), "
             "show the class definitions, and explain when a custom exception is better than reusing "
             "ValueError.\"",
             ""),
            ("Implement one of the AI's suggested exceptions yourself, add a test case that triggers it, "
             "and confirm audit.log still records the run.",
             "uv run python risk_model.py --stale"),
        ],
        test=(
            "All three runs (normal, short history, stale prices) finish without an uncaught traceback, "
            "'connection closed' prints every time, and audit.log contains one timestamped OK/FAILED "
            "line per run."
        ),
    ),
    dict(
        num=34,
        topic=5,
        title="Activity: Loan Risk Classifier with Guarded Data Loading",
        objective="LO4: Build an XGBoost multi-class credit-risk classifier whose data loading, feature selection and scoring are wrapped in exception handling that degrades gracefully.",
        desc=(
            "The capstone activity for Topic 5, from the reference slide. The learner trains an XGBoost "
            "multi-class credit-risk classifier on creditloandata.csv. The loader is wrapped in "
            "try/except: if the CSV is absent or unreadable, the except branch generates a synthetic "
            "dataset of 120 mock records with income, debt-to-income and credit-score features and "
            "assigns risk labels 0/1/2 from a scoring function, so the model always trains. A second "
            "guard handles missing feature columns by dropping them and warning, rather than crashing. "
            "The model is evaluated with accuracy, a classification report, a Seaborn confusion-matrix "
            "heatmap and a multiclass ROC curve."
        ),
        build=(
            "A uv project `lab-34-loan-risk-classifier` with loan_risk.py, a synthetic-data fallback, a "
            "printed classification report, confusion_matrix.png and roc_curve.png."
        ),
        services="uv, pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, AI coding assistant",
        steps=[
            ("Create the project and add the modelling stack.",
             "uv init lab-34-loan-risk-classifier && cd lab-34-loan-risk-classifier && "
             "uv add pandas numpy scikit-learn xgboost matplotlib seaborn"),
            ("AI STEP — prompt your AI assistant with the full requirement: \"Write a Python script "
             "that trains an XGBoost multi-class classifier for credit risk. Wrap the data loading in "
             "try/except: try to read 'creditloandata.csv' with pandas; if FileNotFoundError or "
             "pandas.errors.EmptyDataError is raised, generate a synthetic dataset of 120 records with "
             "columns income, debt_to_income and credit_score, and assign risk labels 0, 1, 2 from a "
             "custom scoring function. Split 75/25 stratified, train XGBClassifier, then report "
             "accuracy, a classification_report, a Seaborn confusion-matrix heatmap and a multiclass "
             "ROC curve. Print clearly which data source was used.\"",
             ""),
            ("Save the generated code as loan_risk.py and READ IT before running — check the fallback "
             "actually produces three populated classes and that the except branch is not catching "
             "bare Exception.",
             "touch loan_risk.py"),
            ("Run the script with NO creditloandata.csv present and confirm the synthetic fallback path "
             "is taken and the model still trains.",
             "uv run python loan_risk.py"),
            ("Create a small real creditloandata.csv with the three feature columns and a risk column, "
             "re-run, and confirm the try branch is taken instead.",
             "uv run python loan_risk.py"),
            ("Add a THIRD guard: wrap feature selection in try/except KeyError so that if "
             "credit_score is missing from the CSV the script warns, drops that feature and trains on "
             "the remaining two rather than crashing.",
             ""),
            ("Test the missing-feature path by deleting the credit_score column from the CSV and "
             "re-running.",
             "uv run python loan_risk.py"),
            ("Discuss: the degraded two-feature model still produced a number. Is a silently degraded "
             "credit model acceptable? Agree as a class where the boundary sits between graceful "
             "degradation and a failure that must stop the run.",
             ""),
            ("Break the script deliberately — feed it a CSV whose risk column contains the string "
             "'high' instead of an integer — capture the resulting traceback, and paste it into your AI "
             "assistant with: \"Explain this traceback from my XGBoost credit risk script and give me "
             "the exception handler that converts the label column safely, raising a clear "
             "InvalidLabelError if the values cannot be mapped to 0, 1 or 2.\"",
             "uv run python loan_risk.py 2> traceback.txt"),
            ("Apply and test the AI's handler, then confirm the confusion-matrix heatmap and ROC curve "
             "are written to disk on a successful run.",
             "uv run python loan_risk.py && ls -la *.png"),
            ("Write a five-line 'error handling contract' comment at the top of loan_risk.py listing "
             "every exception the script handles and the business decision behind each response.",
             ""),
        ],
        test=(
            "The script runs to completion in all four scenarios — CSV present, CSV absent, feature "
            "column missing, label column malformed — never exits with an uncaught traceback, prints "
            "accuracy above 0.60 on the synthetic data, and writes confusion_matrix.png and roc_curve.png."
        ),
    ),
]
