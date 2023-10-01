#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
movement = {
    'U': (1, 0),
    'D': (-1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
too_far = {}
for direction in movement:
    too_far[direction] = (movement[direction][0] * 2, movement[direction][1] * 2)
jumps = {
    (2, 1): (-1, 0),
    (2, -1): (-1, 0),
    (-2, 1): (1, 0),
    (-2, -1): (1, 0),
    (1, 2): (0, -1),
    (1, -2): (0, 1),
    (-1, 2): (0, -1),
    (-1, -2): (0, 1),
    (-2, -2): (1, 1),
    (-2, 2): (1, -1),
    (2, -2): (-1, 1),
    (2, 2): (-1, -1)
}

tail_visited = set()
knots = [(0,0) for _ in range(10)]

def touching(knot_1, knot_2):
    for offset in [(ii, jj) for ii in [-1,0,1] for jj in [-1,0,1]]:
        if (offset[0] + knot_1[0], offset[1] + knot_1[1]) == knot_2:
            return True
    return False

def print_knots(knots, size=20):
    for row in range(size, -size, -1):
        for col in range(-size, size):
            if (row, col) == (0, 0):
                print('s', end='')
            elif (row, col) in knots:
                print(knots.index((row, col)), end='')
            else:
                print('.', end='')
        print('')
    print('')

for line in lines:
    direction, units = line.split(' ')[0], int(line.split(' ')[1])
    for _ in range(units):
        knots[0] =(knots[0][0] + movement[direction][0], knots[0][1] + movement[direction][1])
        for ii in range(1, len(knots)):
            prev_knot = knots[ii - 1]
            row, col = knots[ii][0], knots[ii][1]
            moved = False
            if not touching(prev_knot, knots[ii]):
                for key, pos in too_far.items():
                    if (row + pos[0], col + pos[1]) == prev_knot:
                        knots[ii] = (row + movement[key][0], col + movement[key][1])
                        moved = True
                        break
                if not moved:
                    diff = (prev_knot[0] - row, prev_knot[1] - col)
                    knots[ii] = (prev_knot[0] + jumps[diff][0], prev_knot[1] + jumps[diff][1])
            if ii == len(knots) - 1:
                tail_visited.add(knots[ii])

print(len(tail_visited))
