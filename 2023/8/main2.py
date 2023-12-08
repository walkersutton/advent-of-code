#!/opt/homebrew/bin/python3

from copy import copy
import math
import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
path = 'LRLRLLRLLRRRLRLLRRLRLRRLRRLLLLRRLLRLRRLRRLRLRLRRLRLLRLRLRLRRRLLRLRLRLRRLRRLRRRLRRLRRLRRLRRLRRRLRRLRLLRLLRRRLRLRLLRRRLLRRLLLLRLRRRLLRLRLRRLRRRLRLRRLRLRRLLRLRRLLRLLRRLRLLRLLRRLRRRLLRRLRLRLRRLRRLRRRLRRLRRRLLRRLRLRRRLRRRLRLRRRLRRLRRLRRLRRRLRRLRLRRRLRLRRLLRRLRRRLRLRRRLLRLRRRLRRRLRLRLRRRLLRRLLRLRRRLRRLRRRLLLRRRR'

nodes = []
m = {}
for line in lines:
	k = line[:3]
	if k[2] == 'A':
		nodes.append(k)
	l = line.split('(')[1].split(',')[0]
	r = line.split(',')[1].strip()[:3]
	m[k] = (l, r)

ii = 0
cur = 'AAA'
steps = 0
vals = []
while nodes:
	old_nodes = copy(nodes)
	nodes = []
	while old_nodes:
		cur = old_nodes.pop()
		di = 0 if path[ii] == 'L' else 1
		cur = m[cur][di]
		if cur[2] == 'Z':
			vals.append(steps + 1)
		else:
			nodes.append(cur)
	steps += 1
	ii += 1
	ii %= len(path)

print(math.lcm(*vals))
