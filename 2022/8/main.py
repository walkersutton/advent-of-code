#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
rows = len(lines)
cols = len(lines[0])
seen_trees = set([])
total = 0

# looking from west to east
for ii in range(rows):
    count = 0
    smallest_seen = -1
    for jj in range(cols):
        cur_height = int(lines[ii][jj])
        if cur_height > smallest_seen:
            if (ii, jj) not in seen_trees:
                seen_trees.add((ii, jj))
                count += 1
            smallest_seen = cur_height
    total += count

# looking from east to west
for ii in range(rows):
    count = 0
    smallest_seen = -1
    for jj in range(cols - 1, -1, -1):
        cur_height = int(lines[ii][jj])
        if cur_height > smallest_seen:
            if (ii, jj) not in seen_trees:
                seen_trees.add((ii, jj))
                count += 1
            smallest_seen = cur_height
    total += count

# looking from north to south
for jj in range(cols):
    count = 0
    smallest_seen = -1
    for ii in range(rows):
        cur_height = int(lines[ii][jj])
        if cur_height > smallest_seen:
            if (ii, jj) not in seen_trees:
                seen_trees.add((ii, jj))
                count += 1
            smallest_seen = cur_height
    total += count

# looking from south to north
for jj in range(cols):
    count = 0
    smallest_seen = -1
    for ii in range(rows - 1, -1, -1):
        cur_height = int(lines[ii][jj])
        if cur_height > smallest_seen:
            if (ii, jj) not in seen_trees:
                seen_trees.add((ii, jj))
                count += 1
            smallest_seen = cur_height
    total += count

print(total)
