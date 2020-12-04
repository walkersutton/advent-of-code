import re

VALID_FIELDS = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
VALID_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_valid(person):
  passport_str = person.replace(' ', ':').split(":")
  passport_str.remove('')
  
  passport = {}
  index = 0
  while index < len(passport_str):
    passport[passport_str[index]] = passport_str[index + 1]
    index += 2

  for key in passport:
    value = passport[key]
    if key == 'byr' and not (1920 <= int(value) <= 2002):
      return False
    elif key == 'iyr' and not (2010 <= int(value) <= 2020):
      return False
    elif key == 'eyr' and not (2020 <= int(value) <= 2030):
      return False
    elif key == 'hgt':
      try: 
        num = int(value[:-2])
        unit = value[-2:] 
        if ((unit == 'in' and not (59 <= num <= 76)) or 
            (unit == 'cm' and not (150 <= num <= 193))):
          return False
      except:
        return False
    elif key == 'hcl' and not (len(value[1:]) == 6 and re.search('\A[0-9a-f]+\Z', value[1:])):
      return False
    elif key == 'ecl' and passport[key] not in VALID_COLORS:
      return False
    elif key == 'pid' and not (len(value) == 9 and value.isnumeric()):
      return False

  return True


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
    if valid and is_valid(person):
      total += 1
    person, valid = '', True
  else:
    person += ":" + line

print(total)
