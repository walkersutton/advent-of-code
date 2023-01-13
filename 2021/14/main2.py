import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

def pairs(stri):
	prs = []
	for ii in range(len(stri) - 1):
		prs.append(stri[ii:ii + 2])
	return prs
	

def make_levels(pair, level, rules):
	start_level = len(rules[pair]) - 1
	last = ''
	for ii in range(start_level, level):
		tempstr = ''
		for p in pairs(rules[pair][ii]):
			if tempstr != '':
				last = tempstr[-1]
				tempstr = tempstr[:-1]
			tempstr += rules[p][0]
		rules[pair].append(tempstr)
		

def get_val_at_level(pair, level, rules):
	if len(rules[pair]) >= level:
		return rules[pair][level - 1]
	else:
		make_levels(pair, level, rules)
		return rules[pair][level - 1]
	
lines = input_as_lines('data.txt')
lets = 'OFSVVSFOCBNONHKFHNPK'

rules = {}
for line in lines:
	temp = line.split('->')
	rules[temp[0].strip()] = [temp[0].strip()[0] + temp[1].strip() + temp[0].strip()[1]]

level = 40
prs = pairs(lets)
s = ''
for ii in range(len(prs)):
	if ii == 0:
		s += get_val_at_level(prs[ii], level, rules)
	else:
		s += get_val_at_level(prs[ii], level, rules)[1:]

uniq = set(s)
uniqq = {}
for ea in uniq:
	uniqq[ea] = s.count(ea)
print(max(uniqq.values()) - min(uniqq.values()))
