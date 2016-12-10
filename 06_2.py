#advent of code
#2016, 06, 2

# python 06_2.py < input_06.txt
# correct answer: akothqli

# --- Part Two ---
#
# Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.
#
# In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.
#
# In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.
#
# Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

import sys
import operator
import string

pos_letter_count = {}

for line in sys.stdin:
	for i, c in enumerate(line):
		if c not in string.ascii_lowercase:
			continue
		pos_letter_count[i] = pos_letter_count.get(i, {})
		pos_letter_count[i][c] = pos_letter_count[i].get(c, 0) + 1
		
code = ""

values_by_pos = pos_letter_count.items()
values_by_pos = sorted(values_by_pos, key=operator.itemgetter(0))

for values in values_by_pos:
	(i, letters) = values
	letters = sorted(letters.items(), key=operator.itemgetter(1), reverse=False)
	code += str(letters[0][0])
	
print("Code", code)