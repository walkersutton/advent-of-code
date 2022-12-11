#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
ROUNDS = 20
monkeys = []

class Monkey:
    def __init__(self, index, items, operation, operation_value, test, true, false):
        self.index = index
        self.items = items
        self.operation = operation
        self.operation_value = operation_value
        self.test = test
        self.true = true
        self.false = false
        self.business = 0

for ii in range(0, len(lines), 7):
    index = int(lines[ii].split(' ')[1].split(':')[0])
    items = [int(i) for i in lines[ii + 1].split(':')[1].split(',')]
    operation = '*' if '*' in lines[ii + 2] else '+'
    operation_value = lines[ii + 2].split(' ')[-1]
    if operation_value.isnumeric():
        operation_value = int(operation_value)
    test = int(lines[ii + 3].split(' ')[-1])
    true = int(lines[ii + 4].split(' ')[-1])
    false = int(lines[ii + 5].split(' ')[-1])
    monkeys.append(Monkey(index, items, operation, operation_value, test, true, false))

for _ in range(ROUNDS):
    for monkey in monkeys:
        for worry_level in monkey.items:
            monkey.business += 1
            op_value = worry_level if monkey.operation_value == 'old' else monkey.operation_value
            worry_level = worry_level * op_value if monkey.operation == '*' else worry_level + op_value
            worry_level //= 3
            throw_to = monkey.true if worry_level % monkey.test == 0 else monkey.false
            monkeys[throw_to].items.append(worry_level)
        monkey.items = []

monkey_businesses = [monkey.business for monkey in sorted(monkeys, key = lambda m: m.business, reverse = True)]
print(monkey_businesses[0] * monkey_businesses[1])
