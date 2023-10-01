#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

def print_grid(grid):
    for row in grid:
        for ele in row:
            print(ele, end='')
        print('')

minx, maxx, miny, maxy = float('inf'), -float('inf'), 0, -float('inf')
rocks = []

for line in lines:
    verticies = line.split('->')
    rock = []
    for vertex in verticies:
        x, y = [int(e) for e in vertex.split(',')]
        minx = x if x < minx else minx
        maxx = x if x > maxx else maxx
        maxy = y if y > maxy else maxy
        rock.append((x, y))
    rocks.append(rock)

grid = [['.' for _ in range(maxx - minx + 1)] for y in range(maxy - miny + 1)]
sand_start_posn = (500 - minx, 0)
grid[sand_start_posn[1]][sand_start_posn[0]] = '+'

for rock in rocks:
    for ii in range(1, len(rock)):
        start, end = [rock[ii - 1][0], rock[ii - 1][1]], [rock[ii][0], rock[ii][1]]
        if start[0] > end[0] or start[1] > end[1]:
            start, end = end, start
        if start[0] < end[0]: # go right
            while start[0] <= end[0]:
                grid[start[1] - miny][start[0] - minx] = '#'
                start[0] += 1
        else: # go down
            while start[1] <= end[1]:
                grid[start[1] - miny][start[0] - minx] = '#'
                start[1] += 1

def drop_sand(grid):
    x, y = sand_start_posn[0], sand_start_posn[1]
    moving = True
    while moving:
        moving = False
        while grid[y + 1][x] == '.':
            moving = True
            y += 1
        if grid[y + 1][x - 1] == '.':
            y += 1
            x -= 1
            moving = True
        elif grid[y + 1][x + 1] == '.':
            y += 1
            x += 1
            moving = True
    grid[y][x] = 'o'

ii = 0
while True:
    try:
        drop_sand(grid)
        ii += 1
    except Exception as e:
        print(ii)
        break
