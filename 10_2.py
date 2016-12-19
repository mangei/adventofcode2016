# Advent Of Code 2016 - http://adventofcode.com/2016

# python 10_2.py
# correct answer: 12567

# --- Part Two ---
#
# What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?

import re
import sys


class Bot:
    def __init__(self, id):
        self.id = id
        self.values = []
        self.lowTo = None
        self.lowToType = None
        self.highTo = None
        self.highToType = None

    def isReady(self):
        return len(self.values) == 2 \
               and self.lowTo is not None \
               and self.highTo is not None


bots = {}
outputs = {}


def getBot(id):
    if id not in bots:
        bots[id] = Bot(id)
    return bots[id]


def processBot(id, value):
    bot = getBot(id)
    if len(bot.values) == 2:
        raise Exception("bot has already two values")
    bot.values.append(value)


def processOutput(id, value):
    if id in outputs:
        raise Exception("output already exists")
    outputs[id] = value


def processBots():
    couldProcess = True
    while couldProcess:
        couldProcess = False
        for bot in bots.values():
            if bot.isReady():
                couldProcess = True

                lowValue = min(bot.values)
                highValue = max(bot.values)

                if bot.lowToType == "bot":
                    processBot(bot.lowTo, lowValue)
                elif bot.lowToType == "output":
                    processOutput(bot.lowTo, lowValue)

                if bot.highToType == "bot":
                    processBot(bot.highTo, highValue)
                elif bot.highToType == "output":
                    processOutput(bot.highTo, highValue)

                bot.values.clear()
                break


for line in sys.stdin:
    if line.startswith("value"):
        m = re.match("^value (\d+) goes to bot (\d+)$", line)
        bot = getBot(int(m.group(2)))
        bot.values.append(int(m.group(1)))
    elif line.startswith("bot"):
        m = re.match("^bot (\d+) gives low to (.+) (\d+) and high to (.+) (\d+)$", line)
        bot = getBot(int(m.group(1)))
        bot.lowToType = m.group(2)
        bot.lowTo = int(m.group(3))
        bot.highToType = m.group(4)
        bot.highTo = int(m.group(5))
    processBots()

print("result", outputs[0] * outputs[1] * outputs[2])
