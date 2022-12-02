import sys

from parse import input_as_string, input_as_lines, input_as_ints

sys.path.append("..")

lines = input_as_lines('data.txt')

WIN = 6
TIE = 3
LOSE = 0
total = 0

for line in lines:
    if line not in ('', '\n'):
        p1, outcome = line.split(' ')
        if outcome == 'X': # LOSE
            total += LOSE
            if p1 == 'A':
                total += 3
            elif p1 == 'B':
                total += 1
            else:
                total += 2
        elif outcome == 'Y': # TIE
            total += TIE
            if p1 == 'A':
                total += 1
            elif p1 == 'B':
                total += 2
            else:
                total += 3
        else: # WIN
            total += WIN
            if p1 == 'A':
                total += 2
            elif p1 == 'B':
                total += 3
            else:
                total += 1

print(total)
