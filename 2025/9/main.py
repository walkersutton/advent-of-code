import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

file_name = 'data.txt'
lines = input_as_lines(file_name)

tiles = []
for line in lines:
    x, y = line.split(',')
    tiles.append((int(x), int(y)))

max_area = 0
for ii in range(len(tiles) - 1):
    ax, ay = tiles[ii] 
    for jj in range(ii + 1, len(tiles)):
        bx, by = tiles[jj]
        area = (1 + abs(bx - ax)) * (1 + abs(by - ay))
        if area > max_area:  
            max_area = area

print(max_area) 
