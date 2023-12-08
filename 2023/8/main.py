#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
path = 'LRLRLLRLLRRRLRLLRRLRLRRLRRLLLLRRLLRLRRLRRLRLRLRRLRLLRLRLRLRRRLLRLRLRLRRLRRLRRRLRRLRRLRRLRRLRRRLRRLRLLRLLRRRLRLRLLRRRLLRRLLLLRLRRRLLRLRLRRLRRRLRLRRLRLRRLLRLRRLLRLLRRLRLLRLLRRLRRRLLRRLRLRLRRLRRLRRRLRRLRRRLLRRLRLRRRLRRRLRLRRRLRRLRRLRRLRRRLRRLRLRRRLRLRRLLRRLRRRLRLRRRLLRLRRRLRRRLRLRLRRRLLRRLLRLRRRLRRLRRRLLLRRRR'

m = {}
for line in lines:
	l = line.split('(')[1].split(',')[0]
	r = line.split(',')[1].strip()[:3]
	m[line[:3]] = (l, r)

ii = 0
cur = 'AAA'
steps = 0
while cur != 'ZZZ':
	di = 0 if path[ii] == 'L' else 1
	cur = m[cur][di]
	steps += 1
	ii += 1
	ii %= len(path)

print(steps)
