# Advent Of Code 2016 - http://adventofcode.com/2016

# python 14_1_2.py
# correct answer: 16106

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


def get_triplet(hash):
    hash_len = len(hash)
    for i in range(hash_len - 2):
        current_char = hash[i + 0]
        if hash[i + 1] == current_char and hash[i + 2] == current_char:
            return current_char
    return None


valid_keys = []
hashes = {}


def get_hash(index):
    if index not in hashes:
        hashes[index] = hashlib.md5(input_value + str(index).encode('utf-8')).hexdigest()
    return hashes[index]


def main():
    index = 0
    count = 0

    while count < 64:
        hash_value = get_hash(index)

        triplet = get_triplet(hash_value)
        if triplet is not None:
            fivelet = triplet * 5
            for i in range(1000):
                if fivelet in get_hash(index + i + 1):
                    valid_keys.append(index)
                    count += 1
                    break
        index += 1


main()

print("64th one-time pad key index", valid_keys[63])
