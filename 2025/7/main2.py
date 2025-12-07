import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

file_name = 'data.txt'
lines = input_as_lines(file_name)

for ii in range(len(lines[0])):
    if lines[0][ii] == 'S':
        break

memo = {}
def paths(beam, rowidx):
    if (beam, rowidx) in memo.keys():
        return memo[(beam, rowidx)]
    if rowidx < len(lines):
        if lines[rowidx][beam] == '^':
            val = paths(beam - 1, rowidx + 2) + paths(beam + 1, rowidx + 2)
        else:
            val = paths(beam, rowidx + 2)
        memo[(beam, rowidx)] = val
        return val
    else:
        return 1
        
print(paths(ii, 2))            
