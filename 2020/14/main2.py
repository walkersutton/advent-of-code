infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(element.strip())

memory = {}
mask = ''

for val in vals:
	obj = val.split('=')
	if obj[0][1:2] == 'a':
		mask = list(val.split('=')[1].strip())[::-1]
	else:
		address, value = list(bin(int(obj[0].split('[')[1].strip()[:-1]))[2:])[::-1], int(obj[1].strip())
		while len(address) < len(mask):
			address.append('0')
		for ii in range(len(mask)):
			if mask[ii] == '1' or mask[ii] == 'X':
				address[ii] = mask[ii]
		address.reverse()

		stack = [address]
		while stack:
			temp = stack.pop()
			modified = False
			for ii in range(len(temp)):
				if temp[ii] == 'X':
					temp[ii] = '0'
					stack.append(temp.copy())
					temp[ii] = '1'
					stack.append(temp.copy())
					modified = True
					break
			if not modified:
				memory[int(''.join(temp[::-1]))] = value

print(sum(memory.values()))
