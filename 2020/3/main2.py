import math

infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(list(element.strip()))

width = len(vals[0])
num_trees = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for slope in slopes:
  trees = 0
  cur_x = 0
  cur_y = 0
  while cur_y + slope[1] < len(vals):
    cur_x = ((cur_x + slope[0]) % width)
    cur_y += slope[1]
    if (vals[cur_y][cur_x] == '#'):
      trees += 1

  num_trees.append(trees)

print(math.prod(num_trees))
