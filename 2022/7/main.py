#!/opt/homebrew/bin/python3

import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

class Node:
    def __init__(self, name, size, parent, children):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = children

    def print_tree(self, indent):
        print(' ' * indent, self.name, self.size)
        if self.children:
            for c in self.children:
                c.print_tree(indent + 2)

lines = input_as_lines('data.txt')
cur = root = Node('/', 0, None, [])
lsing = False

for line in lines:
    first, second = line.split(' ')[0], line.split(' ')[1]
    if lsing:
        if first == '$':
            lsing = False
        elif first == 'dir':
            cur.children.append(Node('/' + second, 0, cur, []))
        else: # file
            size = int(first)
            cur.children.append(Node(second, size, cur, None))
            temp = cur
            while temp:
                temp.size += size
                temp = temp.parent
    if not lsing and first == '$':
        if second == 'ls':
            lsing = True
        else: # cd
            third = line.split(' ')[2] 
            if third == '..':
                cur = cur.parent
            else: # change to child directory
                for child in cur.children:
                    if child.name == '/' + third:
                        cur = child
                        break

DISK_SPACE = 70000000
USED_SPACE = root.size
UPDATE_SIZE = 30000000
DIR_MAX_SIZE = 100000
DIR_MIN_SIZE = UPDATE_SIZE - (DISK_SPACE - USED_SPACE)
p1 = 0
p2 = Node('way_too_big', USED_SPACE, None, None)
nodes = [root]

while nodes:
    node = nodes.pop()
    if node.children:
        if node.size <= DIR_MAX_SIZE:
            p1 += node.size
        if p2.size > node.size > DIR_MIN_SIZE:
            p2 = node
    if node.children:
        nodes.extend(node.children)

# root.print_tree(0)
print(p1)
print(p2.size)
