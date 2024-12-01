#!/usr/bin/python3

import os
import sys
from collections import defaultdict

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

l_list_set = set()
r_list_count = defaultdict(int)
l_list_count = defaultdict(int)

l_list, r_list = [], []
for line in lines:
	l = int(line.split()[0])
	l_list_count[l] += 1
	l_list_set.add(l)

for line in lines:
	r = int(line.split()[1])
	if r in l_list_set:
		r_list_count[r] += 1

ret = 0
for val, count in r_list_count.items():
	ret += val * count * l_list_count[val]
print(ret)
