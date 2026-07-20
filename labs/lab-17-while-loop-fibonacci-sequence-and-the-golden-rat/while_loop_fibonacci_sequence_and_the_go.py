"""Lab 17 — While Loop — Fibonacci Sequence and the Golden Ratio in Technical Analysis

Topic 3: Problem Solving with Control Structures
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply a while loop to generate a sequence that repeats until a condition is met, and use it to derive the Fibonacci retracement levels used in technical analysis.

Goal: Fibonacci retracement is one of the most widely used tools in technical analysis, and it rests on the golden ratio 1.618034 that successive Fibonacci numbers converge to. You generate the sequence with a while loop and multiple assignment (a, b = b, a + b), watch the ratio b/a converge, then apply the derived levels — 23.6%, 38.2%, 50%, 61.8% and 78.6% — to a real price swing to produce actual support and resistance prices. You also add the guard every while loop needs: a maximum iteration count so a bad condition cannot loop forever.

You will build: fibonacci_ta.py — generates the Fibonacci sequence with a while loop, shows golden-ratio convergence, and prints Fibonacci retracement price levels for a stock's swing high and low.
Tools: uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python while_loop_fibonacci_sequence_and_the_go.py
"""


def main():
    print("Lab 17: While Loop — Fibonacci Sequence and the Golden Ratio in Technical Analysis")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project.
    #   $ uv init lab-17-fibonacci-ta && cd lab-17-fibonacci-ta
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Warm up with a savings while loop: goal 5000, monthly deposit 450, balance
    # starting at 0. Loop while balance < goal, adding the deposit and counting
    # months, printing each month's balance. Confirm it terminates.
    #   $ uv run python fibonacci_ta.py
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Now build the Fibonacci generator: read n_terms with int(input('How many
    # terms? ')), set a, b = 0, 1 and count = 0, and loop while count < n_terms
    # appending a to a list.
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Inside the loop, use the multiple assignment a, b = b, a + b to advance
    # the sequence, and increment count. Print the finished sequence for 15
    # terms.
    #   $ uv run python fibonacci_ta.py
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Add ratio tracking: inside the loop, when a is not zero, append b / a to a
    # ratios list. Print the last five ratios to 6 decimal places alongside the
    # target golden ratio ~1.618034 and watch them converge.
    #   $ uv run python fibonacci_ta.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Explain in a comment why the `if a != 0` guard is required — the very
    # first term would otherwise raise ZeroDivisionError.
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Apply it to markets: set swing_high = 42.80 and swing_low = 31.20 for an
    # SGX bank. Compute the price range, then loop over the retracement levels
    # [0.236, 0.382, 0.5, 0.618, 0.786] and print swing_high - (range * level)
    # for each, formatted as ${:.2f}.
    #   $ uv run python fibonacci_ta.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # Note in a comment that 0.618 is 1/1.618034 and 0.382 is 0.618 squared —
    # the retracement grid is derived from the ratio your while loop just
    # converged to.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Add a safety guard to this while
    # loop so it can never run forever — cap it at a maximum of 500 iterations
    # and print a warning if the cap is hit. Also validate that n_terms is a
    # positive integer, and explain what happens today if the user enters 0 or a
    # negative number." Review and apply the guard.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Test the guard: enter 0 terms, then -5 terms, then 500 terms, and confirm
    # the script handles all three without hanging or crashing.
    #   $ uv run python fibonacci_ta.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Add a decision line: given a current price of 35.90, use an if-elif ladder
    # to report which two retracement levels the price currently sits between.
    #   $ uv run python fibonacci_ta.py
    # TODO: implement this step

    # ---- Step 12 ----------------------------------------------------------
    # Discuss: a while loop is the right choice here because you do not know in
    # advance how many terms are needed to converge. Name one financial task
    # where a for loop would be the better choice instead.
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python fibonacci_ta.py` and enter 15 terms. The sequence must
    # begin 0, 1, 1, 2, 3, 5, 8, 13 and the last printed ratios must be within
    # 0.0001 of 1.618034. The retracement block must print five price levels
    # between $31.20 and $42.80, with the 61.8% level at approximately $35.63.
    # Entering 0 or -5 must be rejected without hanging.


if __name__ == "__main__":
    main()
