import json
import sys
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

def max_valu(lis):
	max_val = 0
	for ele in lis:
		if isinstance(ele, list):
			max_val = max(max_val, max_valu(ele))
		else:
			max_val = max(max_val, ele)
	return max_val

def max_nest(lis):
	max_level = 0
	for ele in lis:
		if isinstance(ele, list):
			max_level = max(max_level, 1 + max_nest(ele))
	return max_level
		
def is_too_nested(left, right):
	return max_nest(left) > 3 or max_nest(right) > 3

def is_too_big(left, right):
	return max_valu(left) > 10 or max_valu(right) > 10

def explode(lis):
	
	pass

def split(lis):
	pass

def create_pair(left, right):
	if is_too_nested(left, right):
		left = explode(left)
	if is_too_big(left, right):
		left = split(left)
	return [left, right]

# lines = input_as_lines('data.txt')
lines = input_as_lines('test.txt')
fish = []
for line in lines:
	fish.append(json.loads(line))

