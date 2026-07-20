"""
Topic 3 — Problem Solving with Control Structures (labs 13-20).

Hands-on activities for domain 3. Lab `num` is the GLOBAL contiguous lab number
(13..20); `topic` is 3. All labs are finance-focused (SGX / global markets) and
mirror the reference notebook activities: PE-ratio valuation, ROE screening,
income grouping, ternary decisions, Fibonacci & the golden ratio, ROA ranking,
enumerate/zip ROE+ROA tables, break/continue scanning, and comprehensions for
net profit margin. All labs are managed with uv (uv init / uv add / uv run).
"""

DOMAIN3 = [

    dict(
        num=13,
        topic=3,
        title="If-Else PE Ratio Valuation — BUY / HOLD / SELL",
        objective="LO2: Apply control structures to classify a stock's valuation and produce a BUY / HOLD / SELL recommendation from its PE ratio.",
        desc=(
            "You encode the first investment rule of the course as Python conditional logic. A PE ratio "
            "below 15 is treated as Undervalued (Consider Buying), 15 to 25 as Fairly Valued (Hold), and "
            "above 25 as Overvalued (Consider Selling). You start from an if-else skeleton, extend it to a "
            "full if-elif-else ladder, then harden it so a negative or non-numeric PE ratio is rejected "
            "instead of silently producing a BUY signal on a loss-making company."
        ),
        build="pe_valuation.py — a uv-managed script that reads a PE ratio and prints a formatted valuation and recommendation, with input validation.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create and enter the uv project for this lab.", "uv init lab-13-pe-valuation && cd lab-13-pe-valuation"),
            ("Confirm uv pinned a Python 3.12 interpreter for the project.", "uv run python --version"),
            ("Create the script file that will hold your valuation rule.", "touch pe_valuation.py"),
            ("Write a simple two-branch if-else first: PE below 15 prints 'Undervalued', otherwise 'Overvalued'. Read the PE ratio with float(input(\"Enter the stock's PE Ratio: \")).", ""),
            ("Run it and try PE = 12 then PE = 30 to see both branches fire.", "uv run python pe_valuation.py"),
            ("Extend the two-branch version into a three-branch if / elif / else ladder: PE < 15 gives Undervalued + 'Consider Buying'; 15 <= PE <= 25 gives Fairly Valued + 'Hold'; else Overvalued + 'Consider Selling'.", ""),
            ("Format the output with f-strings so it reads as an analyst note: print the PE ratio to 2 decimals, then the valuation, then the recommendation on separate lines.", "uv run python pe_valuation.py"),
            ("AI-ASSIST: in Colab's Gemini panel (or Cursor / Copilot) prompt: \"Rewrite this PE ratio valuation script so it validates the input — reject a negative PE ratio with a clear message because a negative PE means the company is loss-making, and reject non-numeric input using try/except ValueError. Keep the if-elif-else structure.\" Read every line of the generated code before you accept it.", ""),
            ("Paste the AI-generated version into pe_valuation.py, then test the edge cases it claims to handle: -5, the string 'abc', and exactly 15 and exactly 25 (the boundary values).", "uv run python pe_valuation.py"),
            ("Discuss: the boundary PE = 25 falls in 'Hold' because the condition uses <=. Change it to < and re-run with 25 to see the recommendation flip — a one-character change that alters a trading signal.", ""),
            ("Add a short comment block at the top of the script naming the source of the 15 and 25 thresholds, so a reviewer knows the rule is a documented policy and not a magic number.", ""),
        ],
        test="Run `uv run python pe_valuation.py` five times with PE = 12, 15, 20, 25 and 30. You should see Undervalued/Buy, Fairly Valued/Hold, Fairly Valued/Hold, Fairly Valued/Hold and Overvalued/Sell. Entering -5 or 'abc' must print a validation message instead of a recommendation.",
    ),

    dict(
        num=14,
        topic=3,
        title="Activity: Return on Equity (ROE) Screener with a BUY / SELL Threshold",
        objective="LO2: Apply conditional logic to a real SGX fundamental metric, computing ROE from live financial statements and converting it into an investment decision.",
        desc=(
            "You pull DBS Group Holdings (D05.SI) financials with yfinance, compute Return on Equity as "
            "Net Income divided by AVERAGE shareholders' equity, and apply a 15% threshold to generate a "
            "BUY or SELL signal. Using average equity (latest and prior year) rather than closing equity "
            "is the analyst convention, because net income is earned across the whole year. You also meet "
            "your first ZeroDivisionError risk: a company with zero or missing equity."
        ),
        build="roe_screener.py — computes ROE for D05.SI from live yfinance statements and prints a threshold-based BUY/SELL recommendation.",
        services="uv, yfinance, pandas, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project and add the market-data dependencies.", "uv init lab-14-roe-screener && cd lab-14-roe-screener && uv add yfinance pandas"),
            ("Check that uv recorded yfinance and pandas in pyproject.toml.", "uv run python -c \"import yfinance, pandas; print(yfinance.__version__, pandas.__version__)\""),
            ("Create roe_screener.py and fetch DBS: build a yf.Ticker('D05.SI') object, then read stock.financials into income_stmt and stock.balance_sheet into balance_sheet.", ""),
            ("Inspect the raw statements once so you know the row labels you are about to index — print income_stmt.index and balance_sheet.index.", "uv run python roe_screener.py"),
            ("Extract Net Income with income_stmt.loc['Net Income'].iloc[0] (iloc[0] is the most recent year), and extract Stockholders Equity for both .iloc[0] and .iloc[1].", ""),
            ("Compute avg_equity = (equity_latest + equity_prev) / 2, then roe = (net_income / avg_equity) * 100.", ""),
            ("Print a formatted report: company name and ticker, Net Income with thousands separators (${:,.0f}), Average Shareholders Equity, and ROE to 2 decimals with a percent sign.", "uv run python roe_screener.py"),
            ("Add the decision rule with if-else: ROE above 15% prints 'STRONG — Consider BUY', 10% to 15% prints 'MODERATE — HOLD', below 10% prints 'WEAK — Consider SELL'.", "uv run python roe_screener.py"),
            ("AI-ASSIST: prompt your AI tool with: \"This script divides net income by average shareholders equity. Add guards so it fails safely: raise or report a clear message if average equity is zero (ZeroDivisionError), if the 'Net Income' or 'Stockholders Equity' row is missing from the statement (KeyError), or if only one year of balance sheet data exists (IndexError). Do not swallow the error silently.\" Review the generated guards.", ""),
            ("Apply the guarded version and deliberately break it: change the ticker to a nonsense symbol such as 'ZZZZ.SI' and confirm the script reports a clear message rather than crashing with a traceback.", "uv run python roe_screener.py"),
            ("Wrap the whole calculation in a loop over three banks — D05.SI, U11.SI, O39.SI — so one run screens all three and prints one recommendation line each.", "uv run python roe_screener.py"),
            ("Discuss: why does using average equity instead of year-end equity matter most for a company that raised a lot of capital mid-year?", ""),
        ],
        test="Run `uv run python roe_screener.py`. You should see a Net Income figure, an Average Shareholders Equity figure and an ROE percentage for each of D05.SI, U11.SI and O39.SI, each followed by a BUY / HOLD / SELL line. Substituting an invalid ticker must produce a readable message, never an unhandled traceback.",
    ),

    dict(
        num=15,
        topic=3,
        title="If-Elif Income Grouping and Credit Risk Banding",
        objective="LO2: Apply a multi-branch if-elif-else ladder to classify bank customers into income bands and credit-risk categories.",
        desc=(
            "Retail banking runs on segmentation. You build a classifier that maps annual income into Low "
            "(below $30,000), Middle (up to $80,000), High (up to $150,000) and Super High Income bands, "
            "then a second classifier that maps a 300-850 credit score into Excellent / Good / Fair / Poor "
            "with the bank's stated lending posture for each. You will see why the ORDER of elif branches "
            "is load-bearing: reverse two of them and customers land in the wrong band."
        ),
        build="income_grouping.py — classifies annual income into four bands and a credit score into four risk categories, with range validation.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project for the segmentation lab.", "uv init lab-15-income-grouping && cd lab-15-income-grouping"),
            ("Create income_grouping.py and read the customer's annual income with float(input('Enter annual income: ')).", ""),
            ("Write the if-elif ladder: below 30000 is 'Low Income'; up to 80000 is 'Middle Income'; up to 150000 is 'High Income'; else 'Super High Income'.", ""),
            ("Print the result with formatting: income as ${:,.2f} and the classification on its own line.", "uv run python income_grouping.py"),
            ("Test the band boundaries deliberately: 29999.99, 30000, 80000, 150000 and 150000.01. Note which side of each boundary each value lands on.", "uv run python income_grouping.py"),
            ("BREAK IT ON PURPOSE: move the 'income <= 150000' branch above the 'income <= 80000' branch, re-run with 50000, and observe it now misclassifies as High Income. Restore the correct order and write one sentence explaining why elif order matters.", ""),
            ("Add the second classifier in the same script: read a credit score with int(input(...)) and band it — 800+ Excellent ('High probability of loan approval at best rates'), 700+ Good ('Likely approved with standard rates'), 600+ Fair ('May be approved with higher interest rates'), else Poor ('High risk; loan approval unlikely').", "uv run python income_grouping.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Add input validation to this banking classifier — reject a negative annual income, and reject any credit score outside the valid 300 to 850 range with a specific message naming the valid range. Use try/except to handle non-numeric input. Then refactor both classifiers into a single reusable function each.\" Review the generated functions before running them.", ""),
            ("Run the AI-refactored script and test the invalid paths: income of -1000, credit score of 250, credit score of 900, and the text 'seven hundred'.", "uv run python income_grouping.py"),
            ("Add a combined rule at the end: a customer in the High or Super High income band AND with a credit score of 700 or above is flagged 'PRIORITY WEALTH SEGMENT'. Use the logical `and` operator inside a single if.", "uv run python income_grouping.py"),
            ("Discuss: the bands here are hard-coded. What is the operational risk when the bank's segmentation policy changes and this rule is duplicated across five scripts?", ""),
        ],
        test="Run `uv run python income_grouping.py` and enter income 25000 / 55000 / 120000 / 250000 — you should get Low, Middle, High and Super High Income respectively. A credit score of 810 must return Excellent; 250 and 900 must both be rejected with a range message. Income 160000 with score 750 must print PRIORITY WEALTH SEGMENT.",
    ),

    dict(
        num=16,
        topic=3,
        title="Ternary Operator — One-Line Trading Decisions",
        objective="LO2: Apply the ternary conditional expression to write compact, readable one-line financial decision rules.",
        desc=(
            "The ternary operator collapses a four-line if-else into one expression: "
            "value_if_true if condition else value_if_false. You use it for a price-versus-target buy/wait "
            "decision, a margin-call check, a dividend-yield flag and a safe division that returns 0 "
            "instead of raising ZeroDivisionError. You then meet its limit — a nested ternary that is "
            "technically correct but unreadable — and learn when to go back to if-elif."
        ),
        build="ternary_decisions.py — a set of one-line ternary rules covering buy/wait, margin call, yield flagging and zero-safe division.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project.", "uv init lab-16-ternary-decisions && cd lab-16-ternary-decisions"),
            ("Create ternary_decisions.py. Set current_price = 145.50 and target_price = 150.00, then write decision = 'Buy' if current_price < target_price else 'Wait'.", ""),
            ("Print the current price, target price and decision, all formatted to 2 decimals.", "uv run python ternary_decisions.py"),
            ("Write the same rule the long way as a four-line if-else, print both results, and confirm they agree. Keep both in the file as a side-by-side comparison.", "uv run python ternary_decisions.py"),
            ("Add a margin-call ternary: given account_equity = 18000 and maintenance_margin = 20000, set status = 'MARGIN CALL' if account_equity < maintenance_margin else 'OK'.", ""),
            ("Add a zero-safe ternary — the pattern you will reuse all course: margin = (net_income / revenue) * 100 if revenue != 0 else 0. Test it with revenue = 0 and confirm no ZeroDivisionError.", "uv run python ternary_decisions.py"),
            ("Use a ternary inside an f-string to flag high-yield stocks: for a dividend yield of 5.8%, print a line ending in 'HIGH YIELD' if the yield exceeds 4 else 'STANDARD'.", "uv run python ternary_decisions.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Convert this PE-ratio if-elif-else ladder with three branches (Undervalued / Fairly Valued / Overvalued) into a nested ternary expression, then tell me honestly whether the nested version is more readable and when I should NOT use a ternary.\" Read the answer critically.", ""),
            ("Paste the nested ternary in, run it against PE values of 12, 20 and 30, and confirm it matches Lab 13's output. Then write a one-line comment recording your own judgement on readability.", "uv run python ternary_decisions.py"),
            ("Apply the ternary across a small portfolio: loop over the list [('D05.SI', 35.50), ('U11.SI', 28.40), ('O39.SI', 13.10)] with a target of 30.00 and print a Buy/Wait decision per ticker in an aligned table.", "uv run python ternary_decisions.py"),
            ("Discuss: a ternary always evaluates to a value, so it can sit inside a list comprehension or a function argument — where an if statement cannot. Name one place in your own code where that matters.", ""),
        ],
        test="Run `uv run python ternary_decisions.py`. The buy/wait decision must be 'Buy' (145.50 < 150.00), the margin status must be 'MARGIN CALL', the zero-revenue margin must print 0 with no traceback, and the portfolio table must show one Buy/Wait decision per ticker.",
    ),

    dict(
        num=17,
        topic=3,
        title="While Loop — Fibonacci Sequence and the Golden Ratio in Technical Analysis",
        objective="LO2: Apply a while loop to generate a sequence that repeats until a condition is met, and use it to derive the Fibonacci retracement levels used in technical analysis.",
        desc=(
            "Fibonacci retracement is one of the most widely used tools in technical analysis, and it rests "
            "on the golden ratio 1.618034 that successive Fibonacci numbers converge to. You generate the "
            "sequence with a while loop and multiple assignment (a, b = b, a + b), watch the ratio b/a "
            "converge, then apply the derived levels — 23.6%, 38.2%, 50%, 61.8% and 78.6% — to a real "
            "price swing to produce actual support and resistance prices. You also add the guard every "
            "while loop needs: a maximum iteration count so a bad condition cannot loop forever."
        ),
        build="fibonacci_ta.py — generates the Fibonacci sequence with a while loop, shows golden-ratio convergence, and prints Fibonacci retracement price levels for a stock's swing high and low.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project.", "uv init lab-17-fibonacci-ta && cd lab-17-fibonacci-ta"),
            ("Warm up with a savings while loop: goal 5000, monthly deposit 450, balance starting at 0. Loop while balance < goal, adding the deposit and counting months, printing each month's balance. Confirm it terminates.", "uv run python fibonacci_ta.py"),
            ("Now build the Fibonacci generator: read n_terms with int(input('How many terms? ')), set a, b = 0, 1 and count = 0, and loop while count < n_terms appending a to a list.", ""),
            ("Inside the loop, use the multiple assignment a, b = b, a + b to advance the sequence, and increment count. Print the finished sequence for 15 terms.", "uv run python fibonacci_ta.py"),
            ("Add ratio tracking: inside the loop, when a is not zero, append b / a to a ratios list. Print the last five ratios to 6 decimal places alongside the target golden ratio ~1.618034 and watch them converge.", "uv run python fibonacci_ta.py"),
            ("Explain in a comment why the `if a != 0` guard is required — the very first term would otherwise raise ZeroDivisionError.", ""),
            ("Apply it to markets: set swing_high = 42.80 and swing_low = 31.20 for an SGX bank. Compute the price range, then loop over the retracement levels [0.236, 0.382, 0.5, 0.618, 0.786] and print swing_high - (range * level) for each, formatted as ${:.2f}.", "uv run python fibonacci_ta.py"),
            ("Note in a comment that 0.618 is 1/1.618034 and 0.382 is 0.618 squared — the retracement grid is derived from the ratio your while loop just converged to.", ""),
            ("AI-ASSIST: prompt your AI tool with: \"Add a safety guard to this while loop so it can never run forever — cap it at a maximum of 500 iterations and print a warning if the cap is hit. Also validate that n_terms is a positive integer, and explain what happens today if the user enters 0 or a negative number.\" Review and apply the guard.", ""),
            ("Test the guard: enter 0 terms, then -5 terms, then 500 terms, and confirm the script handles all three without hanging or crashing.", "uv run python fibonacci_ta.py"),
            ("Add a decision line: given a current price of 35.90, use an if-elif ladder to report which two retracement levels the price currently sits between.", "uv run python fibonacci_ta.py"),
            ("Discuss: a while loop is the right choice here because you do not know in advance how many terms are needed to converge. Name one financial task where a for loop would be the better choice instead.", ""),
        ],
        test="Run `uv run python fibonacci_ta.py` and enter 15 terms. The sequence must begin 0, 1, 1, 2, 3, 5, 8, 13 and the last printed ratios must be within 0.0001 of 1.618034. The retracement block must print five price levels between $31.20 and $42.80, with the 61.8% level at approximately $35.63. Entering 0 or -5 must be rejected without hanging.",
    ),

    dict(
        num=18,
        topic=3,
        title="For Loop and Range — Top 10 SGX Return on Assets (ROA) Ranking",
        objective="LO2: Apply for loops and the range function to iterate a portfolio of tickers, compute Return on Assets for each, and rank the results.",
        desc=(
            "You iterate a list of ten major SGX tickers — DBS, UOB, OCBC, SingTel, Jardine, Keppel, "
            "Venture, CapitaLand Integrated, Ascendas REIT and City Developments — fetching Net Income and "
            "Total Assets for each and computing ROA = Net Income / Total Assets * 100. You then sort the "
            "results and print a ranked league table. Along the way you use range for a compound-growth "
            "projection and learn why a per-ticker try/except keeps a ten-stock scan alive when one "
            "ticker's data is missing."
        ),
        build="roa_ranking.py — fetches fundamentals for 10 SGX tickers in a for loop and prints a sorted Top 10 ROA league table.",
        services="uv, yfinance, pandas, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project and add market-data dependencies.", "uv init lab-18-roa-ranking && cd lab-18-roa-ranking && uv add yfinance pandas"),
            ("Warm up with range: in roa_ranking.py project a $1,000 principal at 5% for 10 years using `for year in range(1, years + 1)` and the formula principal * (1 + rate) ** year, printing each year-end balance.", "uv run python roa_ranking.py"),
            ("Define the ticker list: sgx_tickers = ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'J36.SI', 'BN4.SI', 'V03.SI', 'C38U.SI', 'A17U.SI', 'C07.SI'].", ""),
            ("Write the main for loop: for each ticker build a yf.Ticker object, read stock.financials and stock.balance_sheet, extract Net Income and Total Assets with .loc[...].iloc[0], compute ROA, and append a dict {'name', 'ticker', 'roa'} to a results list.", ""),
            ("Wrap the body of the loop in try/except so a single failing ticker prints a skip message and the loop continues to the next one instead of aborting the whole scan.", "uv run python roa_ranking.py"),
            ("Pull a readable company name with stock.info.get('shortName', ticker) — the .get default means a missing name falls back to the ticker rather than raising KeyError.", ""),
            ("Sort the results descending by ROA using sorted(results, key=lambda x: x['roa'], reverse=True).", ""),
            ("Print a ranked table with aligned columns: use enumerate(..., 1) for the rank number and f-string width specifiers such as {name:<28} {ticker:<10} {roa:>8.2f}, under a header row and a separator line.", "uv run python roa_ranking.py"),
            ("AI-ASSIST: prompt your AI tool with: \"This loop makes one network call per ticker and re-fetches on every run. Add a simple check that skips a ticker whose Total Assets is zero or missing to avoid ZeroDivisionError, count how many tickers succeeded versus were skipped, and print that summary at the end. Do not add any external caching library.\" Review the changes before applying.", ""),
            ("Apply the AI version and deliberately insert an invalid ticker such as 'XXXX.SI' in the middle of the list. Confirm the scan completes all ten, reports the skip, and the summary counts are correct.", "uv run python roa_ranking.py"),
            ("Add a range-based slice of the league table: use `for i in range(3)` to print only the top three performers under a 'BEST IN CLASS' heading.", "uv run python roa_ranking.py"),
            ("Discuss: ROA and ROE tell different stories for a bank, which is highly leveraged. Which of the two is more comparable across a bank and a REIT, and why?", ""),
        ],
        test="Run `uv run python roa_ranking.py`. You should see the 10-year compound projection, then a ranked ROA table with up to 10 rows sorted highest ROA first, a BEST IN CLASS top-three block, and a final summary line counting successes and skips. Inserting 'XXXX.SI' must not stop the scan.",
    ),

    dict(
        num=19,
        topic=3,
        title="Enumerate, Zip, Break and Continue — Combined ROE and ROA Scanner",
        objective="LO2: Apply enumerate and zip to combine parallel financial series, and break and continue to control early exit and skipping while scanning market data.",
        desc=(
            "Real screening code walks several parallel lists at once — tickers, ROE values and ROA values — "
            "and must decide row by row whether to include, skip or stop. You use zip to fuse the three "
            "series into one table, enumerate to rank it, continue to skip tickers with missing data or "
            "negative returns, and break to stop a budget-constrained buying loop the moment the cash "
            "limit would be breached. You also see the classic zip trap: zip stops silently at the "
            "SHORTEST list, so a mismatched length loses data without any error."
        ),
        build="roe_roa_scanner.py — a combined ROE + ROA screening table built with zip and enumerate, with continue-based skipping and a break-controlled budget allocator.",
        services="uv, yfinance, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project and add yfinance.", "uv init lab-19-roe-roa-scanner && cd lab-19-roe-roa-scanner && uv add yfinance"),
            ("In roe_roa_scanner.py, loop over sgx_tickers = ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'V03.SI'], read stock.info, and append to three parallel lists: tickers, roes (info.get('returnOnEquity', 0) * 100) and roas (info.get('returnOnAssets', 0) * 100).", ""),
            ("Fuse the three lists with data = zip(tickers, roes, roas) and print a header row plus one aligned line per stock using {t:<10} {roe:<10.2f} {roa:<10.2f}.", "uv run python roe_roa_scanner.py"),
            ("SEE THE ZIP TRAP: temporarily append one extra ticker to `tickers` only, re-run, and confirm the extra row disappears with no error. Restore the lists and add a comment recording the lesson.", "uv run python roe_roa_scanner.py"),
            ("Add enumerate to rank the table: `for rank, (t, roe, roa) in enumerate(zip(tickers, roes, roas), 1)` and print the rank in the first column. Note that start=1 gives human-readable ranks.", "uv run python roe_roa_scanner.py"),
            ("Use continue to skip rows with no usable data: inside the loop, if roe == 0 or roa == 0, print a 'no data — skipped' line and continue to the next ticker.", "uv run python roe_roa_scanner.py"),
            ("Add a quality flag column computed with a ternary: 'QUALITY' when ROE > 10 and ROA > 1, otherwise 'REVIEW'.", "uv run python roe_roa_scanner.py"),
            ("Build the break demo — a budget allocator: with budget = 100000 and a list of intended trade sizes [20000, 35000, 30000, 25000, 40000], accumulate them in a for loop and break the moment the next trade would exceed the budget, printing which trade was refused.", "uv run python roe_roa_scanner.py"),
            ("Add a second continue demo on a transaction feed: given [120.50, -50.00, 300.25, -20.00, 150.00, 0, 45.75], skip every non-positive amount (refunds and zeros) and total only genuine expenses.", "uv run python roe_roa_scanner.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Rewrite this scanner so the three parallel lists become a single list of dictionaries, and explain why that is safer than zipping three separate lists that must stay the same length. Keep the enumerate ranking, the continue-based skipping and the identical printed output.\" Compare the two designs side by side.", ""),
            ("Apply the AI refactor into a second file, run both, and confirm the printed tables are byte-for-byte identical.", "uv run python roe_roa_scanner_v2.py"),
            ("Discuss: break exits the loop entirely while continue only skips the current iteration. In a compliance scan of 5,000 transactions, which one would you use to skip malformed records, and which to abort on a hard stop rule?", ""),
        ],
        test="Run `uv run python roe_roa_scanner.py`. The scanner must print a ranked table with Rank, Ticker, ROE %, ROA % and a QUALITY/REVIEW flag for each stock that returned data, skip lines for any that did not, a budget allocator that stops before breaching $100,000, and a total-valid-expenses figure of $616.50 from the transaction feed.",
    ),

    dict(
        num=20,
        topic=3,
        title="Comprehensions — Net Profit Margin for 10 Singapore Stocks in One Line",
        objective="LO2: Apply list, set and dict comprehensions to compute and filter financial metrics across a portfolio in a single readable expression.",
        desc=(
            "Comprehensions are the idiom that makes Python financial code short and reviewable. You build "
            "up from simple currency conversion and GST examples to the topic's headline activity: net "
            "profit margin (Net Income / Total Revenue * 100) computed across ten SGX tickers with a single "
            "list comprehension, plus a set comprehension that de-duplicates tickers from a transaction "
            "history and a dict comprehension that builds a ticker-to-margin lookup and filters it to the "
            "high-margin names. You finish by comparing the comprehension against the equivalent for loop."
        ),
        build="margin_comprehensions.py — computes net profit margin for 10 SGX stocks with a list comprehension, plus set and dict comprehension utilities and a filtered high-margin lookup.",
        services="uv, yfinance, pandas, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project and add the dependencies.", "uv init lab-20-margin-comprehensions && cd lab-20-margin-comprehensions && uv add yfinance pandas"),
            ("Warm up with three list comprehensions in margin_comprehensions.py: convert prices_sgd = [35.50, 28.40, 13.10, 5.20] to USD at 0.74; apply 9% GST to subtotals [100, 250, 45] with round(amt * 1.09, 2); and select tickers priced above $20 using [t for t, p in zip(tickers, prices) if p > 20].", "uv run python margin_comprehensions.py"),
            ("Add a set comprehension over a transaction history list of dicts to extract the unique tickers: {t['ticker'] for t in transactions}. Print the set and its length to prove duplicates were removed.", "uv run python margin_comprehensions.py"),
            ("Add two dict comprehensions: build a market-cap lookup from parallel lists with {t: c for t, c in zip(tickers, market_caps)}, then filter an existing price dict to only stocks above $20 with {t: p for t, p in prices.items() if p > 20}.", "uv run python margin_comprehensions.py"),
            ("Now the main activity. Define a helper function get_margin(ticker) that fetches stock.financials, reads Net Income and Total Revenue with .loc[...].iloc[0], and returns {'ticker': ticker, 'margin': (net_income / revenue) * 100}, returning a margin of None inside an except block.", ""),
            ("Define the ten tickers ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'J36.SI', 'BN4.SI', 'V03.SI', 'C38U.SI', 'A17U.SI', 'C07.SI'] and compute every margin in ONE line: results = [get_margin(t) for t in sgx_tickers].", ""),
            ("Print the results as an aligned table with a header, handling the None case in the f-string so a failed fetch shows 'N/A' rather than crashing on format.", "uv run python margin_comprehensions.py"),
            ("Add a filtering comprehension on top of the results: high_margin = [r for r in results if r['margin'] is not None and r['margin'] > 20] and print how many of the ten cleared the 20% bar.", "uv run python margin_comprehensions.py"),
            ("Build the dict lookup with a dict comprehension: margin_lookup = {r['ticker']: round(r['margin'], 2) for r in results if r['margin'] is not None}, then query a single ticker from it.", "uv run python margin_comprehensions.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Rewrite this single-line list comprehension as an explicit for loop with the same behaviour, then tell me which version you would approve in a code review for a financial reporting system and why. Also point out any case where the comprehension silently hides an error that the for loop would surface.\" Read the reasoning carefully.", ""),
            ("Add the AI's for-loop version alongside the comprehension, run both, and assert they produce identical results with a simple equality check printed as PASS or FAIL.", "uv run python margin_comprehensions.py"),
            ("Discuss: the bare `except:` inside get_margin catches everything, including a typo in a row label. Replace it with `except (KeyError, IndexError, ZeroDivisionError)` and re-run — does anything now fail loudly that was silently returning None before?", "uv run python margin_comprehensions.py"),
        ],
        test="Run `uv run python margin_comprehensions.py`. It must print the USD prices, GST totals and >$20 ticker list; a unique-ticker set of size 3; a market-cap dict and a filtered high-value price dict; a 10-row net profit margin table where any failed fetch shows N/A; a count of stocks above a 20% margin; and a final PASS line confirming the comprehension and the for-loop versions agree.",
    ),
]
