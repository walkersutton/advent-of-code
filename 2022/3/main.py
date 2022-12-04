import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

rucksacks = input_as_lines('data.txt')
tot = 0

def priority(item):
    uni_int = ord(item)
    if 65 <= uni_int <= 90:
        return uni_int - 38
    else:
        return uni_int - 96

def shared_item_priority(rucksack):
    comp_1, comp_2 = set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
    shared_item = list(comp_1.intersection(comp_2))[0]
    return priority(shared_item)

for rucksack in rucksacks:
    tot += shared_item_priority(rucksack)

print(tot)
