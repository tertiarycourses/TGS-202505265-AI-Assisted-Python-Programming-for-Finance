#!/usr/bin/env python3
"""Generate the labs/ folder from the single-source content module.

Produces, for every lab in data_domain1..9:
  labs/lab-NN-<slug>/README.md      the step-by-step instructions
  labs/lab-NN-<slug>/<script>.py    a runnable starter script with the steps as
                                    a guided TODO scaffold
and one combined notebook:
  labs/<SHORT_TITLE>-All-Labs.ipynb  every lab as a markdown + code cell pair,
                                     openable directly in Google Colab.

Everything is derived from the same dicts that drive the PPT, LP and LG, so the
labs can never drift from the rest of the courseware.
"""
import os, re, sys, json

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5; from data_domain6 import DOMAIN6
from data_domain7 import DOMAIN7; from data_domain8 import DOMAIN8
from data_domain9 import DOMAIN9
ACT = (DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5
       + DOMAIN6 + DOMAIN7 + DOMAIN8 + DOMAIN9)

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE)
LABS = os.path.join(REPO, "labs")
os.makedirs(LABS, exist_ok=True)

TOPIC = {t["num"]: t for t in C.TOPICS}

def slug(text, maxlen=48):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:maxlen].rstrip("-")

def script_name(a):
    return slug(a["title"], 40).replace("-", "_") + ".py"

# ---------------------------------------------------------------- per-lab files
def lab_readme(a):
    t = TOPIC[a["topic"]]
    out = [f"# Lab {a['num']} — {a['title']}", "",
           f"**Topic {t['num']}: {t['title']}**  ·  Course: {C.TITLE} ({C.COURSE_CODE})", "",
           f"**Learning objective:** {a['objective']}", "",
           "## Goal", "", a["desc"], "",
           "## What you'll build", "", f"{a['build']}", "",
           f"**Tools:** {a['services']}", "",
           "## Step-by-step", ""]
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        out.append(f"{i}. {instr}")
        if cmd:
            out += ["", "   ```bash", f"   {cmd}", "   ```", ""]
    out += ["", "## Test it", "", a["test"], "",
            "---", "",
            f"Part of *{C.TITLE}* ({C.COURSE_CODE}) — {C.ORG}. "
            f"Accredited under IBF Standard {C.ACCREDITATION['standard']}.", ""]
    return "\n".join(out)

def lab_script(a):
    t = TOPIC[a["topic"]]
    L = [f'"""Lab {a["num"]} — {a["title"]}', "",
         f"Topic {t['num']}: {t['title']}",
         f"Course: {C.TITLE} ({C.COURSE_CODE})", "",
         f"Objective: {a['objective']}", "",
         f"Goal: {a['desc']}", "",
         f"You will build: {a['build']}",
         f"Tools: {a['services']}", "",
         "Run this lab with uv:",
         f"    uv run python {script_name(a)}", '"""', "", "", "def main():", ]
    L.append(f'    print("Lab {a["num"]}: {a["title"]}")')
    L.append("")
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        L.append(f"    # ---- Step {i} " + "-" * max(4, 60 - len(str(i))))
        for line in _wrap(instr, 74):
            L.append(f"    # {line}")
        if cmd:
            L.append(f"    #   $ {cmd}")
        L.append("    # TODO: implement this step")
        L.append("")
    L += ["    # ---- Test it " + "-" * 52]
    for line in _wrap(a["test"], 74):
        L.append(f"    # {line}")
    L += ["", "", 'if __name__ == "__main__":', "    main()", ""]
    return "\n".join(L)

def _wrap(text, width):
    words = str(text).split(); lines = []; cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: lines.append(cur)
    return lines or [""]

written = 0
for a in ACT:
    d = os.path.join(LABS, f"lab-{a['num']:02d}-{slug(a['title'])}")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "README.md"), "w") as f:
        f.write(lab_readme(a))
    with open(os.path.join(d, script_name(a)), "w") as f:
        f.write(lab_script(a))
    written += 1

# ---------------------------------------------------------------- labs index
idx = [f"# {C.TITLE} — Hands-On Labs", "",
       f"Course code **{C.COURSE_CODE}** · {C.ORG} · Version {C.VERSION} ({C.VERSION_DATE})", "",
       f"{len(ACT)} labs across {len(C.TOPICS)} topics. Every lab is a self-contained "
       f"[uv](https://docs.astral.sh/uv/) project.", "",
       "## Getting started", "",
       "```bash",
       "# install uv once",
       "curl -LsSf https://astral.sh/uv/install.sh | sh",
       "",
       "# each lab is its own project",
       "cd lab-01-*/",
       "uv init .",
       "uv add pandas yfinance matplotlib",
       "uv run python *.py",
       "```", "",
       "All labs are also combined into a single notebook you can open in Google Colab: "
       f"[`{C.SHORT_TITLE}-All-Labs.ipynb`]({C.SHORT_TITLE}-All-Labs.ipynb).", "",
       "## Labs by topic", ""]
