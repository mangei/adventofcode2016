#advent of code
#2016, 05, 1

# python 05_1.py
# correct answer: f77a0e6e

# --- Day 5: How About a Nice Game of Chess? ---
#
# You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching hacking movies.
#
# The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).
#
# A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash is the next character of the password.
#
# For example, if the Door ID is abc:
#
#  - The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
#  - 5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8.
#  - The third time a hash starts with five zeroes is for abc5278568, discovering the character f.
#
# In this example, after continuing this search a total of eight times, the password is 18f47a30.
#
# Given the actual Door ID, what is the password?
#
# Your puzzle input is cxdnnyjw.

import hashlib

door_id = "cxdnnyjw"
i = 0
code_len = 0
code = ""

def hex_starts_with_5_zeros(string):
	return string.startswith("00000")
	
def get_sixth_character(string):
	return string[5]

while True:
	next_id = door_id + str(i)
	next_id = next_id.encode('utf-8')
	md5_value = hashlib.md5(next_id)
	hex_representation = md5_value.hexdigest()
	print(next_id, hex_representation, code_len, code)
	if hex_starts_with_5_zeros(hex_representation):
		code += get_sixth_character(hex_representation)
		code_len += 1
		if code_len >= 8:
			break
	i += 1
		
print("Code", code)