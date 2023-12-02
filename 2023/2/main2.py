#!/usr/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

ret = 0
for ii in range(len(lines)):
	line = lines[ii]
	maxes = {
		'red': 0,
		'green': 0,
		'blue': 0
	}
	for sett in line.split(';'):
		counts = {"red": 0, "green": 0, "blue": 0}
		for pull in sett.split(','):
			count, color = pull.strip().split()
			counts[color] += int(count)
		for color in maxes.keys():
			maxes[color] = max(maxes[color], counts[color])
	ret += maxes['red'] * maxes['green'] * maxes['blue']

print(ret)	
