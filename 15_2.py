# Advent Of Code 2016 - http://adventofcode.com/2016

# python 15_2.py < input_15.txt
# correct answer: 3208099

# --- Part Two ---
#
# After getting the first capsule (it contained a star! what great fortune!), the machine detects your success and begins to rearrange itself.
#
# When it's done, the discs are back in their original configuration as if it were time=0 again, but a new disc with 11 positions and starting at position 0 has appeared exactly one second below the previously-bottom disc.
#
# With this new disc, and counting again starting from time=0 with the configuration in your puzzle input, what is the first time you can press the button to get another capsule?

import re

import sys

__author__ = "Manuel Geier (manuel@geier.io)"

discs = []

discDelay = 0
for line in sys.stdin:
    m = re.match("^Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).$", line)
    discPositions = int(m.group(2))
    discInitialPosition = int(m.group(3))
    discs.append((discPositions, discInitialPosition, discDelay))
    discDelay += 1

# additional disc
discs.append((11, 0, discDelay))

t = 0
while True:
    valid = True
    for (discPositions, discInitialPosition, discDelay) in discs:
        currentPosition = (discInitialPosition + t + discDelay) % discPositions
        # print(i, currentPosition)
        if currentPosition != 0:
            valid = False
            break
    if valid:
        break
    t += 1

# drop one second before
t -= 1

print("time", t)
