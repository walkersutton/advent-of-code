infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []

for element in text_data:
  vals.append(int((element.strip())))

invalid = 1492208709

for ii in range(0, len(vals) - 1):
	acc = vals[ii]
	for jj in range(ii + 1, len(vals)):
		acc += vals[jj]
		if acc == invalid:
			print(min(vals[ii:jj]) + max(vals[ii:jj]))
			exit()
		elif acc < invalid:
			continue
		else:
			break
