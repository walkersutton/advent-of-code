import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

h = 0
d = 0

for l in lines:
	l = l.split()

	if l[0] == 'forward':
		h += int(l[1])	
	elif l[0] == 'down':
		d += int(l[1])	
	elif l[0] == 'up':
		d -= int(l[1])	

print(h * d)
