"""
SINGLE SOURCE OF TRUTH — course metadata.

AI Assisted Python Programming for Finance (TGS-2025052659)
IBF-accredited under the Skills Framework for Financial Services,
IBF Standard FSE-DIT-3018-1.1, funded under the IBF Standards Training Scheme.

Every artifact (PPT, LP, LG, LG.md, labs index) is generated from this file plus
data_domain1.py … data_domain9.py so they stay 100% aligned.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "AI Assisted Python Programming for Finance"
SHORT_TITLE  = "AI Assisted Python Programming for Finance"
COURSE_CODE  = "TGS-2025052659"
VERSION      = "v31.0"
VERSION_DATE = "20 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 4

# ------------------------------------------------------------------ accreditation (IBF, not WSQ)
ACCREDITATION = dict(
    scheme="IBF-STS",
    standard="FSE-DIT-3018-1.1",
    framework="Skills Framework for Financial Services",
    body="The Institute of Banking and Finance Singapore (IBF)",
    website="www.ibf.org.sg",
    blurb=(
        "This course has been accredited under the Skills Framework for Financial Services, "
        "IBF Standards: FSE-DIT-3018-1.1, and is eligible for funding under the IBF Standards "
        "Training Scheme (IBF-STS), subject to all eligibility criteria being met. "
        "Participants are advised to assess the suitability of the course and its relevance to "
        "his/her business activities or job roles. The IBF-STS is available to eligible entities "
        "and individuals based on the prevalent funding eligibility, quantum and caps. IBF-STS "
        "provides 50% - 70% course fee subsidy support for direct training costs subject to a cap "
        "of S$3,000 per candidate per course subject to all eligibility criteria being met."
    ),
)

# ------------------------------------------------------------------ toolchain
TOOLING = dict(
    package_manager="uv",
    python="3.12",
    ide="Google Colab / Visual Studio Code / Cursor / AntiGravity",
    app_framework="Streamlit",
    note=(
        "All labs are managed with uv, the fast Python package and project manager. "
        "Learners run `uv init`, `uv add` and `uv run` instead of pip/venv."
    ),
)

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Translate business requirements in financial services into Python programming objectives, "
    "and set up an AI-assisted Python development environment.",
    "LO2: Apply Python data types, operators and control structures to solve financial calculation "
    "and classification problems.",
    "LO3: Construct reusable functions and lambda expressions to compute financial ratios and "
    "metrics for business use cases.",
    "LO4: Implement error handling to build robust financial programs that survive missing, zero "
    "or malformed market data.",
    "LO5: Import, clean, filter and process financial data using the pandas package.",
    "LO6: Aggregate and visualise financial data with groupby, pivot tables and charts, and publish "
    "the results as an interactive Streamlit application.",
    "LO7: Apply object-oriented programming to model financial instruments and analysers.",
    "LO8: Analyse financial data using apply and pipe pipelines, assess code to identify gaps, and "
    "test the results.",
]

# ------------------------------------------------------------------ topics (= skills domains)
TOPICS = [
    dict(num=1, code="01",
         title="Introduction to Python Programming",
         subtitle="Business requirements · Applications in financial services · AI-assisted Python IDE setup with uv",
         weighting="8%",
         concepts=[
             "Python is the leading language in financial services for algorithmic trading, "
             "financial analysis and modelling, portfolio management, fraud detection and risk management.",
             "Business requirements are translated into programming objectives before any code is written.",
             "AI-assisted development tools — Google Colab, VS Code, Cursor and AntiGravity — generate, "
             "explain and refactor Python code from natural-language prompts.",
             "uv is the modern Python project manager: `uv init` creates a project, `uv add` installs "
             "dependencies, and `uv run` executes scripts in a reproducible environment.",
             "Every prompt-generated snippet must be reviewed, tested and understood before it enters "
             "a production financial system.",
         ]),
    dict(num=2, code="02",
         title="Data Types and Operators",
         subtitle="Numbers · Strings · List · Tuple · Dictionary · Set · Operators",
         weighting="12%",
         concepts=[
             "Python supports six major data types used constantly in finance: number, string, list, "
             "tuple, dictionary and set.",
             "String literal formatting (f-strings) renders currency, percentages and millions in "
             "board-ready precision.",
             "Lists are ordered and mutable — ideal for time series of prices; tuples are immutable — "
             "ideal for fixed instrument identifiers.",
             "Dictionaries map a ticker key to a value such as market capitalisation, and sets remove "
             "duplicate tickers and find common holdings across portfolios.",
             "Arithmetic, compound, comparison, membership and logical operators express financial "
             "rules directly in code.",
         ]),
    dict(num=3, code="03",
         title="Problem Solving with Control Structures",
         subtitle="If-Else · If-Elif · Ternary · While · For · Range · Enumerate · Zip · Break · Continue · Comprehensions",
         weighting="14%",
         concepts=[
             "Conditional logic encodes investment rules: a PE ratio or ROE threshold becomes a "
             "BUY / HOLD / SELL recommendation.",
             "While loops repeat until a condition is met — used for Fibonacci sequences underlying "
             "the golden ratio in technical analysis.",
             "For loops with range, enumerate and zip iterate portfolios and combine parallel series "
             "such as tickers with their ROE and ROA.",
             "Break and continue control early exit and skipping when scanning market data.",
             "List, set and dict comprehensions compute metrics such as net profit margin across a "
             "portfolio in a single readable line.",
         ]),
    dict(num=4, code="04",
         title="Scripting with Function and Lambda",
         subtitle="Functions · Return values · Argument styles · Lambda · Map · Filter",
         weighting="14%",
         concepts=[
             "Functions are reusable blocks that turn a business requirement into a named, testable unit.",
             "A function can return multiple values, letting one call deliver a full set of financial ratios.",
             "Multiple, default, named and variable arguments make a pricing or ratio function flexible "
             "without duplication.",
             "Lambda creates small anonymous functions for one-off financial formulas.",
             "Map applies a lambda across a sequence of stocks; filter selects the subset that meets a "
             "business threshold such as high-income customers.",
         ]),
    dict(num=5, code="05",
         title="Error Handling Using Exception",
         subtitle="Exceptions versus syntax errors · Try and Except · Else clause · Finally",
         weighting="10%",
         concepts=[
             "An exception is an event during execution that disrupts normal flow — distinct from a "
             "syntax error, which prevents the program from running at all.",
             "Try/except blocks keep a financial pipeline alive when a ticker is delisted, an API "
             "fails or a denominator is zero.",
             "Common errors in finance code: IndexError, KeyError, TypeError, ValueError and "
             "ZeroDivisionError from a zero equity or revenue base.",
             "The else clause runs when no exception occurred; finally always runs and is used to "
             "release connections and write audit logs.",
             "Robust error handling is a regulatory expectation — a silent failure in a risk model is "
             "worse than a loud one.",
         ]),
    dict(num=6, code="06",
         title="Import and Process Finance Data",
         subtitle="Pandas package · DataFrame and Series · Import · Filter and slice · Clean missing data",
         weighting="14%",
         concepts=[
             "Pandas is the workhorse of financial data analysis; Series is a single labelled column "
             "and DataFrame is a labelled table.",
             "Financial data is imported from CSV, Excel and market APIs such as yfinance.",
             "Filtering and slicing select the rows and columns relevant to an analysis — a date "
             "range, a sector, or a set of tickers.",
             "Missing market data is detected and cleaned by dropping or imputing, and the choice "
             "must be documented because it changes the result.",
             "Moving averages and returns are derived columns that feed trading signals.",
         ]),
    dict(num=7, code="07",
         title="Aggregate and Visualize Finance Data",
         subtitle="Concat, append and merge · Groupby · Pivot table · Assess code for gaps · Test and visualise · Streamlit",
         weighting="14%",
         concepts=[
             "Finance datasets are joined with concat, append and merge to combine prices, "
             "fundamentals and customer records.",
             "Groupby aggregates loan and portfolio data by sector, region, gender or status.",
             "Pivot tables cross-tabulate metrics such as average debt-to-income ratio by segment.",
             "Charts turn an aggregation into a decision — trends, distributions and comparisons.",
             "Streamlit publishes the analysis as an interactive web application that a business user "
             "can operate without touching Python.",
         ]),
    dict(num=8, code="08",
         title="Object Oriented Programming",
         subtitle="Classes and objects · Methods and overloading · Initializer and destructor · Inheritance · Polymorphism",
         weighting="8%",
         concepts=[
             "A class is the blueprint of an object, bundling data (attributes) with behaviour (methods).",
             "An object is an instance of a class — one Stock object per holding in a portfolio.",
             "The initializer __init__ sets up an instance's state; the destructor releases resources.",
             "Inheritance lets an Equity or Bond class extend a common Instrument class without "
             "duplicating code.",
             "Polymorphism allows one valuation call to behave correctly for every instrument type.",
         ]),
    dict(num=9, code="09",
         title="Analyze Finance Data",
         subtitle="Improve code with apply and pipe · Applications of statistics · Analyse finance data to track changes",
         weighting="6%",
         concepts=[
             "The .apply() method runs a function across rows or columns — used to classify credit risk "
             "row by row.",
             "The .pipe() method chains transformations into a readable, testable data pipeline.",
             "Descriptive statistics — mean, median, standard deviation and correlation — summarise "
             "risk and return.",
             "Tracking changes over time reveals trend, volatility and drawdown.",
             "The finished analysis is delivered as a Streamlit capstone dashboard for stakeholders.",
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Python Foundations for Finance — environment, data types and control structures",
    2: "Reusable and Robust Code — functions, lambda and exception handling",
    3: "Financial Data Analysis — pandas, aggregation, visualisation and Streamlit",
    4: "Object-Oriented Finance and Analysis — OOP, apply/pipe, capstone and assessment",
}

# ------------------------------------------------------------------ day → topic mapping (mirrors reference deck)
DAY_TOPICS = {
    1: [1, 2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, 9],
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), open-ended, 1 hour, open book.",
    practical=(
        "Practical Test (PP) — 7 open-ended practical tasks based on the Financial Data Solutions Inc. "
        "scenario, mapped to abilities A1.1–A1.9, 120 minutes, open book."
    ),
    passing_score="80%",
    note=(
        "A minimum of 75% attendance is required to be eligible for assessment and IBF-STS funding. "
        "Open book assessment includes the slides, Learner Guide and lab files only."
    ),
)
