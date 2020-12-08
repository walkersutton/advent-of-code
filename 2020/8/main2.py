infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []

for element in text_data:
  vals.append((element.strip()))

vcopy = vals.copy()
seen = set()
acc, index, last_cur, cur = 0, 0, -1, -1

while True:
	if cur == -1:
		for ii in range(last_cur + 1, len(vals)):
			if vals[ii][0:3] == 'nop' or vals[ii][0:3] == 'jmp':
				vals[ii] = ('jmp' if vals[ii][0:3] == 'nop' else 'nop') + vals[ii][3:]
				cur, last_cur = ii, ii
				break
	try:
		move, argument = vals[index].split()
		sign, value = argument[0], int(argument[1:])
	except:
		print(acc)
		exit()

	if index in seen:
		seen.clear()
		vals = vcopy.copy()
		cur, acc, index = -1, 0, 0
		move = 'invalid'
	else:
		seen.add(index)

	if move == 'nop':
		index += 1
	elif move == 'acc':
		acc = acc + value if sign == '+' else acc - value
		index += 1
	elif move == 'jmp':
		index = index + value if sign == '+' else index - value
