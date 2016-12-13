# Advent Of Code 2016 - http://adventofcode.com/2016

# python 09_2_1.py
# this version is not memory efficient

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

decompressed_length = 0

with open("input_09.txt") as f:
    for line in f:
        new_data = line
        line = []

        while len(new_data) != len(line):
            line = new_data
            new_data = []
            pos = 0
            marker = []
            within_marker = False

            while pos < len(line):
                if line[pos] == "(":
                    within_marker = True
                    pos += 1
                elif line[pos] == ")":
                    within_marker = False
                    pos += 1

                    m = re.match("^(\d+)x(\d+)$", "".join(marker))
                    data_size = int(m.group(1))
                    repeat_count = int(m.group(2))

                    repeat_data = line[pos:(pos + data_size)]
                    for i in range(repeat_count):
                        new_data.append(repeat_data)

                    pos += data_size
                    marker = []
                else:
                    if within_marker:
                        marker.append(line[pos])
                    else:
                        new_data.append(line[pos])
                    pos += 1

            new_data = "".join(new_data).strip()

            #print(new_data)

        decompressed_length += len(new_data)

print("decompressed length", decompressed_length)