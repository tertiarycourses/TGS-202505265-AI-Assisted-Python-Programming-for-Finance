# Lab 42 — Activity: Algorithmic Trading — Moving Average Crossover Backtest

**Topic 6: Import and Process Finance Data**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO5: Backtest a moving-average crossover strategy on three years of market data, computing performance KPIs and visualising the signals.

## Goal

The capstone activity for Topic 6, from the reference slide. The learner prompts for a ticker and for short and long moving-average windows, downloads three years of data with yfinance, generates buy and sell signals where the short SMA crosses the long SMA, and backtests the resulting position against buy-and-hold. Performance is reported as total return, annualised return, annualised volatility, Sharpe ratio at a zero risk-free rate, and maximum drawdown. A matplotlib chart plots the price with both moving averages, green '^' markers at buy signals and red 'v' markers at sell signals. The whole run is wrapped in the Topic 5 error handling and uses the Topic 6 cleaning decisions.

## What you'll build

A uv project `lab-42-ma-crossover-backtest` with backtest.py, a printed KPI table comparing the strategy with buy-and-hold, and backtest_chart.png showing price, both SMAs and the marked signals.

**Tools:** uv, yfinance, pandas, numpy, matplotlib, AI coding assistant

## Step-by-step

1. Create the project and add the full backtesting stack.

   ```bash
   uv init lab-42-ma-crossover-backtest && cd lab-42-ma-crossover-backtest && uv add yfinance pandas numpy matplotlib
   ```

2. AI STEP — prompt your AI assistant with the full specification: "Write a Python script using yfinance, pandas, numpy and matplotlib that backtests a Moving Average Crossover strategy on 3 years of daily data. Prompt the user for a stock ticker and integer short and long SMA windows. Generate a buy signal when the short SMA crosses above the long SMA and a sell signal when it crosses below. Compute Total Return, Annualised Return, Annualised Volatility, Sharpe Ratio at a 0 percent risk-free rate, and Maximum Drawdown, for both the strategy and buy-and-hold. Plot the close price with both moving average lines, green '^' markers at buy signals and red 'v' markers at sell signals, and save it as backtest_chart.png. Handle an invalid ticker with try/except."
3. Save the result as backtest.py and READ IT BEFORE RUNNING. Check three specific things: that the signal is shifted by one day before being applied to returns, that the SMAs use only past data, and that the drawdown is computed from the cumulative equity curve.

   ```bash
   touch backtest.py
   ```

4. Run the backtest on AAPL with windows 20 and 50.

   ```bash
   uv run python backtest.py
   ```

5. Discuss the look-ahead bias check: if the position is not shifted by one day, the strategy trades on a signal derived from the same day's close — an impossible trade that flatters every KPI. Confirm your script shifts.
6. Fix any look-ahead bias you found, re-run, and compare the KPIs before and after — note how much the Sharpe ratio fell.

   ```bash
   uv run python backtest.py
   ```

7. Run the same backtest on a Singapore bank, D05.SI, with the same windows and compare the results across the two markets.

   ```bash
   uv run python backtest.py
   ```

8. Sweep the window pair: run 10/30, 20/50 and 50/200 on the same ticker and tabulate total return and Sharpe for each.

   ```bash
   uv run python backtest.py
   ```

9. Discuss overfitting: the best window pair in this sample is not the best pair out of sample. Why does picking the winner from a sweep overstate expected live performance?
10. Inspect backtest_chart.png and verify the markers sit exactly at the crossover points and that buys and sells alternate.

   ```bash
   open backtest_chart.png
   ```

11. Add the Topic 6 cleaning decision explicitly: forward-fill any missing closes before computing the SMAs, and print a note stating the treatment used.

   ```bash
   uv run python backtest.py
   ```

12. Write a short conclusion in the script header: did the crossover strategy beat buy-and-hold on your ticker after the look-ahead fix, and what would you need to add before trusting the result (transaction costs, slippage, out-of-sample testing)?

## Test it

The script accepts a ticker and two windows, prints a KPI table with Total Return, Annualised Return, Annualised Volatility, Sharpe Ratio and Maximum Drawdown for both the strategy and buy-and-hold, writes backtest_chart.png with both SMA lines and alternating green '^' and red 'v' markers at the crossovers, and exits cleanly on an invalid ticker.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
