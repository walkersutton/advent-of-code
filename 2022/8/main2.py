#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
rows = len(lines)
cols = len(lines[0])

def scenic_score(r, c):
    tree_house_height = lines[r][c]
    ge, gw, gs, gn = 0, 0, 0, 0

    # looking from west to east
    for ii in range(c + 1, cols):
        cur_height = lines[r][ii]
        if cur_height < tree_house_height:
            ge += 1
        elif cur_height >= tree_house_height:
            ge += 1
            break

    # looking from east to west
    for ii in range(c - 1, -1, -1):
        cur_height = lines[r][ii]
        if cur_height <tree_house_height:
            gw += 1
        elif cur_height >=tree_house_height:
            gw += 1
            break

    # looking from north to south
    for ii in range(r + 1, rows):
        cur_height = lines[ii][c]
        if cur_height <tree_house_height:
            gs += 1
        elif cur_height >=tree_house_height:
            gs += 1
            break

    # looking from south to north
    for ii in range(r - 1, -1, -1):
        cur_height = lines[ii][c]
        if cur_height <tree_house_height:
            gn += 1
        elif cur_height >=tree_house_height:
            gn += 1
            break

    return ge * gw * gs * gn

highest = 0
for ii in range(rows):
    for jj in range(cols):
        highest = max(highest, scenic_score(ii, jj))

print(highest)
