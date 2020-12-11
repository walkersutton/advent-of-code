infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(list(element.strip()))

POSNS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

def mod_seat(vals, row, col):
	seat = vals[row][col]
	if seat == 'L' or seat == '#':
		occupied_seats = 0
		for p in POSNS:
			temp_posn = (row + p[0], col + p[1])
			while not (temp_posn[0] < 0 or temp_posn[1] < 0 or temp_posn[0] >= len(vals) or temp_posn[1] >= len(vals[0])):
				seat_status = vals[temp_posn[0]][temp_posn[1]]
				if seat_status == '#':
					occupied_seats += 1
					break
				elif seat_status == 'L':
					break
				temp_posn = (temp_posn[0] + p[0], temp_posn[1] + p[1])
		if (seat == 'L' and occupied_seats == 0) or (seat == '#' and occupied_seats >= 5):
			return (row, col)

seats = [0]

while seats:
	seats.clear()
	for row in range(len(vals)):
		for col in range(len(vals[row])):
			seat = mod_seat(vals, row, col)
			if seat:
				seats.append(seat)
	if seats:
		for seat in seats:
			row, col = seat[0], seat[1]
			if vals[row][col] == '#':
				vals[row][col] = 'L'
			elif vals[row][col] == 'L':
				vals[row][col] = '#'

count = 0
for row in range(len(vals)):
	for col in range(len(vals[row])):
		if vals[row][col] == '#':
			count += 1

print(count)
