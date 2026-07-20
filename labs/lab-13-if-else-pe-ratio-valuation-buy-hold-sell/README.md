# Lab 13 — If-Else PE Ratio Valuation — BUY / HOLD / SELL

**Topic 3: Problem Solving with Control Structures**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO2: Apply control structures to classify a stock's valuation and produce a BUY / HOLD / SELL recommendation from its PE ratio.

## Goal

You encode the first investment rule of the course as Python conditional logic. A PE ratio below 15 is treated as Undervalued (Consider Buying), 15 to 25 as Fairly Valued (Hold), and above 25 as Overvalued (Consider Selling). You start from an if-else skeleton, extend it to a full if-elif-else ladder, then harden it so a negative or non-numeric PE ratio is rejected instead of silently producing a BUY signal on a loss-making company.

## What you'll build

pe_valuation.py — a uv-managed script that reads a PE ratio and prints a formatted valuation and recommendation, with input validation.

**Tools:** uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

## Step-by-step

1. Create and enter the uv project for this lab.

   ```bash
   uv init lab-13-pe-valuation && cd lab-13-pe-valuation
   ```

2. Confirm uv pinned a Python 3.12 interpreter for the project.

   ```bash
   uv run python --version
   ```

3. Create the script file that will hold your valuation rule.

   ```bash
   touch pe_valuation.py
   ```

4. Write a simple two-branch if-else first: PE below 15 prints 'Undervalued', otherwise 'Overvalued'. Read the PE ratio with float(input("Enter the stock's PE Ratio: ")).
5. Run it and try PE = 12 then PE = 30 to see both branches fire.

   ```bash
   uv run python pe_valuation.py
   ```

6. Extend the two-branch version into a three-branch if / elif / else ladder: PE < 15 gives Undervalued + 'Consider Buying'; 15 <= PE <= 25 gives Fairly Valued + 'Hold'; else Overvalued + 'Consider Selling'.
7. Format the output with f-strings so it reads as an analyst note: print the PE ratio to 2 decimals, then the valuation, then the recommendation on separate lines.

   ```bash
   uv run python pe_valuation.py
   ```

8. AI-ASSIST: in Colab's Gemini panel (or Cursor / Copilot) prompt: "Rewrite this PE ratio valuation script so it validates the input — reject a negative PE ratio with a clear message because a negative PE means the company is loss-making, and reject non-numeric input using try/except ValueError. Keep the if-elif-else structure." Read every line of the generated code before you accept it.
9. Paste the AI-generated version into pe_valuation.py, then test the edge cases it claims to handle: -5, the string 'abc', and exactly 15 and exactly 25 (the boundary values).

   ```bash
   uv run python pe_valuation.py
   ```

10. Discuss: the boundary PE = 25 falls in 'Hold' because the condition uses <=. Change it to < and re-run with 25 to see the recommendation flip — a one-character change that alters a trading signal.
11. Add a short comment block at the top of the script naming the source of the 15 and 25 thresholds, so a reviewer knows the rule is a documented policy and not a magic number.

## Test it

Run `uv run python pe_valuation.py` five times with PE = 12, 15, 20, 25 and 30. You should see Undervalued/Buy, Fairly Valued/Hold, Fairly Valued/Hold, Fairly Valued/Hold and Overvalued/Sell. Entering -5 or 'abc' must print a validation message instead of a recommendation.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
