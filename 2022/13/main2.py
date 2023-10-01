#!/opt/homebrew/bin/python3

import json
import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints, quicksort

lines = input_as_lines('data.txt')

def correct(left, right):
    left_islist, right_islist = isinstance(left, list), isinstance(right, list)
    if left_islist and right_islist:
        if not left:
            if not right:
                return 'inconclusive'
            else:
                return True
        elif not right:
            return False
        else:
            value = correct(left[0], right[0])
            if value != 'inconclusive':
                return value
            else:
                return correct(left[1:], right[1:])
    elif left_islist:
        return correct(left, [right])
    elif right_islist:
        return correct([left], right)
    else:
        if left < right:
            return True
        elif left == right:
            return 'inconclusive'
        else:
            return False

pairs = [[[2]], [[6]]]
for line in lines:
    if line:
        pairs.append(json.loads(line))

quicksort(pairs, correct)
print((pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1))
