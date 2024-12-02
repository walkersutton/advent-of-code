#!/usr/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

def safe_report(report):
	is_increasing = report[1] - report[0] > 0
	for ii in range(len(report) - 1):
		a, b = report[ii], report[ii + 1]
		if 1 <= abs(a - b) <= 3:
			if is_increasing:
				if a > b:
					return False
			else:
				if a < b:
					return False
		else:
			return False
	return True

num_safe = 0
for line in lines:
	report = [int(v) for v in line.split()]
	num_safe += 1 if safe_report(report) else 0

print(num_safe)
