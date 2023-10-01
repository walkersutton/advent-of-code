infile = open('data3.txt', 'r')
text_data = infile.readlines()
vals = []

for element in text_data:
  vals.append(int((element.strip())))

vals.sort()
vals.append(vals[-1] + 3)

jolts = 0
one_differences = 0
three_differences = 0
two_differences = 0

for adapter in vals:
	diff = adapter - jolts
	if diff <= 3:
		if diff == 0:
			break
		elif diff == 1:
			one_differences += 1
			jolts += 1
		elif diff == 3:
			three_differences += 1
			jolts += 3
		else:
			two_differences += 1
			jolts += 2
	else:
		break

p = 1
for _ in range(two_differences):
	p *= 2
for _ in range(three_differences):
	p *= 3

print(p)
