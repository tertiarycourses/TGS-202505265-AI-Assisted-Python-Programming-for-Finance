# AI Assisted Python Programming for Finance — Hands-On Labs

Course code **TGS-2025052659** · Tertiary Infotech Academy Pte Ltd · Version v31.0 (20 July 2026)

62 labs across 9 topics. Every lab is a self-contained [uv](https://docs.astral.sh/uv/) project.

## Getting started

```bash
# install uv once
curl -LsSf https://astral.sh/uv/install.sh | sh

# each lab is its own project
cd lab-01-*/
uv init .
uv add pandas yfinance matplotlib
uv run python *.py
```

All labs are also combined into a single notebook you can open in Google Colab: [`AI Assisted Python Programming for Finance-All-Labs.ipynb`](AI Assisted Python Programming for Finance-All-Labs.ipynb).

## Labs by topic

### Topic 1 — Introduction to Python Programming

*Business requirements · Applications in financial services · AI-assisted Python IDE setup with uv*

| # | Lab | You'll build |
|---|-----|--------------|
| 1 | [Set Up an AI-Assisted Python Environment with uv](lab-01-set-up-an-ai-assisted-python-environment-with-uv/README.md) | A working uv project `lab-01-hello-finance` with yfinance and pandas installed, and an environment-check script that prints the course SGX watchlist. |
| 2 | [Hello World — Your First Finance Script](lab-02-hello-world-your-first-finance-script/README.md) | A script `hello_finance.py` that prints a formatted trading-desk banner with a currency-formatted portfolio value. |
| 3 | [CPF Contribution Calculator](lab-03-cpf-contribution-calculator/README.md) | A script `cpf_calculator.py` that takes a monthly salary and age and prints the employee, employer and total CPF contribution with the wage ceiling applied. |
| 4 | [From Business Requirement to Programming Objective — SGX Price Fetcher](lab-04-from-business-requirement-to-programming-objecti/README.md) | A requirements note plus `sgx_prices.py`, which fetches and prints the latest close for DBS, UOB, OCBC, Singtel and CapitaLand. |

### Topic 2 — Data Types and Operators

*Numbers · Strings · List · Tuple · Dictionary · Set · Operators*

| # | Lab | You'll build |
|---|-----|--------------|
| 5 | [Number and String Literal Formatting for Financial Reporting](lab-05-number-and-string-literal-formatting-for-financi/README.md) | A script `format_report.py` that renders a set of raw financial figures as a formatted revenue and market-cap summary in millions. |
| 6 | [Loan Amortisation Calculator](lab-06-loan-amortisation-calculator/README.md) | A script `loan_calculator.py` that returns the monthly instalment, total repayment and total interest for a given principal, annual rate and tenor. |
| 7 | [Retirement Savings Calculator](lab-07-retirement-savings-calculator/README.md) | A script `retirement_calculator.py` that projects retirement savings from a monthly contribution, expected return and years to retirement. |
| 8 | [String Methods and Extracting the Company Name from an Email](lab-08-string-methods-and-extracting-the-company-name-f/README.md) | A script `extract_company.py` that parses an email address and returns the corporate client's company name, with validation. |
| 9 | [Lists — Top 10 SGX Companies by Market Capitalisation](lab-09-lists-top-10-sgx-companies-by-market-capitalisat/README.md) | A script `top10_sgx.py` that fetches market caps for a basket of SGX tickers and prints the top 10 ranked by market capitalisation. |
| 10 | [Tuples — Immutable Instrument Identifiers](lab-10-tuples-immutable-instrument-identifiers/README.md) | A script `tuples_demo.py` demonstrating tuple unpacking of OHLC records and a function returning a tuple of financial ratios. |
| 11 | [Dictionaries — Company Stock Values and Market Cap Lookup](lab-11-dictionaries-company-stock-values-and-market-cap/README.md) | A script `stock_dict.py` holding a ticker-to-market-cap dictionary with a safe lookup and a formatted portfolio valuation. |
| 12 | [Sets and Operators — Common Holdings Across Portfolios](lab-12-sets-and-operators-common-holdings-across-portfo/README.md) | A script `portfolio_sets.py` that reports common, unique and combined holdings across two portfolios plus an operator-driven eligibility check. |

### Topic 3 — Problem Solving with Control Structures

*If-Else · If-Elif · Ternary · While · For · Range · Enumerate · Zip · Break · Continue · Comprehensions*

| # | Lab | You'll build |
|---|-----|--------------|
| 13 | [If-Else PE Ratio Valuation — BUY / HOLD / SELL](lab-13-if-else-pe-ratio-valuation-buy-hold-sell/README.md) | pe_valuation.py — a uv-managed script that reads a PE ratio and prints a formatted valuation and recommendation, with input validation. |
| 14 | [Activity: Return on Equity (ROE) Screener with a BUY / SELL Threshold](lab-14-activity-return-on-equity-roe-screener-with-a-bu/README.md) | roe_screener.py — computes ROE for D05.SI from live yfinance statements and prints a threshold-based BUY/SELL recommendation. |
| 15 | [If-Elif Income Grouping and Credit Risk Banding](lab-15-if-elif-income-grouping-and-credit-risk-banding/README.md) | income_grouping.py — classifies annual income into four bands and a credit score into four risk categories, with range validation. |
| 16 | [Ternary Operator — One-Line Trading Decisions](lab-16-ternary-operator-one-line-trading-decisions/README.md) | ternary_decisions.py — a set of one-line ternary rules covering buy/wait, margin call, yield flagging and zero-safe division. |
| 17 | [While Loop — Fibonacci Sequence and the Golden Ratio in Technical Analysis](lab-17-while-loop-fibonacci-sequence-and-the-golden-rat/README.md) | fibonacci_ta.py — generates the Fibonacci sequence with a while loop, shows golden-ratio convergence, and prints Fibonacci retracement price levels for a stock's swing high and low. |
| 18 | [For Loop and Range — Top 10 SGX Return on Assets (ROA) Ranking](lab-18-for-loop-and-range-top-10-sgx-return-on-assets-r/README.md) | roa_ranking.py — fetches fundamentals for 10 SGX tickers in a for loop and prints a sorted Top 10 ROA league table. |
| 19 | [Enumerate, Zip, Break and Continue — Combined ROE and ROA Scanner](lab-19-enumerate-zip-break-and-continue-combined-roe-an/README.md) | roe_roa_scanner.py — a combined ROE + ROA screening table built with zip and enumerate, with continue-based skipping and a break-controlled budget allocator. |
| 20 | [Comprehensions — Net Profit Margin for 10 Singapore Stocks in One Line](lab-20-comprehensions-net-profit-margin-for-10-singapor/README.md) | margin_comprehensions.py — computes net profit margin for 10 SGX stocks with a list comprehension, plus set and dict comprehension utilities and a filtered high-margin lookup. |

### Topic 4 — Scripting with Function and Lambda

*Functions · Return values · Argument styles · Lambda · Map · Filter*

| # | Lab | You'll build |
|---|-----|--------------|
| 21 | [Functions — A Reusable Financial Formula Library](lab-21-functions-a-reusable-financial-formula-library/README.md) | finance_formulas.py — a module of documented, reusable financial functions (CAGR, simple interest, break-even units) with a demonstration block. |
| 22 | [Return Multiple Values — A Full Income Statement Analysis in One Call](lab-22-return-multiple-values-a-full-income-statement-a/README.md) | income_analysis.py — an income statement analyser returning gross profit, net income and margin, in tuple, dict and namedtuple variants. |
| 23 | [Activity: Net Profit Margin Function with Zero-Revenue Handling](lab-23-activity-net-profit-margin-function-with-zero-re/README.md) | net_profit_margin.py — a validated net profit margin function with assertion-based tests, applied to live SGX financial statements. |
| 24 | [Multiple, Default and Named Arguments — A Flexible Valuation Toolkit](lab-24-multiple-default-and-named-arguments-a-flexible/README.md) | valuation_toolkit.py — portfolio total, net salary, investment projection, dividend yield and ROI functions demonstrating multiple, default and named arguments. |
| 25 | [Variable Arguments — *args and **kwargs for Portfolios of Any Size](lab-25-variable-arguments-args-and-kwargs-for-portfolio/README.md) | variable_args.py — variable-argument portfolio, expense and metric functions using *args and **kwargs, plus argument unpacking from existing collections. |
| 26 | [Activity: Max ROE Function — Finding the Best Performer in a Portfolio](lab-26-activity-max-roe-function-finding-the-best-perfo/README.md) | max_roe.py — fetches ROE for 10 SGX tickers and reports the top performer via a hand-written max function, a built-in max version and a generalised find_max_by. |
| 27 | [Lambda and Map — Gross Profit Margin and ROE Across a Portfolio](lab-27-lambda-and-map-gross-profit-margin-and-roe-acros/README.md) | lambda_map.py — gross profit margin and ROE computed with lambda expressions and applied across a portfolio using map, benchmarked against a list comprehension. |
| 28 | [Filter — Top Income Customers and High-ROE Stock Screening](lab-28-filter-top-income-customers-and-high-roe-stock-s/README.md) | customer_filter.py — a filter-based screening tool producing a ranked top-income customer list, a high-ROE stock screen and a chained filter-then-map pipeline. |

### Topic 5 — Error Handling Using Exception

*Exceptions versus syntax errors · Try and Except · Else clause · Finally*

| # | Lab | You'll build |
|---|-----|--------------|
| 29 | [Exceptions vs Syntax Errors in a Price Loader](lab-29-exceptions-vs-syntax-errors-in-a-price-loader/README.md) | A uv project `lab-29-exception-basics` containing price_loader.py, a captured traceback file traceback.txt, and a short written comparison of syntax errors versus exceptions. |
| 30 | [Try/Except on a Failing Market-Data Fetch](lab-30-try-except-on-a-failing-market-data-fetch/README.md) | A uv project `lab-30-market-fetch` with fetch_prices.py that returns a summary dict of successful tickers and a separate list of failed tickers with the reason for each failure. |
| 31 | [ZeroDivisionError in an ROE and Ratio Calculator](lab-31-zerodivisionerror-in-an-roe-and-ratio-calculator/README.md) | A uv project `lab-31-roe-guard` with ratios.py exposing safe_roe(), safe_margin() and safe_debt_to_equity(), all returning None with a printed warning when the ratio is undefined. |
| 32 | [KeyError and ValueError in a Portfolio Input Handler](lab-32-keyerror-and-valueerror-in-a-portfolio-input-han/README.md) | A uv project `lab-32-portfolio-input` with portfolio_tool.py providing a resilient ticker lookup and a validated loan-amount prompt that never crashes on bad input. |
| 33 | [Else, Finally and a Custom InsufficientDataError for a Risk Model](lab-33-else-finally-and-a-custom-insufficientdataerror/README.md) | A uv project `lab-33-risk-guard` with risk_model.py defining InsufficientDataError, a guarded compute_volatility(), and audit.log recording every run whether it succeeded or failed. |
| 34 | [Activity: Loan Risk Classifier with Guarded Data Loading](lab-34-activity-loan-risk-classifier-with-guarded-data/README.md) | A uv project `lab-34-loan-risk-classifier` with loan_risk.py, a synthetic-data fallback, a printed classification report, confusion_matrix.png and roc_curve.png. |

### Topic 6 — Import and Process Finance Data

*Pandas package · DataFrame and Series · Import · Filter and slice · Clean missing data*

| # | Lab | You'll build |
|---|-----|--------------|
| 35 | [Pandas Series vs DataFrame with Price Data](lab-35-pandas-series-vs-dataframe-with-price-data/README.md) | A uv project `lab-35-series-dataframe` with series_vs_frame.py demonstrating Series construction, DataFrame construction, column and row selection, and a printed comparison of .loc versus .iloc. |
| 36 | [Import Finance Data from CSV](lab-36-import-finance-data-from-csv/README.md) | A uv project `lab-36-csv-import` containing prices.csv, load_csv.py with a correctly parameterised read_csv call, and a printed dtype report proving Close is float64 and the index is a DatetimeIndex. |
| 37 | [Import Live Market Data with yfinance](lab-37-import-live-market-data-with-yfinance/README.md) | A uv project `lab-37-yfinance-import` with load_market.py producing a tidy long-format DataFrame and a cached market_data.csv covering three years and at least four tickers. |
| 38 | [Inspect a Dataset with head, info and describe](lab-38-inspect-a-dataset-with-head-info-and-describe/README.md) | A uv project `lab-38-inspect-data` with profile.py printing a full data-quality report and a written list of every anomaly found in the dataset. |
| 39 | [Filter and Slice by Date, Sector and Ticker](lab-39-filter-and-slice-by-date-sector-and-ticker/README.md) | A uv project `lab-39-filter-slice` with screen.py answering five stated screening questions, each as a documented boolean mask. |
| 40 | [Handle Missing Market Data and Compare the Choices](lab-40-handle-missing-market-data-and-compare-the-choic/README.md) | A uv project `lab-40-missing-data` with clean_compare.py printing a comparison table of total return, mean daily return and annualised volatility under each of the four treatments, plus a written recommendation. |
| 41 | [Derived Columns — Daily Returns and Moving Averages](lab-41-derived-columns-daily-returns-and-moving-average/README.md) | A uv project `lab-41-derived-columns` with features.py producing enriched_prices.csv containing daily_return, log_return, cum_return, sma_20, sma_50 and vol_20 per ticker. |
| 42 | [Activity: Algorithmic Trading — Moving Average Crossover Backtest](lab-42-activity-algorithmic-trading-moving-average-cros/README.md) | A uv project `lab-42-ma-crossover-backtest` with backtest.py, a printed KPI table comparing the strategy with buy-and-hold, and backtest_chart.png showing price, both SMAs and the marked signals. |

### Topic 7 — Aggregate and Visualize Finance Data

*Concat, append and merge · Groupby · Pivot table · Assess code for gaps · Test and visualise · Streamlit*

| # | Lab | You'll build |
|---|-----|--------------|
| 43 | [Generate Mock Credit-Loan Data with df_finance](lab-43-generate-mock-credit-loan-data-with-df-finance/README.md) | A uv project containing generate_data.py and a saved df_finance.csv of 500 mock loan applicants. |
| 44 | [Join Finance Datasets with concat, append and merge](lab-44-join-finance-datasets-with-concat-append-and-mer/README.md) | A join_data.py script producing df_all — the combined multi-branch loan book enriched with regional risk ratings. |
| 45 | [Groupby: Annual Income by Gender and Region](lab-45-groupby-annual-income-by-gender-and-region/README.md) | A groupby_income.py script printing income statistics by Gender, by Region and by the Gender x Region cross-section. |
| 46 | [Loan Application Counts by Status and Type](lab-46-loan-application-counts-by-status-and-type/README.md) | A loan_counts.py script producing a Loan_Type x Loan_Status count table plus an approval-rate table. |
| 47 | [Multi-Metric Aggregation by Employment Sector with .agg()](lab-47-multi-metric-aggregation-by-employment-sector-wi/README.md) | A sector_agg.py script producing a flat, renamed one-row-per-sector summary table exported to sector_summary.csv. |
| 48 | [Pivot Table of Debt-to-Income Ratio and Matplotlib Visualisation](lab-48-pivot-table-of-debt-to-income-ratio-and-matplotl/README.md) | A pivot_and_charts.py script writing dti_pivot.csv plus chart_income_by_sector.png, chart_approval_by_score.png and chart_dti_distribution.png. |
| 49 | [Streamlit Capstone Part 1 — Portfolio & Loan Analytics App Shell](lab-49-streamlit-capstone-part-1-portfolio-loan-analyti/README.md) | A Streamlit project with app.py serving the filtered KPI dashboard at localhost:8501. |
| 50 | [Streamlit Capstone Part 2 — Charts and Pivot Tab in the Dashboard](lab-50-streamlit-capstone-part-2-charts-and-pivot-tab-i/README.md) | An extended app.py with a three-tab analytics section: sector charts, loan mix, and a user-configurable risk pivot. |

### Topic 8 — Object Oriented Programming

*Classes and objects · Methods and overloading · Initializer and destructor · Inheritance · Polymorphism*

| # | Lab | You'll build |
|---|-----|--------------|
| 51 | [Build a Stock Class — Attributes, Methods and __init__](lab-51-build-a-stock-class-attributes-methods-and-init/README.md) | A stock.py module defining the Stock class with four financial methods, plus a demo creating three holdings. |
| 52 | [A Portfolio Class Holding Many Stock Objects](lab-52-a-portfolio-class-holding-many-stock-objects/README.md) | A portfolio.py module defining Portfolio, importing Stock from lab 51, with a demo book of six holdings. |
| 53 | [Dunder Methods — __str__, __repr__, __len__ and __add__ to Combine Portfolios](lab-53-dunder-methods-str-repr-len-and-add-to-combine-p/README.md) | Enhanced stock.py and portfolio.py with six dunder methods, supporting print(), len(), iteration and portfolio_a + portfolio_b. |
| 54 | [Inheritance — an Instrument Base Class with Equity and Bond Subclasses](lab-54-inheritance-an-instrument-base-class-with-equity/README.md) | An instruments.py module with Instrument, Equity and Bond classes, each subclass calling super().__init__(). |
| 55 | [Polymorphism — One .value() Call Across a Mixed Instrument Book](lab-55-polymorphism-one-value-call-across-a-mixed-instr/README.md) | A book.py script valuing a heterogeneous instrument book through one polymorphic loop, plus an asset-class breakdown. |
| 56 | [StockTechnicalAnalyzer — an OOP Class Computing SMA, RSI and BUY/SELL Signals](lab-56-stocktechnicalanalyzer-an-oop-class-computing-sm/README.md) | An analyzer.py module defining StockTechnicalAnalyzer, producing a signals table and a two-panel PNG chart. |

### Topic 9 — Analyze Finance Data

*Improve code with apply and pipe · Applications of statistics · Analyse finance data to track changes*

| # | Lab | You'll build |
|---|-----|--------------|
| 57 | [Credit Risk Classification with .apply()](lab-57-credit-risk-classification-with-apply/README.md) | A risk_apply.py script adding Calculated_Risk_Score and Risk_Profile columns to df_finance and exporting df_scored.csv. |
| 58 | [Lambda versus Named Functions in .apply()](lab-58-lambda-versus-named-functions-in-apply/README.md) | A classify.py module with three implementations plus test_classify.py containing passing boundary-value tests. |
| 59 | [Building a clean → enrich → score Pipeline with .pipe()](lab-59-building-a-clean-enrich-score-pipeline-with-pipe/README.md) | A pipeline.py module of four pipe-able functions and a single readable chained expression producing sector_pipeline_summary.csv. |
| 60 | [Descriptive Statistics, Correlation and Tracking Change Over Time](lab-60-descriptive-statistics-correlation-and-tracking/README.md) | A stats_analysis.py script producing the loan-book statistics and correlation matrix, plus a drawdown/volatility report and chart. |
| 61 | [Streamlit Capstone Part 3 — Technical Analysis and Risk Scoring Pages](lab-61-streamlit-capstone-part-3-technical-analysis-and/README.md) | A multi-page app.py with Loan Analytics, Technical Analysis and Risk Scoring pages, importing analyzer.py and pipeline.py. |
| 62 | [Streamlit Capstone Finale — Test, Polish and Deploy the Analytics App](lab-62-streamlit-capstone-finale-test-polish-and-deploy/README.md) | The finished, tested and deployed Portfolio & Loan Analytics application with a README and a passing test suite. |
