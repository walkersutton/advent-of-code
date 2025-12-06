import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

data = 'data.txt'
lines = input_as_lines(data)

dial = 50
count = 0

for line in lines:
    # if dial starts on 0 and goes left, it didn't pass 0
    was_zero = dial == 0

    direction, val = line[0], line[1:]
    val = int(val)
    
    # multiple rotations
    count += int(val/100)
    val %= 100
    
    if direction == 'L':
        dial -= val
    else:
        dial += val

    if dial > 99:
        dial -= 100
        count += 1
    elif dial < 0:
        dial += 100
        if not was_zero:
            count += 1
    elif dial == 0:
        if not was_zero:
            count += 1

print(count)
