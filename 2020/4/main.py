VALID_FIELDS = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append((element.strip()))

total = 0
person, valid = '', True

for line in vals:
  if line == '':
    for field in VALID_FIELDS:
      if field not in person:
        valid = False
        break
    if valid: 
      total += 1 
    person, valid = '', True
  else:
    person += line

print(total)
