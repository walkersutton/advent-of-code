import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

crates = [
    ['D', 'L', 'J', 'R', 'V', 'G', 'F'],
    ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S'],
    ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C'],
    ['M', 'D', 'P', 'N', 'G', 'Q'],
    ['J', 'L', 'H', 'N', 'F'],
    ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z'],
    ['F', 'D', 'B', 'L'],
    ['M', 'J', 'B', 'S', 'V', 'D', 'N'],
    ['G', 'L', 'D']
]

for line in lines:
    quantity = int(line.split(' ')[1])
    fr = int(line.split(' ')[3]) - 1
    to = int(line.split(' ')[5]) - 1
    
    temp = []
    for _ in range(quantity):
        temp.append(crates[fr].pop())

    temp.reverse()
    for crate in temp:
        crates[to].append(crate)

for crate in crates:
    print(crate[len(crate) - 1])
