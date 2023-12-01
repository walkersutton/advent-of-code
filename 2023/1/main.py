import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

ret = 0

for line in lines:
	first_digit, last_digit = None, None
	for c in line:
		if c.isnumeric():
			if first_digit is None:
				first_digit = c
			last_digit = c
	ret += int(first_digit + last_digit)

print(ret)
