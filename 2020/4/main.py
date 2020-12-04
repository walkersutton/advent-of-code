infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append((element.strip()))

total = 0
person = ''

for line in vals:
  if line == '':
    if   ('byr:' in person
      and 'iyr:' in person
      and 'eyr:' in person
      and 'hgt:' in person
      and 'hcl:' in person
      and 'ecl:' in person
      and 'pid:' in person):
      total += 1 
    person = ''
  else:
    person += line

print(total)
