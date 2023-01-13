import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

line = input_as_lines('test.txt')
nums = [int(n) for n in line[0].split(',')]
nums = [[n,1] for n in nums]
nums.sort()
fuel = 0
m = 1
	

kv = {}
for ii in range(len(nums)):
	if nums[ii][0] in kv:
		kv[nums[ii][1]] += 1
	else:
		kv[nums[ii][1]] = nums[ii][1]

maxx = 0	

for e in kv:
	maxx = max(maxx, e)

print( len(nums) - maxx)
