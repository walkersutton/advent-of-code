timestamp = 1003240
ids = [19,'x','x','x','x','x','x','x','x',41,'x','x','x',37,'x','x','x','x','x',787,'x','x','x','x','x','x','x','x','x','x','x','x',13,'x','x','x','x','x','x','x','x','x',23,'x','x','x','x','x',29,'x',571,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',17]

ids = list(filter(lambda x: x != 'x', ids))

options = []
for bid in ids:
	options.append((abs(bid - timestamp % bid), bid))

options.sort()
print(options[0][0] * options[0][1])

