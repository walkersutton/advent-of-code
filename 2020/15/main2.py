vals = [1,0,18,10,19,6]
history = {}
for ii in range(len(vals)):
	history[vals[ii]] = [ii + 1]

ii = len(vals) + 1
last_spoken = vals[-1]

while ii <= 30000000:
	last_spoken = 0 if last_spoken not in history else max(history[last_spoken]) - min(history[last_spoken])
	if last_spoken not in history:
		history[last_spoken] = [ii]
	else:
		if len(history[last_spoken]) > 1:
			history[last_spoken].remove(min(history[last_spoken]))
		history[last_spoken].append(ii)
	ii += 1

print(last_spoken)
