# AI Assisted Python Programming for Finance

[![Course](https://img.shields.io/badge/Course-TGS--2025052659-1f6feb)](https://www.tertiarycourses.com.sg/ibf-ai-assisted-python-programming-for-finance.html)
[![IBF](https://img.shields.io/badge/IBF--STS-FSE--DIT--3018--1.1-10b981)](https://www.ibf.org.sg)
[![Python](https://img.shields.io/badge/Python-3.12-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/managed%20by-uv-de5fe9)](https://docs.astral.sh/uv/)
[![Streamlit](https://img.shields.io/badge/Streamlit-capstone-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/)

Courseware for the 4-day instructor-led course **AI Assisted Python Programming for Finance**, delivered by
**Tertiary Infotech Academy Pte Ltd** (UEN 201200696W).

**📅 [Register for this course →](https://www.tertiarycourses.com.sg/ibf-ai-assisted-python-programming-for-finance.html)**

Accredited under the **Skills Framework for Financial Services**, IBF Standard **FSE-DIT-3018-1.1**, and
eligible for funding under the **IBF Standards Training Scheme (IBF-STS)** — 50–70% course fee subsidy,
capped at S$3,000 per candidate per course, subject to all eligibility criteria being met.
Find out more at [ibf.org.sg](https://www.ibf.org.sg).

---

## What this course covers

Learners translate real business requirements from financial services into working, tested Python — using
AI assistants (Google Colab Gemini, GitHub Copilot, Cursor) to draft code, then reviewing and correcting
every line before it is trusted. The course runs from first principles through to a deployed Streamlit
analytics application.

| # | Topic | Labs |
|---|-------|------|
| 1 | Introduction to Python Programming | 1–4 |
| 2 | Data Types and Operators | 5–12 |
| 3 | Problem Solving with Control Structures | 13–20 |
| 4 | Scripting with Function and Lambda | 21–28 |
| 5 | Error Handling Using Exception | 29–34 |
| 6 | Import and Process Finance Data | 35–42 |
| 7 | Aggregate and Visualize Finance Data | 43–50 |
| 8 | Object Oriented Programming | 51–56 |
| 9 | Analyze Finance Data | 57–62 |

**62 hands-on labs**, every one grounded in a financial task — CPF contributions, loan amortisation,
retirement projection, SGX market data, ROE/ROA/PE screening, credit-risk classification, moving-average
crossover backtesting, portfolio and instrument modelling, and a progressive Streamlit dashboard capstone.

## Learning outcomes

- **LO1** Translate business requirements in financial services into Python programming objectives
- **LO2** Apply data types, operators and control structures to financial calculation and classification
- **LO3** Construct reusable functions and lambda expressions to compute financial ratios
- **LO4** Implement error handling that survives missing, zero or malformed market data
- **LO5** Import, clean, filter and process financial data with pandas
- **LO6** Aggregate and visualise financial data, and publish it as an interactive Streamlit application
- **LO7** Apply object-oriented programming to model financial instruments and analysers
- **LO8** Analyse financial data with apply/pipe pipelines, assess code for gaps, and test the results

## Repository layout

```
courseware/    slide deck (PPTX + PDF), Lesson Plan and Learner Guide (DOCX + PDF)
labs/          62 lab folders (README.md + starter .py) + the combined Colab notebook
LG-*.md        the Learner Guide as Markdown, generated from the same source as the DOCX
```

> The assessment set (question papers and answer keys) is **deliberately excluded** from this
> repository — it is trainer-only material and is distributed through the LMS.
>
> The `reference/` folder (the original source deck and notebook this courseware was derived
> from) is likewise **excluded** — it is third-party source material, not ours to republish.

## Running the labs

Every lab is a self-contained [uv](https://docs.astral.sh/uv/) project. uv replaces pip, virtualenv and
pyenv, and records exact dependency versions — reproducibility is an audit requirement in financial
services.

```bash
# install uv once
curl -LsSf https://astral.sh/uv/install.sh | sh          # macOS / Linux

# then, per lab
cd labs/lab-03-cpf-contribution-calculator
uv init .
uv add pandas yfinance matplotlib
uv run python cpf_contribution_calculator.py
```

Prefer the browser? Open [`labs/AI Assisted Python Programming for Finance-All-Labs.ipynb`](labs/)
in Google Colab — every lab is included as an instruction cell plus a code cell.

The Streamlit capstone (labs 49, 50, 61, 62) builds one application progressively:

```bash
uv add streamlit
uv run streamlit run app.py
```

## Single-source build

All artifacts are generated from one content module, so the slides, Lesson Plan, Learner Guide and labs
cannot drift apart:

```
course_data.py + data_domain1..9.py
        │
        ├─→ build_slides.py        → courseware/*.pptx
        ├─→ build_lesson_plan.py   → courseware/LP-*.docx
        ├─→ build_learner_guide.py → courseware/LG-*.docx + LG-*.md
        └─→ build_labs.py          → labs/**  + the combined .ipynb
```

```bash
bash .claude/skills/courseware-build/build/build_courseware.sh
python3 .claude/skills/courseware-build/build/build_labs.py
```

## Assessment

| Instrument | Format | Duration |
|---|---|---|
| Written Assessment (WA) | 8 open-ended short-answer questions (K1–K8) | 60 min |
| Practical Test (PP) | 7 open-ended practical questions (A1.1–A1.9) | 120 min |

Open book — slides, Learner Guide and lab files. Passing score **80%**. A minimum of **75% attendance**
is required to be eligible for assessment and IBF-STS funding.

---

**Register:** [AI Assisted Python Programming for Finance](https://www.tertiarycourses.com.sg/ibf-ai-assisted-python-programming-for-finance.html)

© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). All rights reserved.
[www.tertiarycourses.com.sg](https://www.tertiarycourses.com.sg) · enquiry@tertiaryinfotech.com · +65 6100 0613
