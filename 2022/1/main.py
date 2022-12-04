import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
abs_max = 0
temp_sum = 0

for line in lines:
    if line not in ('', '\n'):
        temp_sum += int(line)
    else:
        abs_max = max(abs_max, temp_sum)
        temp_sum = 0

abs_max = max(abs_max, temp_sum)

print(abs_max)
