target = [[156, 202], [-110, -69]]

count = 0
for ii in range(0, 203):
	for jj in range(-200, 200):
		x, y = 0, 0
		xi, xv, yi, yv = ii, ii, jj, jj
		my = -1
		while True:
			if x > max(target[0]) or y < min(target[1]):
				break
			elif min(target[0]) <= x <= max(target[0]) and min(target[1]) <= y <= max(target[1]):
				count += 1
				break
			x += xv
			y += yv
			if xv < 0:
				xv += 1
			elif xv > 0:
				xv -= 1
			yv -= 1

print(count)
