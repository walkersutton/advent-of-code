#!/opt/homebrew/bin/python3

times = [49, 97,  94, 94]
dists = [263, 1532, 1378, 1851]

num_wins = []
for ii in range(len(times)):
	time, best_dist = times[ii], dists[ii]
	wins = 0
	for jj in range(time + 1):
		cur_dist = (time - jj) * jj
		if cur_dist > best_dist:
			wins += 1
	num_wins.append(wins)
	
ret = 1
for v in num_wins:
	ret *= v
print(ret)
