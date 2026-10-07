#!/usr/bin/env python3
import sys

current_key = None
male = 0
female = 0
total = 0

def emit_result():
    if current_key is not None:
        print(f"{current_key}\t{int(male)},{int(female)},{int(total)}")

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, values = line.split("\t", 1)
        m, f, t = map(float, values.split(","))

        if current_key != key:
            emit_result()

            current_key = key
            male = 0
            female = 0
            total = 0

        male += m
        female += f
        total += t

    except ValueError:
        continue

emit_result()
