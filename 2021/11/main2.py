import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
octs = []
for line in lines:
	octs.append([int(n) for n in line])

def all_zeros(nums):
	return sum([sum(row) for row in nums]) == 0

def increment_by_one(nums):
	for ii in range(len(nums)):
		for jj in range(len(nums[ii])):
			nums[ii][jj] = nums[ii][jj] + 1

def flash(nums):
	flashed = []
	toflash = []
	for ii in range(len(nums)):
		for jj in range(len(nums[ii])):
			if nums[ii][jj] > 9:
				toflash.append([ii, jj])
	while len(toflash) > 0:
		[ii, jj] = toflash.pop()
		if [ii, jj] not in flashed:
			adjs = [[ii, jj + 1], [ii, jj - 1], [ii + 1, jj], [ii - 1, jj], [ii + 1, jj + 1], [ii + 1, jj - 1], [ii - 1, jj + 1], [ii - 1, jj - 1]]
			valid_coords = []
			for coord in adjs:
				if 0 <= coord[0] <= 9 and 0 <= coord[1] <= 9:
					valid_coords.append(coord)
			for adj in valid_coords:	
				try:
					nums[adj[0]][adj[1]] += 1
					if nums[adj[0]][adj[1]] > 9:
						toflash.append([adj[0], adj[1]])
				except Exception:
					pass
			flashed.append([ii, jj])

	for octo in flashed:
		nums[octo[0]][octo[1]] = 0

	return len(flashed)

ii = 0
while True:
	increment_by_one(octs)
	flash(octs)
	ii += 1
	if all_zeros(octs):
		break
print(ii)
