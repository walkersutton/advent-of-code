import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

line = input_as_lines('data.txt')
nums = [int(n) for n in line[0].split(',')]

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in nums:
	counts[n] += 1

for day in range(256):
	a = counts.pop(0)
	counts[6] += a
	counts.append(a)

print(sum(counts))
