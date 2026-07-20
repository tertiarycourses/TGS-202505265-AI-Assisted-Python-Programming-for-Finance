"""
Topic 6 — Import and Process Finance Data.

Hands-on activities (labs 35-42) for domain 6 of "AI Assisted Python Programming
for Finance". Every lab is finance-oriented and maps to LO5: import, clean,
filter and process financial data using the pandas package.

Tooling: uv (uv init / uv add / uv run) — never pip or venv.
"""

DOMAIN6 = [
    dict(
        num=35,
        topic=6,
        title="Pandas Series vs DataFrame with Price Data",
        objective="LO5: Construct and distinguish a pandas Series and a DataFrame, and index both with financial labels.",
        desc=(
            "The learner builds a Series of closing prices indexed by date, then a DataFrame holding "
            "open, high, low, close and volume for several tickers. Working with both side by side "
            "makes the distinction concrete: a Series is one labelled column — a single instrument's "
            "price history — while a DataFrame is a labelled table where a column selection returns a "
            "Series again. The learner also compares `.loc` label-based access against `.iloc` "
            "position-based access, the source of most beginner indexing bugs in finance code."
        ),
        build=(
            "A uv project `lab-35-series-dataframe` with series_vs_frame.py demonstrating Series "
            "construction, DataFrame construction, column and row selection, and a printed comparison "
            "of .loc versus .iloc."
        ),
        services="uv, pandas, AI coding assistant",
        steps=[
            ("Create the project and add pandas.",
             "uv init lab-35-series-dataframe && cd lab-35-series-dataframe && uv add pandas"),
            ("In series_vs_frame.py build a Series of 10 daily closing prices for D05.SI indexed by a "
             "pd.date_range of business days, and print it with its .index, .dtype and .name.",
             "touch series_vs_frame.py"),
            ("Print series.mean(), series.max() and series.pct_change() and note that a Series carries "
             "its index through every operation.",
             "uv run python series_vs_frame.py"),
            ("Build a DataFrame with columns Open, High, Low, Close and Volume over the same dates, "
             "and print df.shape, df.columns and df.dtypes.",
             ""),
            ("Select a single column with df['Close'] and confirm with type() that it is a Series, not "
             "a DataFrame; then select df[['Close', 'Volume']] and confirm that a list of columns "
             "returns a DataFrame.",
             "uv run python series_vs_frame.py"),
            ("Discuss: the single-bracket versus double-bracket distinction. Passing a Series where a "
             "DataFrame is expected is a very common error in financial pipelines.",
             ""),
            ("Compare label and position indexing: df.loc['2024-03-05'] against df.iloc[2], and "
             "df.loc['2024-03-04':'2024-03-08'] against df.iloc[1:4]. Note that .loc slices are "
             "INCLUSIVE of the endpoint while .iloc slices are not.",
             "uv run python series_vs_frame.py"),
            ("AI STEP — prompt your AI assistant: \"Explain the difference between a pandas Series and "
             "a DataFrame using a stock price example, and give me three short code snippets showing "
             "when .loc silently returns different rows than .iloc on a date-indexed price table. "
             "Include the off-by-one trap on slice endpoints.\"",
             ""),
            ("Run the AI's snippets yourself and verify each claim against your own DataFrame — do not "
             "accept the endpoint behaviour on trust.",
             "uv run python series_vs_frame.py"),
            ("Add a multi-ticker DataFrame with a two-level column index (ticker, field) and select "
             "just the Close columns for all tickers.",
             "uv run python series_vs_frame.py"),
        ],
        test=(
            "The script prints the Series with its DatetimeIndex, confirms type(df['Close']) is Series "
            "and type(df[['Close']]) is DataFrame, and shows .loc and .iloc returning the expected rows "
            "with the inclusive/exclusive endpoint difference clearly labelled."
        ),
    ),
    dict(
        num=36,
        topic=6,
        title="Import Finance Data from CSV",
        objective="LO5: Import a financial CSV into pandas with correct date parsing, index and dtypes.",
        desc=(
            "The learner imports a historical prices CSV and confronts the three defects that make most "
            "real finance CSVs unusable on the first read: dates loaded as strings, numbers loaded as "
            "objects because of thousands separators or currency symbols, and an unnamed index column. "
            "The learner fixes each with read_csv parameters — parse_dates, index_col, thousands, "
            "dtype and na_values — rather than by post-processing, and confirms the fix with .dtypes."
        ),
        build=(
            "A uv project `lab-36-csv-import` containing prices.csv, load_csv.py with a correctly "
            "parameterised read_csv call, and a printed dtype report proving Close is float64 and the "
            "index is a DatetimeIndex."
        ),
        services="uv, pandas, AI coding assistant",
        steps=[
            ("Create the project and add pandas.",
             "uv init lab-36-csv-import && cd lab-36-csv-import && uv add pandas"),
            ("Create prices.csv with columns Date, Ticker, Open, Close, Volume — deliberately writing "
             "volumes with thousands commas like '1,204,300', a few cells as 'N/A', and dates in "
             "DD/MM/YYYY form.",
             "touch prices.csv"),
            ("Load it with a naive pd.read_csv('prices.csv') and print df.dtypes and df.head().",
             "uv run python load_csv.py"),
            ("Discuss: Date came in as object, Volume came in as object because of the commas, and "
             "'N/A' was not recognised as missing. Every downstream calculation on these columns would "
             "either fail or be silently wrong.",
             ""),
            ("Re-import with parse_dates=['Date'], dayfirst=True, index_col='Date', "
             "thousands=',' and na_values=['N/A', '', '-'], then reprint df.dtypes.",
             "uv run python load_csv.py"),
            ("Verify the index with df.index.dtype and confirm df.index.is_monotonic_increasing; sort "
             "the index if it is not.",
             "uv run python load_csv.py"),
            ("AI STEP — prompt your AI assistant: \"Here are the first five rows of my stock price CSV "
             "<paste rows>. Write the single pd.read_csv call that parses the DD/MM/YYYY dates into a "
             "DatetimeIndex, strips thousands separators from Volume, treats 'N/A' and '-' as missing, "
             "and forces Close to float64. Explain each parameter you used.\"",
             ""),
            ("Compare the AI's read_csv call with your own. Check specifically that it set dayfirst "
             "correctly — a wrong dayfirst silently swaps day and month for the first twelve days of "
             "each month and is nearly invisible.",
             ""),
            ("Prove the parse is right by printing the rows for a date after the 12th of a month and "
             "checking it against the raw CSV text.",
             "uv run python load_csv.py"),
            ("Save the cleaned frame back out and confirm the round trip is stable.",
             "uv run python load_csv.py && head -3 prices_clean.csv"),
        ],
        test=(
            "df.dtypes shows Close and Open as float64, Volume as int64 or float64, and df.index is a "
            "DatetimeIndex sorted ascending. The 'N/A' cells appear as NaN, and a spot-checked date "
            "after the 12th matches the raw CSV."
        ),
    ),
    dict(
        num=37,
        topic=6,
        title="Import Live Market Data with yfinance",
        objective="LO5: Download multi-ticker market data with yfinance and reshape the result into an analysis-ready DataFrame.",
        desc=(
            "The learner downloads three years of daily data for a small multi-market portfolio with "
            "yfinance and immediately meets its awkward output shape: a MultiIndex column frame when "
            "several tickers are requested, and a flat frame when only one is. The learner writes a "
            "loader that normalises both cases into a tidy long-format DataFrame with Date, Ticker and "
            "Close, caches it to CSV so the rest of the course is not dependent on the network, and "
            "wraps the download in the try/except pattern learned in Topic 5."
        ),
        build=(
            "A uv project `lab-37-yfinance-import` with load_market.py producing a tidy long-format "
            "DataFrame and a cached market_data.csv covering three years and at least four tickers."
        ),
        services="uv, yfinance, pandas, AI coding assistant",
        steps=[
            ("Create the project and add the data dependencies.",
             "uv init lab-37-yfinance-import && cd lab-37-yfinance-import && uv add yfinance pandas"),
            ("Download three years of daily data for a single ticker and inspect the shape of what "
             "comes back.",
             "uv run python -c \"import yfinance as yf; d=yf.download('AAPL', period='3y'); print(d.columns); print(d.head())\""),
            ("Now download four tickers at once — AAPL, MSFT, D05.SI, O39.SI — and print the columns "
             "again to see the MultiIndex.",
             "uv run python load_market.py"),
            ("Discuss: with one ticker the columns are flat; with several they are a (field, ticker) "
             "MultiIndex. Code written against one shape breaks against the other — a very common "
             "production bug.",
             ""),
            ("In load_market.py write fetch(tickers, period) that always returns a tidy long frame with "
             "columns Date, Ticker, Open, High, Low, Close, Volume, using .stack() to flatten the "
             "MultiIndex case and adding a Ticker column in the single case.",
             ""),
            ("Wrap the download in try/except (Topic 5 pattern) so a failed or empty ticker is reported "
             "and skipped rather than aborting the whole fetch.",
             "uv run python load_market.py"),
            ("Cache the tidy frame to market_data.csv and add a guard so the script reads the cache "
             "when it exists and only hits the network otherwise.",
             "uv run python load_market.py && wc -l market_data.csv"),
            ("AI STEP — prompt your AI assistant: \"yf.download returns a MultiIndex column DataFrame "
             "for multiple tickers and a flat one for a single ticker. Write a function that normalises "
             "both into a long-format DataFrame with columns Date, Ticker, Open, High, Low, Close, "
             "Volume. Handle auto_adjust and explain what Adj Close means for a dividend-paying stock.\"",
             ""),
            ("Test the AI's normaliser with a one-ticker call AND a four-ticker call and confirm both "
             "produce identical column layouts.",
             "uv run python load_market.py"),
            ("Discuss the AI's explanation of adjusted close: why backtesting on unadjusted close "
             "overstates losses around ex-dividend dates.",
             ""),
            ("Print a summary — the date range, the row count per ticker, and the number of trading "
             "days captured.",
             "uv run python load_market.py"),
        ],
        test=(
            "market_data.csv exists, covers roughly three years, contains all four tickers in long "
            "format with one row per ticker per trading day, and the loader returns the same column "
            "layout whether called with one ticker or four."
        ),
    ),
    dict(
        num=38,
        topic=6,
        title="Inspect a Dataset with head, info and describe",
        objective="LO5: Profile a financial dataset with head, tail, info, describe and value_counts to identify data-quality problems before analysis.",
        desc=(
            "Before any calculation, an analyst profiles the data. The learner runs the standard "
            "inspection sequence over the cached market data and reads each output as a finance "
            "question: does info() show fewer non-null Closes than rows, meaning gaps? Does describe() "
            "show a minimum price of zero or a negative volume, meaning corrupt records? Does "
            "value_counts() over Ticker show one instrument with far fewer rows, meaning a late listing "
            "or a suspension? The learner writes a reusable profiling function that answers all of them."
        ),
        build=(
            "A uv project `lab-38-inspect-data` with profile.py printing a full data-quality report and "
            "a written list of every anomaly found in the dataset."
        ),
        services="uv, pandas, AI coding assistant",
        steps=[
            ("Create the project, add pandas, and copy in market_data.csv from lab 37.",
             "uv init lab-38-inspect-data && cd lab-38-inspect-data && uv add pandas && "
             "cp ../lab-37-yfinance-import/market_data.csv ."),
            ("Load the CSV with proper date parsing and print df.head(10) and df.tail(10) to see the "
             "start and end of the series.",
             "uv run python profile.py"),
            ("Print df.info() and read it as a finance question: compare the non-null count of Close "
             "against the total row count to find missing prices.",
             "uv run python profile.py"),
            ("Print df.describe() and inspect the min, max and quartiles of Close and Volume for "
             "impossible values — a zero price, a negative volume, or a max thousands of times the "
             "median.",
             "uv run python profile.py"),
            ("Print df['Ticker'].value_counts() and check every ticker has a similar row count; "
             "investigate any that does not.",
             "uv run python profile.py"),
            ("Discuss: the three anomalies you found and what each would do to a portfolio return "
             "calculation if left uncorrected.",
             ""),
            ("Write profile_dataset(df) that packages the whole sequence — shape, dtypes, null counts "
             "per column, describe, per-ticker row counts and date coverage — into one printed report.",
             "uv run python profile.py"),
            ("AI STEP — prompt your AI assistant: \"Write a pandas data-quality report function for a "
             "long-format stock price DataFrame with columns Date, Ticker, Close, Volume. It must "
             "report: missing values per column, duplicate (Date, Ticker) rows, non-positive prices, "
             "gaps of more than 5 calendar days in each ticker's date coverage, and any date that is "
             "not a business day. Print it as a readable table.\"",
             ""),
            ("Run the AI's report on your data and verify each finding by hand against the raw CSV "
             "before trusting it.",
             "uv run python profile.py"),
            ("Record the confirmed anomalies as a comment block at the top of profile.py — this is the "
             "data-quality note that must accompany any published analysis.",
             ""),
        ],
        test=(
            "profile.py prints shape, dtypes, per-column null counts, describe output, per-ticker row "
            "counts and date coverage, plus a list of duplicate or non-positive-price rows. The learner "
            "can name at least two concrete data-quality issues found in their own dataset."
        ),
    ),
    dict(
        num=39,
        topic=6,
        title="Filter and Slice by Date, Sector and Ticker",
        objective="LO5: Select subsets of financial data with boolean masks, date-range slicing and multi-condition filters.",
        desc=(
            "The learner attaches a sector mapping to the price data and then answers a series of real "
            "screening questions with boolean masks: all bank stocks in Q1, every day AAPL closed above "
            "its own 200-day average, the intersection of a date window and a ticker list. The lab "
            "covers the operator-precedence trap unique to pandas — `&` and `|` with parentheses, never "
            "`and`/`or` — plus .isin(), .between(), .query() and .loc date slicing on a DatetimeIndex."
        ),
        build=(
            "A uv project `lab-39-filter-slice` with screen.py answering five stated screening questions, "
            "each as a documented boolean mask."
        ),
        services="uv, pandas, AI coding assistant",
        steps=[
            ("Create the project, add pandas and copy in the market data.",
             "uv init lab-39-filter-slice && cd lab-39-filter-slice && uv add pandas && "
             "cp ../lab-37-yfinance-import/market_data.csv ."),
            ("Add a SECTORS dict mapping each ticker to a sector — AAPL and MSFT to Technology, D05.SI "
             "and O39.SI to Financials — and map it into a new Sector column.",
             "touch screen.py"),
            ("Question 1: slice the last full calendar year using .loc with a date range on the "
             "DatetimeIndex, and print the row count.",
             "uv run python screen.py"),
            ("Question 2: select only the Financials rows with a boolean mask df['Sector'] == "
             "'Financials', and print the tickers it contains to verify.",
             "uv run python screen.py"),
            ("Question 3: combine two conditions — Financials AND Close above 30 — using & with "
             "parentheses around each condition. Then deliberately try it with `and` and read the "
             "resulting ValueError.",
             "uv run python screen.py"),
            ("Discuss: pandas cannot evaluate the truth of a whole Series, which is why `and` fails and "
             "`&` is required. Forgetting the parentheses gives a wrong answer silently because of "
             "operator precedence.",
             ""),
            ("Question 4: use .isin(['AAPL', 'D05.SI']) to select a ticker subset, and .between() on "
             "Close to select a price band, and combine both.",
             "uv run python screen.py"),
            ("Question 5: rewrite the most complex mask using .query() and compare readability with the "
             "bracket form; time both on the full dataset.",
             "uv run python screen.py"),
            ("AI STEP — prompt your AI assistant: \"Using a pandas DataFrame with columns Date "
             "(DatetimeIndex), Ticker, Sector, Close and Volume, write filters for: all Financials "
             "rows in 2024 where Close rose more than 2 percent from the prior day, and the 10 "
             "highest-volume days for any Technology stock. Use boolean masks with correct parentheses "
             "and explain why `and` would fail.\"",
             ""),
            ("Run the AI's filters and verify the row counts by cross-checking a couple of rows "
             "manually — an incorrect mask usually returns a plausible but wrong number of rows.",
             "uv run python screen.py"),
            ("Save each screened subset to its own CSV for use in the next lab.",
             "uv run python screen.py && ls *.csv"),
        ],
        test=(
            "All five screening questions print a result with its row count, the `and` version raises "
            "the expected ValueError with an explanatory printed note, and the .query() result is "
            "identical to the bracket-mask result."
        ),
    ),
    dict(
        num=40,
        topic=6,
        title="Handle Missing Market Data and Compare the Choices",
        objective="LO5: Detect missing market data with isna, and compare dropna, fillna and forward-fill, quantifying how each choice changes the analytical result.",
        desc=(
            "The central judgement lab of Topic 6. Market data has gaps: public holidays that differ "
            "between SGX and NASDAQ, trading suspensions, and vendor errors. The learner injects and "
            "detects gaps, then applies three treatments — dropna, fillna with the mean, and forward-fill "
            "— to the SAME series, computes total return and volatility under each, and puts the three "
            "answers side by side. The point is that the numbers genuinely differ, so the cleaning "
            "choice is an analytical decision that must be documented, not a formatting step."
        ),
        build=(
            "A uv project `lab-40-missing-data` with clean_compare.py printing a comparison table of "
            "total return, mean daily return and annualised volatility under each of the four "
            "treatments, plus a written recommendation."
        ),
        services="uv, pandas, numpy, AI coding assistant",
        steps=[
            ("Create the project and add the dependencies.",
             "uv init lab-40-missing-data && cd lab-40-missing-data && uv add pandas numpy && "
             "cp ../lab-37-yfinance-import/market_data.csv ."),
            ("Reindex a single ticker's Close series onto a full business-day calendar so every "
             "non-trading gap becomes an explicit NaN, then count them with .isna().sum().",
             "uv run python clean_compare.py"),
            ("Print the specific dates that are missing and identify which are public holidays versus "
             "genuine data gaps.",
             "uv run python clean_compare.py"),
            ("Treatment A — dropna(): drop the missing rows, then compute total return, mean daily "
             "return and annualised volatility.",
             "uv run python clean_compare.py"),
            ("Treatment B — fillna(series.mean()): fill every gap with the series mean and recompute "
             "the same three metrics.",
             "uv run python clean_compare.py"),
            ("Treatment C — ffill(): forward-fill the last traded price across the gap, which is the "
             "standard convention for a non-trading day, and recompute.",
             "uv run python clean_compare.py"),
            ("Treatment D — interpolate(method='time'): linearly interpolate across the gap and "
             "recompute.",
             "uv run python clean_compare.py"),
            ("Print all four sets of metrics in one comparison table and identify the largest "
             "discrepancy between treatments.",
             "uv run python clean_compare.py"),
            ("DISCUSS — the key judgement of this topic: filling with the series mean injects a huge "
             "artificial price jump and inflates volatility; dropna understates the number of periods; "
             "forward-fill correctly implies zero return on a non-trading day but suppresses volatility "
             "if used across a long suspension. Which treatment would you defend to an auditor, and for "
             "which kind of gap?",
             ""),
            ("AI STEP — prompt your AI assistant: \"I have a daily stock Close series with NaNs from "
             "public holidays and one three-week trading suspension. Compare dropna, fillna(mean), "
             "ffill and time interpolation for computing daily returns and annualised volatility. For "
             "each, state the assumption it makes about what happened during the gap and when it "
             "biases the volatility estimate up or down.\"",
             ""),
            ("Check the AI's reasoning against your own measured numbers from the comparison table — "
             "does its claimed direction of bias match what you actually observed?",
             "uv run python clean_compare.py"),
            ("Write your recommendation as a comment block: which treatment for a holiday, which for a "
             "suspension, and which you would never use.",
             ""),
        ],
        test=(
            "The comparison table prints four rows of metrics that visibly differ, the missing dates "
            "are listed by date, and the file ends with a written, justified recommendation naming a "
            "treatment per gap type."
        ),
    ),
    dict(
        num=41,
        topic=6,
        title="Derived Columns — Daily Returns and Moving Averages",
        objective="LO5: Create derived analytical columns — daily and cumulative returns, rolling moving averages and rolling volatility — with pct_change, shift and rolling.",
        desc=(
            "The learner turns a price table into an analytics table. Daily simple returns come from "
            "pct_change(); log returns from np.log on a shift() ratio; cumulative growth from cumprod. "
            "Rolling windows produce the 20-day and 50-day simple moving averages and a 20-day rolling "
            "volatility. The lab emphasises correct grouping — every derived column must be computed "
            "per ticker with groupby, or the first return of each ticker will be contaminated by the "
            "last price of the previous one, a mistake that is easy to make and hard to see."
        ),
        build=(
            "A uv project `lab-41-derived-columns` with features.py producing enriched_prices.csv "
            "containing daily_return, log_return, cum_return, sma_20, sma_50 and vol_20 per ticker."
        ),
        services="uv, pandas, numpy, AI coding assistant",
        steps=[
            ("Create the project and add the dependencies.",
             "uv init lab-41-derived-columns && cd lab-41-derived-columns && uv add pandas numpy && "
             "cp ../lab-37-yfinance-import/market_data.csv ."),
            ("Load the long-format data, sort by Ticker then Date, and add daily_return using "
             "df.groupby('Ticker')['Close'].pct_change().",
             "uv run python features.py"),
            ("Deliberately compute the same column WITHOUT groupby and compare the first row of each "
             "ticker between the two versions.",
             "uv run python features.py"),
            ("Discuss: without groupby the first row of MSFT was computed against the last price of "
             "AAPL, producing a nonsense return. Nothing raised an error — this is a silent correctness "
             "bug that survives all the way to a published number.",
             ""),
            ("Add log_return using np.log(close / close.shift(1)) within the groupby, and explain when "
             "log returns are preferred (time-additivity for multi-period aggregation).",
             "uv run python features.py"),
            ("Add cum_return as (1 + daily_return).cumprod() - 1 per ticker, and print the three-year "
             "cumulative return for each instrument.",
             "uv run python features.py"),
            ("Add sma_20 and sma_50 with groupby + rolling(window).mean(), and confirm the first 19 and "
             "49 values respectively are NaN by design.",
             "uv run python features.py"),
            ("Add vol_20 as the 20-day rolling standard deviation of daily_return, annualised by "
             "multiplying by the square root of 252.",
             "uv run python features.py"),
            ("AI STEP — prompt your AI assistant: \"Given a long-format pandas DataFrame with columns "
             "Date, Ticker and Close, write vectorised code that adds daily simple returns, log "
             "returns, cumulative return, a 20-day and 50-day SMA, and 20-day annualised rolling "
             "volatility — all computed per ticker with groupby so no value leaks across tickers. "
             "Explain why min_periods matters on the rolling calls.\"",
             ""),
            ("Verify the AI's output on the boundary rows: check the first row of each ticker is NaN "
             "for daily_return, and that no SMA value appears before its window is full.",
             "uv run python features.py"),
            ("Write the enriched frame to enriched_prices.csv and print a per-ticker summary of "
             "cumulative return and mean annualised volatility.",
             "uv run python features.py && head -3 enriched_prices.csv"),
        ],
        test=(
            "enriched_prices.csv contains all six derived columns, the first row of every ticker has "
            "NaN daily_return, sma_50 is NaN for exactly the first 49 rows of each ticker, and the "
            "per-ticker summary prints a plausible cumulative return and volatility."
        ),
    ),
    dict(
        num=42,
        topic=6,
        title="Activity: Algorithmic Trading — Moving Average Crossover Backtest",
        objective="LO5: Backtest a moving-average crossover strategy on three years of market data, computing performance KPIs and visualising the signals.",
        desc=(
            "The capstone activity for Topic 6, from the reference slide. The learner prompts for a "
            "ticker and for short and long moving-average windows, downloads three years of data with "
            "yfinance, generates buy and sell signals where the short SMA crosses the long SMA, and "
            "backtests the resulting position against buy-and-hold. Performance is reported as total "
            "return, annualised return, annualised volatility, Sharpe ratio at a zero risk-free rate, "
            "and maximum drawdown. A matplotlib chart plots the price with both moving averages, green "
            "'^' markers at buy signals and red 'v' markers at sell signals. The whole run is wrapped "
            "in the Topic 5 error handling and uses the Topic 6 cleaning decisions."
        ),
        build=(
            "A uv project `lab-42-ma-crossover-backtest` with backtest.py, a printed KPI table "
            "comparing the strategy with buy-and-hold, and backtest_chart.png showing price, both SMAs "
            "and the marked signals."
        ),
        services="uv, yfinance, pandas, numpy, matplotlib, AI coding assistant",
        steps=[
            ("Create the project and add the full backtesting stack.",
             "uv init lab-42-ma-crossover-backtest && cd lab-42-ma-crossover-backtest && "
             "uv add yfinance pandas numpy matplotlib"),
            ("AI STEP — prompt your AI assistant with the full specification: \"Write a Python script "
             "using yfinance, pandas, numpy and matplotlib that backtests a Moving Average Crossover "
             "strategy on 3 years of daily data. Prompt the user for a stock ticker and integer short "
             "and long SMA windows. Generate a buy signal when the short SMA crosses above the long "
             "SMA and a sell signal when it crosses below. Compute Total Return, Annualised Return, "
             "Annualised Volatility, Sharpe Ratio at a 0 percent risk-free rate, and Maximum Drawdown, "
             "for both the strategy and buy-and-hold. Plot the close price with both moving average "
             "lines, green '^' markers at buy signals and red 'v' markers at sell signals, and save it "
             "as backtest_chart.png. Handle an invalid ticker with try/except.\"",
             ""),
            ("Save the result as backtest.py and READ IT BEFORE RUNNING. Check three specific things: "
             "that the signal is shifted by one day before being applied to returns, that the SMAs use "
             "only past data, and that the drawdown is computed from the cumulative equity curve.",
             "touch backtest.py"),
            ("Run the backtest on AAPL with windows 20 and 50.",
             "uv run python backtest.py"),
            ("Discuss the look-ahead bias check: if the position is not shifted by one day, the "
             "strategy trades on a signal derived from the same day's close — an impossible trade that "
             "flatters every KPI. Confirm your script shifts.",
             ""),
            ("Fix any look-ahead bias you found, re-run, and compare the KPIs before and after — note "
             "how much the Sharpe ratio fell.",
             "uv run python backtest.py"),
            ("Run the same backtest on a Singapore bank, D05.SI, with the same windows and compare the "
             "results across the two markets.",
             "uv run python backtest.py"),
            ("Sweep the window pair: run 10/30, 20/50 and 50/200 on the same ticker and tabulate total "
             "return and Sharpe for each.",
             "uv run python backtest.py"),
            ("Discuss overfitting: the best window pair in this sample is not the best pair out of "
             "sample. Why does picking the winner from a sweep overstate expected live performance?",
             ""),
            ("Inspect backtest_chart.png and verify the markers sit exactly at the crossover points and "
             "that buys and sells alternate.",
             "open backtest_chart.png"),
            ("Add the Topic 6 cleaning decision explicitly: forward-fill any missing closes before "
             "computing the SMAs, and print a note stating the treatment used.",
             "uv run python backtest.py"),
            ("Write a short conclusion in the script header: did the crossover strategy beat "
             "buy-and-hold on your ticker after the look-ahead fix, and what would you need to add "
             "before trusting the result (transaction costs, slippage, out-of-sample testing)?",
             ""),
        ],
        test=(
            "The script accepts a ticker and two windows, prints a KPI table with Total Return, "
            "Annualised Return, Annualised Volatility, Sharpe Ratio and Maximum Drawdown for both the "
            "strategy and buy-and-hold, writes backtest_chart.png with both SMA lines and alternating "
            "green '^' and red 'v' markers at the crossovers, and exits cleanly on an invalid ticker."
        ),
    ),
]
