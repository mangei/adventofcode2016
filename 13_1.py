# Advent Of Code 2016 - http://adventofcode.com/2016

# python 13_1.py
# correct answer: 86

# --- Day 13: A Maze of Twisty Little Cubicles ---
#
# You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.
#
# Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward positive x and y; negative values are invalid, as they represent a location outside the building. You are in a small waiting area at 1,1.
#
# While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:
#
#  - Find x*x + 3*x + 2*x*y + y + y*y.
#  - Add the office designer's favorite number (your puzzle input).
#  - Find the binary representation of that sum; count the number of bits that are 1.
#     - If the number of bits that are 1 is even, it's an open space.
#     - If the number of bits that are 1 is odd, it's a wall.
#
# For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as ., the corner of the building containing 0,0 would look like this:
#
#   0123456789
# 0 .#.####.##
# 1 ..#..#...#
# 2 #....##...
# 3 ###.#.###.
# 4 .##..#..#.
# 5 ..##....#.
# 6 #...##.###
#
# Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:
#
#   0123456789
# 0 .#.####.##
# 1 .O#..#...#
# 2 #OOO.##...
# 3 ###O#.###.
# 4 .##OO#OO#.
# 5 ..##OOO.#.
# 6 #...##.###
#
# Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).
#
# What is the fewest number of steps required for you to reach 31,39?
#
# Your puzzle input is 1364.

import os
from queue import PriorityQueue
from time import sleep

__author__ = "Manuel Geier (manuel@geier.io)"

input_value = 1364


class Position:
    def __init__(self, coordinate, steps, distance, previousPosition):
        self.coordinate = coordinate
        self.steps = steps
        self.distance = distance
        self.previousPosition = previousPosition

    def __lt__(self, other):
        return self.steps < other.steps


start_coordinate = (1, 1)
target_coordinate = (31, 39)
max_coordinate = 50
grid = []

visited_coordinates = {}  # (x, y) | Position
search_queue = PriorityQueue()


def is_wall(coordinate):
    (x, y) = coordinate
    value = x * x + 3 * x + 2 * x * y + y + y * y
    value += input_value
    binary = "{0:b}".format(value)
    sum = 0
    for b in binary:
        if b == "1":
            sum += 1
    return sum % 2 != 0


def print_grid():
    s = []
    for line in grid:
        s.append("".join(line) + "\x1b[0m\n")
    os.system('clear')
    print("".join(s)

          # colors :D
          .replace("#", "\x1b[0;30;43m ")
          .replace(".", "\x1b[0m ")
          .replace("x", "\x1b[0;36;42m ")
          .replace("G", "\x1b[0;33;41m ")
          + "\x1b[0m")


def mark_grid(coordinate, c):
    x = coordinate[0]
    y = coordinate[1]
    if x < max_coordinate and y < max_coordinate:
        grid[y][x] = c


def generate_grid():
    for y in range(max_coordinate):
        line = []
        grid.append(line)
        for x in range(max_coordinate):
            if is_wall((x, y)):
                line.append("#")
            else:
                line.append(".")


def get_distance_to_target(pos):
    return abs(target_coordinate[0] - pos[0]) + abs(target_coordinate[1] - pos[1])
    pass


def add_next_coordinates(current_position):
    (x, y) = current_position.coordinate
    add_valid_position_to_queue((x + 1, y), current_position)
    add_valid_position_to_queue((x - 1, y), current_position)
    add_valid_position_to_queue((x, y + 1), current_position)
    add_valid_position_to_queue((x, y - 1), current_position)


class FinalException(Exception):
    pass


def add_valid_position_to_queue(coordinate, previous_position):
    # check for target
    if coordinate == target_coordinate:
        raise FinalException("steps", previous_position.steps + 1)

    distance = get_distance_to_target(coordinate)
    if coordinate in visited_coordinates:
        pass
        # TODO update previous position if steps are lesser
    else:
        next_position = Position(coordinate, previous_position.steps + 1, distance, previous_position)
        visited_coordinates[coordinate] = next_position
        if is_valid(coordinate) and not is_wall(coordinate):
            mark_grid(coordinate, "x")
            search_queue.put((distance, next_position))


def is_valid(pos):
    return pos[0] >= 0 and pos[1] >= 0


def search():
    while not search_queue.empty():
        next_entry = search_queue.get()
        next_position = next_entry[1]
        add_next_coordinates(next_position)

        # animation :)
        print_grid()
        sleep(0.05)


generate_grid()
mark_grid(start_coordinate, "S")
mark_grid(target_coordinate, "G")
print_grid()
search_queue.put((0, Position(start_coordinate, 0, 0, None)))
search()
