#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

# string = input_as_string('data.txt')
lines = input_as_lines('data.txt')
lines = input_as_lines('data2.txt')
MINUTES = 30
# ints = input_as_ints('data.txt')


'''
start in AA - already opened
1 min to move
1 min to open
'''
valves = {}
duds = []

for line in lines:
    index = int(ord(line.split(' ')[1][0])) - 65
    rate = int(line.split(' ')[4][:-1].split('=')[1])

    vs = line.split('to valve')[1]
    if ',' in vs:
        vs = vs.split(',')
    else:
        vs = [vs]
    if vs[0][0] == 's':
        vs[0] = vs[0][1:]
    vs = [int(ord(v.strip()[0])) - 65 for v in vs]
    if rate == 0:
        duds.append(index)
    valves[index] = {'rate': rate, 'valves': vs}

# memo = {}
# def dtd(vs, start, nd, seen):
#     print(start, nd, end = '')
#     if (start, nd) in memo.keys():
#         return memo[(start, nd)]
#     if nd in vs[start]['valves']:
#         memo[(start, nd)] = 1
#         print(1)
#         print(' ')
#         return 1
#     else:
#         v = 1 + min([dtd(vs, childv, nd, seen + [childv]) for childv in vs[start]['valves'] if childv not in seen])
#         memo[(start, nd)] = v
#         print(v)
#         print(' ')
#         return v

def can_get_to(start, end):
    if end in open:
        return True
    else:
        tried = set({})
        possibles = []
        for child in valves[start]['valves']:
            if (start, child) not in tried:
                possibles.append((start, child))
        while possibles:
            possible = possibles.pop()
            tried.add(possible)
            if possible[1] == end:
                return True
            else:
                for child in valves[possible[0]]['valves']:
                    if (possible[0], child) not in tried:
                        possibles.append((possible[0], child))
        return False

costs = []
costs[(start, end)] = 
import heapq
explore = [(-valves[v]['rate'], v) for v in valves[0]['valves'] if v not in duds]
heapq.heapify(explore)
# explore has unopened valves with rates != 0
tot_pres = 0
open = set({0})
cur_pres = valves[0]['rate']

# print('distance from a to c', dtd(valves, 0, 2, [0]))
## #print(can_get_to(0, 7))

for _ in range(MINUTES):
    
    # heapq.heappush(explore, ele)
    



    
    tot_pres += cur_pres

print(tot_pres)
