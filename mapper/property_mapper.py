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

        if len(row) < 8:
            continue

        state = row[0].strip()
        year = row[1].strip()

        cases_recovered = float(row[4] or 0)
        cases_stolen = float(row[5] or 0)
        value_recovered = float(row[6] or 0)
        value_stolen = float(row[7] or 0)

        year = int(float(year))

        print(
            f"{state},{year}\t"
            f"{cases_stolen},{cases_recovered},"
            f"{value_stolen},{value_recovered}"
        )

    except (ValueError, IndexError):
        continue
