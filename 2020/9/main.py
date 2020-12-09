infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []

for element in text_data:
  vals.append(int((element.strip())))

preamble = 25

def sum_set(start, end, vals):
	sums = set()
	for ii in range(start, end - 1):
		for kk in range(ii + 1, end):
			sums.add(vals[ii] + vals[kk])
	return sums

for ii in range(preamble, len(vals)):
	sums = sum_set(ii - preamble, ii, vals)
	if vals[ii] not in sums:
		print(vals[ii])
		exit()
