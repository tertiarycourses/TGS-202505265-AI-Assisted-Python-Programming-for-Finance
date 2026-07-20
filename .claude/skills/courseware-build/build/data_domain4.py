"""
Topic 4 — Scripting with Function and Lambda (labs 21-28).

Hands-on activities for domain 4. Lab `num` is the GLOBAL contiguous lab number
(21..28); `topic` is 4. All labs are finance-focused (SGX / global markets) and
mirror the reference notebook activities: function basics (CAGR, simple interest,
break-even), returning multiple values from an income statement, the net profit
margin function, multiple / default / named / variable arguments, the Max ROE
function, lambda for gross profit margin, map for ROE across stocks, and filter
for top-income customers. All labs are managed with uv (uv init / uv add / uv run).
"""

DOMAIN4 = [

    dict(
        num=21,
        topic=4,
        title="Functions — A Reusable Financial Formula Library",
        objective="LO3: Construct reusable functions that turn a business requirement into a named, testable unit computing standard financial metrics.",
        desc=(
            "You build your first reusable module: three named functions covering Compound Annual Growth "
            "Rate, simple interest and break-even units. Each gets a docstring stating the formula, because "
            "in a regulated environment the formula must be auditable from the code. You then see the "
            "difference between a function that returns a value and one that only prints, and why the "
            "returning version is the only one you can test."
        ),
        build="finance_formulas.py — a module of documented, reusable financial functions (CAGR, simple interest, break-even units) with a demonstration block.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project for your formula library.", "uv init lab-21-finance-formulas && cd lab-21-finance-formulas"),
            ("In finance_formulas.py define calculate_cagr(beginning_value, ending_value, years) returning ((ending_value / beginning_value) ** (1 / years)) - 1, with a one-line docstring naming the metric.", ""),
            ("Define calculate_simple_interest(principal, rate, time) returning principal * (rate / 100) * time — note the rate is passed as a whole number of percent, and say so in the docstring.", ""),
            ("Define break_even_units(fixed_costs, price_per_unit, variable_cost_per_unit) returning fixed_costs / (price_per_unit - variable_cost_per_unit).", ""),
            ("Call all three with the worked examples — CAGR from 10000 to 15000 over 5 years, simple interest on 5000 at 4.5% for 2 years, break-even on 20000 fixed costs at a $50 price and $30 variable cost — and print each result with the right format specifier ({:.2%} for CAGR, ${:.2f} for interest, whole units for break-even).", "uv run python finance_formulas.py"),
            ("CONTRAST: write a fourth function that prints the CAGR instead of returning it. Try to use its output in a further calculation and observe that you get None. Write a comment recording why 'return' beats 'print' in a library.", "uv run python finance_formulas.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Add input validation to these three financial functions. calculate_cagr must reject a zero or negative beginning value and zero years; break_even_units must reject a contribution margin of zero or below because that means the product never breaks even (ZeroDivisionError). Raise ValueError with a message naming the offending argument.\" Review the exceptions it chose.", ""),
            ("Apply the validated version and test each failure path: CAGR with beginning_value = 0, CAGR with years = 0, and break-even where the variable cost exceeds the price.", "uv run python finance_formulas.py"),
            ("Add a `if __name__ == '__main__':` guard around the demonstration block so the module can be imported by later labs without running the demo.", "uv run python finance_formulas.py"),
            ("Prove the guard works by importing the module and calling one function from a one-liner.", "uv run python -c \"from finance_formulas import calculate_cagr; print(f'{calculate_cagr(10000, 15000, 5):.2%}')\""),
            ("Discuss: what does the CAGR figure hide about the year-by-year path an investment took, and why does that matter to a client conversation?", ""),
        ],
        test="Run `uv run python finance_formulas.py`. CAGR must print 8.45%, simple interest $450.00, and break-even 1000 units. The import one-liner must print 8.45% with no demonstration output, proving the __main__ guard works. All three invalid-input tests must raise a ValueError naming the bad argument.",
    ),

    dict(
        num=22,
        topic=4,
        title="Return Multiple Values — A Full Income Statement Analysis in One Call",
        objective="LO3: Construct a function that returns multiple values so a single call delivers a complete set of financial ratios, and unpack them cleanly.",
        desc=(
            "A single call should be able to hand back a whole analysis. You build "
            "analyze_income_statement(revenue, cogs, operating_expenses) which returns gross profit, net "
            "income and profit margin as a tuple, then unpack all three in one assignment. You compare "
            "tuple return against dictionary return, learn why the tuple's ORDER is a silent trap when a "
            "caller unpacks it wrongly, and finish with a named-tuple version that removes the trap."
        ),
        build="income_analysis.py — an income statement analyser returning gross profit, net income and margin, in tuple, dict and namedtuple variants.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project.", "uv init lab-22-income-analysis && cd lab-22-income-analysis"),
            ("In income_analysis.py define analyze_income_statement(revenue, cogs, operating_expenses). Compute gross_profit = revenue - cogs, net_income = gross_profit - operating_expenses, and profit_margin = (net_income / revenue) * 100 if revenue != 0 else 0.", ""),
            ("Return all three as a tuple: `return gross_profit, net_income, profit_margin`. Note in the docstring that this is a tuple return even though there are no parentheses.", ""),
            ("Call it with revenue 500000, COGS 200000 and operating expenses 150000, unpacking with `gp, ni, pm = analyze_income_statement(...)`.", ""),
            ("Print a formatted mini income statement: Revenue, Gross Profit and Net Income with thousands separators, and Profit Margin to 2 decimals with a percent sign.", "uv run python income_analysis.py"),
            ("SEE THE TRAP: deliberately unpack in the wrong order as `pm, ni, gp = ...` and re-run. Nothing errors, but the report is nonsense. Restore the correct order and comment on the risk.", "uv run python income_analysis.py"),
            ("Confirm the zero-revenue guard: call the function with revenue = 0 and check the margin comes back as 0 rather than raising ZeroDivisionError.", "uv run python income_analysis.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Rewrite this function to return a dictionary with keys gross_profit, net_income and profit_margin instead of a positional tuple, and then a third version using collections.namedtuple. Explain which of the three is safest for a financial reporting system where callers are written by different teams.\" Read the trade-off argument.", ""),
            ("Add both AI variants to the file as analyze_income_statement_dict and analyze_income_statement_nt, and call all three on the same inputs to confirm identical numbers.", "uv run python income_analysis.py"),
            ("Extend the analysis: add operating margin ((gross_profit - operating_expenses) / revenue * 100) and a cost ratio (cogs / revenue * 100) to the dict version, so one call now returns five metrics.", "uv run python income_analysis.py"),
            ("Run the analyser over three mock companies held in a list of tuples, printing one comparison row per company in an aligned table.", "uv run python income_analysis.py"),
            ("Discuss: the tuple version is faster to write and the dict version is safer to consume. At what team size does that trade-off flip?", ""),
        ],
        test="Run `uv run python income_analysis.py`. For revenue 500000 / COGS 200000 / OpEx 150000 it must report Gross Profit $300,000, Net Income $150,000 and Profit Margin 30.00%. The dict and namedtuple versions must return the same three numbers, revenue = 0 must return a margin of 0 without a traceback, and the three-company comparison table must print three aligned rows.",
    ),

    dict(
        num=23,
        topic=4,
        title="Activity: Net Profit Margin Function with Zero-Revenue Handling",
        objective="LO3: Construct a single-responsibility function computing net profit margin, and defend it against the zero and missing data cases found in real filings.",
        desc=(
            "This is the topic's core activity, built to production standard. "
            "calculate_net_profit_margin(net_income, revenue) returns (net_income / revenue) * 100, guarded "
            "so a revenue of zero returns 0 rather than raising ZeroDivisionError. You then apply it to "
            "live SGX filings, handle the negative-margin case (a loss-making company is not a bug), and "
            "write a small set of assertions that prove the function behaves — your first taste of testing."
        ),
        build="net_profit_margin.py — a validated net profit margin function with assertion-based tests, applied to live SGX financial statements.",
        services="uv, yfinance, pandas, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project and add market-data dependencies.", "uv init lab-23-net-profit-margin && cd lab-23-net-profit-margin && uv add yfinance pandas"),
            ("In net_profit_margin.py define calculate_net_profit_margin(net_income, revenue) with a docstring stating the formula (Net Income / Total Revenue) * 100. Return 0 if revenue is 0, otherwise the computed margin.", ""),
            ("Test it with the sample figures from the reference: net income 1,000,000 on revenue 5,000,000. Print the result to 2 decimals with a percent sign.", "uv run python net_profit_margin.py"),
            ("Test the loss case: net income of -250,000 on revenue 5,000,000 should return -5.00%. Confirm the function does NOT suppress the negative — a loss must stay visible.", "uv run python net_profit_margin.py"),
            ("Test the guard: call it with revenue = 0 and confirm it returns 0 with no traceback. Add a comment on why returning 0 here is a design choice a reviewer might challenge.", "uv run python net_profit_margin.py"),
            ("Wire it to live data: fetch D05.SI with yfinance, read Net Income and Total Revenue from stock.financials with .loc[...].iloc[0], and pass both into your function.", "uv run python net_profit_margin.py"),
            ("Loop the live version over five SGX tickers ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'V03.SI'], printing a formatted margin table with a header row and a separator.", "uv run python net_profit_margin.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Write five assert statements that test this net profit margin function: the normal case, a zero-revenue case, a negative net income case, a 100% margin case, and a case where revenue is negative. Then tell me whether returning 0 for zero revenue is better than raising an exception in a financial reporting context, and argue both sides.\" Review the tests and the argument.", ""),
            ("Add the generated assertions to the bottom of the file under a run_tests() function and execute them — all five must pass silently.", "uv run python net_profit_margin.py"),
            ("Add a classification wrapper on top: a margin above 20% is 'EXCELLENT', 10 to 20% is 'HEALTHY', 0 to 10% is 'THIN', below 0 is 'LOSS-MAKING'. Apply it to each row of the live table.", "uv run python net_profit_margin.py"),
            ("Discuss: net profit margin is not comparable across sectors — a bank and a supermarket sit on completely different bases. What would you add to the output to stop a reader making that mistake?", ""),
        ],
        test="Run `uv run python net_profit_margin.py`. The sample case must report 20.00%, the loss case -5.00%, and the zero-revenue case 0 with no traceback. All five assertions must pass without output. The live table must show five SGX tickers each with a margin and one of the four classification labels.",
    ),

    dict(
        num=24,
        topic=4,
        title="Multiple, Default and Named Arguments — A Flexible Valuation Toolkit",
        objective="LO3: Construct functions using multiple, default and named arguments so one function serves several business cases without duplication.",
        desc=(
            "You learn the three argument styles that stop a codebase filling up with near-duplicate "
            "functions. Multiple arguments give a fixed three-stock portfolio total; default arguments let "
            "calculate_net_salary assume a 15% tax rate while still accepting a custom one; named arguments "
            "make calculate_dividend_yield(stock_price=120.00, dividend_per_share=3.60) unambiguous "
            "regardless of order. You also meet the mutable-default-argument trap, one of Python's most "
            "notorious bugs."
        ),
        build="valuation_toolkit.py — portfolio total, net salary, investment projection, dividend yield and ROI functions demonstrating multiple, default and named arguments.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project.", "uv init lab-24-valuation-toolkit && cd lab-24-valuation-toolkit"),
            ("MULTIPLE ARGUMENTS: define calculate_portfolio_total(stock1, stock2, stock3) returning their sum, and call it with 1500.50, 2300.75 and 850.00. Then call it with only two values and read the TypeError carefully.", "uv run python valuation_toolkit.py"),
            ("DEFAULT ARGUMENTS: define calculate_net_salary(gross_salary, tax_rate=0.15) returning gross_salary minus the tax. Call it once on 5000 using the default and once with tax_rate=0.20, printing both.", "uv run python valuation_toolkit.py"),
            ("Add estimate_investment_value(principal, years, annual_return=0.07) returning principal * (1 + annual_return) ** years. Call it as (1000, 5) with the default and as (1000, 5, 0.10) with a custom return.", "uv run python valuation_toolkit.py"),
            ("NAMED ARGUMENTS: define calculate_dividend_yield(dividend_per_share, stock_price) returning (dps / price) * 100. Call it twice with the arguments in DIFFERENT orders using keywords, and confirm both give the right answer.", "uv run python valuation_toolkit.py"),
            ("Now call the same function positionally with the arguments swapped — (50.00, 2.50) — and observe it returns a nonsense 2000% yield with no error. Write a comment: named arguments are a correctness control, not a style preference.", "uv run python valuation_toolkit.py"),
            ("Add calculate_roi(initial_investment, final_value) returning ((final - initial) / initial) * 100 and call it with named arguments for clarity.", "uv run python valuation_toolkit.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Show me the mutable default argument trap using a function like add_holding(ticker, portfolio=[]) that appends to a portfolio list. Demonstrate the bug by calling it three times, explain exactly why the list persists between calls, and give me the correct fix using portfolio=None.\" Run the buggy version first so you SEE the bug.", ""),
            ("Add both the buggy and the fixed add_holding to your file, call each three times, and print the resulting portfolios side by side so the difference is undeniable.", "uv run python valuation_toolkit.py"),
            ("Combine the styles: extend calculate_net_salary with a second default argument cpf_rate=0.20 and call it with only the keyword you want to override, leaving the other at its default.", "uv run python valuation_toolkit.py"),
            ("Enforce clarity: place a bare `*` in a signature (def calculate_dividend_yield(*, dividend_per_share, stock_price)) to make both arguments keyword-only, then confirm the positional call now raises a TypeError instead of silently returning 2000%.", "uv run python valuation_toolkit.py"),
            ("Discuss: a default value baked into a function is a policy decision. Who owns the 15% tax rate default, and what happens when the policy changes?", ""),
        ],
        test="Run `uv run python valuation_toolkit.py`. Portfolio total must be $4,651.25; net salary $4,250.00 at the default rate and $4,000.00 at 20%; investment value $1,402.55 at the default 7%; both dividend yield calls 5.00% and 3.00%. The buggy add_holding must show a growing shared list while the fixed one shows a fresh list each call, and the keyword-only version must raise TypeError on a positional call.",
    ),

    dict(
        num=25,
        topic=4,
        title="Variable Arguments — *args and **kwargs for Portfolios of Any Size",
        objective="LO3: Construct functions accepting a variable number of arguments so one function handles a portfolio of any size or a metric set of any shape.",
        desc=(
            "A portfolio does not have a fixed number of holdings, so a fixed-arity function is the wrong "
            "shape. You rebuild calculate_portfolio_total with *stock_values so it sums three holdings or "
            "fifty, add a category-plus-amounts expense reporter, then move to **kwargs to accept an "
            "arbitrary named metric set. You finish with unpacking — passing an existing list into an "
            "*args function with the star operator, and a dict into a **kwargs function with double-star."
        ),
        build="variable_args.py — variable-argument portfolio, expense and metric functions using *args and **kwargs, plus argument unpacking from existing collections.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project.", "uv init lab-25-variable-args && cd lab-25-variable-args"),
            ("In variable_args.py redefine calculate_portfolio_total(*stock_values) returning sum(stock_values). Call it with three values (1500.50, 2300.75, 850.00) and then five values (500, 1200, 450, 3000, 150) — same function, both work.", "uv run python variable_args.py"),
            ("Print len(stock_values) inside the function to prove *args arrives as a tuple, and confirm the type with a print of type(stock_values).", "uv run python variable_args.py"),
            ("Handle the empty case: call calculate_portfolio_total() with no arguments. sum(()) returns 0 — decide whether that is the right answer for an empty portfolio and note your reasoning in a comment.", "uv run python variable_args.py"),
            ("Define list_expenses(category, *amounts) which prints the category name, the number of items, and the total formatted to 2 decimals. Call it for 'Trading Fees' with four amounts and for 'Custody' with one.", "uv run python variable_args.py"),
            ("UNPACKING: given an existing list holdings = [1500.50, 2300.75, 850.00, 1200.00], call calculate_portfolio_total(*holdings) with the star operator. Then call it without the star and observe you get a TypeError or a single-tuple result.", "uv run python variable_args.py"),
            ("Move to **kwargs: define report_metrics(ticker, **metrics) that prints the ticker then one aligned line per keyword metric. Call it as report_metrics('D05.SI', roe=15.8, roa=1.2, npm=42.5, pe=11.4).", "uv run python variable_args.py"),
            ("Unpack a dict into it: build metrics_dict = {'roe': 12.1, 'roa': 0.9, 'pe': 9.8} and call report_metrics('O39.SI', **metrics_dict).", "uv run python variable_args.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Write a function build_trade_order(ticker, quantity, *, order_type='LIMIT', **extras) that accepts required positional arguments, a keyword-only default, and arbitrary extra parameters. Show me the exact order the four argument categories must appear in a Python signature and what error I get if I put them in the wrong order.\" Test the wrong order yourself to see the SyntaxError.", ""),
            ("Add the generated build_trade_order to your file, call it with and without extras, and print the resulting order dict.", "uv run python variable_args.py"),
            ("Combine everything: write summarise_portfolio(name, *values, currency='SGD', **tags) printing the portfolio name, holding count, total in the given currency, and any tags supplied.", "uv run python variable_args.py"),
            ("Discuss: *args and **kwargs make a function flexible but also make its contract invisible to a caller reading the signature. Where would you refuse to use them in a trading system?", ""),
        ],
        test="Run `uv run python variable_args.py`. The three-stock total must be $4,651.25 and the five-stock total $5,300.00 from the same function. The unpacked call with *holdings must total $5,851.25. report_metrics must print four aligned metric lines for D05.SI and three for O39.SI, and summarise_portfolio must print the name, count, currency-formatted total and every tag supplied.",
    ),

    dict(
        num=26,
        topic=4,
        title="Activity: Max ROE Function — Finding the Best Performer in a Portfolio",
        objective="LO3: Construct a function that scans a list of financial records and returns the maximum value by a chosen metric, and compare it against Python's built-in max.",
        desc=(
            "You fetch Return on Equity for ten SGX companies, then write find_max_roe(data_list) that "
            "walks the list of dicts and returns the single best entry — implementing the max algorithm by "
            "hand before replacing it with max(data_list, key=lambda x: x['roe']). Handling the empty list "
            "(return None, not an IndexError) is the point of the lab: a screener that finds nothing must "
            "say so calmly. You then generalise it to find_max_by(data_list, metric) so one function serves "
            "ROE, ROA and margin."
        ),
        build="max_roe.py — fetches ROE for 10 SGX tickers and reports the top performer via a hand-written max function, a built-in max version and a generalised find_max_by.",
        services="uv, yfinance, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project and add yfinance.", "uv init lab-26-max-roe && cd lab-26-max-roe && uv add yfinance"),
            ("In max_roe.py loop over the ten tickers ['D05.SI', 'U11.SI', 'O39.SI', 'Z74.SI', 'J36.SI', 'BN4.SI', 'V03.SI', 'C38U.SI', 'A17U.SI', 'C07.SI'], read stock.info.get('returnOnEquity'), and append {'ticker': ..., 'roe': roe * 100} only when the value is not None.", ""),
            ("Wrap each fetch in try/except so one failing ticker does not abort the scan, and print how many of the ten returned usable ROE data.", "uv run python max_roe.py"),
            ("Print the full ROE sequence as an aligned table before any ranking, so you can verify the winner by eye.", "uv run python max_roe.py"),
            ("Write find_max_roe(data_list) by hand: return None immediately if the list is empty, otherwise seed max_entry with data_list[0] and loop comparing entry['roe'] against max_entry['roe'], reassigning on a higher value.", ""),
            ("Call it and print the winner: 'TOP PERFORMER: {ticker} with ROE {roe:.2f}%'.", "uv run python max_roe.py"),
            ("Test the empty case: call find_max_roe([]) and confirm it returns None rather than raising IndexError. Print a 'no qualifying stocks found' message when it does.", "uv run python max_roe.py"),
            ("Replace the hand-written loop with the built-in: best = max(data_list, key=lambda x: x['roe']) and confirm it names the same winner. Note that max on an empty list raises ValueError unless you pass default=None.", "uv run python max_roe.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Generalise find_max_roe into find_max_by(data_list, metric) that takes the metric name as a string so the same function works for roe, roa or margin. Add a matching find_min_by, handle the empty list and the case where the metric key is missing from some records, and explain the trade-off versus just using max with a key lambda.\" Review the missing-key handling especially.", ""),
            ("Add the generalised functions, extend your fetch loop to also collect returnOnAssets, and call find_max_by twice — once for 'roe' and once for 'roa' — printing both winners.", "uv run python max_roe.py"),
            ("Add a top-three report using sorted(data_list, key=lambda x: x['roe'], reverse=True)[:3] and print it as a ranked podium with enumerate.", "uv run python max_roe.py"),
            ("Discuss: the highest ROE in the list may be driven by high leverage rather than operating strength. What second metric would you require before acting on this screener's winner?", ""),
        ],
        test="Run `uv run python max_roe.py`. It must print the count of tickers with usable data, the full ROE table, a single TOP PERFORMER line, and confirmation that the hand-written find_max_roe and the built-in max agree on the same ticker. find_max_roe([]) must return None with a 'no qualifying stocks' message, and find_max_by must report a winner for both 'roe' and 'roa'.",
    ),

    dict(
        num=27,
        topic=4,
        title="Lambda and Map — Gross Profit Margin and ROE Across a Portfolio",
        objective="LO3: Construct lambda expressions for one-off financial formulas and apply them across a sequence of stocks with map.",
        desc=(
            "Lambda gives you a formula without the ceremony of def, and map applies it across a whole "
            "portfolio in one expression. You write lambdas for simple interest, currency conversion and "
            "percent change, then the topic's activity: a gross profit margin lambda "
            "((Revenue - COGS) / Revenue * 100) with a zero-revenue ternary guard. You then use map with a "
            "lambda to compute ROE for a list of SGX companies from hard-coded net income and equity, and "
            "compare map against the equivalent list comprehension."
        ),
        build="lambda_map.py — gross profit margin and ROE computed with lambda expressions and applied across a portfolio using map, benchmarked against a list comprehension.",
        services="uv, Python 3.12, Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project.", "uv init lab-27-lambda-map && cd lab-27-lambda-map"),
            ("In lambda_map.py write three lambdas: calculate_interest = lambda p, r, t: p * (r / 100) * t; sgd_to_usd = lambda amount: amount * 0.74; percent_change = lambda new, old: ((new - old) / old) * 100. Call each and print the results.", "uv run python lambda_map.py"),
            ("ACTIVITY — GROSS PROFIT MARGIN: write calculate_gross_margin = lambda revenue, cogs: ((revenue - cogs) / revenue) * 100 if revenue != 0 else 0. Call it with revenue 500000 and COGS 300000 and print revenue, COGS and the margin.", "uv run python lambda_map.py"),
            ("Confirm the guard by calling calculate_gross_margin(0, 100) and checking it returns 0 rather than raising ZeroDivisionError.", "uv run python lambda_map.py"),
            ("Introduce map with three quick examples: apply 9% GST to transactions [100.0, 250.50, 45.0, 1200.0] with round(x * 1.09, 2); extract tickers from a list of portfolio dicts; and normalise prices [35.50, 36.20, 34.80, 37.00] against the first price.", "uv run python lambda_map.py"),
            ("Note that map returns a lazy iterator — print the map object itself before wrapping it in list() so you see the difference, and comment on why the list() call is required.", "uv run python lambda_map.py"),
            ("ACTIVITY — ROE VIA MAP: define financial_data as a list of dicts for five SGX companies with net_income and equity in SGD billions (D05.SI 10.3/57.1, U11.SI 5.7/45.2, O39.SI 7.0/54.8, Z74.SI 1.9/26.5, V03.SI 1.1/12.4).", ""),
            ("Write roe_calculator as a lambda returning {'ticker': x['ticker'], 'roe': (x['net_income'] / x['equity']) * 100 if x['equity'] != 0 else 0}, then apply it with roe_results = list(map(roe_calculator, financial_data)).", ""),
            ("Print the results as an aligned table with a header and separator, each ROE to 2 decimals.", "uv run python lambda_map.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Rewrite this map plus lambda as a list comprehension and as a named def function, then tell me which of the three you would use in a financial codebase that other analysts must maintain, and explain when a lambda is genuinely the better choice.\" Weigh the answer against your own reading of the code.", ""),
            ("Add all three versions to the file, run them on the same data, and print a PASS line confirming they produce identical output.", "uv run python lambda_map.py"),
            ("Apply the gross margin lambda across a portfolio with map: given a list of (revenue, cogs) tuples for four companies, use map with a lambda taking the tuple and print each company's gross margin.", "uv run python lambda_map.py"),
        ],
        test="Run `uv run python lambda_map.py`. Simple interest must be $100.00, $100 SGD must convert to $74.00, percent change must be 20.00%, and the gross profit margin on 500000/300000 must be 40.00%. The map-based ROE table must show five tickers with D05.SI at approximately 18.04% and V03.SI at approximately 8.87%, and the final PASS line must confirm the map, comprehension and def versions agree.",
    ),

    dict(
        num=28,
        topic=4,
        title="Filter — Top Income Customers and High-ROE Stock Screening",
        objective="LO3: Construct filter expressions with lambda to select the subset of a dataset that meets a business threshold, and chain filtering with sorting to produce a ranked shortlist.",
        desc=(
            "Filter is the screening primitive: it keeps only the records where a lambda returns True. You "
            "generate 20 mock banking customers with random incomes between $30,000 and $200,000, filter "
            "for the top earners above a $150,000 threshold, and produce a sorted priority-contact list. "
            "You then apply the same pattern to stock screening (ROE above 10%), large-transaction "
            "monitoring and SGX-only ticker selection, and finish by chaining filter with map to build a "
            "complete screen-then-compute pipeline — the closing exercise of Topic 4."
        ),
        build="customer_filter.py — a filter-based screening tool producing a ranked top-income customer list, a high-ROE stock screen and a chained filter-then-map pipeline.",
        services="uv, Python 3.12 (random module), Google Colab / Cursor, Gemini or Copilot",
        steps=[
            ("Create the uv project.", "uv init lab-28-customer-filter && cd lab-28-customer-filter"),
            ("In customer_filter.py import random and generate 20 mock customers with a list comprehension: [{'id': i, 'name': f'Customer {i}', 'income': random.randint(30000, 200000)} for i in range(1, 21)].", ""),
            ("Set random.seed(42) before generating so your run is reproducible — essential when a colleague must verify your screening result. Print the first three customers to confirm.", "uv run python customer_filter.py"),
            ("ACTIVITY — TOP INCOME CUSTOMERS: set threshold = 150000 and apply top_earners = list(filter(lambda c: c['income'] > threshold, customers)).", ""),
            ("Print the total customer count, the number of top earners, and then the top earners sorted descending by income using sorted(top_earners, key=lambda x: x['income'], reverse=True), each formatted as 'Customer N: $NNN,NNN'.", "uv run python customer_filter.py"),
            ("Test the empty result: raise the threshold to 500000, re-run, and confirm the script prints a clear 'no customers meet this threshold' message rather than an empty block. Restore 150000.", "uv run python customer_filter.py"),
            ("Add three more filter examples: high-ROE stocks (list of dicts, keep roe > 10), large transactions from [120.50, 800.00, 45.00, 1500.25, 300.00] keeping x > 500, and SGX-only tickers from ['AAPL', 'D05.SI', 'TSLA', 'U11.SI', 'GOOG'] using t.endswith('.SI').", "uv run python customer_filter.py"),
            ("CHAIN FILTER AND MAP: filter the customers to those above the threshold, then map a lambda that adds a 'tier' key ('PLATINUM' above 180000, else 'GOLD') and an estimated annual fee at 0.5% of income. Print the enriched list.", "uv run python customer_filter.py"),
            ("AI-ASSIST: prompt your AI tool with: \"Refactor this filter-plus-lambda screening code to use a named predicate function instead of an inline lambda, add a second filter criterion so only customers who are BOTH above the income threshold AND have an id below 15 are selected, and explain when filter is clearer than a list comprehension with an if.\" Review the combined predicate for correct and/or logic.", ""),
            ("Apply the AI version, run it, and manually verify two or three selected records against the raw customer list to confirm both criteria really were applied.", "uv run python customer_filter.py"),
            ("Produce the final deliverable: a formatted 'PRIORITY WEALTH CONTACT LIST' with a header, a rank column from enumerate, name, income and tier, plus a footer line reporting the total addressable income of the shortlist.", "uv run python customer_filter.py"),
            ("Discuss: this screen uses income alone. Name two additional fields a bank would need before this list could be used for an actual wealth-management outreach, and one governance concern about acting on it.", ""),
        ],
        test="Run `uv run python customer_filter.py`. With random.seed(42) the run must be reproducible across executions. It must print 20 total customers, the count above $150,000, and a descending-sorted list of those top earners. Raising the threshold to 500000 must produce a 'no customers meet this threshold' message. The final PRIORITY WEALTH CONTACT LIST must show a rank, name, formatted income and PLATINUM/GOLD tier per row, plus a total addressable income footer.",
    ),
]
