import sys
import math
sys.path.append("..")

from parse import input_as_string, input_as_lines, input_as_ints

st = input_as_string('test.txt')

def read_literal(stri):
	re = ''
	cur = 0
	while True:
		if stri[cur] == '0':
			re += stri[cur + 1:cur + 5]
			break
		else:
			re += stri[cur + 1:cur + 5]
			cur += 5
	return re

def read_subp(stri, subplen):
	print(stri, subplen)
	re = ''
	cur = 0
	for ii in range(math.floor(len(stri) / subplen)):
		print('this')
		print(str(int(stri[cur:cur + 11], 2)))
		re += str(int(stri[cur:cur + 11], 2))
		cur += 11
	return re
		
		
pri_packet = ''
for l in st:
	t = str(bin(int(l, 16)))[2:]
	for ii in range(4 - len(t)):
		pri_packet += '0'
	pri_packet += t

packets = [pri_packet]
version_total = 0
while len(packets) > 0:
	cur_packet = packets.pop()
	version = cur_packet[0:3]
	version_total += int(version, 2)
	type_id = cur_packet[3:6]	
	if type_id == bin(4)[2:]:
		break
	else: # operator
	if int(cur_packet[6:7]) == 0:
		sub_packet_len = int(cur_packet[7:22], 2)
		packets.append(cur_packet[22: 22 + sub_packet_len])
	else:
		sub_packet_len = int(re[7:18], 2)
		packets.extend(get_sub_packets(cur_packet[18:], sub_packet_len)
		print(read_subp(re[18:], 11))
		
# if version == bin(6)[2:]:
		
		
	



	



# a = re[6:11]
# b = re[11:16]
# c = re[17:22]
