# Advent Of Code 2016 - http://adventofcode.com/2016

# python 08_1.py
# correct answer: 110

# --- Day 8: Two-Factor Authentication ---
#
# You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.
#
# To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.
#
# Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.
#
# The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:
#
#  - rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
#  - rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
#  - rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
#
# For example, here is a simple sequence on a smaller screen:
#
# rect 3x2 creates a small rectangle in the top-left corner:
#
# ###....
# ###....
# .......
#
#  - rotate column x=1 by 1 rotates the second column down by one pixel:
#
# #.#....
# ###....
# .#.....
#
#  - rotate row y=0 by 4 rotates the top row right by four pixels:
#
# ....#.#
# ###....
# .#.....
#
#  - rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:
#
# .#..#.#
# #.#....
# .#.....
#
# As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.
#
# There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

import re


class Screen:
    display = None
    w = None
    height = None

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.display = []
        for i in range(h):
            row = []
            self.display.append(row)
            for j in range(w):
                row.append(".")

    def rect(self, w, h):
        for y in range(h):
            for x in range(w):
                self.display[y][x] = "#"

    def rotate_row_by(self, y, by):
        for i in range(by):
            self.rotate_row(y)

    def rotate_row(self, y):
        last = self.display[y][self.w - 1]
        for i in range(self.w - 2, -1, -1):
            self.display[y][i + 1] = self.display[y][i]
        self.display[y][0] = last

    def rotate_column_by(self, x, by):
        for i in range(by):
            self.rotate_column(x)

    def rotate_column(self, x):
        last = self.display[self.h - 1][x]
        for i in range(self.h - 2, -1, -1):
            self.display[i + 1][x] = self.display[i][x]
        self.display[0][x] = last

    def getLitLedCount(self):
        count = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.display[i][j] == "#":
                    count += 1
        return count

    def __str__(self):
        rows = []
        for y in range(self.h):
            rows.append("".join(self.display[y]) + "\n")
        return "".join(rows)


screen = Screen(50, 6)
print(screen)

with open("input_08.txt") as f:
    for command in f:
        print(command)
        if command.startswith("rect"):
            m = re.match("^rect (\d+)x(\d+)$", command)
            screen.rect(int(m.group(1)), int(m.group(2)))
        elif command.startswith("rotate row"):
            m = re.match("^rotate row y=(\d+) by (\d+)$", command)
            screen.rotate_row_by(int(m.group(1)), int(m.group(2)))
        elif command.startswith("rotate column"):
            m = re.match("^rotate column x=(\d+) by (\d+)$", command)
            screen.rotate_column_by(int(m.group(1)), int(m.group(2)))
        else:
            raise Exception("unknown command")

        print(screen)

print(screen)
print("LEDs", screen.getLitLedCount())
