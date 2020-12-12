infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(element.strip())

DIRS = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

posn = (0, 0)
waypoint = (10, 1)

for val in vals:
	if val[0] == 'F':
		n = int(val[1:])
		posn = (posn[0] + (waypoint[0] * n), posn[1] + (waypoint[1] * n))
	elif val[0] == 'L' or val[0] == 'R':
		dire = val[0]
		n =  int((int(val[1:]) / 90) % 4)
		if (dire == 'L' and n == 1) or (dire == 'R' and n == 3):
			waypoint = (waypoint[1] * -1, waypoint[0])
		elif n == 2:
			waypoint = (waypoint[0] * -1, waypoint[1] * -1)
		elif (dire == 'L' and n == 3) or (dire == 'R' and n == 1):
			waypoint = (waypoint[1], waypoint[0] * -1)
	else:
		n = int(val[1:])
		waypoint = (waypoint[0] + DIRS[val[0]][0] * n, waypoint[1] + DIRS[val[0]][1] * n)

print(abs(posn[0]) + abs(posn[1]))
