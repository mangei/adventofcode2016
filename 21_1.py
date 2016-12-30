# Advent Of Code 2016 - http://adventofcode.com/2016

# python 21_1.py < input_21.txt
# correct answer: bdfhgeca

# --- Day 21: Scrambled Letters and Hash ---
#
# The computer system you're breaking into uses a weird scrambling function to store its passwords. It shouldn't be much trouble to create your own scrambled password so you can add it to the system; you just have to implement the scrambler.
#
# The scrambling function is a series of operations (the exact list is provided in your puzzle input). Starting with the password to be scrambled, apply each operation in succession to the string. The individual operations behave as follows:
#
#  - swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
#  - swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
#  - rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
#  - rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
#  - reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
#  - move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
#
# For example, suppose you start with abcde and perform the following operations:
#
#  - swap position 4 with position 0 swaps the first and last letters, producing the input for the next step, ebcda.
#  - swap letter d with letter b swaps the positions of d and b: edcba.
#  - reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
#  - rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the end of the string: bcdea.
#  - move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 (the end of the string): bdeac.
#  - move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 (the front of the string): abdec.
#  - rotate based on position of letter b finds the index of letter b (1), then rotates the string right once plus a number of times equal to that index (2): ecabd.
#  - rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, plus a number of times equal to that index, plus an additional time because the index was at least 4, for a total of 6 right rotations: decab.
#
# After these steps, the resulting scrambled password is decab.
#
# Now, you just need to generate a new scrambled password and you can access the system. Given the list of scrambling operations in your puzzle input, what is the result of scrambling abcdefgh?

import re
import sys

__author__ = "Manuel Geier (manuel@geier.io)"


def swapPositionXWithPositionY(data, x, y):
    data_list = list(data)
    data_list[y], data_list[x] = data_list[x], data_list[y]
    return "".join(data_list)


assert swapPositionXWithPositionY("abcde", 4, 0) == "ebcda"


def swapLetterXWithLetterY(data, x, y):
    return data.replace(x, "?").replace(y, x).replace("?", y)


assert swapLetterXWithLetterY("abc", "a", "b") == "bac"


def rotateLeft(data):
    return data[1:] + data[0]


assert rotateLeft("abc") == "bca"


def rotateRight(data):
    return data[-1] + data[:-1]


assert rotateRight("abc") == "cab"


def rotate(data, direction, steps):
    for i in range(steps):
        if direction == "left":
            data = rotateLeft(data)
        else:
            data = rotateRight(data)
    return data


assert rotate("abcdef", "left", 2) == "cdefab"
assert rotate("abcdef", "right", 2) == "efabcd"


def rotateBasedOnPositionOfLetterY(data, x):
    index = data.index(x)
    steps = index + 1 + (1 if index >= 4 else 0)
    return rotate(data, "right", steps)


assert rotateBasedOnPositionOfLetterY("abdec", "b") == "ecabd"
assert rotateBasedOnPositionOfLetterY("ecabd", "d") == "decab"


def reversePositionsXthroughY(data, x, y):
    return data[:x] + data[x:y + 1][::-1] + data[y + 1:]


assert reversePositionsXthroughY("edcba", 0, 4) == "abcde"
assert reversePositionsXthroughY("edcba", 1, 3) == "ebcda"


def movePositionXToPositionY(data, x, y):
    data_list = []
    c = data[x]
    for i in range(len(data)):
        if i != x:
            data_list.append(data[i])
    data_list2 = []
    for i in range(len(data_list)):
        if i == y:
            data_list2.append(c)
        data_list2.append(data_list[i])
    if y == len(data_list):
        data_list2.append(c)
    return "".join(data_list2)


assert movePositionXToPositionY("bcdea", 1, 4) == "bdeac"
assert movePositionXToPositionY("bdeac", 3, 0) == "abdec"

data = "abcdefgh"

for line in sys.stdin:
    if line.startswith("swap position"):
        m = re.match("^swap position (\d+) with position (\d+)$", line)
        data = swapPositionXWithPositionY(data, int(m.group(1)), int(m.group(2)))
    elif line.startswith("swap letter"):
        m = re.match("^swap letter (.) with letter (.)$", line)
        data = swapLetterXWithLetterY(data, m.group(1), m.group(2))
    elif line.startswith("rotate based on position of letter"):
        m = re.match("^rotate based on position of letter (.)$", line)
        data = rotateBasedOnPositionOfLetterY(data, m.group(1))
    elif line.startswith("rotate"):
        m = re.match("^rotate (.*) (\d+) step", line)
        data = rotate(data, m.group(1), int(m.group(2)))
    elif line.startswith("reverse positions"):
        m = re.match("^reverse positions (\d+) through (\d+)$", line)
        data = reversePositionsXthroughY(data, int(m.group(1)), int(m.group(2)))
        pass
    elif line.startswith("move position"):
        m = re.match("^move position (\d+) to position (\d+)$", line)
        data = movePositionXToPositionY(data, int(m.group(1)), int(m.group(2)))
    else:
        raise Exception("unknown command: " + line)

print("scramble", data)
