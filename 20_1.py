# Advent Of Code 2016 - http://adventofcode.com/2016

# python 20_1.py < input_20.txt
# correct answer: 31053880

# --- Day 20: Firewall Rules ---
#
# You'd like to set up a small hidden computer here so you can use it to get back into the network later. However, the corporate firewall only allows communication with certain external IP addresses.
#
# You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in dot-decimal notation, they are written as plain 32-bit integers, which can have any value from 0 through 4294967295, inclusive.
#
# For example, suppose only the values 0 through 9 were valid, and that you retrieved the following blacklist:
#
# 5-8
# 0-2
# 4-7
# The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are not allowed. Then, the only IPs that this firewall allows are 3 and 9, since those are the only numbers not in any range.
#
# Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?


import re
import sys

__author__ = "Manuel Geier (manuel@geier.io)"


class Firewall:
    def __init__(self):
        self.ranges = []
        self.lowestNonBlockedIP = 0

    def addBlockedRange(self, newRange):
        self.ranges.append(newRange)

        # optimization: remove all ranges which are below ip

        updated = True
        while updated:
            updated = False

            oldRanges = self.ranges
            self.ranges = []

            for range in oldRanges:
                (low, high) = range
                if low <= self.lowestNonBlockedIP <= high:
                    # lowest ip is in range. hence update lowest ip and remove range (don't add range)
                    self.lowestNonBlockedIP = high + 1
                    updated = True
                elif self.lowestNonBlockedIP <= low:
                    # keep range
                    self.ranges.append(range)
                else:
                    # range removed, since it is below ip
                    updated = True

    def getLowestNonBlockedIP(self):
        return self.lowestNonBlockedIP


def main():
    firewall = Firewall()
    for range_input in sys.stdin:
        m = re.match("^(\d+)-(\d+)", range_input)
        newRange = (int(m.group(1)), int(m.group(2)))
        firewall.addBlockedRange(newRange)

    print("lowest-valued IP", firewall.getLowestNonBlockedIP())


if __name__ == '__main__':
    main()
