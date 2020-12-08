infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []

for element in text_data:
  vals.append((element.strip()))

seen = set()
acc, index = 0, 0

while True:
	if index in seen:
		print(acc)
		exit()
	else:
		seen.add(index)

	move, argument = vals[index].split()
	sign, value = argument[0], int(argument[1:])

	if move == 'nop':
		index += 1
	elif move == 'acc':
		acc = acc + value if sign == '+' else acc - value
		index += 1
	else:
		index = index + value if sign == '+' else index - value
