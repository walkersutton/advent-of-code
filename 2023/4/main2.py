#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

num_wins = [0] * len(lines)
num_cards = [1] * len(lines)
for ii in range(len(lines)):
	line = lines[ii]
	temp = line.split('|')
	winners = [val for val in temp[0].strip().split(' ') if val != '']
	nums = [val for val in temp[1].strip().split(' ') if val != '']
	num_winners = 0
	for n in nums:
		if n in set(winners):
			num_winners += 1
	num_wins[ii] = num_winners

for ii in range(len(lines)):
	wins = num_wins[ii]
	if wins > 0:
		for jj in range(ii + 1, min(len(lines), wins + ii + 1)):
			num_cards[jj] += num_cards[ii]

print(sum(num_cards))
