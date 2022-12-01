import heapq
import sys

from parse import input_as_string, input_as_lines, input_as_ints

sys.path.append("..")

lines = input_as_lines('data.txt')
heap = []
temp_sum = 0

for line in lines:
    if line not in ('', '\n'):
        temp_sum += int(line)
    else:
        heap.append(temp_sum)
        temp_sum = 0

heap.append(temp_sum)

heapq.heapify(heap)

print(sum(heapq.nlargest(3, heap)))
