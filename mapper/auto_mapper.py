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

        if len(row) < 7:
            continue

        state = row[0].strip()
        year = int(float(row[1].strip()))

        recovered = float(row[5] or 0)
        stolen = float(row[6] or 0)

        print(f"{state},{year}\t{stolen},{recovered}")

    except (ValueError, IndexError):
        continue
