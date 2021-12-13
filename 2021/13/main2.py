import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

folds = [
	['x', 655],
	['y', 447],
	['x', 327],
	['y', 223],
	['x', 163],
	['y', 111],
	['x', 81],
	['y', 55],
	['x', 40],
	['y', 27],
	['y', 13],
	['y', 6]
]

maxx = 0
maxy = 0
dots = []
for line in lines:
	vals = line.split(',')
	x, y = int(vals[1]), int(vals[0])
	dots.append([y, x])
	maxx = max(maxx, x)
	maxy = max(maxy, y)

row = []
for ii in range(maxy + 1):
	row.append(0)

paper = []	
for ii in range(maxx + 1):
	paper.append(row.copy())

for dot in dots:
	paper[dot[1]][dot[0]] = 1

for fold in folds:
	if fold[0] == 'x':
		for jj in range(len(paper)):
			for ii in range(fold[1]):
				try:
					paper[jj][fold[1] - ii - 1] = max(paper[jj][fold[1] - ii - 1], paper[jj][fold[1] + ii + 1])
				except Exception as e:
					pass
		for ii in range(len(paper)):
			paper[ii] = paper[ii][0:fold[1]]
	else:
		for jj in range(fold[1]):
			for ii in range(len(paper[0])):
				try:
					paper[fold[1] - jj - 1][ii] = max(paper[fold[1] - jj - 1][ii], paper[fold[1] + jj + 1][ii])
				except Exception as e:
					pass
		paper = paper[0:fold[1]]

for row in paper:
	print(row)

print('use your eyes - find the 8 LETTERS')

