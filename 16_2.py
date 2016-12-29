# Advent Of Code 2016 - http://adventofcode.com/2016

# python 16_2.py
# correct answer: 01100111101101111

# --- Part Two ---
#
# The second disk you have to fill has length 35651584. Again using the initial state in your puzzle input, what is the correct checksum for this disk?
#
# Your puzzle input is still 10001110011110000.

__author__ = "Manuel Geier (manuel@geier.io)"

puzzle_input = "10001110011110000"
disc_size = 35651584


def expand_data(data):
    return data + "0" + flip(data[::-1])


def flip(data):
    return data.replace("1", "2").replace("0", "1").replace("2", "0")


assert expand_data("1") == "100"
assert expand_data("0") == "001"
assert expand_data("11111") == "11111000000"
assert expand_data("111100001010") == "1111000010100101011110000"


def get_pair_code(data):
    code = []
    i = 0
    while i < len(data) - 1:
        if data[i] == data[i + 1]:
            code.append("1")
        else:
            code.append("0")
        i += 2
    return "".join(code)


assert get_pair_code("110010110100") == "110101"
assert get_pair_code("110101") == "100"


def get_checksum(data):
    checksum = get_pair_code(data)
    while len(checksum) % 2 == 0:
        checksum = get_pair_code(checksum)
    return checksum


assert get_checksum("110010110100") == "100"


def generate_min_data(initialData, minimum):
    data = initialData
    while len(data) < minimum:
        data = expand_data(data)
    return data


assert generate_min_data("10000", 20) == "10000011110010000111110"


def generate_data(initialData, size):
    return generate_min_data(initialData, size)[:size]


assert generate_data("10000", 20) == "10000011110010000111"

data = generate_data(puzzle_input, disc_size)
checksum = get_checksum(data)
print("checksum", checksum)
