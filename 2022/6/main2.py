#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

string = input_as_string('data.txt')
buffer = []

for ii in range(len(string)):
    while len(buffer) < 14:
        buffer.append(string[ii])
    if len(buffer) == 14:
        if len(set(buffer)) == 14:
            print(ii + 1)
            break
        buffer.pop(0)
