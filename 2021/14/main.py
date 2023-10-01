import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
lets = 'OFSVVSFOCBNONHKFHNPK'
rules = {}
for line in lines:
	temp = line.split('->')
	rules[temp[0].strip()] = temp[1].strip()

lets = list(lets)


for jj in range(40):
	print(jj)
	ii = 0
	idx = 1
	while ii < len(lets) - 1:
		lets.insert(idx, rules[lets[ii] + lets[ii + 1]])
		ii += 2
		idx += 2

uniq = set(lets)
uniqq = {}	
for ele in uniq:
	uniqq[ele] = lets.count(ele)

print(max(uniqq.values()) - min(uniqq.values()))

#print(lets)
