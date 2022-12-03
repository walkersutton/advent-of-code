import sys

from parse import input_as_string, input_as_lines, input_as_ints

sys.path.append("..")

rucksacks = input_as_lines('data.txt')
tot = 0
group = []

def priority(item):
    uni_int = ord(item)
    if 65 <= uni_int <= 90:
        return uni_int - 38
    else:
        return uni_int - 96

def shared_item_priority(rucksacks):
    ruck_1, ruck_2, ruck_3 = [set(rucksack) for rucksack in rucksacks]
    shared_item = list(ruck_1.intersection(ruck_2, ruck_3))[0]
    return priority(shared_item)

for rucksack in rucksacks:
    if len(group) < 3:
        group.append(rucksack)
    else:
        tot += shared_item_priority(group)
        group = [rucksack]

tot += shared_item_priority(group)
print(tot)
