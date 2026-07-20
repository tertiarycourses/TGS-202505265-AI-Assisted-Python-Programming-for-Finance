"""Lab 8 — String Methods and Extracting the Company Name from an Email

Topic 2: Data Types and Operators
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO2: Apply the string data type and its methods to parse, clean and classify financial client data.

Goal: The learner exercises the core string methods — len, upper, lower, strip, split, startswith, replace — on messy client data, then mirrors the reference notebook activity by extracting a corporate client's company name from an email address, hardening it against malformed input and free-email domains such as gmail.com.

You will build: A script `extract_company.py` that parses an email address and returns the corporate client's company name, with validation.
Tools: uv, Python 3.12, VS Code / Cursor / Google Colab, Gemini or Copilot

Run this lab with uv:
    uv run python string_methods_and_extracting_the_compan.py
"""


def main():
    print("Lab 8: String Methods and Extracting the Company Name from an Email")

    # ---- Step 1 -----------------------------------------------------------
    # Create the project.
    #   $ uv init lab-08-string-methods && cd lab-08-string-methods
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # Create strings_demo.py using a messy value of the kind that arrives from a
    # CRM export, and print its length, upper case and stripped form.
    #   $ text = '  DBS Group Holdings Ltd.  '; print(len(text), text.upper(), repr(text.strip()))
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Split it into words and test a prefix, the way a screening rule would.
    #   $ print(text.strip().split(' '), text.strip().startswith('DBS'))
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # Clean a ticker field with replace and strip so 'd05 .si ' becomes a valid
    # uppercase ticker.
    #   $ print(' d05 .si '.replace(' ', '').upper())
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Now start extract_company.py and implement the reference activity: split
    # the email on '@' and take the first label of the domain.
    #   $ email = input('Enter your email address: '); parts = email.split('@')
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Guard the split and extract the company label, printing it in upper case.
    #   $ if len(parts) == 2: print(f"Extracted Company Name: {parts[1].split('.')[0].upper()}")
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Run it against angch@tertiaryinfotech.com and against treasury@dbs.com.sg.
    #   $ uv run python extract_company.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # PROMPT THE AI ASSISTANT with: 'Harden extract_company.py. Reject an input
    # with no @ or more than one @, or an empty local part or domain, printing a
    # clear validation message. Treat gmail.com, yahoo.com, hotmail.com and
    # outlook.com as personal domains and print PERSONAL ACCOUNT - NOT A
    # CORPORATE CLIENT instead of a company name. Handle multi-level domains
    # such as dbs.com.sg by taking only the first label. Also add a function
    # that processes a list of ten sample client emails and prints a table of
    # email, company and account type.' Apply the code.
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # REVIEW the AI output: check the personal-domain list is compared in lower
    # case, that the multi-@ case is genuinely rejected, and that the batch
    # function does not stop at the first bad row.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Run the batch function and confirm the table.
    #   $ uv run python extract_company.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Test the edge cases: 'no-at-sign', 'a@@b.com', '@dbs.com', 'user@', and
    # 'ANALYST@UOB.COM.SG'.
    #   $ uv run python extract_company.py
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # treasury@dbs.com.sg returns 'DBS', analyst@uob.com.sg returns 'UOB',
    # jane@gmail.com is flagged as a personal account, and every malformed input
    # prints a validation message rather than a traceback.


if __name__ == "__main__":
    main()
