# Lab 54 — Inheritance — an Instrument Base Class with Equity and Bond Subclasses

**Topic 8: Object Oriented Programming**  ·  Course: AI Assisted Python Programming for Finance (TGS-2025052659)

**Learning objective:** LO7: Use inheritance so Equity and Bond extend a shared Instrument class without duplicating code.

## Goal

The learner refactors to a proper instrument hierarchy. A base Instrument class holds what every instrument shares (identifier, name, quantity, currency) and defines a value() method that raises NotImplementedError. Equity(Instrument) adds price and dividend_yield; Bond(Instrument) adds face_value, coupon_rate, years_to_maturity and market_yield, and values itself by discounting coupons and principal. Both use super().

## What you'll build

An instruments.py module with Instrument, Equity and Bond classes, each subclass calling super().__init__().

**Tools:** uv, Python 3.12, VS Code / Cursor AI assistant

## Step-by-step

1. Create the project.

   ```bash
   uv init lab-54-inheritance-instruments && cd lab-54-inheritance-instruments
   ```

2. Sketch the hierarchy on paper: what data does EVERY instrument have, and what belongs only to an Equity or only to a Bond? Only the shared fields go in the base class.
3. Prompt your AI assistant: "Write a Python class hierarchy for financial instruments. Base class Instrument has __init__(identifier, name, quantity, currency='SGD'), a value() method that raises NotImplementedError, and an income() method returning 0.0. Subclass Equity(Instrument) adds price and dividend_yield, overrides value() as quantity * price and income() as value * dividend_yield. Subclass Bond(Instrument) adds face_value, coupon_rate, years_to_maturity and market_yield, and overrides value() to return the present value of the coupon stream plus the discounted principal, multiplied by quantity. Both subclasses must call super().__init__() and each must have a __str__."
4. Save as instruments.py and confirm both subclasses call super().__init__() rather than re-assigning the shared attributes.
5. Verify the inheritance chain with isinstance and the MRO.

   ```bash
   uv run python -c "from instruments import Instrument, Equity, Bond; e=Equity('D05','DBS',100,38.40,0.055); print(isinstance(e, Instrument), Equity.__mro__)"
   ```

6. Confirm the abstract base refuses to value itself.

   ```bash
   uv run python -c "from instruments import Instrument; 
import traceback
try: Instrument('X','Generic',1).value()
except NotImplementedError: print('correctly abstract')"
   ```

7. Value an Equity and a Bond.

   ```bash
   uv run python instruments.py
   ```

8. Sanity-check the bond maths: a bond priced at par (market_yield == coupon_rate) must value at face_value * quantity.

   ```bash
   uv run python -c "from instruments import Bond; b=Bond('SGB10','SG Govt Bond',10,1000,0.03,5,0.03); print(round(b.value(),2))"
   ```

9. Check a discount bond: raise market_yield above coupon_rate and confirm the value falls below par.
10. Discuss: what code would you have duplicated if Equity and Bond were unrelated classes, and what breaks when a third instrument type is added later?

## Test it

isinstance(equity, Instrument) is True; Instrument.value() raises NotImplementedError; a par bond values at exactly face_value * quantity and a bond yielding above its coupon values below par.

---

Part of *AI Assisted Python Programming for Finance* (TGS-2025052659) — Tertiary Infotech Academy Pte Ltd. Accredited under IBF Standard FSE-DIT-3018-1.1.
