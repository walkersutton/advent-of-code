#!/usr/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

file_name = 'data.txt'
string = input_as_string(file_name)

def id_is_invalid(val):
    val = str(val)
    length = len(val)
    if length % 2 == 0:
        left, right = val[:length//2], val[length//2:]
        return left == right
    return False

invalid_id_sum = 0

for id_ranges in string.split(','):
    left, right = id_ranges.split('-')
    for ii in range(int(left), int(right) + 1):
        if id_is_invalid(ii):
            invalid_id_sum += ii

print(invalid_id_sum)
