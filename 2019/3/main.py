def manhattan_distance(destination):
  return abs(destination[0]) + abs(destination[1])

def path(wire):
  cur = (0,0,'x')
  path = []
  for movement in wire:
    direction = movement[0]
    val = int(movement[1:])
    if direction == 'R':
      for _ in range(val):
        cur = (cur[0] + 1, cur[1],'h')
        path.append(cur)
    if direction == 'U':
      for _ in range(val):
        cur = (cur[0], cur[1] + 1,'v')
        path.append(cur)
    if direction == 'D':
      for _ in range(val):
        cur = (cur[0], cur[1] - 1,'v')
        path.append(cur)
    if direction == 'L':
      for _ in range(val):
        cur = (cur[0] - 1, cur[1], 'h')
        path.append(cur)
  return path

infile = open('data.txt', 'r')
text_data = infile.readlines()
w1_path = path([ele.strip() for ele in text_data[0].split(',')])
w2_path = path([ele.strip() for ele in text_data[1].split(',')])

hits = []
for ii, location in enumerate(w2_path):
  # print(str(ii/len(w2_path)) + "%")
  if location[2] == 'v':
    location = (location[0], location[1],'h')
  else:
    location = (location[0], location[1],'v')
  if location in w1_path:
    hits.append(manhattan_distance(location))

print(min(hits))



