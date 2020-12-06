infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []

for element in text_data:
  vals.append((element.strip()))

aggreements = 0
question_set= set()
new_group = True

for response in vals:
	if response == '':
		aggreements += len(question_set)
		new_group = True
		question_set.clear()
	else:
		if len(question_set) == 0 and new_group:
			for question in response:
				question_set.add(question)
		else:
			set_copy = question_set.copy()
			for question in set_copy:
				if question not in response:
					question_set.remove(question)
			new_group = False

print(aggreements)
	
