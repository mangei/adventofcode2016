# Advent Of Code 2016 - http://adventofcode.com/2016

# python 12_1.py < input_12.txt
# correct answer: 318083

# --- Day 12: Leonardo's Monorail ---
#
# You finally reach the top floor of this building: a garden with a slanted glass ceiling. Looks like there are no more stars to be had.
#
# While sitting on a nearby bench amidst some tiger lilies, you manage to decrypt some of the files you extracted from the servers downstairs.
#
# According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings in the nearby area. They're all connected by a local monorail, and there's another building not far from here! Unfortunately, being night, the monorail is currently not operating.
#
# You remotely connect to the monorail control systems and discover that the boot sequence expects a password. The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's assembunny code designed for the new computer you just assembled. You'll have to execute the code and get the password.
#
# The assembunny code you've extracted operates on four registers (a, b, c, and d) that start at 0 and can hold any integer. However, it seems to make use of only a few instructions:
#
# - cpy x y copies x (either an integer or the value of a register) into register y.
# - inc x increases the value of register x by one.
# - dec x decreases the value of register x by one.
# - jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
#
# The jnz instruction moves relative to itself: an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.
#
# For example:
#
# cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a
#
# The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past the last instruction, the program halts.
#
# After executing the assembunny code in your puzzle input, what value is left in register a?

import re
import sys

registers = {
    "a": 0,
    "b": 0,
    "c": 0,
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
