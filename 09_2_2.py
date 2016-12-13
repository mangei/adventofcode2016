# Advent Of Code 2016 - http://adventofcode.com/2016

# python 09_2_2.py
# correct answer: 10755693147

# --- Part Two ---
#
# Apparently, the file actually uses version two of the format.
#
# In version two, the only difference is that markers within decompressed data are decompressed. This, the documentation explains, provides much more substantial compression capabilities, allowing many-gigabyte files to be stored in only a few kilobytes.
#
# For example:
#
#  - (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
#  - X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
#  - (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
#  - (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
#
# Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file; you'll have to come up with another way to get its decompressed length.
#
# What is the decompressed length of the file using this improved format?


import re


def get_elements(element):
    (repeat, _, string, _) = element
    data_sizes = []
    pos = 0
    marker = []
    within_marker = False
    data = []

    while pos < len(string):
        if string[pos] == "(":
            within_marker = True
            pos += 1

            if len(data) > 0:
                data_sizes.append((1, True, len(data), data))
                data = []
        elif string[pos] == ")":
            within_marker = False
            pos += 1

            m = re.match("^(\d+)x(\d+)$", "".join(marker))
            data_size = int(m.group(1))
            repeat_count = int(m.group(2))

            data_sizes.append((repeat_count, False, string[pos:pos + data_size], ""))

            pos += data_size
            marker = []
        else:
            if within_marker:
                marker.append(string[pos])
            else:
                data.append(string[pos])
            pos += 1

    if len(data) > 0:
        data_sizes.append((1, True, len(data), data))

    return data_sizes


def resolve_element(element):
    (repeat, isData, string, plain_data) = element
    childs = get_elements(element)
    resolved_childs = []
    for child in childs:
        (_, isData, _, _) = child
        if isData:
            resolved_childs.append(child)
        else:
            resolved_childs.append(resolve_element(child))
    return (repeat, isData, resolved_childs, plain_data)


def calculate_decompressed_length(element):
    (repeat, isData, childs, _) = element
    if isinstance(childs, list):
        decompressed_length = 0
        for child in childs:
            decompressed_length += repeat * calculate_decompressed_length(child)
        return decompressed_length
    else:
        return childs


def print_tree(element, depth=0):
    (repeat, isData, childs, plain_data) = element
    intend = "  " * depth
    if isinstance(childs, list):
        print(intend + "+ " + str(repeat) + "x")
        for child in childs:
            print_tree(child, depth + 1)
    else:
        print(intend + "+ " + str(childs) + " " + "".join(plain_data))


new_data = None

with open("input_09.txt") as f:
    for line in f:
        new_data = resolve_element((1, False, line.strip(), ""))
        print_tree(new_data)
        decompressed_length = calculate_decompressed_length(new_data)
        print("decompressed length", decompressed_length)
