import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

line = input_as_lines('data.txt')
nums = [int(n) for n in line[0].split(',')]

for day in range(80):
	toadd = 0
	for ii in range(len(nums)):
		if nums[ii] == 0:
			toadd += 1
			nums[ii] = 6
		else:
			nums[ii] -= 1
	for ii in range(toadd):
		nums.append(8)

print(len(nums))
