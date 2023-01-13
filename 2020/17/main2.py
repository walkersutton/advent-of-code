import copy
infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(element.strip())

section = 0
valid_ranges = {}
key_map = {}
tickets = []
your_ticket = None

for val in vals:
	if val == '':
		section += 1
	else:
		if section == 0:
			field_key = val.split(':')[0]
			valid_ranges[len(key_map)] = []
			key_map[len(key_map)] = field_key
			field_ranges = val.split(':')[1].split('or')
			for rng in field_ranges:
				rng = rng.strip().split('-')
				valid_ranges[len(key_map) - 1].append((int(rng[0]), int(rng[1])))
		elif section == 1:
			val = val.split(',')
			if len(val) == len(valid_ranges):
				your_ticket = [int(value) for value in val]
		elif section == 2:
			val = val.split(',')
			if len(val) == len(valid_ranges):
				tickets.append([int(value) for value in val])

bad_ticket_indices = []
for ii in range(len(tickets)):
	for v in tickets[ii]:
		good = False
		for field_ranges in valid_ranges.values():
			for valid in field_ranges:
				if valid[1] >= v >= valid[0]:
					good = True
					break
		if not good:
			bad_ticket_indices.insert(0, ii)

for bad_index in bad_ticket_indices:
	tickets.pop(bad_index)

field_map = []
index_set = [ii for ii in range(len(valid_ranges))]

for _ in range(len(valid_ranges)):
	field_map.append(index_set.copy())

field_map_copy = copy.deepcopy(field_map)
for field_index in range(len(field_map_copy)):
	for col in field_map_copy[field_index]:
		for t in tickets:
			good = False
			t_val = t[col]
			for rng in valid_ranges[field_index]:
				if rng[1] >= t_val >= rng[0]:
					good = True
					break
			if not good:
				field_map[field_index].remove(col)
				break

field_values = {}
while True:
	to_remove = -1
	jj = 0
	for jj in range(len(field_map)):
		if len(field_map[jj]) == 1:
			to_remove = field_map[jj][0]
			break
	for ii in range(len(field_map)):
		if to_remove in field_map[ii] and ii != jj:
			field_map[ii].remove(to_remove)
	if to_remove == -1:
		break
	field_values[key_map[jj]] = to_remove 
	field_map[jj] = []

product = 1
for field in field_values:
	if 'departure' in field:
		product *= your_ticket[field_values[field]]

print(product)