for t in C.TOPICS:
    acts = [a for a in ACT if a["topic"] == t["num"]]
    idx += [f"### Topic {t['num']} — {t['title']}", "", f"*{t['subtitle']}*", ""]
    idx.append("| # | Lab | You'll build |")
    idx.append("|---|-----|--------------|")
    for a in acts:
        d = f"lab-{a['num']:02d}-{slug(a['title'])}"
        idx.append(f"| {a['num']} | [{a['title']}]({d}/README.md) | {a['build']} |")
    idx.append("")
with open(os.path.join(LABS, "README.md"), "w") as f:
    f.write("\n".join(idx))

# ---------------------------------------------------------------- combined notebook
cells = []
def md(src):  cells.append({"cell_type": "markdown", "metadata": {}, "source": src})
def cd(src):  cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                            "outputs": [], "source": src})

md([f"# {C.TITLE}\n", "\n",
    f"**Course code:** {C.COURSE_CODE}  \n",
    f"**Conducted by:** {C.ORG} ({C.UEN.replace('UEN: ', 'UEN ')})  \n",
    f"**Version:** {C.VERSION} · {C.VERSION_DATE}  \n",
    f"**Accreditation:** {C.ACCREDITATION['framework']} · IBF Standard "
    f"{C.ACCREDITATION['standard']} · Funded under IBF-STS\n", "\n",
    f"This notebook combines all {len(ACT)} hands-on labs. Each lab appears as a set of "
    "instructions followed by a code cell for you to complete.\n", "\n",
    "Run the setup cell below first.\n"])
cd(["# SETUP — Google Colab only.\n",
    "# This notebook is the Colab companion to the labs. Colab manages its own\n",
    "# environment, so the packages are installed into the running session here.\n",
    "#\n",
    "# WORKING LOCALLY? Do NOT run this cell. Every lab is a uv project:\n",
    "#     uv init lab-01-hello-finance\n",
    "#     cd lab-01-hello-finance\n",
    "#     uv add pandas numpy matplotlib yfinance streamlit scikit-learn\n",
    "#     uv run python main.py\n",
    "# uv is the tool used throughout this course; pip is used below only because\n",
    "# Colab has no project directory to attach a uv environment to.\n",
    "!uv pip install --system -q pandas numpy matplotlib yfinance streamlit scikit-learn \\\n",
    "  || %pip install -q pandas numpy matplotlib yfinance streamlit scikit-learn\n",
    "\n",
    "import pandas as pd, numpy as np, matplotlib.pyplot as plt\n",
    "print('Environment ready — pandas', pd.__version__)\n"])

for t in C.TOPICS:
    acts = [a for a in ACT if a["topic"] == t["num"]]
    md([f"---\n", "\n", f"# Topic {t['num']} — {t['title']}\n", "\n",
        f"*{t['subtitle']}*\n", "\n",
        f"**Topic weighting:** {t['weighting']}\n", "\n",
        "**Key concepts**\n", "\n"] + [f"- {c}\n" for c in t["concepts"]])
    for a in acts:
        src = [f"## Lab {a['num']} — {a['title']}\n", "\n",
               f"**Objective:** {a['objective']}\n", "\n",
               f"**Goal:** {a['desc']}\n", "\n",
               f"**You'll build:** {a['build']}\n", "\n",
               f"**Tools:** {a['services']}\n", "\n",
               "### Steps\n", "\n"]
        for i, (instr, cmd) in enumerate(a["steps"], 1):
            src.append(f"{i}. {instr}\n")
            if cmd:
                src.append(f"   ```bash\n   {cmd}\n   ```\n")
        src += ["\n", f"**Test it:** {a['test']}\n"]
        md(src)
        cd([f"# Lab {a['num']} — {a['title']}\n",
            f"# Objective: {a['objective']}\n",
            "#\n",
            "# Work through the steps above. Use the AI assistant to draft the code,\n",
            "# then READ, RUN and TEST it before moving on.\n", "\n",
            "\n"])

md(["---\n", "\n", "## End of the labs\n", "\n",
    "You have completed every hands-on lab for this course. Before the assessment:\n", "\n",
    "1. Re-run any lab whose **Test it** check you could not pass from memory.\n",
    "2. Make sure you can write a function from a plain-English requirement *without* an AI assistant.\n",
    "3. Review the Financial Formula Reference in the Learner Guide.\n", "\n",
    f"© 2026 {C.ORG}. All rights reserved.\n"])

nb = {"cells": cells,
      "metadata": {"colab": {"provenance": [], "toc_visible": True},
                   "kernelspec": {"display_name": "Python 3", "name": "python3"},
                   "language_info": {"name": "python"}},
      "nbformat": 4, "nbformat_minor": 0}
NB = os.path.join(LABS, f"{C.SHORT_TITLE}-All-Labs.ipynb")
with open(NB, "w") as f:
    json.dump(nb, f, indent=1)

print(f"Wrote {written} lab folders (README.md + .py) into {LABS}")
print(f"Wrote labs index      {os.path.join(LABS,'README.md')}")
print(f"Wrote combined notebook {NB}  ({len(cells)} cells)")
