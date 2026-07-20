# Lab 56 — StockTechnicalAnalyzer — an OOP Class Computing SMA, RSI and BUY/SELL Signals

**Topic 8: Object Oriented Programming**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO7: Encapsulate a complete technical-analysis workflow in one class with modular methods and generated trading signals.

## Goal

This is the reference slide 148 activity and the class the Topic 9 capstone consumes. The learner builds StockTechnicalAnalyzer following OOP principles: the ticker and analysis period are instance attributes (encapsulation) and the work is split into modular methods — fetch_data() returning a boolean status, calculate_indicators() computing a 20-day SMA and 14-day RSI, generate_signals() emitting BUY when RSI < 30 and price crosses above the SMA and SELL when RSI > 70 or price crosses below, and plot_analysis() drawing price/SMA and RSI matplotlib subplots. A run_analysis() method orchestrates the sequence and fails gracefully when the download returns nothing.

## What you'll build

An analyzer.py module defining StockTechnicalAnalyzer, producing a signals table and a two-panel PNG chart.

**Tools:** uv, yfinance, pandas, matplotlib, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project and add the market-data stack.

   ```bash
   uv init lab-56-stock-analyzer && cd lab-56-stock-analyzer && uv add yfinance pandas matplotlib
   ```

2. Prompt your AI assistant with the slide-148 brief: "Write a Python class StockTechnicalAnalyzer following OOP principles to perform stock analysis using yfinance. Encapsulation: store the ticker and analysis period as instance attributes set in __init__, with self.data starting as None. Modular methods: fetch_data() downloads historical data with yfinance and returns a boolean status, storing it on self.data; calculate_indicators() computes a 20-day Simple Moving Average and a 14-day Relative Strength Index as new columns; generate_signals() returns a DataFrame of BUY and SELL signals where BUY is RSI below 30 with the close crossing above the SMA and SELL is RSI above 70 or the close crossing below the SMA; plot_analysis() uses matplotlib subplots to visualise close price with the SMA on the top panel and RSI with 30/70 reference lines on the bottom panel, saving to PNG. Add run_analysis() that calls the methods in order and returns early with a message if fetch_data() fails."
3. Save as analyzer.py and review the RSI calculation — confirm it uses a 14-period average gain over average loss and not a simple percentage change.
4. Confirm the encapsulation: fetch_data() must store to self.data, and calculate_indicators() must read self.data rather than take the frame as an argument.
5. Instantiate the analyzer for one ticker and fetch.

   ```bash
   uv run python -c "from analyzer import StockTechnicalAnalyzer; a=StockTechnicalAnalyzer('AAPL','6mo'); print(a.fetch_data()); print(a.data.shape)"
   ```

6. Run the full analysis end to end.

   ```bash
   uv run python analyzer.py
   ```

7. Check the indicators: the first 19 SMA values must be NaN and every non-null RSI must sit between 0 and 100.

   ```bash
   uv run python -c "from analyzer import StockTechnicalAnalyzer; a=StockTechnicalAnalyzer('AAPL','6mo'); a.run_analysis(); d=a.data.dropna(); print(d['RSI'].min(), d['RSI'].max())"
   ```

8. Inspect the generated signals table and verify each BUY row really has RSI below 30.
9. Test the failure path with a nonsense ticker — fetch_data() must return False and run_analysis() must exit cleanly with a message, not a traceback.

   ```bash
   uv run python -c "from analyzer import StockTechnicalAnalyzer; a=StockTechnicalAnalyzer('NOTATICKER','6mo'); print(a.run_analysis())"
   ```

10. Create three analyzer objects for three different tickers and confirm each keeps its own independent self.data — the payoff of instance state. Keep analyzer.py: lab 61 imports this class into the Streamlit app.

## Test it

run_analysis() produces a PNG with two panels and a signals table where every BUY has RSI < 30 and every SELL has RSI > 70 or a downward SMA cross; an invalid ticker returns False from fetch_data() with no traceback.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
