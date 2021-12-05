import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

max_x, max_y = 0, 0

segments = []
for line in lines:
	segment = []
	line = line.split(' -> ')
	start = line[0].split(',')
	start = [int(start[0]), int(start[1])]
	end = line[1].split(',')
	end = [int(end[0]), int(end[1])]
	segments.append([start, end])
	max_x = max(max_x, start[0], end[0])
	max_y = max(max_y, start[1], end[1])

board = []
for ii in range(max_y + 1):
	row = []
	for jj in range(max_x + 1):
		row.append(0)
	board.append(row)	

for s in segments:
	start = s[0]	
	end = s[1]
	# vertical
	if start[0] == end[0]:
		for ii in range(abs(start[1] - end[1]) + 1):
			board[min(start[1], end[1]) + ii][start[0]] += 1
	# horizontal
	elif start[1] == end[1]:
		for ii in range(abs(start[0] - end[0]) + 1):
			board[start[1]][min(start[0], end[0]) + ii] += 1
	# diagnoal
	else: 
		# ensure the start variable is the leftmost x value
		if start[0] > end[0]:
			temp = start
			start = end
			end = temp
		# step down
		if start[1] < end[1]:
			for ii in range(abs(start[1] - end[1]) + 1):
				board[start[1] + ii][start[0] + ii] += 1
		# step up
		else:
			for ii in range(abs(start[1] - end[1]) + 1):
				board[start[1] - ii][start[0] + ii] += 1

count = 0
for row in board:
	for ele in row:
		if ele >= 2:
			count += 1
print(count)
