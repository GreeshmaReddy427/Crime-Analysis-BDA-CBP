#!/usr/bin/env python3
import sys

current_key = None
total_stolen = 0
total_recovered = 0

def emit_result():
    if current_key is not None:
        print(f"{current_key}\t{int(total_stolen)},{int(total_recovered)}")

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, values = line.split("\t", 1)
        stolen, recovered = map(float, values.split(","))

        if current_key != key:
            emit_result()

            current_key = key
            total_stolen = 0
            total_recovered = 0

        total_stolen += stolen
        total_recovered += recovered

    except ValueError:
        continue

emit_result()
