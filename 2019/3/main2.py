def path(wire):
  cur = (0,0,'x', 0)
  path = {}
  for movement in wire:
    direction = movement[0]
    val = int(movement[1:])
    if direction == 'R':
      for _ in range(val):
        cur = (cur[0] + 1, cur[1],'h', cur[3] + 1)
        path[(cur[0], cur[1], cur[2])] = cur[3]
    if direction == 'U':
      for _ in range(val):
        cur = (cur[0], cur[1] + 1,'v', cur[3] + 1)
        path[(cur[0], cur[1], cur[2])] = cur[3]
    if direction == 'D':
      for _ in range(val):
        cur = (cur[0], cur[1] - 1,'v', cur[3] + 1)
        path[(cur[0], cur[1], cur[2])] = cur[3]
    if direction == 'L':
      for _ in range(val):
        cur = (cur[0] - 1, cur[1], 'h', cur[3] + 1)
        path[(cur[0], cur[1], cur[2])] = cur[3]
  return path

infile = open('data.txt', 'r')
text_data = infile.readlines()
w1_path = path([ele.strip() for ele in text_data[0].split(',')])
w2_path = path([ele.strip() for ele in text_data[1].split(',')])
hits = []
for ii, location in enumerate(w2_path):
  # print(str(ii/len(w2_path)) + "%")
  old_location = location
  if location[2] == 'v':
    location = (location[0], location[1],'h')
  else:
    location = (location[0], location[1],'v')
  if location in w1_path:
    hits.append(w2_path[old_location] + w1_path[location])

print(min(hits))



