#!/opt/homebrew/bin/python3

import collections
import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

# import numpy as np

# string = input_as_string('data.txt')
lines = input_as_lines('data.txt')
grid = []
for line in lines:
    row = []
    for c in line:
        if c == 'E':
            row.append(ord('z'))
            goal_row = lines.index(line)
        elif c == 'S':
            row.append(ord('a'))
            start_row = lines.index(line)
        else:
            row.append(ord(c))
    grid.append(row)

width = len(grid[0])
height = len(grid)

start = (start_row, lines[start_row].index('S'))
goal = (goal_row, lines[goal_row].index('E'))

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
explored = set()
options = [start]
while options:
    cur = options.pop(0)
    cur_height = grid[cur[0]][cur[1]]
    for move in moves:
        p_row, p_col = cur[0] + move[0], cur[1] + move[1]
        if 0 <= p_row < height and 0 <= p_col < width:
            if grid[p_row][p_col] < cur_height:
                options.append((p_row, p_col))





