# Advent Of Code 2016 - http://adventofcode.com/2016

# python 20_2.py
# correct answer: 117

# --- Part Two ---
#
# How many IPs are allowed by the blacklist?

import re
import sys

__author__ = "Manuel Geier (manuel@geier.io)"


class Firewall:
    def __init__(self):
        self.ranges = []
        self.MAX_IPS = 4294967296

    def addBlockedRange(self, newRange):
        self.ranges.append([newRange[0], newRange[1]])
        self.ranges = sorted(self.ranges)

        # merge ranges
        oldRanges = self.ranges[1:]
        currentRange = self.ranges[0]
        self.ranges = [currentRange]
        for range in oldRanges:
            if currentRange[1] >= range[0] - 1:
                # merge if overlap or stick together
                currentRange[0] = min(currentRange[0], range[0])
                currentRange[1] = max(currentRange[1], range[1])
            else:
                self.ranges.append(range)
                currentRange = range

    def getLowestNonBlockedIP(self):
        return self.ranges[0][1] + 1  # first range, high limit + 1

    def getMaxAllowedIPsCount(self):
        count = self.MAX_IPS
        for (low, high) in self.ranges:
            count -= (high - low) + 1  # +1 because inclusive range
        return count


def main():
    firewall = Firewall()
    for range_input in sys.stdin:
        m = re.match("^(\d+)-(\d+)", range_input)
        newRange = (int(m.group(1)), int(m.group(2)))
        firewall.addBlockedRange(newRange)

    print("lowest-valued IP", firewall.getLowestNonBlockedIP())
    print("allowed IP count", firewall.getMaxAllowedIPsCount())


if __name__ == '__main__':
    main()
