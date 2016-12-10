# Advent Of Code 2016 - http://adventofcode.com/2016

# python 08_1.py
# correct answer: ZJHRKCPLYJ

# ####...##.#..#.###..#..#..##..###..#....#...#..##.
# ...#....#.#..#.#..#.#.#..#..#.#..#.#....#...#...#.
# ..#.....#.####.#..#.##...#....#..#.#.....#.#....#.
# .#......#.#..#.###..#.#..#....###..#......#.....#.
# #....#..#.#..#.#.#..#.#..#..#.#....#......#..#..#.
# ####..##..#..#.#..#.#..#..##..#....####...#...##..

# --- Part Two ---
#
# You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.
#
# After you swipe your card, what code is the screen trying to display?

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
