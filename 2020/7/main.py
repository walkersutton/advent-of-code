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
		rules[root_bag].append((words[ii + 1], words[ii + 2]))
		ii += 4

shiny_bags = set()
shiny_bags.add(('shiny', 'gold'))

was_modified = True

while was_modified:
	was_modified = False
	for root_bag in rules:
		bags_copy = shiny_bags.copy()
		for bag in bags_copy:
			if bag in rules[root_bag]:
				if root_bag not in shiny_bags:
					shiny_bags.add(root_bag)
					was_modified = True

print(len(shiny_bags) - 1)
