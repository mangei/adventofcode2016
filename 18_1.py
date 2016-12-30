# Advent Of Code 2016 - http://adventofcode.com/2016

# python 18_1.py < input_18.txt
# correct answer: 1978

# --- Day 18: Like a Rogue ---
#
# As you enter this room, you hear a loud click! Some of the tiles in the floor here seem to be pressure plates for traps, and the trap you just triggered has run out of... whatever it tried to do to you. You doubt you'll be so lucky next time.
#
# Upon closer examination, the traps and safe tiles in this room seem to follow a pattern. The tiles are arranged into rows that are all the same width; you take note of the safe tiles (.) and traps (^) in the first row (your puzzle input).
#
# The type of tile (trapped or safe) in each row is based on the types of the tiles in the same position, and to either side of that position, in the previous row. (If either side is off either end of the row, it counts as "safe" because there isn't a trap embedded in the wall.)
#
# For example, suppose you know the first row (with tiles marked by letters) and want to determine the next row (with tiles marked by numbers):
#
# ABCDE
# 12345
#
# The type of tile 2 is based on the types of tiles A, B, and C; the type of tile 5 is based on tiles D, E, and an imaginary "safe" tile. Let's call these three tiles from the previous row the left, center, and right tiles, respectively. Then, a new tile is a trap only in one of the following situations:
#
#  - Its left and center tiles are traps, but its right tile is not.
#  - Its center and right tiles are traps, but its left tile is not.
#  - Only its left tile is a trap.
#  - Only its right tile is a trap.
#
# In any other situation, the new tile is safe.
#
# Then, starting with the row ..^^., you can determine the next row by applying those rules to each new tile:
#
#  - The leftmost character on the next row considers the left (nonexistent, so we assume "safe"), center (the first ., which means "safe"), and right (the second ., also "safe") tiles on the previous row. Because all of the trap rules require a trap in at least one of the previous three tiles, the first tile on this new row is also safe, ..
#  - The second character on the next row considers its left (.), center (.), and right (^) tiles from the previous row. This matches the fourth rule: only the right tile is a trap. Therefore, the next tile in this new row is a trap, ^.
#  - The third character considers .^^, which matches the second trap rule: its center and right tiles are traps, but its left tile is not. Therefore, this tile is also a trap, ^.
#  - The last two characters in this new row match the first and third rules, respectively, and so they are both also traps, ^.
#
# After these steps, we now know the next row of tiles in the room: .^^^^. Then, we continue on to the next row, using the same rules, and get ^^..^. After determining two new rows, our map looks like this:
#
# ..^^.
# .^^^^
# ^^..^
#
# Here's a larger example with ten tiles per row and ten rows:
#
# .^^.^.^^^^
# ^^^...^..^
# ^.^^.^.^^.
# ..^^...^^^
# .^^^^.^^.^
# ^^..^.^^..
# ^^^^..^^^.
# ^..^^^^.^^
# .^^^..^.^^
# ^^.^^^..^^
#
# In ten rows, this larger example has 38 safe tiles.
#
# Starting with the map in your puzzle input, in a total of 40 rows (including the starting row), how many safe tiles are there?

import sys

__author__ = "Manuel Geier (manuel@geier.io)"

TRAP = "^"
SAVE = "."


def isTrap(tile):
    return tile == TRAP


assert isTrap("^")
assert not isTrap(".")


def isNextTileTrap(leftTile, centerTile, rightTile):
    return (isTrap(leftTile) and isTrap(centerTile) and not isTrap(rightTile)) or \
           (isTrap(centerTile) and isTrap(rightTile) and not isTrap(leftTile)) or \
           (isTrap(leftTile) and not isTrap(centerTile) and not isTrap(rightTile)) or \
           (isTrap(rightTile) and not isTrap(leftTile) and not isTrap(centerTile))


assert isNextTileTrap(TRAP, TRAP, SAVE)
assert isNextTileTrap(SAVE, TRAP, TRAP)
assert isNextTileTrap(TRAP, SAVE, SAVE)
assert isNextTileTrap(SAVE, SAVE, TRAP)
assert not isNextTileTrap(SAVE, SAVE, SAVE)
assert not isNextTileTrap(TRAP, TRAP, TRAP)
assert not isNextTileTrap(TRAP, SAVE, TRAP)
assert not isNextTileTrap(SAVE, TRAP, SAVE)


def getTiles(row, index):
    leftTile = SAVE if index == 0 else row[index - 1]
    centerTile = row[index]
    rightTile = SAVE if index == len(row) - 1 else row[index + 1]
    return (leftTile, centerTile, rightTile)


assert getTiles("..^^.", 0) == (SAVE, SAVE, SAVE)
assert getTiles("..^^.", 1) == (SAVE, SAVE, TRAP)
assert getTiles("..^^.", 2) == (SAVE, TRAP, TRAP)
assert getTiles("..^^.", 4) == (TRAP, SAVE, SAVE)


def getNextRow(row):
    nextRow = []
    for i in range(len(row)):
        (leftTile, centerTile, rightTile) = getTiles(row, i)
        if isNextTileTrap(leftTile, centerTile, rightTile):
            nextRow.append(TRAP)
        else:
            nextRow.append(SAVE)
    return "".join(nextRow)


assert getNextRow("..^^.") == ".^^^^"
assert getNextRow(".^^^^") == "^^..^"

testRoom = [".^^.^.^^^^",
            "^^^...^..^",
            "^.^^.^.^^.",
            "..^^...^^^",
            ".^^^^.^^.^",
            "^^..^.^^..",
            "^^^^..^^^.",
            "^..^^^^.^^",
            ".^^^..^.^^",
            "^^.^^^..^^"]

for i in range(len(testRoom) - 1):
    row = testRoom[i]
    assert getNextRow(row) == testRoom[i + 1]


def countTiles(row, type):
    return row.count(type)


def countSaveTiles(row):
    return row.count(SAVE)


assert countSaveTiles(".^^.^.^^^^") == 3


def countSaveTilesInRoom(room):
    count = 0
    for row in room:
        count += countSaveTiles(row)
    return count


assert countSaveTilesInRoom(testRoom) == 38


def generateRoom(initialRow, size):
    room = [initialRow]
    currentRow = initialRow
    for i in range(size - 1):
        currentRow = getNextRow(currentRow)
        room.append(currentRow)
    return room


assert generateRoom(".^^.^.^^^^", 10) == testRoom


def main():
    initialRow = sys.stdin.readline().strip()
    size = 40

    room = generateRoom(initialRow, size)
    count = countSaveTilesInRoom(room)

    print("count save tiles", count)


if __name__ == '__main__':
    main()
