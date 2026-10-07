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
        if row[0].strip().upper() == "STATE/UT":
            continue

        # We need at least STATE/UT, DISTRICT, YEAR and TOTAL IPC CRIMES
        if len(row) < 33:
            continue

        state = row[0].strip()
        district = row[1].strip()
        year = row[2].strip()
        total_ipc = row[32].strip()

        # Remove aggregate/summary rows
        if district.upper() == "TOTAL":
            continue

        if state.upper().startswith("TOTAL"):
            continue

        # Validate year and crime value
        year_int = int(year)
        total_ipc_int = int(float(total_ipc))

        # Mapper output:
        # key = state,year
        # value = total IPC crimes
        print(f"{state},{year_int}\t{total_ipc_int}")

    except (ValueError, IndexError):
        continue
