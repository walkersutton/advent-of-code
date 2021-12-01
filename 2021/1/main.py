import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

ints = input_as_ints('data.txt')

count = 0

for ii in range(0, len(ints) - 1):
	val = ints[ii]
	if val < ints[ii + 1]:
		count += 1

print(count)
