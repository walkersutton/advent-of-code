#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

maps = ['sts', 'stf', 'ftw', 'wtl', 'ltt', 'tth', 'htl']
seeds = [919339981, 562444630, 3366006921, 67827214, 1496677366, 101156779, 4140591657,5858311, 2566406753, 71724353, 2721360939, 35899538, 383860877, 424668759, 3649554897, 442182562, 2846055542, 49953829, 2988140126, 256306471]

m_vals = {}
for m in maps:
	vals = []
	lines = input_as_lines(f'{m}.txt')
	for line in lines:
		destination_start, source_start, rl = [int(num) for num in line.split(' ')]
		vals.append((destination_start, source_start, rl))
	m_vals[m] = vals

ret = float('inf')
for seed in seeds:
	for m in maps:
		vals = m_vals[m]
		for destination_start, source_start, rl in vals:
			if source_start <= seed < source_start + rl:
				seed = abs(seed - source_start) + destination_start
				break
	ret = min(ret, seed)

print(ret)
