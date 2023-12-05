#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

ret = 0
for line in lines:
	num_winners = 0
	win_value = 0
	
	temp = line.split('|')
	winners = [val for val in temp[0].strip().split(' ') if val != '']
	nums = [val for val in temp[1].strip().split(' ') if val != '']
	for n in nums:
		if n in set(winners):
			num_winners += 1
			if num_winners == 1:
				win_value = 1
			else:
				win_value *= 2
	ret += win_value

print(ret)
