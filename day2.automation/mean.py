#!/usr/bin/python

import sys

def mean(values):
    if len(values) == 0:
        return 0

    s = 0
    for val in values:
        s += val

    return s

input_values = []
for line in sys.stdin:
    input_values.append(float(line))
print mean(input_values)
