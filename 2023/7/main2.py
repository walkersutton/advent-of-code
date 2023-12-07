#!/opt/homebrew/bin/python3

from collections import defaultdict
from functools import cmp_to_key
import os
import sys

sys.path.append(os.path.pardir)
from parse import input_as_string, input_as_lines, input_as_ints

lines = input_as_lines('data.txt')

# nightmare
def score(hand):
	s = set(hand)

	counts = defaultdict(int)
	for card in hand:
		counts[card] += 1
	count_list = [ele[1] for ele in sorted(list(counts.items()), key=lambda x: x[1], reverse=True)]

	if count_list[0] == 5:
		return 7
	elif count_list[0] == 4:
		if 'J' in s:
			return 7
		else:
			return 6
	elif count_list[0] == 3:
		if count_list[1] == 2:
			if 'J' in s:
				return 7
			else:
				return 5
		elif count_list[1] == 1:
			if 'J' in s:
				return 6
			else:
				return 4
	elif count_list[0] == 2:
		if count_list[1] == 2:
			if 'J' in s:
				jcount = counts['J']
				if jcount == 2:
					return 6
				else:
					return  5
			else:
				return 3
		else:
			if 'J' in s:
					return 4
			else:
				return 2
	else:
		if 'J' in s:
			return 2
	return 1
	

card_strengths = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def strength(card):
	return 13 - card_strengths.index(card)

def comparator(l, r):
	left_hand = l[0]
	right_hand = r[0]
	left_hand_score = score(left_hand)
	right_hand_score = score(right_hand)
	if left_hand_score < right_hand_score:
		return 1
	elif left_hand_score > right_hand_score:
		return -1

	for ii in range(len(left_hand)):
		left_card, right_card = left_hand[ii], right_hand[ii]
		left_card_strength, right_card_strength = strength(left_card), strength(right_card)
		if left_card_strength < right_card_strength:
			return 1
		elif left_card_strength > right_card_strength:
			return -1
	return 0
				

games = []
for line in lines:
	hand, bid = line.split()
	games.append((hand, bid))
games.sort(key=cmp_to_key(comparator), reverse=True)

ret = 0
for ii in range(len(games)):
	ret += (ii + 1) * int(games[ii][1])
print(ret)
