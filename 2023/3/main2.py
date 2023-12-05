#!/opt/homebrew/bin/python3

import os
import sys
from collections import defaultdict

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

def gears_posn_touches(posn):
	gears = []
	dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
	def valid_idx(posn):
		return 0 <= posn[0] < len(lines) and 0 <= posn[1] < len(lines[posn[0]])
	def is_gear(posn):
		return lines[posn[0]][posn[1]] == '*'
	for dy, dx in dirs:
		newposn = (dy + posn[0], dx + posn[1])
		if valid_idx(newposn) and is_gear(newposn):
			gears.append(newposn)
	return gears

def gears_word_touches(posns):
	gears = set()
	for posn in posns:
		for gear in gears_posn_touches(posn):
			gears.add(gear)
	return gears
		
all_nums = []
for row in range(len(lines)):
	cur = []
	for col in range(len(lines[row])):
		c = lines[row][col]
		if c.isnumeric():
			cur.append((c, row, col))
		else:
			if len(cur) > 0:
				full_num = []
				dig_posns = []
				for dig, row, col in cur:
					full_num.append(dig)
					dig_posns.append((row, col))
				all_nums.append((int(''.join(full_num)), dig_posns))
				cur = []
	if len(cur) > 0:
		full_num = []
		dig_posns = []
		for dig, row, col in cur:
			full_num.append(dig)
			dig_posns.append((row, col))
		all_nums.append((int(''.join(full_num)), dig_posns))
		
gear_map = defaultdict(list)
for num, posns in all_nums:
	gears = gears_word_touches(posns)
	for gear in gears:
		gear_map[gear].append(num)

ret = 0
for gear, vals in gear_map.items():
	if len(vals) == 2:
		ret += vals[0] * vals[1]

print(ret)
