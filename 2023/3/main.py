#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

def touching_symbol(posn):
	dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
	def valid_idx(posn):
		return 0 <= posn[0] < len(lines) and 0 <= posn[1] < len(lines[posn[0]])
	def is_symbol(posn):
		val = lines[posn[0]][posn[1]]
		return (not val.isnumeric()) and val != '.'
	for dy, dx in dirs:
		newposn = (dy + posn[0], dx + posn[1])
		if valid_idx(newposn) and is_symbol(newposn):
			return True
	return False

def word_touch_symbol(posns):
	for posn in posns:
		if touching_symbol(posn):
			return True
	return False
		
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
			
ret = 0
for num, posns in all_nums:
	if word_touch_symbol(posns):
		ret += num

print(ret)
