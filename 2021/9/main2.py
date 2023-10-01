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
			lowps.append([yval, xval])

for lowp in lowps:
	ggood = [lowp]
	new = [lowp]	
	while len(new) > 0:
		did = False
		newv = new.pop()
		yval = newv[0]
		xval = newv[1]
		try:
			if [yval - 1,xval] in ggood:
				pass
			elif nums[yval - 1][xval] > val:
				did = True
				if [yval-1, xval] in new:
					new.remove([yval - 1, xval])
				else:
					new.append([yval - 1, xval])
			elif nums[yval - 1][xval] in ggood:
				new.remove([yval - 1, xval])
		except Exception:
			pass

		try:
			if [yval + 1,xval] in ggood:
				pass
			elif nums[yval + 1][xval] > val:
				did = True
				if [yval+1, xval] in new:
					ggood.append([yval + 1, xval])
					new.remove([yval + 1, xval])
				else:
					new.append([yval + 1, xval])
			elif nums[yval + 1][xval] in ggood:
				new.remove([yval + 1, xval])
		except Exception:
			pass

		try:
			if [yval, xval + 1] in ggood:
				pass
			elif nums[yval][xval + 1] > val:
				did = True
				if [yval, xval + 1] in new:
					ggood.append([yval, 1 + xval])
					new.remove([yval, 1 + xval])
				else:
					new.append([yval, 1 + xval])
			elif nums[yval][xval + 1] in ggood:
				new.remove([yval, xval + 1])
		except Exception:
			pass

		try:
			if [yval, xval - 1] in ggood:
				pass
			elif nums[yval][xval - 1] > val:
				did = True
				if [yval, xval - 1] in new:
					ggood.append([yval, xval - 1])
					new.remove([yval, xval - 1])
				else:
					new.append([yval,xval - 1])
			elif nums[yval][xval - 1] in ggood:
				new.remove([yval, xval - 1])
		except Exception:
			pass

		# print('new:')
		# print(new)
		if did:
			ggood.append(newv)
			new.append(newv)
		
	print('--here')	
	print(ggood)	
		



