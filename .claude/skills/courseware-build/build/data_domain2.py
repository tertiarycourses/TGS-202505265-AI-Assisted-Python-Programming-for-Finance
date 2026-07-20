"""
Topic 2 — Data Types and Operators (labs 5–12).

Hands-on activities for domain 2, mirroring the reference notebook activities
(number/string literal formatting in millions, Loan Calculator, Retirement
Calculator, string methods and Extract Company Name, List and Top 10 SGX
companies by market cap, Tuple, Dictionary and Company Stock Values, Set and
Common Company Stocks, Operators). All labs are managed with uv and every lab
contains at least one AI-prompting step.
"""

DOMAIN2 = [
    dict(
        num=5,
        topic=2,
        title="Number and String Literal Formatting for Financial Reporting",
        objective="LO2: Apply Python number and string data types and literal formatting to present financial figures in board-ready precision.",
        desc=(
            "The learner works with int and float financial values and uses f-string literal formatting "
            "to render revenue and market capitalisation in millions and billions, percentages to basis "
            "point precision, and currency with thousands separators — then confronts float rounding, "
            "the reason Decimal exists in settlement systems."
        ),
        build="A script `format_report.py` that renders a set of raw financial figures as a formatted revenue and market-cap summary in millions.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project.", "uv init lab-05-number-format && cd lab-05-number-format"),
            ("Create format_report.py with two raw revenue figures using Python's numeric underscore separators for readability.", "num1 = 12_345_678.90; num2 = 7_890_123.45; result = num1 + num2"),
            ("Format the sum in millions to two decimals — the standard unit in an SGX results announcement.", "print(f'{num1/1_000_000:.2f}M + {num2/1_000_000:.2f}M = {result/1_000_000:.2f}M')"),
            ("Add a market-cap line in billions and a margin line as a percentage.", "print(f'Market cap: {84_500_000_000/1_000_000_000:.2f}B | Net margin: {0.2837:.2%}')"),
            ("Demonstrate the float trap that matters in settlement: run the classic check and note the result is not exactly 0.3.", "uv run python -c \"print(0.1 + 0.2, 0.1 + 0.2 == 0.3)\""),
            ("Discuss why a bank posts ledger entries with Decimal or integer cents rather than float, and where the tolerance threshold sits in your own organisation.", ""),
            ("PROMPT THE AI ASSISTANT with: 'Extend format_report.py with a function format_sgd(amount) that returns a string: values of 1 billion or more as $x.xxB, values of 1 million or more as $x.xxM, values of 1 thousand or more as $x.xK, and anything smaller as $x,xxx.xx. Include a right-aligned printed table of DBS 84500000000, Singtel 52300000000, CapitaLand 13800000000 and a small holding of 4250.75.' Apply the code.", ""),
            ("REVIEW the AI output: check the thresholds are tested largest-first, that negative amounts do not break the sign, and that the alignment uses an f-string width specifier.", ""),
            ("Run the script and inspect the alignment of the table.", "uv run python format_report.py"),
            ("Test the boundaries: pass exactly 1_000_000, exactly 999_999.99, 0 and -2_500_000 to format_sgd and confirm each renders sensibly.", "uv run python format_report.py"),
        ],
        test="format_sgd returns '$84.50B' for DBS, '$13.80M'-style output for millions, and the printed table is right-aligned with every figure carrying its correct unit suffix.",
    ),
    dict(
        num=6,
        topic=2,
        title="Loan Amortisation Calculator",
        objective="LO2: Apply numeric data types and arithmetic operators to solve a financial calculation problem — the monthly instalment on an amortising loan.",
        desc=(
            "Mirroring the reference notebook activity, the learner implements the standard amortisation "
            "formula P·[r(1+r)^n]/[(1+r)^n−1] for a Singapore housing loan, then extends it with total "
            "interest paid, the zero-interest edge case, and input validation so the tool is safe to hand "
            "to a relationship manager."
        ),
        build="A script `loan_calculator.py` that returns the monthly instalment, total repayment and total interest for a given principal, annual rate and tenor.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project.", "uv init lab-06-loan-calculator && cd lab-06-loan-calculator"),
            ("Create loan_calculator.py and collect the three inputs a mortgage quote needs.", "principal = float(input('Enter loan amount: ')); annual_rate = float(input('Enter annual interest rate (e.g., 5 for 5%): ')); years = int(input('Enter loan term in years: '))"),
            ("Convert the annual rate to a monthly rate and the tenor to a number of payments — the two conversions candidates most often get wrong.", "monthly_rate = annual_rate / 100 / 12; n = years * 12"),
            ("Implement the amortisation formula using the exponent operator.", "monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)"),
            ("Derive the total repayment and the total interest, then print all three formatted as SGD.", "total_payment = monthly_payment * n; print(f'Monthly: ${monthly_payment:,.2f} | Total: ${total_payment:,.2f} | Interest: ${total_payment - principal:,.2f}')"),
            ("Run it for a typical Singapore HDB loan: principal 500000, rate 2.6, term 25 years.", "uv run python loan_calculator.py"),
            ("Try a rate of 0 and observe the ZeroDivisionError — a real defect, because interest-free staff loans exist.", "uv run python loan_calculator.py"),
            ("PROMPT THE AI ASSISTANT with: 'Refactor loan_calculator.py into a function monthly_instalment(principal, annual_rate_pct, years) that returns monthly payment, total repayment and total interest. Handle a zero interest rate by dividing the principal evenly across the months instead of using the amortisation formula. Reject a principal of zero or less, a negative rate and a term under one year with a clear message. Format all output as SGD with thousands separators.' Apply the code.", ""),
            ("REVIEW the AI output: confirm the zero-rate branch is chosen before the formula runs, that the rate is still divided by both 100 and 12, and that the three returned values are consistent.", ""),
            ("Re-run the zero-rate case and a private-property case: 1200000 at 3.5% over 30 years.", "uv run python loan_calculator.py"),
            ("Compare your 500000 / 2.6% / 25-year answer with a bank's published mortgage calculator and record any difference in your lab notes.", ""),
        ],
        test="A loan of $500,000 at 2.6% over 25 years gives a monthly instalment of approximately $2,268.51 and total interest near $180,554. A rate of 0% returns principal/months with no ZeroDivisionError.",
    ),
    dict(
        num=7,
        topic=2,
        title="Retirement Savings Calculator",
        objective="LO2: Apply numeric data types, arithmetic operators and compound assignment to solve a retirement future-value calculation problem.",
        desc=(
            "Mirroring the reference notebook activity, the learner computes the future value of a regular "
            "monthly savings plan using the annuity formula, then adds a CPF top-up scenario and a "
            "year-by-year projection table so a client can see the compounding effect rather than just a "
            "single number."
        ),
        build="A script `retirement_calculator.py` that projects retirement savings from a monthly contribution, expected return and years to retirement.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project.", "uv init lab-07-retirement && cd lab-07-retirement"),
            ("Create retirement_calculator.py and collect the four planning inputs.", "current_age = int(input('Enter your current age: ')); retirement_age = int(input('Enter your target retirement age: ')); monthly_savings = float(input('Enter amount you save monthly: ')); annual_return_rate = float(input('Enter expected annual return rate (e.g., 5 for 5%): '))"),
            ("Derive the horizon in months and the monthly rate.", "months = (retirement_age - current_age) * 12; monthly_rate = annual_return_rate / 100 / 12"),
            ("Implement the future-value-of-an-annuity formula, guarding the zero-return case with a conditional.", "total = monthly_savings * (((1 + monthly_rate) ** months - 1) / monthly_rate) if monthly_rate > 0 else monthly_savings * months"),
            ("Print the projection with thousands separators, and print the total contributed so the client can see how much is growth rather than saving.", "print(f'Projected: ${total:,.2f} | Contributed: ${monthly_savings*months:,.2f} | Growth: ${total - monthly_savings*months:,.2f}')"),
            ("Run a realistic Singapore case: age 30 to 65, $1,000 a month, 5% expected return.", "uv run python retirement_calculator.py"),
            ("PROMPT THE AI ASSISTANT with: 'Extend retirement_calculator.py to also print a year-by-year table with columns Age, Contributed To Date, Balance and Growth, using a compound assignment (balance += ...) inside a loop over the months and printing one row at each year boundary. Add a CPF Special Account scenario at a fixed 4% return alongside the user rate, and print both projected balances side by side. Reject a retirement age not greater than the current age.' Apply the code.", ""),
            ("REVIEW the AI output: check the loop applies the monthly return before adding the contribution consistently, that the final loop balance agrees with the closed-form formula to within a dollar, and that the validation actually stops execution.", ""),
            ("Run and verify the closed-form and the iterative balance agree.", "uv run python retirement_calculator.py"),
            ("Test sensitivity: re-run at 3%, 5% and 7% and note in your lab record how much of the final balance is growth in each case.", "uv run python retirement_calculator.py"),
            ("Discuss: what does this model ignore — inflation, fees, sequence-of-returns risk — and how would you disclose that to a client?", ""),
        ],
        test="Saving $1,000 a month from age 30 to 65 at 5% projects approximately $1,136,000, with roughly $420,000 contributed and the remainder growth; the year-by-year table's final row matches the closed-form figure.",
    ),
    dict(
        num=8,
        topic=2,
        title="String Methods and Extracting the Company Name from an Email",
        objective="LO2: Apply the string data type and its methods to parse, clean and classify financial client data.",
        desc=(
            "The learner exercises the core string methods — len, upper, lower, strip, split, startswith, "
            "replace — on messy client data, then mirrors the reference notebook activity by extracting a "
            "corporate client's company name from an email address, hardening it against malformed input "
            "and free-email domains such as gmail.com."
        ),
        build="A script `extract_company.py` that parses an email address and returns the corporate client's company name, with validation.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project.", "uv init lab-08-string-methods && cd lab-08-string-methods"),
            ("Create strings_demo.py using a messy value of the kind that arrives from a CRM export, and print its length, upper case and stripped form.", "text = '  DBS Group Holdings Ltd.  '; print(len(text), text.upper(), repr(text.strip()))"),
            ("Split it into words and test a prefix, the way a screening rule would.", "print(text.strip().split(' '), text.strip().startswith('DBS'))"),
            ("Clean a ticker field with replace and strip so 'd05 .si ' becomes a valid uppercase ticker.", "print(' d05 .si '.replace(' ', '').upper())"),
            ("Now start extract_company.py and implement the reference activity: split the email on '@' and take the first label of the domain.", "email = input('Enter your email address: '); parts = email.split('@')"),
            ("Guard the split and extract the company label, printing it in upper case.", "if len(parts) == 2: print(f\"Extracted Company Name: {parts[1].split('.')[0].upper()}\")"),
            ("Run it against angch@tertiaryinfotech.com and against treasury@dbs.com.sg.", "uv run python extract_company.py"),
            ("PROMPT THE AI ASSISTANT with: 'Harden extract_company.py. Reject an input with no @ or more than one @, or an empty local part or domain, printing a clear validation message. Treat gmail.com, yahoo.com, hotmail.com and outlook.com as personal domains and print PERSONAL ACCOUNT - NOT A CORPORATE CLIENT instead of a company name. Handle multi-level domains such as dbs.com.sg by taking only the first label. Also add a function that processes a list of ten sample client emails and prints a table of email, company and account type.' Apply the code.", ""),
            ("REVIEW the AI output: check the personal-domain list is compared in lower case, that the multi-@ case is genuinely rejected, and that the batch function does not stop at the first bad row.", ""),
            ("Run the batch function and confirm the table.", "uv run python extract_company.py"),
            ("Test the edge cases: 'no-at-sign', 'a@@b.com', '@dbs.com', 'user@', and 'ANALYST@UOB.COM.SG'.", "uv run python extract_company.py"),
        ],
        test="treasury@dbs.com.sg returns 'DBS', analyst@uob.com.sg returns 'UOB', jane@gmail.com is flagged as a personal account, and every malformed input prints a validation message rather than a traceback.",
    ),
    dict(
        num=9,
        topic=2,
        title="Lists — Top 10 SGX Companies by Market Capitalisation",
        objective="LO2: Apply the list data type, indexing, slicing and sorting to rank financial instruments by a business metric.",
        desc=(
            "The learner exercises list creation, indexing, slicing, index() and pop() on a price series, "
            "then mirrors the reference notebook activity by fetching market capitalisation for a basket "
            "of SGX tickers with yfinance and producing a ranked top-10 list of Singapore's largest "
            "listed companies."
        ),
        build="A script `top10_sgx.py` that fetches market caps for a basket of SGX tickers and prints the top 10 ranked by market capitalisation.",
        services="uv, Python 3.12, yfinance, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project and add the market-data dependency with uv (not pip).", "uv init lab-09-top10-sgx && cd lab-09-top10-sgx && uv add yfinance"),
            ("Create lists_demo.py with a short closing-price series and practise indexing and slicing.", "prices = [35.20, 35.80, 36.10, 35.95, 36.40]; print(prices[0], prices[-1], prices[0:3])"),
            ("Find the position of a value and pop the latest observation — the two list operations used most in a rolling window.", "print(prices.index(36.10)); print(prices.pop(), prices)"),
            ("Create top10_sgx.py and define the SGX basket as a list of tickers.", "sgx_tickers = ['D05.SI','U11.SI','O39.SI','Z74.SI','J36.SI','BN4.SI','V03.SI','C38U.SI','A17U.SI','C07.SI','C31.SI','U96.SI','F34.SI','S68.SI','BS6.SI']"),
            ("Loop the basket, pull marketCap and shortName from yfinance, and append a dict per company to a results list, skipping any ticker that fails.", "company_data.append({'name': name, 'ticker': ticker, 'market_cap': market_cap})"),
            ("Sort descending by market cap and slice the top ten.", "top_10 = sorted(company_data, key=lambda x: x['market_cap'], reverse=True)[:10]"),
            ("Run it and note how long the fetch takes — API latency is a design constraint in any production screen.", "uv run python top10_sgx.py"),
            ("PROMPT THE AI ASSISTANT with: 'Improve top10_sgx.py. Skip any ticker whose marketCap is missing or zero instead of ranking it as zero. Print a numbered table with rank, company name, ticker and market cap formatted in SGD billions to two decimals, plus a final line giving the combined market cap of the top 10 and each company's percentage share of that total. Cache the fetched results to a local JSON file so a re-run does not hit the API again.' Apply the code.", ""),
            ("REVIEW the AI output: confirm missing caps are filtered before the sort, that the percentage shares total 100%, and that the cache is read before the network call rather than after.", ""),
            ("Run the improved script twice and confirm the second run is served from the cache.", "uv run python top10_sgx.py"),
            ("Add a deliberately invalid ticker 'ZZZZ.SI' to the basket and re-run to prove the skip logic holds.", "uv run python top10_sgx.py"),
        ],
        test="The script prints a numbered top-10 table led by DBS (D05.SI) with market caps in SGD billions, the percentage shares sum to 100%, and the invalid ticker is silently skipped.",
    ),
    dict(
        num=10,
        topic=2,
        title="Tuples — Immutable Instrument Identifiers",
        objective="LO2: Apply the tuple data type and unpacking to represent fixed financial identifiers that must not change during processing.",
        desc=(
            "The learner creates tuples of SGX tickers and OHLC records, practises indexing, slicing, "
            "length and unpacking, and proves immutability by attempting a write. The lab then applies "
            "tuples where they genuinely belong in finance: as fixed instrument identifiers, as multiple "
            "return values from a ratio function, and as dictionary keys."
        ),
        build="A script `tuples_demo.py` demonstrating tuple unpacking of OHLC records and a function returning a tuple of financial ratios.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project.", "uv init lab-10-tuples && cd lab-10-tuples"),
            ("Create tuples_demo.py with the core bank tickers as an immutable tuple, and index and slice it.", "stock_tuple = ('D05.SI', 'U11.SI', 'O39.SI'); print(stock_tuple[0], stock_tuple[0:2], len(stock_tuple))"),
            ("Unpack the tuple into three named variables in one statement.", "ticker1, ticker2, ticker3 = stock_tuple; print(ticker1, ticker2, ticker3)"),
            ("Prove immutability: uncomment the assignment and observe the TypeError, then discuss why an approved instrument list should be immutable.", "stock_tuple[0] = 'S68.SI'"),
            ("Build a list of OHLC tuples for one trading day and unpack each in a loop.", "bars = [('D05.SI', 35.20, 36.10, 35.05, 35.90), ('U11.SI', 32.10, 32.80, 31.95, 32.60)]"),
            ("Iterate with tuple unpacking directly in the for statement.", "for tkr, o, h, l, c in bars: print(f'{tkr}: range {h-l:.2f}, change {c-o:+.2f}')"),
            ("PROMPT THE AI ASSISTANT with: 'Add a function ratios(net_profit, revenue, equity, assets) to tuples_demo.py that returns a tuple of net profit margin, ROE and ROA as percentages. Call it for DBS with net profit 11290000000, revenue 20180000000, equity 62400000000 and assets 739000000000, unpack the returned tuple into three variables and print each to two decimals with a percent sign. Then build a dictionary keyed by the tuple (ticker, financial_year) holding those ratios for two years and print it.' Apply the code.", ""),
            ("REVIEW the AI output: confirm the function returns a tuple rather than a list, that each ratio is multiplied by 100 exactly once, and that the tuple key is valid because it is immutable.", ""),
            ("Run the script.", "uv run python tuples_demo.py"),
            ("Try to use a list as the dictionary key instead of the tuple and observe the TypeError — this is the practical reason tuples exist.", "uv run python tuples_demo.py"),
        ],
        test="The OHLC loop prints the day range and change for each bank, ratios() returns a three-element tuple giving a DBS net margin near 55.95%, ROE near 18.09% and ROA near 1.53%, and the tuple-keyed dictionary prints without error.",
    ),
    dict(
        num=11,
        topic=2,
        title="Dictionaries — Company Stock Values and Market Cap Lookup",
        objective="LO2: Apply the dictionary data type to map financial instrument keys to values and build a fast lookup for portfolio reporting.",
        desc=(
            "Mirroring the reference notebook activity, the learner builds a dictionary of stock "
            "attributes, practises access, update, membership testing, pop and iteration, then constructs "
            "a ticker-to-market-cap dictionary with a comprehension and uses .get() with a default to "
            "make the lookup safe for a missing ticker."
        ),
        build="A script `stock_dict.py` holding a ticker-to-market-cap dictionary with a safe lookup and a formatted portfolio valuation.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project.", "uv init lab-11-dictionaries && cd lab-11-dictionaries"),
            ("Create stock_dict.py with a dictionary describing one holding, and read a value by key.", "stock_info = {'ticker': 'D05.SI', 'name': 'DBS Group Holdings', 'price': 35.50}; print(stock_info['name'])"),
            ("Add a new key and update an existing one — the two operations that make dictionaries the right structure for a mutable position record.", "stock_info['currency'] = 'SGD'; stock_info['price'] = 36.20"),
            ("Test membership before access, then pop a key and iterate the remaining items.", "if 'ticker' in stock_info: print(stock_info['ticker'])"),
            ("Iterate keys and values for a printed position record.", "for key, value in stock_info.items(): print(f'{key}: {value}')"),
            ("Build the ticker-to-market-cap dictionary with a dict comprehension over a list of company records.", "company_market_values = {item['ticker']: item['market_cap'] for item in top_10_data}"),
            ("Use .get() with a default so a delisted ticker returns a safe value instead of raising KeyError.", "print(f\"DBS market cap: ${company_market_values.get('D05.SI', 0):,.0f}\")"),
            ("Compare .get() with direct bracket access on a missing ticker and observe the KeyError.", "uv run python stock_dict.py"),
            ("PROMPT THE AI ASSISTANT with: 'Extend stock_dict.py with a portfolio dictionary mapping ticker to number of shares for D05.SI 2000, U11.SI 1500, O39.SI 3000 and Z74.SI 10000, and a prices dictionary for the same tickers. Compute each position value and the total portfolio value, print a table of ticker, shares, price, value and weight as a percentage of the portfolio sorted by value descending, and use .get() with a default of 0 so a ticker missing from prices reports a value of zero with a warning line rather than crashing.' Apply the code.", ""),
            ("REVIEW the AI output: confirm the weights sum to 100%, that .get() defaults are used on the prices lookup and not on the shares lookup, and that the sort is descending by value.", ""),
            ("Delete Z74.SI from the prices dictionary and re-run to prove the warning path works.", "uv run python stock_dict.py"),
        ],
        test="The portfolio table prints four positions sorted by value with weights summing to 100%; removing Singtel from the prices dictionary produces a warning line and a zero-value row instead of a KeyError.",
    ),
    dict(
        num=12,
        topic=2,
        title="Sets and Operators — Common Holdings Across Portfolios",
        objective="LO2: Apply the set data type and arithmetic, compound, comparison, membership and logical operators to compare portfolios and encode financial rules.",
        desc=(
            "Mirroring the reference notebook activities, the learner uses set intersection, union and "
            "difference to find overlapping and unique holdings across two SGX portfolios and to "
            "de-duplicate a ticker list, then works through the full operator families — arithmetic, "
            "compound assignment, comparison, membership and logical — applied to a portfolio "
            "concentration and eligibility rule."
        ),
        build="A script `portfolio_sets.py` that reports common, unique and combined holdings across two portfolios plus an operator-driven eligibility check.",
        services="uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot",
        steps=[
            ("Create the project.", "uv init lab-12-sets-operators && cd lab-12-sets-operators"),
            ("Create portfolio_sets.py with two portfolios as sets of SGX tickers.", "set_a = {'D05.SI','U11.SI','O39.SI','Z74.SI','V03.SI'}; set_b = {'Z74.SI','C38U.SI','D05.SI','A17U.SI','S68.SI'}"),
            ("Find the overlap with intersection — these are the concentrated positions a risk officer cares about.", "print(f'Common: {set_a.intersection(set_b)}')"),
            ("Find the combined universe with union and the fund-specific holdings with difference.", "print(set_a.union(set_b)); print(set_a.difference(set_b)); print(set_b.difference(set_a))"),
            ("Add a ticker, then de-duplicate a messy list of tickers by converting it through a set.", "unique = list(set(['D05.SI','U11.SI','D05.SI','O39.SI','U11.SI'])); print(unique)"),
            ("Work the operators: use compound assignment to accumulate a running portfolio value, and membership to test whether a ticker is held.", "total = 0.0; total += 2000 * 35.90; print('D05.SI' in set_a)"),
            ("Combine comparison and logical operators into a real eligibility rule: a stock qualifies if ROE is above 10% AND the PE ratio is below 20, OR it is held in both portfolios.", "eligible = (roe > 10 and pe < 20) or (ticker in set_a.intersection(set_b))"),
            ("Run the script and check each operator's result against your expectation before trusting it.", "uv run python portfolio_sets.py"),
            ("PROMPT THE AI ASSISTANT with: 'Extend portfolio_sets.py so it prints a reconciliation report between the two portfolios: the count and list of common tickers, tickers only in Fund A, tickers only in Fund B, the total combined universe size, and the overlap percentage computed as the intersection size divided by the union size. Then add a screen that uses comparison, membership and logical operators to classify each ticker in the union as BUY, HOLD or REVIEW from a dictionary of ROE and PE values, treating a missing ROE or PE as REVIEW.' Apply the code.", ""),
            ("REVIEW the AI output: confirm the overlap percentage uses the union and not the sum of the two sets, that the missing-data branch is checked before the comparison operators run, and that the classifications are mutually exclusive.", ""),
            ("Run the reconciliation and the screen.", "uv run python portfolio_sets.py"),
            ("Test the edge cases: two identical portfolios (overlap should be 100%), two disjoint portfolios (0%), and a ticker whose PE is missing.", "uv run python portfolio_sets.py"),
        ],
        test="The reconciliation reports D05.SI and Z74.SI as the common tickers, an overlap of 25% across a combined universe of eight tickers, and every ticker in the union is classified as exactly one of BUY, HOLD or REVIEW with missing data landing in REVIEW.",
    ),
]
