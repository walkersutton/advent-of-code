import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

ints = input_as_ints('data.txt')

count = 0

for ii in range(0, len(ints) - 3):
	w1 = ints[ii] + ints[ii + 1] + ints[ii + 2]
	w2 = w1 - ints[ii] + ints[ii + 3]
	if w1 < w2:
		count += 1

print(count)
