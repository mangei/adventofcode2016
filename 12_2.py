# Advent Of Code 2016 - http://adventofcode.com/2016

# python 12_2.py < input_12.txt
# correct answer: 9227737

# --- Part Two ---
#
# As you head down the fire escape to the monorail, you notice it didn't start; register c needs to be initialized to the position of the ignition key.
#
# If you instead initialize register c to be 1, what value is now left in register a?

import re
import sys

registers = {
    "a": 0,
    "b": 0,
    "c": 1,
    "d": 0
}
instructions = []
instruction_pointer = 0

# read instructions
for instruction in sys.stdin:
    instructions.append(instruction)

# perform instructions
while instruction_pointer < len(instructions):
    # print(registers)
    next_instruction = instructions[instruction_pointer]
    if next_instruction.startswith("inc"):
        m = re.match("^inc (.+)$", next_instruction)
        register = m.group(1)
        registers[register] += 1
        instruction_pointer += 1
    elif next_instruction.startswith("dec"):
        m = re.match("^dec (.+)$", next_instruction)
        register = m.group(1)
        registers[register] -= 1
        instruction_pointer += 1
    elif next_instruction.startswith("cpy"):
        m = re.match("^cpy (.+) (.+)$", next_instruction)
        value = m.group(1)
        target_register = m.group(2)
        try:
            value = int(value)
        except ValueError:
            value = registers[value]
        registers[target_register] = value
        instruction_pointer += 1
    elif next_instruction.startswith("jnz"):
        m = re.match("^jnz (.+) (.+)$", next_instruction)
        condition = m.group(1)
        try:
            condition = int(condition)
        except ValueError:
            condition = registers[condition]
        value = int(m.group(2))
        if condition != 0:
            instruction_pointer += value
        else:
            instruction_pointer += 1
    else:
        raise Exception("Unknown instruction: " + next_instruction)

# print result
print("register a", registers["a"])
