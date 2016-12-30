# Advent Of Code 2016 - http://adventofcode.com/2016

# python 21_2.py < input_21.txt
# correct answer: gdfcabeh

# --- Part Two ---
#
# You scrambled the password correctly, but you discover that you can't actually modify the password file on the system. You'll need to un-scramble one of the existing passwords by reversing the scrambling process.
#
# What is the un-scrambled version of the scrambled password fbgdceah?
import re
import sys

__author__ = "Manuel Geier (manuel@geier.io)"


def swapPositionXWithPositionY(data, x, y):
    data_list = list(data)
    data_list[y], data_list[x] = data_list[x], data_list[y]
    return "".join(data_list)


assert swapPositionXWithPositionY("abcde", 4, 0) == "ebcda"
assert swapPositionXWithPositionY("ebcda", 0, 4) == "abcde"


def swapLetterXWithLetterY(data, x, y):
    return data.replace(x, "?").replace(y, x).replace("?", y)


assert swapLetterXWithLetterY("abc", "a", "b") == "bac"
assert swapLetterXWithLetterY("bac", "b", "a") == "abc"


def rotateLeft(data):
    return data[1:] + data[0]


assert rotateLeft("abc") == "bca"


def rotateRight(data):
    return data[-1] + data[:-1]


assert rotateRight("abc") == "cab"
assert "abc" == rotateRight(rotateLeft("abc"))
assert "abc" == rotateLeft(rotateRight("abc"))


def rotate(data, direction, steps):
    for i in range(steps):
        if direction == "left":
            data = rotateLeft(data)
        else:
            data = rotateRight(data)
    return data


assert rotate("abcdef", "left", 2) == "cdefab"
assert rotate("cdefab", "right", 2) == "abcdef"
assert rotate("abcdef", "right", 2) == "efabcd"
assert rotate("efabcd", "left", 2) == "abcdef"


def rotateBasedOnPositionOfLetterY(data, x):
    index = data.index(x)
    steps = index + 1 + (1 if index >= 4 else 0)
    return rotate(data, "right", steps)


assert rotateBasedOnPositionOfLetterY("abcde", "b") == "deabc"
assert rotateBasedOnPositionOfLetterY("abcde", "e") == "eabcd"
assert rotateBasedOnPositionOfLetterY("abdec", "b") == "ecabd"
assert rotateBasedOnPositionOfLetterY("ecabd", "d") == "decab"


def unrotateBasedOnPositionOfLetterY(data, x):
    original_data = data
    data_scrambled = data
    # brute force
    while rotateBasedOnPositionOfLetterY(data_scrambled, x) != original_data:
        data_scrambled = rotateLeft(data_scrambled)
    return data_scrambled


assert unrotateBasedOnPositionOfLetterY("deabc", "b") == "abcde"
assert unrotateBasedOnPositionOfLetterY("eabcd", "e") == "abcde"
assert unrotateBasedOnPositionOfLetterY("ecabd", "b") == "abdec"
assert unrotateBasedOnPositionOfLetterY("decab", "d") == "ecabd"


def reversePositionsXthroughY(data, x, y):
    return data[:x] + data[x:y + 1][::-1] + data[y + 1:]


assert reversePositionsXthroughY("edcba", 0, 4) == "abcde"
assert reversePositionsXthroughY("abcde", 0, 4) == "edcba"
assert reversePositionsXthroughY("edcba", 1, 3) == "ebcda"
assert reversePositionsXthroughY("ebcda", 1, 3) == "edcba"


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
assert movePositionXToPositionY("bdeac", 4, 1) == "bcdea"
assert movePositionXToPositionY("bdeac", 3, 0) == "abdec"
assert movePositionXToPositionY("abdec", 0, 3) == "bdeac"

commands = []
for line in sys.stdin:
    commands.append(line)


def unscramble(data):
    for line in commands[::-1]:
        oldData = data
        if line.startswith("swap position"):
            m = re.match("^swap position (\d+) with position (\d+)$", line)
            data = swapPositionXWithPositionY(data, int(m.group(1)), int(m.group(2)))
        elif line.startswith("swap letter"):
            m = re.match("^swap letter (.) with letter (.)$", line)
            data = swapLetterXWithLetterY(data, m.group(1), m.group(2))
        elif line.startswith("rotate based on position of letter"):
            m = re.match("^rotate based on position of letter (.)$", line)
            data = unrotateBasedOnPositionOfLetterY(data, m.group(1))
        elif line.startswith("rotate"):
            m = re.match("^rotate (.*) (\d+) step", line)
            data = rotate(data, "left" if m.group(1) == "right" else "right", int(m.group(2)))
        elif line.startswith("reverse positions"):
            m = re.match("^reverse positions (\d+) through (\d+)$", line)
            data = reversePositionsXthroughY(data, int(m.group(1)), int(m.group(2)))
        elif line.startswith("move position"):
            m = re.match("^move position (\d+) to position (\d+)$", line)
            data = movePositionXToPositionY(data, int(m.group(2)), int(m.group(1)))
        else:
            raise Exception("unknown command: " + line)

        if len(oldData) != len(data):
            print(line)
            raise Exception()

    return data


assert unscramble("bdfhgeca") == "abcdefgh"

print("un-scrambled", unscramble("fbgdceah"))
