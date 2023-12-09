#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

def extrapolate(history):
	history = [history]
	while True:
		cur = history[-1]
		last = cur[0]
		extrapolated = []
		all_zeros = True
		for ii in range(1, len(cur)):
			diff= cur[ii] - last
			if diff != 0:
				all_zeros = False
			extrapolated.append(diff)
			last = cur[ii]
		history.append(extrapolated)
		if all_zeros:
			break

	for ii in range(len(history) - 2, -1, -1):
		cur = history[ii]
		history[ii - 1][0] -= cur[0]
	return history[0][0]

ret = 0	
for history in lines:
	ret += extrapolate([int(v) for v in history.split()])
print(ret)
