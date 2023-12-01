import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
rev_digits = [digit[::-1] for digit in digits]
ret = 0

for line in lines:
	rev_line = line[::-1]
	first_index, last_index = float('inf'), float('inf')
	first_digit, last_digit = None, None

	# spelled out digits
	for ii in range(len(digits)):
		digit = digits[ii]
		rev_digit = rev_digits[ii]
		if digit in line:
			idx = line.index(digit)
			if idx < first_index:
				first_index = idx
				first_digit = str(ii + 1)
		if rev_digit in rev_line:
			idx = rev_line.index(rev_digit)
			if idx < last_index:
				last_index = idx
				last_digit = str(ii + 1)

	# numeric digits
	for ii in range(len(line)):
		c = line[ii]
		rev_c = rev_line[ii]
		if c.isnumeric():
			if ii < first_index:
				first_index = ii
				first_digit = c
		if rev_c.isnumeric():
			if ii < last_index:
				last_index = ii
				last_digit = rev_line[ii]

	ret += int(first_digit + last_digit)

print(ret)
