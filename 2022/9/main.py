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
tail_visited = set()
head, tail = (0, 0), (0, 0)

def touching(knot_1, knot_2):
    for offset in [(ii, jj) for ii in [-1,0,1] for jj in [-1,0,1]]:
        if (offset[0] + knot_1[0], offset[1] + knot_1[1]) == knot_2:
            return True
    return False

for line in lines:
    direction, units = line.split(' ')[0], int(line.split(' ')[1])
    for _ in range(units):
        head = (head[0] + movement[direction][0], head[1] + movement[direction][1])
        tail_moved = False
        if not touching(head, tail):
            for offset in too_far.values():
                if (tail[0] + offset[0], tail[1] + offset[1]) == head:
                    tail = (tail[0] + movement[direction][0], tail[1] + movement[direction][1])
                    tail_moved = True
                    break
            if not tail_moved:
                tail = (head[0] - movement[direction][0], head[1] - movement[direction][1])
        tail_visited.add(tail)

print(len(tail_visited))
