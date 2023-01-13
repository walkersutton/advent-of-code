import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

ints = input_as_lines('test.txt')
nums = []
for line in ints:
	l = []
	for n in line:
		l.append(int(n))
	nums.append(l)


lowps = []	
for yval in range(len(nums)):
	for xval in range(len(nums[yval])):
		good = True
		val = nums[yval][xval]
		try:
			if nums[yval - 1][xval] > val:
				pass
			else:
				good = False
		except Exception:
			pass
		try:
			if nums[yval + 1][xval] > val:
				pass
			else:
				good = False
		except Exception:
			pass
		try:
			if nums[yval][xval + 1] > val:
				pass
			else:
				good = False
		except Exception:
			pass
		try:
			if nums[yval][xval - 1] > val:
				pass
			else:
				good = False
		except Exception:
			pass
		if good:
			lowps.append(val)



