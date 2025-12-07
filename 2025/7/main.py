import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

file_name = 'data.txt'
lines = input_as_lines(file_name)

for ii in range(len(lines[0])):
    if lines[0][ii] == 'S':
        break

beams = set([ii])
count = 0

for jj in range(2, len(lines), 2):
    new_beams = set()
    for beam in beams:
        if lines[jj][beam] == '^':
            new_beams.update([beam - 1, beam + 1])
            count += 1
        else:
            new_beams.add(beam)
    beams = new_beams

print(count)
