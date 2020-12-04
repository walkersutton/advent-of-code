import re

def is_valid(person):
  s = person.split(":")
  s.remove('')
  index = 0
  di = {}

  while index < len(s):
    di[s[index]] = s[index + 1]
    index += 2

  good = True
  for key in di:
    if key == 'byr':
      if di[key].isnumeric() and 1920 <= int(di[key]) <= 2002:
        continue
      else:
        good = False
    elif key == 'iyr':
      if di[key].isnumeric() and 2010 <= int(di[key]) <= 2020:
        continue
      else:
        good = False
    elif key == 'eyr':
      if di[key].isnumeric() and 2020 <= int(di[key]) <= 2030:
        continue
      else:
        good = False
    elif key == 'hgt':
      num = di[key][:-2]
      unit = di[key][-2:] 
      if num.isnumeric():
        num = int(num)
        if unit == 'in':
          if 59 <= num <= 76:
            continue
          else:
            good = False
        elif unit == 'cm':
          if 150 <= num <= 193:
            continue
          else:
            good = False
        else:
          good = False
      else:
        good = False
    elif key == 'hcl':
      if di[key][0] == '#':
        val = di[key][1:]
        if len(val) == 6 :
          if re.search('\A[0-9a-f]+\Z', val):
            continue
          else:
            good = False
        else:
          good = False
      else:
        good = False
    elif key == 'ecl':
      valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
      if di[key] in valid_colors:
        continue
      else:
        good = False
    elif key == 'pid':
      if len(di[key]) == 9 and di[key].isnumeric():
        continue
      else:
        good = False
    if not good:
      return good

  return good

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
      and 'pid:' in person
      and is_valid(person.replace(' ', ':'))):
      total += 1 
    person = ''
  else:
    person += ":"
    person += line


print(total)
