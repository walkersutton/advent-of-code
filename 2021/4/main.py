import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

nums = [0,56,39,4,52,7,73,57,65,13,3,72,69,96,18,9,49,83,24,31,12,64,29,21,80,71,66,95,2,62,68,46,11,33,74,88,17,15,5,6,98,30,51,78,76,75,28,53,87,48,20,22,55,86,82,90,47,19,25,1,27,60,94,38,97,58,70,10,43,40,89,26,34,32,23,45,50,91,61,44,35,85,63,16,99,92,8,36,81,84,79,37,93,67,59,54,41,77,42,14]

lines = input_as_lines('data.txt')

def winner(board):
	for row in board:
		horiz_win = True
		for ele in row:
			if ele != -1:
				horiz_win = False
				break
		if horiz_win:
			return True
	for col_index in range(len(board)):
		vert_win = True
		for ele_index in range(len(board)):
			if board[ele_index][col_index] != -1:
				vert_win = False
				break
		if vert_win:
			return True
	return False

def score(board):
	score = 0
	for row in board:
		for ele in row:
			if ele != -1:
				score += ele
	return score
			
def bingo(board, nums):
	for draw in nums:
		for row in board:
			if draw in row:
				row[row.index(draw)] = -1	
				if winner(board): # something is buggy here
					return [nums.index(draw), draw, score(board)]
	return None


boards = []
board = []
for ii in range(len(lines)):
	if lines[ii] == '':
		boards.append(board)
		board = []
	else:
		line = lines[ii].split(' ')
		if '' in line:
			line.remove('')
		board.append([int(ele) for ele in line])
	boards.append(board)

winners = []
for board in boards:
	result = bingo(board, nums)
	if result:
		winners.append(result)

super_winner = [100]
for winner in winners:
	if winner[0] < super_winner[0]:
		super_winner = winner

print(super_winner[1] * super_winner[2])
