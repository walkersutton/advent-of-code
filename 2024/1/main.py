#!/usr/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

l_list, r_list = [], []
for line in lines:
	l, r = line.split()
	l_list.append(int(l))
	r_list.append(int(r))

l_list.sort()
r_list.sort()

diff_sum = 0
for ii in range(len(l_list)):
	diff_sum += abs(l_list[ii] - r_list[ii])

print(diff_sum)
