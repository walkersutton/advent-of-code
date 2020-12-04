infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(list(element.strip()))

cur_x= -3
x_slope = 3
width = len(vals[0])
trees = 0

for row in vals:
  cur_x = ((cur_x + x_slope) % width)
  if (row[cur_x] == '#'):
    trees += 1

print(trees)
