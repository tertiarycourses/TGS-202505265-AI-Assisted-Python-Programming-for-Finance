# Lab 34 — Activity: Loan Risk Classifier with Guarded Data Loading

**Topic 5: Error Handling Using Exception**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO4: Build an XGBoost multi-class credit-risk classifier whose data loading, feature selection and scoring are wrapped in exception handling that degrades gracefully.

## Goal

The capstone activity for Topic 5, from the reference slide. The learner trains an XGBoost multi-class credit-risk classifier on creditloandata.csv. The loader is wrapped in try/except: if the CSV is absent or unreadable, the except branch generates a synthetic dataset of 120 mock records with income, debt-to-income and credit-score features and assigns risk labels 0/1/2 from a scoring function, so the model always trains. A second guard handles missing feature columns by dropping them and warning, rather than crashing. The model is evaluated with accuracy, a classification report, a Seaborn confusion-matrix heatmap and a multiclass ROC curve.

## What you'll build

A uv project `lab-34-loan-risk-classifier` with loan_risk.py, a synthetic-data fallback, a printed classification report, confusion_matrix.png and roc_curve.png.

**Tools:** uv, pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, AI coding assistant

## Step-by-step

1. Create the project and add the modelling stack.

   ```bash
   uv init lab-34-loan-risk-classifier && cd lab-34-loan-risk-classifier && uv add pandas numpy scikit-learn xgboost matplotlib seaborn
   ```

2. AI STEP — prompt your AI assistant with the full requirement: "Write a Python script that trains an XGBoost multi-class classifier for credit risk. Wrap the data loading in try/except: try to read 'creditloandata.csv' with pandas; if FileNotFoundError or pandas.errors.EmptyDataError is raised, generate a synthetic dataset of 120 records with columns income, debt_to_income and credit_score, and assign risk labels 0, 1, 2 from a custom scoring function. Split 75/25 stratified, train XGBClassifier, then report accuracy, a classification_report, a Seaborn confusion-matrix heatmap and a multiclass ROC curve. Print clearly which data source was used."
3. Save the generated code as loan_risk.py and READ IT before running — check the fallback actually produces three populated classes and that the except branch is not catching bare Exception.

   ```bash
   touch loan_risk.py
   ```

4. Run the script with NO creditloandata.csv present and confirm the synthetic fallback path is taken and the model still trains.

   ```bash
   uv run python loan_risk.py
   ```

5. Create a small real creditloandata.csv with the three feature columns and a risk column, re-run, and confirm the try branch is taken instead.

   ```bash
   uv run python loan_risk.py
   ```

6. Add a THIRD guard: wrap feature selection in try/except KeyError so that if credit_score is missing from the CSV the script warns, drops that feature and trains on the remaining two rather than crashing.
7. Test the missing-feature path by deleting the credit_score column from the CSV and re-running.

   ```bash
   uv run python loan_risk.py
   ```

8. Discuss: the degraded two-feature model still produced a number. Is a silently degraded credit model acceptable? Agree as a class where the boundary sits between graceful degradation and a failure that must stop the run.
9. Break the script deliberately — feed it a CSV whose risk column contains the string 'high' instead of an integer — capture the resulting traceback, and paste it into your AI assistant with: "Explain this traceback from my XGBoost credit risk script and give me the exception handler that converts the label column safely, raising a clear InvalidLabelError if the values cannot be mapped to 0, 1 or 2."

   ```bash
   uv run python loan_risk.py 2> traceback.txt
   ```

10. Apply and test the AI's handler, then confirm the confusion-matrix heatmap and ROC curve are written to disk on a successful run.

   ```bash
   uv run python loan_risk.py && ls -la *.png
   ```

11. Write a five-line 'error handling contract' comment at the top of loan_risk.py listing every exception the script handles and the business decision behind each response.

## Test it

The script runs to completion in all four scenarios — CSV present, CSV absent, feature column missing, label column malformed — never exits with an uncaught traceback, prints accuracy above 0.60 on the synthetic data, and writes confusion_matrix.png and roc_curve.png.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
