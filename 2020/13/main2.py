t_ids = [19,'x','x','x','x','x','x','x','x',41,'x','x','x',37,'x','x','x','x','x',787,'x','x','x','x','x','x','x','x','x','x','x','x',13,'x','x','x','x','x','x','x','x','x',23,'x','x','x','x','x',29,'x',571,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',17]

t_ids = [1789,37,47,1889]
t_ids = [17,'x',13,19]
ids = []
increment = 0
for bid in t_ids:
	if bid != 'x':
		ids.append(bid)
	else:
		ids.append(-1)


import time as tim

max_index = ids.index(max(ids))

time = 0
while True:
	print(time)
	tim.sleep(1)
	no_go = False	
	ii = max_index - 1
	clock = time + ii
	while ii >= 0:
		print(ids[ii], clock)
		if ids[ii] == -1:
			pass
		elif clock % bid != 0:
			no_go = True
			break
		clock -= 1
	if not no_go:
		ii = max_index	
		clock = time + ii
		while ii < len(ids):
			if ids[ii] == -1:
				pass
			elif clock % bid != 0:
				no_go = True
				break
			clock += 1
	if not no_go:
		print(time)
		exit()
	time += ids[max_index]
