#!/opt/homebrew/bin/python3

time = 49979494
dist = 263153213781851

low_val, high_val = None, None

l, r = 0, time + 1
while l <= r:
	cur_idx = ((r - l) // 2) + l
	cur_dist = (time - cur_idx) * cur_idx
	if cur_dist > dist:
		r = cur_idx - 1
	else:
		l = cur_idx + 1
low_val = cur_idx

l, r = low_val, time + 1
while l <= r:
	cur_idx = ((r - l) // 2) + l
	cur_dist = (time - cur_idx) * cur_idx
	if cur_dist > dist:
		l = cur_idx + 1
	else:
		r = cur_idx - 1
high_val = cur_idx

print(high_val - low_val)
