infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(element.strip())

DIRS = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

posn = (0, 0)
cur_dir = 'E'

for val in vals:
	if val[0] == 'F':
		n = int(val[1:])
		posn = (posn[0] + (DIRS[cur_dir][0] * n), posn[1] + (DIRS[cur_dir][1] * n))
	elif val[0] == 'L':
		for _ in range(int((int(val[1:]) / 90) % 4)):
			if cur_dir == 'N':
				cur_dir = 'W'
			elif cur_dir == 'E':
				cur_dir = 'N'
			elif cur_dir == 'S':
				cur_dir = 'E'
			else:
				cur_dir = 'S'
	elif val[0] == 'R':
		for _ in range(int((int(val[1:]) / 90) % 4)):
			if cur_dir == 'N':
				cur_dir = 'E'
			elif cur_dir == 'E':
				cur_dir = 'S'
			elif cur_dir == 'S':
				cur_dir = 'W'
			else:
				cur_dir = 'N'
	else:
		n = int(val[1:])
		posn = (posn[0] + (DIRS[val[0]][0] * n), posn[1] + (DIRS[val[0]][1] * n))

print(abs(posn[0]) + abs(posn[1]))
