#advent of code
#2016, 06, 1

# python 06_1.py < input_06.txt
# correct answer: qtbjqiuq

# --- Day 6: Signals and Noise ---
#
# Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.
#
# In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.
#
# All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:
#
# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
#
# The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.
#
# Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

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
	letters = sorted(letters.items(), key=operator.itemgetter(1), reverse=True)
	code += str(letters[0][0])
	
print("Code", code)