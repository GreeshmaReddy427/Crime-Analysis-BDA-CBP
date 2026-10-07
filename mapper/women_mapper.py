#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        row = next(csv.reader([line]))

        # Skip header
        if row[0].strip().upper() == "AREA_NAME":
            continue

        if len(row) < 21:
            continue

        state = row[0].strip()
        year = int(float(row[1].strip()))

        cases_chargesheeted = float(row[7] or 0)
        cases_convicted = float(row[9] or 0)
        cases_reported = float(row[17] or 0)
        pending_trial = float(row[15] or 0)

        print(
            f"{state},{year}\t"
            f"{cases_reported},"
            f"{cases_chargesheeted},"
            f"{cases_convicted},"
            f"{pending_trial}"
        )

    except (ValueError, IndexError):
        continue
