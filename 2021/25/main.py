import sys
sys.path.append("..")
from copy import deepcopy

from parse import input_as_string, input_as_lines, input_as_ints

def move_east(sea):
	for line in sea:
		tomove = []
		for ii in range(len(line)):
			if line[ii] == '>':
				temp_pos = 0 if ii + 1 >= len(line) else ii + 1
				if line[temp_pos] == '.':
					tomove.append([ii, temp_pos])
		for ea in tomove:
			line[ea[0]] = '.'
			line[ea[1]] = '>'

def move_south(sea):
	tomove = []
	for ii in range(len(sea)):
		for jj in range(len(sea[ii])):
			if sea[ii][jj] == 'v':
				temp_pos = 0 if ii + 1 >= len(sea) else ii + 1
				if sea[temp_pos][jj] == '.' and [ii, jj]:
					tomove.append([ii, temp_pos, jj])
	for ea in tomove:
		sea[ea[0]][ea[2]] = '.'
		sea[ea[1]][ea[2]] = 'v'

lines = input_as_lines('data.txt')

sea = []
for line in lines:
	temp_line = []
	for ch in line:
		temp_line.append(ch)
	sea.append(temp_line)

for step in range(1000):
	prev_sea = deepcopy(sea)
	move_east(sea)
	move_south(sea)
	if prev_sea == sea:
		print(step + 1)
		break
