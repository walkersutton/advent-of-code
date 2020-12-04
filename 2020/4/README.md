# AOC 2020 - Day 4

[link](https://adventofcode.com/2020/day/4)

## Part 1

### Excpected Fields:
* byr (Birth Year)
* iyr (Issue Year)
* eyr (Expiration Year)
* hgt (Height)
* hcl (Hair Color)
* ecl (Eye Color)
* pid (Passport ID)
* cid (Country ID)

> Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
(The _required fields_ include all of the fields except for the `cid field`)

## Part 2

### Valid Values
* byr (Birth Year) - four digits; at least 1920 and at most 2002.
* iyr (Issue Year) - four digits; at least 2010 and at most 2020.
* eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
* hgt (Height) - a number followed by either cm or in:
* If cm, the number must be at least 150 and at most 193.
* If in, the number must be at least 59 and at most 76.
* hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
* ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
* pid (Passport ID) - a nine-digit number, including leading zeroes.
* cid (Country ID) - ignored, missing or not.

> Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
