# Advent Of Code 2016 - http://adventofcode.com/2016

# python 14_1.py
# correct answer:
# wrong: 133969, 133060, 17357

# THIS CODE IS NOT CORRECT!!! use 14_1_2.py

# --- Day 14: One-Time Pad ---
#
# In order to communicate securely with Santa while you're on this mission, you've been using a one-time pad that you generate using a pre-agreed algorithm. Unfortunately, you've run out of keys in your one-time pad, and so you need to generate some more.
#
# To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) and an increasing integer index (starting with 0, and represented in decimal); the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.
#
# However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:
#
#  - It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
#  - One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
#
# Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.
#
# For example, if the pre-arranged salt is abc:
#
#  - The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
#  - The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
#  - None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999.
#  - Eventually, index 22728 meets all of the criteria to generate the 64th key.
#
# So, using our example salt of abc, index 22728 produces the 64th key.
#
# Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?
#
# Your puzzle input is zpqevtbw.


import hashlib

__author__ = "Manuel Geier (manuel@geier.io)"

input_value = "zpqevtbw".encode('utf-8')


# input_value = "abc".encode('utf-8')


def analyse_hash(hash, index, char3):
    found_3chars = []
    found_5chars = []
    hash_len = len(hash)
    for i in range(hash_len - 2):
        current_char = hash[i + 0]
        if hash[i + 1] == current_char and hash[i + 2] == current_char:

            is_triplet = True
            if i > 0 and hash[i - 1] == current_char:
                is_triplet = False
            if i < hash_len - 3 and hash[i + 3] == current_char:
                is_triplet = False

            if is_triplet and current_char not in found_3chars:
                found_3chars.append(current_char)

            if i < hash_len - 4 and hash[i + 3] == current_char and hash[i + 4] == current_char:

                is_fivelet = True
                if i > 0 and hash[i - 1] == current_char:
                    is_fivelet = False
                if i < hash_len - 5 and hash[i + 5] == current_char:
                    is_fivelet = False

                if is_fivelet and current_char not in found_5chars:
                    found_5chars.append(current_char)

    # remember index for first 3 chars
    if len(found_3chars) > 0:
        char3[found_3chars[0]].append(index)

    return found_5chars


class ResultException(Exception):
    def __init__(self, result):
        self.result = result


valid_keys = []


def main():
    hashes = []
    char3 = {}
    index = 0
    finishIndex = None

    count = 0

    for i in "0123456789abcdef":
        char3[i] = []

    while finishIndex is None or index <= finishIndex:
        hash_value = hashlib.md5(input_value + str(index).encode('utf-8')).hexdigest()
        hashes.append(hash_value)

        found_5chars = analyse_hash(hash_value, index, char3)

        if len(found_5chars) > 0:
            # print(index, hash_value)
            print(found_5chars, index)
            for char5_entry in found_5chars:
                char3_indices = char3[char5_entry]
                valid_indices = []
                for char3_index in char3_indices:
                    if char3_index >= index - 1000:
                        valid_indices.append(char3_index)
                print(valid_indices)
                for valid_index in valid_indices:
                    count += 1
                    valid_keys.append(valid_index)

        index += 1

        if count >= 64 and finishIndex is None:
            finishIndex = index + 1000


def run_tests():
    c3 = {"a": []}
    c5 = analyse_hash("asdfasdf", 42, c3)
    assert len(c5) == 0
    assert len(c3["a"]) == 0

    c3 = {"a": []}
    c5 = analyse_hash("a", 42, c3)
    assert len(c5) == 0
    assert len(c3["a"]) == 0

    c3 = {"a": []}
    c5 = analyse_hash("aa", 42, c3)
    assert len(c5) == 0
    assert len(c3["a"]) == 0

    c3 = {"a": []}
    c5 = analyse_hash("aaa", 42, c3)
    assert len(c5) == 0
    assert len(c3["a"]) == 1
    assert c3["a"] == [42]

    c3 = {"a": []}
    c5 = analyse_hash("aaaa", 0, c3)
    assert len(c5) == 0
    assert len(c3["a"]) == 0

    c3 = {"a": []}
    c5 = analyse_hash("aaaaa", 42, c3)
    assert len(c5) == 1
    assert c5 == ["a"]
    assert len(c3["a"]) == 0

    c3 = {"a": []}
    c5 = analyse_hash("aaaaaa", 42, c3)
    assert len(c5) == 0
    assert len(c3["a"]) == 0

    c3 = {"a": []}
    c5 = analyse_hash("asdfaaaxyz", 42, c3)
    assert len(c5) == 0
    assert len(c3["a"]) == 1
    assert c3["a"] == [42]

    c3 = {"a": [], "b": []}
    c5 = analyse_hash("asdfaaaxyzbbbwidk", 42, c3)
    assert len(c5) == 0
    assert len(c3["a"]) == 1
    assert c3["a"] == [42]
    assert len(c3["b"]) == 0

    c3 = {}
    c5 = analyse_hash("asdfasdf", 42, c3)
    assert len(c5) == 0
    assert len(c3) == 0


run_tests()

try:
    main()
except ResultException as e:
    print("index", e.result)

valid_keys = sorted(valid_keys)

if len(valid_keys) >= 64:
    print(valid_keys[63])
print(valid_keys)
print(len(valid_keys))
