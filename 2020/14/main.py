infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(element.strip())

memory = {}
mask = ''

for val in vals:
	obj = val.split('=')
	if obj[0][0:4] == 'mask':
		mask = list(val.split('=')[1].strip())[::-1]
	else:
		address, value = int(obj[0].split('[')[1].strip()[:-1]), list(bin(int(obj[1].strip()))[2:])[::-1]
		while len(value) < len(mask):
			value.append('0')
		for ii in range(len(mask)):
			if mask[ii] == '1' or mask[ii] == '0':
				value[ii] = mask[ii]
		memory[address] = int(''.join(value[::-1]), 2)

print(sum(memory.values()))
