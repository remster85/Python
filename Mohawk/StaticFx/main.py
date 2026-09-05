"""
Mohawk PythonStage example.

Contract:
  - run(rows) receives the previous stage's output as a list of plain dict
    rows, or None if this is the first stage in the workflow.
  - It must return a list of dict rows (or a pandas.DataFrame, if you have
    one — Mohawk detects it automatically via .to_dict(), no import needed
    here just to comply).
  - Every value must be a flat scalar: str, int, float, bool, None, date,
    datetime, or Decimal. Nested lists/dicts are rejected with a clear error.
"""

from datetime import date


def run(rows):
    if rows is None:
        # First stage in the chain — fabricate some rows so you can see
        # something end-to-end without wiring up a database yet.
        return [
            {"ccy": "EUR", "rate": 1.01},
            {"ccy": "GBP", "rate": 1.37},
            {"ccy": "JPY", "rate": 0.0077},
        ]

    # Middle/last stage — do something with what came before it.
    return [
        {**row, "rate_doubled": row["rate"] * 2, "as_of": date.today()}
        for row in rows
    ]
