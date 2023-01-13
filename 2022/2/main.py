import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

WIN = 6
TIE = 3
LOSE = 0
rps_vals = {'X': 1, 'Y': 2, 'Z': 3}
outcomes = {
    ('A', 'Y'): WIN,
    ('A', 'Z'): LOSE,
    ('B', 'X'): LOSE,
    ('B', 'Z'): WIN,
    ('C', 'X'): WIN,
    ('C', 'Y'): LOSE,
}
total = 0

for line in lines:
    if line not in ('', '\n'):
        p1, p2 = line.split(' ')
        total += rps_vals[p2]
        if (p1, p2) in outcomes:
            total += outcomes[(p1, p2)]
        else:
            total += TIE

print(total)
