import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints


class Node:
	def __init__(self, value, children):
		self.value = value
		self.children = children

lines = input_as_lines('test.txt')
starts_str = []
ends_str = []
connections = []

for line in lines:
	line = line.split('-')
	if line[0] == 'start':
		starts_str.append(line[1])
	elif line[1] == 'end':
		ends_str.append(line[0])
	else:
		temppath = []
		connections.append([point for point in line])

nodes = {}
starts = []
ends = []
for start in starts_str:
	cur = Node(start, [])
	nodes[start] = cur
	starts.append(cur.value)

for end in ends_str:
	cur = Node(end, [])
	nodes[end] = cur
	ends.append(cur.value)

for connection in connections:
	# print(connection)
	last_pos = None
	for val in connection:
		if val in nodes:
			cur = nodes[val]
		else:
			cur = Node(val, [])
			# print('making new node')
			# print(val)
			nodes[val] = cur
		if last_pos:
			last_pos.children.append(cur)
			cur.children.append(last_pos)
		last_pos = cur


# for start in starts:
# 	path = [start]
# 	for node in start.children:
# 		path.append(node)
# 		if node in path:
# 			break
# 	paths.append(path)
# 	path = [start]

# print(len(paths))
# for path in paths:
# 	for pos in path:
# 		print(pos.value, end='')
# 	print('')


def list_path(node, seen):
	if len(seen) == 0:
		seen.append(node.value)
		print(node.value, 'start is here')
		for child in node.children:
			list_path(child, seen.copy())
	elif node.value not in seen:
		seen.append(node.value)
		if len(node.children) == 0:
			print(node.value, 'last')
			print(1)
		else:
			for child in node.children:
				print(node.value, 'next')
				list_path(child, seen.copy())
	else:
		print(node.value, 'last')
		print(1)

count = 0
for node in nodes:
	if nodes[node].value in starts:
		print('starting at', nodes[node].value)
		list_path(nodes[node], [])
print(count)
