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
        group = row[2].strip().upper()

        victims = float(row[5] or 0)

        male = 0
        female = 0
        total = 0

        if "MALE" in group:
            male = victims
        elif "FEMALE" in group:
            female = victims
        elif "TOTAL" in group:
            total = victims

        print(f"{state},{year}\t{int(male)},{int(female)},{int(total)}")

    except (ValueError, IndexError):
        continue

