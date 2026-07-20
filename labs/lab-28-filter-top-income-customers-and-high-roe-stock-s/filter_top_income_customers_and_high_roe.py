"""Lab 28 — Filter — Top Income Customers and High-ROE Stock Screening

Topic 4: Scripting with Function and Lambda
Course: AI Assisted Python Programming for Finance (TGS-2025052659)

Objective: LO3: Construct filter expressions with lambda to select the subset of a dataset that meets a business threshold, and chain filtering with sorting to produce a ranked shortlist.

Goal: Filter is the screening primitive: it keeps only the records where a lambda returns True. You generate 20 mock banking customers with random incomes between $30,000 and $200,000, filter for the top earners above a $150,000 threshold, and produce a sorted priority-contact list. You then apply the same pattern to stock screening (ROE above 10%), large-transaction monitoring and SGX-only ticker selection, and finish by chaining filter with map to build a complete screen-then-compute pipeline — the closing exercise of Topic 4.

You will build: customer_filter.py — a filter-based screening tool producing a ranked top-income customer list, a high-ROE stock screen and a chained filter-then-map pipeline.
Tools: uv, Python 3.12 (random module), Google Colab / Cursor, Gemini or Copilot

Run this lab with uv:
    uv run python filter_top_income_customers_and_high_roe.py
"""


def main():
    print("Lab 28: Filter — Top Income Customers and High-ROE Stock Screening")

    # ---- Step 1 -----------------------------------------------------------
    # Create the uv project.
    #   $ uv init lab-28-customer-filter && cd lab-28-customer-filter
    # TODO: implement this step

    # ---- Step 2 -----------------------------------------------------------
    # In customer_filter.py import random and generate 20 mock customers with a
    # list comprehension: [{'id': i, 'name': f'Customer {i}', 'income':
    # random.randint(30000, 200000)} for i in range(1, 21)].
    # TODO: implement this step

    # ---- Step 3 -----------------------------------------------------------
    # Set random.seed(42) before generating so your run is reproducible —
    # essential when a colleague must verify your screening result. Print the
    # first three customers to confirm.
    #   $ uv run python customer_filter.py
    # TODO: implement this step

    # ---- Step 4 -----------------------------------------------------------
    # ACTIVITY — TOP INCOME CUSTOMERS: set threshold = 150000 and apply
    # top_earners = list(filter(lambda c: c['income'] > threshold, customers)).
    # TODO: implement this step

    # ---- Step 5 -----------------------------------------------------------
    # Print the total customer count, the number of top earners, and then the
    # top earners sorted descending by income using sorted(top_earners,
    # key=lambda x: x['income'], reverse=True), each formatted as 'Customer N:
    # $NNN,NNN'.
    #   $ uv run python customer_filter.py
    # TODO: implement this step

    # ---- Step 6 -----------------------------------------------------------
    # Test the empty result: raise the threshold to 500000, re-run, and confirm
    # the script prints a clear 'no customers meet this threshold' message
    # rather than an empty block. Restore 150000.
    #   $ uv run python customer_filter.py
    # TODO: implement this step

    # ---- Step 7 -----------------------------------------------------------
    # Add three more filter examples: high-ROE stocks (list of dicts, keep roe >
    # 10), large transactions from [120.50, 800.00, 45.00, 1500.25, 300.00]
    # keeping x > 500, and SGX-only tickers from ['AAPL', 'D05.SI', 'TSLA',
    # 'U11.SI', 'GOOG'] using t.endswith('.SI').
    #   $ uv run python customer_filter.py
    # TODO: implement this step

    # ---- Step 8 -----------------------------------------------------------
    # CHAIN FILTER AND MAP: filter the customers to those above the threshold,
    # then map a lambda that adds a 'tier' key ('PLATINUM' above 180000, else
    # 'GOLD') and an estimated annual fee at 0.5% of income. Print the enriched
    # list.
    #   $ uv run python customer_filter.py
    # TODO: implement this step

    # ---- Step 9 -----------------------------------------------------------
    # AI-ASSIST: prompt your AI tool with: "Refactor this filter-plus-lambda
    # screening code to use a named predicate function instead of an inline
    # lambda, add a second filter criterion so only customers who are BOTH above
    # the income threshold AND have an id below 15 are selected, and explain
    # when filter is clearer than a list comprehension with an if." Review the
    # combined predicate for correct and/or logic.
    # TODO: implement this step

    # ---- Step 10 ----------------------------------------------------------
    # Apply the AI version, run it, and manually verify two or three selected
    # records against the raw customer list to confirm both criteria really were
    # applied.
    #   $ uv run python customer_filter.py
    # TODO: implement this step

    # ---- Step 11 ----------------------------------------------------------
    # Produce the final deliverable: a formatted 'PRIORITY WEALTH CONTACT LIST'
    # with a header, a rank column from enumerate, name, income and tier, plus a
    # footer line reporting the total addressable income of the shortlist.
    #   $ uv run python customer_filter.py
    # TODO: implement this step

    # ---- Step 12 ----------------------------------------------------------
    # Discuss: this screen uses income alone. Name two additional fields a bank
    # would need before this list could be used for an actual wealth-management
    # outreach, and one governance concern about acting on it.
    # TODO: implement this step

    # ---- Test it ----------------------------------------------------
    # Run `uv run python customer_filter.py`. With random.seed(42) the run must
    # be reproducible across executions. It must print 20 total customers, the
    # count above $150,000, and a descending-sorted list of those top earners.
    # Raising the threshold to 500000 must produce a 'no customers meet this
    # threshold' message. The final PRIORITY WEALTH CONTACT LIST must show a
    # rank, name, formatted income and PLATINUM/GOLD tier per row, plus a total
    # addressable income footer.


if __name__ == "__main__":
    main()
