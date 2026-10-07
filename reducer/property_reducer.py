#!/usr/bin/env python3

import sys

current_key = None

cases_stolen = 0
cases_recovered = 0
value_stolen = 0
value_recovered = 0


def emit_result():
    if current_key is None:
        return

    if value_stolen > 0:
        recovery_rate = value_recovered / value_stolen
    else:
        recovery_rate = 0

    print(
        f"{current_key}\t"
        f"{int(cases_stolen)},"
        f"{int(cases_recovered)},"
        f"{int(value_stolen)},"
        f"{int(value_recovered)},"
        f"{recovery_rate:.4f}"
    )


for line in sys.stdin:

    line = line.strip()

    if not line:
        continue

    try:
        key, values = line.split("\t", 1)

        stolen, recovered, stolen_value, recovered_value = map(
            float,
            values.split(",")
        )

        if current_key != key:

            emit_result()

            current_key = key

            cases_stolen = 0
            cases_recovered = 0
            value_stolen = 0
            value_recovered = 0

        cases_stolen += stolen
        cases_recovered += recovered
        value_stolen += stolen_value
        value_recovered += recovered_value

    except ValueError:
        continue


emit_result()

