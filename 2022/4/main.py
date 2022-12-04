import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')
quantity = 0

for line in lines:
    sec_1, sec_2 = line.split(',')
    mi_1, ma_1 = [int(v) for v in sec_1.split('-')]
    mi_2, ma_2 = [int(v) for v in sec_2.split('-')]

    if mi_1 >= mi_2 and ma_1 <= ma_2:
        quantity += 1
    elif mi_2 >= mi_1 and ma_2 <= ma_1:
        quantity += 1

print(quantity)
