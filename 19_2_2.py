# Advent Of Code 2016 - http://adventofcode.com/2016

# python 19_2_2.py
# correct answer: 1424135

# --- Part Two ---
#
# Realizing the folly of their present-exchange rules, the Elves agree to instead steal presents from the Elf directly across the circle. If two Elves are across the circle, the one on the left (from the perspective of the stealer) is stolen from. The other rules remain unchanged: Elves with no presents are removed from the circle entirely, and the other elves move in slightly to keep the circle evenly spaced.
#
# For example, with five Elves (again numbered 1 to 5):
#
#  - The Elves sit in a circle; Elf 1 goes first:
#
#   1
# 5   2
#  4 3
#
#  - Elves 3 and 4 are across the circle; Elf 3's present is stolen, being the one to the left. Elf 3 leaves the circle, and the rest of the Elves move in:
#
#   1           1
# 5   2  -->  5   2
#  4 -          4
#
#  - Elf 2 steals from the Elf directly across the circle, Elf 5:
#
#   1         1
# -   2  -->     2
#   4         4
#
#  - Next is Elf 4 who, choosing between Elves 1 and 2, steals from Elf 1:
#
#  -          2
#     2  -->
#  4          4
#
#  - Finally, Elf 2 steals from Elf 4:
#
#  2
#     -->  2
#  -
#
# So, with five Elves, the Elf that sits starting in position 2 gets all the presents.
#
# With the number of Elves given in your puzzle input, which Elf now gets all the presents?
#
# Your puzzle input is still 3018458.
import sys

import time

__author__ = "Manuel Geier (manuel@geier.io)"

puzzle_input = 3018458


class WhiteElephantParty:
    def __init__(self, elf_count):
        self.elf_count = elf_count
        self.elves_with_presents_count = elf_count
        self.elves = [(i + 1) for i in range(elf_count)]

    def movePresentsFromTo(self, fromIndex, toIndex):
        # print(self.elves[toIndex], self.elves, self.elves[fromIndex])
        del self.elves[fromIndex]
        # print(" ", self.elves)
        self.elves_with_presents_count -= 1

    def getOppositeElfIndex(self, index):
        oppositeElfIndex = (index + int(self.elves_with_presents_count / 2)) % self.elves_with_presents_count
        return oppositeElfIndex if oppositeElfIndex != index else None

    def getWinningElf(self):
        print("start", self.elf_count)
        sys.stdout.flush()

        tBegin = time.time()
        t = time.time()

        currentElfIndex = 0
        while True:
            oppositeElfIndex = self.getOppositeElfIndex(currentElfIndex)
            if oppositeElfIndex is not None:
                self.movePresentsFromTo(oppositeElfIndex, currentElfIndex)
                if oppositeElfIndex < currentElfIndex:
                    # element before the current was deleted, hence, we don't have to increment, since it incremented
                    # "implicitly"
                    pass
                else:
                    currentElfIndex += 1
                currentElfIndex %= self.elves_with_presents_count
            else:
                break

            if self.elves_with_presents_count % 10000 == 0:
                tCur = time.time()
                print(self.elves_with_presents_count, tCur - t, tCur - tBegin)
                t = tCur
                sys.stdout.flush()

        print("total time", time.time() - tBegin)
        sys.stdout.flush()

        return self.elves[currentElfIndex]


def main():
    whiteElephantParty = WhiteElephantParty(1)
    assert whiteElephantParty.getWinningElf() == 1

    whiteElephantParty = WhiteElephantParty(2)
    assert whiteElephantParty.getWinningElf() == 1

    whiteElephantParty = WhiteElephantParty(3)
    assert whiteElephantParty.getWinningElf() == 3

    whiteElephantParty = WhiteElephantParty(4)
    assert whiteElephantParty.getWinningElf() == 1

    whiteElephantParty = WhiteElephantParty(5)
    assert whiteElephantParty.getWinningElf() == 2

    whiteElephantParty = WhiteElephantParty(6)
    assert whiteElephantParty.getWinningElf() == 3

    whiteElephantParty = WhiteElephantParty(7)
    assert whiteElephantParty.getWinningElf() == 5

    whiteElephantParty = WhiteElephantParty(puzzle_input)
    print("final elf", whiteElephantParty.getWinningElf())


if __name__ == '__main__':
    main()
