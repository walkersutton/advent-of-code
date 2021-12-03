import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

bins = []
for line in lines:
	bins.append(line)

gamma = ''

for ii in range(len(bins[0])):
	ones, zeros = 0, 0
	for jj in range(len(bins)):
		if bins[jj][ii] == '0':
			zeros += 1
		else:
			ones += 1
	if ones > zeros:
		gamma += '1'
	else:
		gamma += '0'

gamma = int(gamma, 2)
epsilon = gamma ^ int('111111111111', 2)

print(gamma * epsilon)
