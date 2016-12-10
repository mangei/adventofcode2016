# advent of code
# 2016, 07, 1

# python 07_1.py
# correct answer: 115

# --- Day 7: Internet Protocol Version 7 ---
#
# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).
#
# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.
#
# For example:
#
# - abba[mnop]qrst supports TLS (abba outside square brackets).
# - abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
# - aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
# - ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
#
# How many IPs in your puzzle input support TLS?

import re


def is_abba(string):
    for i in range(len(string) - 3):
        if string[i] != string[i + 1] and string[i] == string[i + 3] and string[i + 1] == string[i + 2]:
            return True
    return False


count = 0

with open("input_07.txt") as f:
    for line in f:
        groups = re.split("[\[\]]", line)
        valid = True
        should_contain = True
        contained_abba = False
        for group in groups:
            if should_contain and is_abba(group):
                contained_abba = True
            elif not should_contain and is_abba(group):
                valid = False
                break
            should_contain = not should_contain
        if valid and contained_abba:
            count += 1

print("Count", count)
