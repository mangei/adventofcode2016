# Advent Of Code 2016 - http://adventofcode.com/2016

# python 18_2.py < input_18.txt
# correct answer: 20003246

# --- Part Two ---
#
# How many safe tiles are there in a total of 400000 rows?

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


def countSaveTilesByInitalRowAndSize(initialRow, size):
    count = countSaveTiles(initialRow)
    currentRow = initialRow
    for i in range(size - 1):
        currentRow = getNextRow(currentRow)
        count += countSaveTiles(currentRow)
    return count


assert countSaveTilesByInitalRowAndSize(testRoom[0], 10) == 38


def main():
    initialRow = sys.stdin.readline().strip()
    size = 400000

    count = countSaveTilesByInitalRowAndSize(initialRow, size)

    print("count save tiles", count)


if __name__ == '__main__':
    main()
