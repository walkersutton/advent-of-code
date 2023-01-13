#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
cycles = [20, 60, 100, 140, 180, 220]
signal_strengths = []
x = 1
cycle = 1
operation = 0

for line in lines:
    if len(line.split(' ')) > 1: # addx
        cycle += 2
        signal_strengths.extend([x * (cycle - 2), x * (cycle - 1)])
        operation = int(line.split(' ')[1])
    else: # noop
        cycle += 1
        signal_strengths.append(x * (cycle - 1))
        operation = 0
    x += operation

print(sum([signal_strengths[ii - 1] for ii in cycles]))
