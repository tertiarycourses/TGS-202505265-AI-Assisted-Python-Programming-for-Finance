# Lab 5 — Number and String Literal Formatting for Financial Reporting

**Topic 2: Data Types and Operators**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO2: Apply Python number and string data types and literal formatting to present financial figures in board-ready precision.

## Goal

The learner works with int and float financial values and uses f-string literal formatting to render revenue and market capitalisation in millions and billions, percentages to basis point precision, and currency with thousands separators — then confronts float rounding, the reason Decimal exists in settlement systems.

## What you'll build

A script `format_report.py` that renders a set of raw financial figures as a formatted revenue and market-cap summary in millions.

**Tools:** uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

## Step-by-step

1. Create the project.

   ```bash
   uv init lab-05-number-format && cd lab-05-number-format
   ```

2. Create format_report.py with two raw revenue figures using Python's numeric underscore separators for readability.

   ```bash
   num1 = 12_345_678.90; num2 = 7_890_123.45; result = num1 + num2
   ```

3. Format the sum in millions to two decimals — the standard unit in an SGX results announcement.

   ```bash
   print(f'{num1/1_000_000:.2f}M + {num2/1_000_000:.2f}M = {result/1_000_000:.2f}M')
   ```

4. Add a market-cap line in billions and a margin line as a percentage.

   ```bash
   print(f'Market cap: {84_500_000_000/1_000_000_000:.2f}B | Net margin: {0.2837:.2%}')
   ```

5. Demonstrate the float trap that matters in settlement: run the classic check and note the result is not exactly 0.3.

   ```bash
   uv run python -c "print(0.1 + 0.2, 0.1 + 0.2 == 0.3)"
   ```

6. Discuss why a bank posts ledger entries with Decimal or integer cents rather than float, and where the tolerance threshold sits in your own organisation.
7. PROMPT THE AI ASSISTANT with: 'Extend format_report.py with a function format_sgd(amount) that returns a string: values of 1 billion or more as $x.xxB, values of 1 million or more as $x.xxM, values of 1 thousand or more as $x.xK, and anything smaller as $x,xxx.xx. Include a right-aligned printed table of DBS 84500000000, Singtel 52300000000, CapitaLand 13800000000 and a small holding of 4250.75.' Apply the code.
8. REVIEW the AI output: check the thresholds are tested largest-first, that negative amounts do not break the sign, and that the alignment uses an f-string width specifier.
9. Run the script and inspect the alignment of the table.

   ```bash
   uv run python format_report.py
   ```

10. Test the boundaries: pass exactly 1_000_000, exactly 999_999.99, 0 and -2_500_000 to format_sgd and confirm each renders sensibly.

   ```bash
   uv run python format_report.py
   ```


## Test it

format_sgd returns '$84.50B' for DBS, '$13.80M'-style output for millions, and the printed table is right-aligned with every figure carrying its correct unit suffix.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
