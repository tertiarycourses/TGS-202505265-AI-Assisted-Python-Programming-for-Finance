"""
Topic 8 — Object Oriented Programming (labs 51-56).

Maps to LO7: apply object-oriented programming to model financial instruments
and analysers.

The arc: a Stock class (51) -> a Portfolio holding many Stocks (52) -> dunder
methods so portfolios print and combine naturally (53) -> an Instrument base
class with Equity and Bond subclasses (54) -> polymorphic valuation across a
mixed book (55) -> the reference slide-148 StockTechnicalAnalyzer producing
SMA, RSI and BUY/SELL signals (56), which Topic 9's capstone consumes.
All labs use uv, never pip/venv.
"""

DOMAIN8 = [
    dict(
        num=51,
        topic=8,
        title="Build a Stock Class — Attributes, Methods and __init__",
        objective="LO7: Model a financial instrument as a class with attributes and behaviour, initialised through __init__.",
        desc=(
            "The learner writes the first finance class: Stock. Instance attributes (ticker, name, "
            "sector, shares, buy_price, current_price) are set in the __init__ initializer, and "
            "methods add behaviour — market_value(), cost_basis(), unrealised_pnl() and "
            "pnl_percent(). The lab contrasts a class attribute (a shared CURRENCY = 'SGD') with "
            "instance attributes, and shows why every holding needs its own state."
        ),
        build="A stock.py module defining the Stock class with four financial methods, plus a demo creating three holdings.",
        services="uv, Python 3.12, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project.", "uv init lab-51-stock-class && cd lab-51-stock-class"),
            ("Write a minimal class by hand first — class Stock with a class attribute CURRENCY = 'SGD' and a method describe() — to see the blueprint-versus-instance distinction before adding __init__.", ""),
            ("Prompt your AI assistant: \"Write a Python class Stock for a portfolio holding. The __init__ initializer takes ticker, name, sector, shares, buy_price and current_price and stores them as instance attributes, with a class attribute CURRENCY = 'SGD'. Add methods market_value() returning shares * current_price, cost_basis() returning shares * buy_price, unrealised_pnl() returning market_value minus cost_basis, and pnl_percent() returning the P&L as a percentage of cost basis guarding against a zero cost basis. Add a describe() method printing a formatted one-line summary with the currency.\"", ""),
            ("Save the answer as stock.py. Read it and confirm every method takes self as its first parameter and reads attributes via self.", ""),
            ("Create three objects — instances of the same class with different state.", "uv run python -c \"from stock import Stock; s=Stock('D05','DBS Group','Banking',500,32.10,38.40); print(s.market_value(), s.unrealised_pnl(), round(s.pnl_percent(),2))\""),
            ("Prove instance independence: create two Stock objects, change current_price on one, and confirm the other is unaffected.", ""),
            ("Prove the class attribute is shared: print Stock.CURRENCY and s.CURRENCY and confirm they are the same object.", ""),
            ("Test the zero-cost-basis guard by creating a Stock with buy_price=0 and calling pnl_percent().", "uv run python -c \"from stock import Stock; s=Stock('X','Test','Tech',10,0,5); print(s.pnl_percent())\""),
            ("Write a demo block under if __name__ == '__main__': that builds three holdings and prints each describe() line.", "uv run python stock.py"),
            ("Discuss: what did wrapping price and shares in a class buy us over keeping parallel lists of tickers and prices?", ""),
        ],
        test="Three Stock objects report independent market values; pnl_percent() returns 0.0 (not a ZeroDivisionError) when buy_price is 0; Stock.CURRENCY is visible from every instance.",
    ),
    dict(
        num=52,
        topic=8,
        title="A Portfolio Class Holding Many Stock Objects",
        objective="LO7: Compose objects — a Portfolio class that aggregates many Stock instances and reports book-level metrics.",
        desc=(
            "The learner builds a Portfolio class that holds a list of Stock objects (composition). "
            "Methods include add_holding(), total_value(), total_pnl(), weights() returning each "
            "holding's share of the book, sector_allocation() aggregating by sector, and "
            "top_holdings(n). The lab demonstrates why the Portfolio should never duplicate price "
            "data — it delegates to each Stock's own methods."
        ),
        build="A portfolio.py module defining Portfolio, importing Stock from lab 51, with a demo book of six holdings.",
        services="uv, Python 3.12, pandas, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add pandas.", "uv init lab-52-portfolio-class && cd lab-52-portfolio-class && uv add pandas"),
            ("Copy stock.py from lab 51 so Portfolio can import it.", "cp ../lab-51-stock-class/stock.py ."),
            ("Prompt your AI assistant: \"Write a Python class Portfolio that holds a list of Stock objects. __init__ takes an owner name and an optional list of holdings. Add add_holding(stock), total_value() summing each holding's market_value(), total_cost(), total_pnl(), weights() returning a dict of ticker to percentage of total_value, sector_allocation() returning a dict of sector to total market value, and top_holdings(n=3) returning the n largest holdings by market value. The Portfolio must call the Stock methods rather than recomputing prices itself.\"", ""),
            ("Save as portfolio.py and review — confirm total_value() calls h.market_value() and does not re-implement shares * price.", ""),
            ("Build a six-stock demo book across at least three sectors.", ""),
            ("Print the book-level totals.", "uv run python -c \"from portfolio import build_demo; p=build_demo(); print(p.total_value(), p.total_pnl())\""),
            ("Check the weights sum to 100%.", "uv run python -c \"from portfolio import build_demo; p=build_demo(); print(round(sum(p.weights().values()),6))\""),
            ("Confirm sector_allocation() totals equal total_value().", "uv run python portfolio.py"),
            ("Update one Stock's current_price and re-run total_value() — the Portfolio total must change with no Portfolio code touched. This is the payoff of delegation.", ""),
            ("Discuss: composition (a Portfolio HAS Stocks) versus inheritance (an Equity IS an Instrument) — why is Portfolio the wrong place to use inheritance?", ""),
        ],
        test="weights() sums to 100.0; sum(sector_allocation().values()) equals total_value(); changing one Stock's current_price changes the Portfolio total without editing portfolio.py.",
    ),
    dict(
        num=53,
        topic=8,
        title="Dunder Methods — __str__, __repr__, __len__ and __add__ to Combine Portfolios",
        objective="LO7: Apply method overloading through dunder methods so financial objects print, size and merge naturally.",
        desc=(
            "The learner adds Python's special (dunder) methods to Stock and Portfolio: __str__ for "
            "a human-readable holding line, __repr__ for the debugger-friendly form, __len__ so "
            "len(portfolio) returns the number of holdings, __getitem__ so a portfolio can be "
            "indexed and iterated, __eq__ to compare by ticker, and __add__ so two portfolios can be "
            "merged with the + operator — combining shares where the same ticker appears in both. "
            "This is operator overloading applied to a real fund-merger scenario."
        ),
        build="Enhanced stock.py and portfolio.py with six dunder methods, supporting print(), len(), iteration and portfolio_a + portfolio_b.",
        services="uv, Python 3.12, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and copy the lab 52 modules.", "uv init lab-53-dunder-methods && cd lab-53-dunder-methods && cp ../lab-52-portfolio-class/*.py ."),
            ("Observe the default behaviour first: print a Stock object and note the unhelpful <stock.Stock object at 0x...> output.", "uv run python -c \"from stock import Stock; print(Stock('D05','DBS','Banking',500,32.10,38.40))\""),
            ("Prompt your AI assistant: \"Add dunder methods to these Stock and Portfolio classes. Stock gets __str__ returning 'D05 | DBS Group | 500 sh @ SGD 38.40 | MV 19,200.00 | P&L +3,150.00', __repr__ returning Stock(ticker='D05', shares=500), and __eq__ comparing by ticker. Portfolio gets __len__ returning the number of holdings, __getitem__ so it can be indexed and iterated, __str__ returning a multi-line table of holdings with the total, and __add__ that merges two Portfolios into a new one, summing shares and recomputing a weighted average buy_price when the same ticker appears in both.\"", ""),
            ("Apply the generated dunder methods and read the __add__ implementation carefully — confirm it returns a NEW Portfolio and does not mutate either operand.", ""),
            ("Test __str__ and __repr__.", "uv run python -c \"from stock import Stock; s=Stock('D05','DBS Group','Banking',500,32.10,38.40); print(str(s)); print(repr(s))\""),
            ("Test __len__ and iteration.", "uv run python -c \"from portfolio import build_demo; p=build_demo(); print(len(p)); [print(h.ticker) for h in p]\""),
            ("Build two portfolios that share at least one ticker and merge them with the + operator.", "uv run python merge_demo.py"),
            ("Verify the merge conserves value: (a + b).total_value() must equal a.total_value() + b.total_value().", ""),
            ("Verify neither operand was mutated — len(a) and len(b) are unchanged after the merge.", ""),
            ("Discuss: when is operator overloading good design, and when does a + on a domain object become misleading to the next developer?", ""),
        ],
        test="print(stock) shows the formatted line; len(portfolio) returns the holding count; (a + b).total_value() equals a.total_value() + b.total_value() and both a and b are unchanged.",
    ),
    dict(
        num=54,
        topic=8,
        title="Inheritance — an Instrument Base Class with Equity and Bond Subclasses",
        objective="LO7: Use inheritance so Equity and Bond extend a shared Instrument class without duplicating code.",
        desc=(
            "The learner refactors to a proper instrument hierarchy. A base Instrument class holds "
            "what every instrument shares (identifier, name, quantity, currency) and defines a "
            "value() method that raises NotImplementedError. Equity(Instrument) adds price and "
            "dividend_yield; Bond(Instrument) adds face_value, coupon_rate, years_to_maturity and "
            "market_yield, and values itself by discounting coupons and principal. Both use super()."
        ),
        build="An instruments.py module with Instrument, Equity and Bond classes, each subclass calling super().__init__().",
        services="uv, Python 3.12, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project.", "uv init lab-54-inheritance-instruments && cd lab-54-inheritance-instruments"),
            ("Sketch the hierarchy on paper: what data does EVERY instrument have, and what belongs only to an Equity or only to a Bond? Only the shared fields go in the base class.", ""),
            ("Prompt your AI assistant: \"Write a Python class hierarchy for financial instruments. Base class Instrument has __init__(identifier, name, quantity, currency='SGD'), a value() method that raises NotImplementedError, and an income() method returning 0.0. Subclass Equity(Instrument) adds price and dividend_yield, overrides value() as quantity * price and income() as value * dividend_yield. Subclass Bond(Instrument) adds face_value, coupon_rate, years_to_maturity and market_yield, and overrides value() to return the present value of the coupon stream plus the discounted principal, multiplied by quantity. Both subclasses must call super().__init__() and each must have a __str__.\"", ""),
            ("Save as instruments.py and confirm both subclasses call super().__init__() rather than re-assigning the shared attributes.", ""),
            ("Verify the inheritance chain with isinstance and the MRO.", "uv run python -c \"from instruments import Instrument, Equity, Bond; e=Equity('D05','DBS',100,38.40,0.055); print(isinstance(e, Instrument), Equity.__mro__)\""),
            ("Confirm the abstract base refuses to value itself.", "uv run python -c \"from instruments import Instrument; \nimport traceback\ntry: Instrument('X','Generic',1).value()\nexcept NotImplementedError: print('correctly abstract')\""),
            ("Value an Equity and a Bond.", "uv run python instruments.py"),
            ("Sanity-check the bond maths: a bond priced at par (market_yield == coupon_rate) must value at face_value * quantity.", "uv run python -c \"from instruments import Bond; b=Bond('SGB10','SG Govt Bond',10,1000,0.03,5,0.03); print(round(b.value(),2))\""),
            ("Check a discount bond: raise market_yield above coupon_rate and confirm the value falls below par.", ""),
            ("Discuss: what code would you have duplicated if Equity and Bond were unrelated classes, and what breaks when a third instrument type is added later?", ""),
        ],
        test="isinstance(equity, Instrument) is True; Instrument.value() raises NotImplementedError; a par bond values at exactly face_value * quantity and a bond yielding above its coupon values below par.",
    ),
    dict(
        num=55,
        topic=8,
        title="Polymorphism — One .value() Call Across a Mixed Instrument Book",
        objective="LO7: Apply polymorphism so a single valuation loop handles every instrument type correctly.",
        desc=(
            "The learner adds a third subclass (a simple CashDeposit or FXForward), then builds a "
            "mixed book of Equity, Bond and Cash objects in one list and values the entire book with "
            "a single loop calling item.value() — Python dispatches to the correct override at "
            "runtime. The lab also adds a duck-typed report_book() function that works on any object "
            "exposing .value(), showing polymorphism does not require inheritance, and proves the "
            "open/closed principle by adding a fourth instrument type without editing the valuation loop."
        ),
        build="A book.py script valuing a heterogeneous instrument book through one polymorphic loop, plus an asset-class breakdown.",
        services="uv, Python 3.12, pandas, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project, add pandas and copy the lab 54 hierarchy.", "uv init lab-55-polymorphism-book && cd lab-55-polymorphism-book && uv add pandas && cp ../lab-54-inheritance-instruments/instruments.py ."),
            ("Prompt your AI assistant: \"Extend this instruments module with a CashDeposit(Instrument) subclass holding a principal and an annual interest rate, overriding value() as principal plus accrued interest and income() as principal * rate. Then write a function value_book(items) that takes a list of ANY Instrument subclasses and returns a pandas DataFrame with columns Identifier, Asset_Class (the class name), Value and Income, plus the book total — using a single loop that calls item.value() with no isinstance checks and no if/elif on type.\"", ""),
            ("Save as book.py and audit the loop: if the generated code contains isinstance() or a type check inside value_book(), that is NOT polymorphism — rewrite it.", ""),
            ("Build a mixed book of at least two Equities, two Bonds and one CashDeposit in a single Python list.", ""),
            ("Run the polymorphic valuation.", "uv run python book.py"),
            ("Confirm each row's Asset_Class is derived at runtime via type(item).__name__ — the loop never knew the type in advance.", ""),
            ("Group the book by Asset_Class to produce the allocation table.", "uv run python -c \"from book import value_book, build_book; df=value_book(build_book()); print(df.groupby('Asset_Class')['Value'].sum().round(2))\""),
            ("Prove the open/closed principle: add a fourth subclass (e.g. FXForward) with its own value(), append one to the book, and re-run WITHOUT changing value_book().", ""),
            ("Verify the book total rose by exactly the new instrument's value.", ""),
            ("Discuss: how does polymorphism reduce risk in a valuation engine compared with a long if/elif chain on instrument type?", ""),
        ],
        test="value_book() contains no isinstance or type comparisons; adding a brand-new Instrument subclass to the list changes the book total with zero edits to value_book(), and the Asset_Class column names it correctly.",
    ),
    dict(
        num=56,
        topic=8,
        title="StockTechnicalAnalyzer — an OOP Class Computing SMA, RSI and BUY/SELL Signals",
        objective="LO7: Encapsulate a complete technical-analysis workflow in one class with modular methods and generated trading signals.",
        desc=(
            "This is the reference slide 148 activity and the class the Topic 9 capstone consumes. "
            "The learner builds StockTechnicalAnalyzer following OOP principles: the ticker and "
            "analysis period are instance attributes (encapsulation) and the work is split into "
            "modular methods — fetch_data() returning a boolean status, calculate_indicators() "
            "computing a 20-day SMA and 14-day RSI, generate_signals() emitting BUY when RSI < 30 "
            "and price crosses above the SMA and SELL when RSI > 70 or price crosses below, and "
            "plot_analysis() drawing price/SMA and RSI matplotlib subplots. A run_analysis() method "
            "orchestrates the sequence and fails gracefully when the download returns nothing."
        ),
        build="An analyzer.py module defining StockTechnicalAnalyzer, producing a signals table and a two-panel PNG chart.",
        services="uv, yfinance, pandas, matplotlib, VS Code / Cursor AI assistant",
        steps=[
            ("Create the project and add the market-data stack.", "uv init lab-56-stock-analyzer && cd lab-56-stock-analyzer && uv add yfinance pandas matplotlib"),
            ("Prompt your AI assistant with the slide-148 brief: \"Write a Python class StockTechnicalAnalyzer following OOP principles to perform stock analysis using yfinance. Encapsulation: store the ticker and analysis period as instance attributes set in __init__, with self.data starting as None. Modular methods: fetch_data() downloads historical data with yfinance and returns a boolean status, storing it on self.data; calculate_indicators() computes a 20-day Simple Moving Average and a 14-day Relative Strength Index as new columns; generate_signals() returns a DataFrame of BUY and SELL signals where BUY is RSI below 30 with the close crossing above the SMA and SELL is RSI above 70 or the close crossing below the SMA; plot_analysis() uses matplotlib subplots to visualise close price with the SMA on the top panel and RSI with 30/70 reference lines on the bottom panel, saving to PNG. Add run_analysis() that calls the methods in order and returns early with a message if fetch_data() fails.\"", ""),
            ("Save as analyzer.py and review the RSI calculation — confirm it uses a 14-period average gain over average loss and not a simple percentage change.", ""),
            ("Confirm the encapsulation: fetch_data() must store to self.data, and calculate_indicators() must read self.data rather than take the frame as an argument.", ""),
            ("Instantiate the analyzer for one ticker and fetch.", "uv run python -c \"from analyzer import StockTechnicalAnalyzer; a=StockTechnicalAnalyzer('AAPL','6mo'); print(a.fetch_data()); print(a.data.shape)\""),
            ("Run the full analysis end to end.", "uv run python analyzer.py"),
            ("Check the indicators: the first 19 SMA values must be NaN and every non-null RSI must sit between 0 and 100.", "uv run python -c \"from analyzer import StockTechnicalAnalyzer; a=StockTechnicalAnalyzer('AAPL','6mo'); a.run_analysis(); d=a.data.dropna(); print(d['RSI'].min(), d['RSI'].max())\""),
            ("Inspect the generated signals table and verify each BUY row really has RSI below 30.", ""),
            ("Test the failure path with a nonsense ticker — fetch_data() must return False and run_analysis() must exit cleanly with a message, not a traceback.", "uv run python -c \"from analyzer import StockTechnicalAnalyzer; a=StockTechnicalAnalyzer('NOTATICKER','6mo'); print(a.run_analysis())\""),
            ("Create three analyzer objects for three different tickers and confirm each keeps its own independent self.data — the payoff of instance state. Keep analyzer.py: lab 61 imports this class into the Streamlit app.", ""),
        ],
        test="run_analysis() produces a PNG with two panels and a signals table where every BUY has RSI < 30 and every SELL has RSI > 70 or a downward SMA cross; an invalid ticker returns False from fetch_data() with no traceback.",
    ),
]
