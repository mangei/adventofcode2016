# Advent Of Code 2016 - http://adventofcode.com/2016

# python 19_2.py
# correct answer:

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

__author__ = "Manuel Geier (manuel@geier.io)"

puzzle_input = 3018458


class WhiteElephantParty:
    def __init__(self, elf_count):
        self.elf_count = elf_count
        self.elves_with_presents_count = elf_count
        self.elves = [1 for i in range(elf_count)]

    def movePresentsFromTo(self, fromIndex, toIndex):
        self.elves[toIndex] += self.elves[fromIndex]
        self.elves[fromIndex] = 0
        self.elves_with_presents_count -= 1

    def hasPresents(self, index):
        return self.elves[index] > 0

    def getNextElfIndex(self, index, skip=0):
        for i in range(1, self.elf_count + 1):
            currentIndex = (index + i) % self.elf_count
            if self.hasPresents(currentIndex):
                if skip == 0:
                    return currentIndex
                skip -= 1

    def getOppositeElfIndex(self, index):
        skip_elves = int(self.elves_with_presents_count / 2) - 1
        oppositeElfIndex = self.getNextElfIndex(index, skip_elves)
        return oppositeElfIndex

    def getWinningElf(self):
        currentElfIndex = 0
        while True:
            oppositeElfIndex = self.getOppositeElfIndex(currentElfIndex)
            if oppositeElfIndex is not None:
                self.movePresentsFromTo(oppositeElfIndex, currentElfIndex)
                currentElfIndex = self.getNextElfIndex(currentElfIndex)
            else:
                break

        # increase by one, since it starts with 1
        return currentElfIndex + 1


def main():
    whiteElephantParty = WhiteElephantParty(5)
    assert whiteElephantParty.getWinningElf() == 2

    whiteElephantParty = WhiteElephantParty(puzzle_input)
    print("final elf", whiteElephantParty.getWinningElf())


if __name__ == '__main__':
    main()
