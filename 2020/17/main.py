infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(element.strip())

section = 0
valid_ranges = []
invalid_sum = 0

for val in vals:
	if val == '':
		section += 1
	else:
		if section == 0:
			field_ranges = val.split(':')[1].split('or')
			for rng in field_ranges:
				rng = rng.strip().split('-')
				valid_ranges.append((int(rng[0]), int(rng[1])))
		elif section == 2:
			val = val.split(',')
			if len(val) == len(valid_ranges) / 2:
				for v in val:
					v = int(v)
					good = False
					for valid in valid_ranges:
						if good:
							break
						elif v >= valid[0] and v <= valid[1]:
							good = True
					if not good:
						invalid_sum += v

print(invalid_sum)
