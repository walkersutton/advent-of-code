infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []

for element in text_data:
  vals.append((element.strip()))

rules = {}

for rule in vals:
	words = rule.split()
	root_bag = (words[0], words[1])
	rules[root_bag] = []
	ii = 4
	while ii < len(words):
		if words[ii] == 'no':
			break
		rules[root_bag].append((int(words[ii]), (words[ii + 1], words[ii + 2])))
		ii += 4

frontier = [('shiny', 'gold')]

count = 0
while frontier:
	root_bag = frontier.pop()
	for bag in rules[root_bag]:
		for _ in range(bag[0]):
			frontier.append(bag[1])
			count += 1

print(count)
