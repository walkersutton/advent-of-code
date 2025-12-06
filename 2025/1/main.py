import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

data = 'data.txt'
lines = input_as_lines(data)

dial = 50
count = 0

for line in lines:
    direction, val = line[0], line[1:]
    val = int(val)
    
    if direction == 'L':
        dial -= val
    else:
        dial += val

    dial %= 100
    if dial < 0:
        dial += 100
    elif dial > 99:
        dial -= 100
    
    if dial == 0:
        count += 1

print(count)
