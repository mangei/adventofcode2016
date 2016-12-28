# Advent Of Code 2016 - http://adventofcode.com/2016

# python 13_2.py
# correct answer: 127

# --- Part Two ---
#
# How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?

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

max_steps = 50
reachable_count = 1

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
    global reachable_count

    if coordinate in visited_coordinates:
        pass
    else:
        new_steps = previous_position.steps + 1
        distance = get_distance_to_target(coordinate)
        next_position = Position(coordinate, new_steps, distance, previous_position)
        visited_coordinates[coordinate] = next_position
        if is_valid(coordinate) and not is_wall(coordinate) and new_steps < max_steps:
            reachable_count += 1
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

print("reachable_count", reachable_count)
