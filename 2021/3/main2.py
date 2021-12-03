import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

bins = []
for line in lines:
	bins.append(line)

o2 = ''
co2 = ''

binstemp = bins
for ii in range(len(binstemp[0])):
	ones, zeros = 0, 0
	oneslist, zeroslist = [], []
	for jj in range(len(binstemp)):
		if binstemp[jj][ii] == '0':
			zeroslist.append(binstemp[jj])
		else:
			oneslist.append(binstemp[jj])
	if len(oneslist) < len(zeroslist):
		binstemp = oneslist
	else:
		binstemp= zeroslist
	ol = []
	zl = []
	if len(binstemp) == 1:
		co2 = binstemp[0]
		break

binstemp = bins
for ii in range(len(binstemp[0])):
	ones, zeros = 0, 0
	oneslist, zeroslist = [], []
	for jj in range(len(binstemp)):
		if binstemp[jj][ii] == '0':
			zeroslist.append(binstemp[jj])
		else:
			oneslist.append(binstemp[jj])
	if len(oneslist) >= len(zeroslist):
		binstemp = oneslist
	else:
		binstemp= zeroslist
	ol = []
	zl = []
	if len(binstemp) == 1:
		o2 = binstemp[0]
		break

print(int(o2, 2) * int(co2, 2))
