# Lab 33 — Else, Finally and a Custom InsufficientDataError for a Risk Model

**Topic 5: Error Handling Using Exception**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO4: Use the else and finally clauses and raise a custom exception to enforce a data-sufficiency rule in a risk model.

## Goal

A volatility model computed from four price observations is not a risk estimate — it is noise. The learner defines a custom InsufficientDataError, raises it when a price history is shorter than the model's minimum window, and structures the calculation with the full try / except / else / finally form: else runs the downstream risk write-up only when no exception occurred, and finally always closes the simulated API connection and appends a line to an audit log — the behaviour a regulator expects to see evidenced.

## What you'll build

A uv project `lab-33-risk-guard` with risk_model.py defining InsufficientDataError, a guarded compute_volatility(), and audit.log recording every run whether it succeeded or failed.

**Tools:** uv, pandas, numpy, AI coding assistant

## Step-by-step

1. Create the project and add the numeric dependencies.

   ```bash
   uv init lab-33-risk-guard && cd lab-33-risk-guard && uv add pandas numpy
   ```

2. In risk_model.py define `class InsufficientDataError(Exception)` with a docstring stating it is raised when a price history is too short for a reliable risk estimate.

   ```bash
   touch risk_model.py
   ```

3. Write compute_volatility(prices, min_obs=30) that raises InsufficientDataError with a message naming the actual and required observation counts when len(prices) < min_obs, and otherwise returns the annualised standard deviation of daily returns.
4. Write a fake connection object with open() and close() methods that print their action, to stand in for a market-data API session.
5. Assemble the full structure: try (open connection, compute volatility) / except InsufficientDataError (print the reason, mark the run FAILED) / else (print the volatility and the risk band, mark the run OK) / finally (close the connection and append a timestamped line to audit.log).
6. Run the model against a 250-day series and confirm the else branch executes.

   ```bash
   uv run python risk_model.py
   ```

7. Run it again against a 12-day series and confirm the custom exception is caught, the else branch is skipped, and the connection is STILL closed.

   ```bash
   uv run python risk_model.py --short
   ```

8. Inspect the audit log and confirm both runs are recorded with their outcome.

   ```bash
   cat audit.log
   ```

9. Discuss: finally ran in both the success and failure paths. Without it, a failed model run would leak the API session and leave no audit trail — the failure that is invisible is the one that gets you sanctioned.
10. AI STEP — prompt your AI assistant: "Review this Python risk model. I use a custom InsufficientDataError plus try/except/else/finally. Suggest two more domain-specific exceptions a volatility model should raise (for example on stale or non-numeric prices), show the class definitions, and explain when a custom exception is better than reusing ValueError."
11. Implement one of the AI's suggested exceptions yourself, add a test case that triggers it, and confirm audit.log still records the run.

   ```bash
   uv run python risk_model.py --stale
   ```


## Test it

All three runs (normal, short history, stale prices) finish without an uncaught traceback, 'connection closed' prints every time, and audit.log contains one timestamped OK/FAILED line per run.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
