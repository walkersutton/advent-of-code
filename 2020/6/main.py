infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []

for element in text_data:
  vals.append((element.strip()))

questions_answered = 0
question_set= set()

for response in vals:
	if response== '':
		questions_answered += len(question_set)
		question_set.clear()
	else:
		for question in response:
			question_set.add(question)

print(questions_answered)
	
