#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
signal_strengths = []
x = 1
operation = 0

for line in lines:
    if len(line.split(' ')) > 1: # addx
        signal_strengths.extend([x, x])
        operation = int(line.split(' ')[1])
    else: # noop
        signal_strengths.append(x)
        operation = 0
    x += operation

for ii, strength in enumerate(signal_strengths):
    pixel_x = ii % 40
    if pixel_x == 0 and ii != 0:
        print('')
    if strength - 1 <= pixel_x <= strength + 1:
        print('#', end='')
    else:
        print('.', end='')
