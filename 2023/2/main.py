#!/usr/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

maxes = {
	'red': 12,
	'green': 13,
	'blue': 14
}
ret = 0
for ii in range(len(lines)):
	line = lines[ii]
	valid = True
	for sett in line.split(';'):
		counts = {"red": 0, "blue": 0, "green": 0}
		for pull in sett.split(','):
			count, color = pull.strip().split()
			counts[color] += int(count)
		for color in counts.keys():
			if counts[color] > maxes[color]:
				valid = False
				break
	if valid:
		ret += (ii + 1)
			
print(ret)
