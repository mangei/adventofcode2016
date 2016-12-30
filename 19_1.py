# Advent Of Code 2016 - http://adventofcode.com/2016

# python 19_1.py
# correct answer: 1842613

# --- Day 19: An Elephant Named Joseph ---
#
# The Elves contact you over a highly secure emergency channel. Back at the North Pole, the Elves are busy misunderstanding White Elephant parties.
#
# Each Elf brings a present. They all sit in a circle, numbered starting with position 1. Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left. An Elf with no presents is removed from the circle and does not take turns.
#
# For example, with five Elves (numbered 1 to 5):
#
#   1
# 5   2
#  4 3
#
#  - Elf 1 takes Elf 2's present.
#  - Elf 2 has no presents and is skipped.
#  - Elf 3 takes Elf 4's present.
#  - Elf 4 has no presents and is also skipped.
#  - Elf 5 takes Elf 1's two presents.
#  - Neither Elf 1 nor Elf 2 have any presents, so both are skipped.
#  - Elf 3 takes Elf 5's three presents.
#
# So, with five Elves, the Elf that sits starting in position 3 gets all the presents.
#
# With the number of Elves given in your puzzle input, which Elf gets all the presents?
#
# Your puzzle input is 3018458.

import numpy as np

__author__ = "Manuel Geier (manuel@geier.io)"

puzzle_input = 3018458


class WhiteElephantParty:
    def __init__(self, elf_count):
        self.elf_count = elf_count
        self.elves = np.empty(elf_count)
        self.elves.fill(1)

    def movePresentsFromTo(self, fromIndex, toIndex):
        self.elves[toIndex] += self.elves[fromIndex]
        self.elves[fromIndex] = 0

    def getNextElfIndex(self, index):
        for i in range(1, self.elf_count + 1):
            currentIndex = (index + i) % self.elf_count
            if self.elves[currentIndex] > 0:
                return currentIndex

    def getWinningElf(self):
        currentElfIndex = 0
        while True:
            nextElfIndex = self.getNextElfIndex(currentElfIndex)
            if currentElfIndex != nextElfIndex:
                self.movePresentsFromTo(nextElfIndex, currentElfIndex)
                currentElfIndex = self.getNextElfIndex(nextElfIndex)
            else:
                break

        # increase by one, since it starts with 1
        return currentElfIndex + 1


def main():
    whiteElephantParty = WhiteElephantParty(5)
    assert whiteElephantParty.getWinningElf() == 3

    whiteElephantParty = WhiteElephantParty(puzzle_input)
    print("final elf", whiteElephantParty.getWinningElf())


if __name__ == '__main__':
    main()
