# Lab 29 — Exceptions vs Syntax Errors in a Price Loader

**Topic 5: Error Handling Using Exception**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO4: Distinguish an exception from a syntax error and read a Python traceback for a financial script.

## Goal

The learner builds a small closing-price loader that contains, in turn, a deliberate syntax error and a deliberate runtime exception. By running both versions under uv the learner sees that a syntax error stops the interpreter before a single line executes, while an exception occurs mid-flight and leaves a traceback pointing at the failing line. The learner then pastes the traceback into an AI assistant and asks it to explain and fix the fault, comparing the AI's diagnosis with their own reading of the traceback.

## What you'll build

A uv project `lab-29-exception-basics` containing price_loader.py, a captured traceback file traceback.txt, and a short written comparison of syntax errors versus exceptions.

**Tools:** uv, Python 3.12, VS Code / Cursor, AI coding assistant

## Step-by-step

1. Create and enter the uv project for this lab.

   ```bash
   uv init lab-29-exception-basics && cd lab-29-exception-basics
   ```

2. Create price_loader.py holding a dict of closing prices for AAPL, MSFT and DBS, and a function get_price(ticker) that returns prices[ticker].

   ```bash
   touch price_loader.py
   ```

3. Introduce a deliberate SYNTAX error — remove the colon from the `def get_price(ticker)` line — then run the script and record what Python reports.

   ```bash
   uv run python price_loader.py
   ```

4. Discuss: the interpreter printed `SyntaxError: expected ':'` and NO other output ran. A syntax error is found at parse time, so the program never starts. Nothing can catch it.
5. Restore the colon, then trigger a RUNTIME exception by calling get_price('LEHMAN') for a ticker that is not in the dict. Run again and capture the full traceback to a file.

   ```bash
   uv run python price_loader.py 2> traceback.txt; cat traceback.txt
   ```

6. Discuss: this time the earlier print statements DID run before the KeyError appeared. An exception happens during execution, is raised at a specific line, and can be caught.
7. AI STEP — paste the captured traceback into your AI assistant with this prompt: "Here is a Python traceback from my stock price loader: <paste traceback.txt>. Explain in plain English what KeyError means here, which line raised it, and show me the smallest correct fix using try/except that returns None for an unknown ticker."
8. Review the AI's answer critically: check that it catches KeyError specifically and NOT a bare `except:`, then apply the fix to price_loader.py.
9. Re-run the fixed script and confirm the unknown ticker is now reported gracefully while the known tickers still print their prices.

   ```bash
   uv run python price_loader.py
   ```

10. Write a three-line comment block at the top of price_loader.py summarising the difference between a syntax error and an exception in your own words.

## Test it

Running `uv run python price_loader.py` exits with status 0, prints prices for AAPL, MSFT and DBS, and prints a friendly 'ticker LEHMAN not found' message instead of crashing. traceback.txt contains the original KeyError trace for reference.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
