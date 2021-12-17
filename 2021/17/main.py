target = [[156, 202], [-110, -69]]

maxmaxy = 0
for ii in range(0, 203):
	for jj in range(-100, 500):
		x, y, xi, xv, yi, yv = 0, 0, ii, ii, jj, jj
		maxy = -1
		while True:
			maxy = max(maxy, y)
			if x > max(target[0]) or y < min(target[1]):
				break
			elif min(target[0]) <= x <= max(target[0]) and min(target[1]) <= y <= max(target[1]):
				maxmaxy = max(maxmaxy, maxy)				
				break
			x += xv
			y += yv
			if xv < 0:
				xv += 1
			elif xv > 0:
				xv -= 1
			yv -= 1
print(maxmaxy)
