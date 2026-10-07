#!/usr/bin/env python3
import sys

current_key = None
reported = 0
chargesheeted = 0
convicted = 0
pending_trial = 0

def emit_result():
    if current_key is not None:
        print(
            f"{current_key}\t"
            f"{int(reported)},"
            f"{int(chargesheeted)},"
            f"{int(convicted)},"
            f"{int(pending_trial)}"
        )

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, values = line.split("\t", 1)

        r, c, v, p = map(float, values.split(","))

        if current_key != key:
            emit_result()

            current_key = key
            reported = 0
            chargesheeted = 0
            convicted = 0
            pending_trial = 0

        reported += r
        chargesheeted += c
        convicted += v
        pending_trial += p

    except ValueError:
        continue

emit_result()
