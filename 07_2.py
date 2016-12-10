# advent of code
# 2016, 07, 2

# python 07_2.py
# correct answer: 231

# --- Part Two ---
#
# You would also like to know which IPs support SSL (super-secret listening).
#
# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.
#
# For example:
#
#  - aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
#  - xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
#  - aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
#  - zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
#
# How many IPs in your puzzle input support SSL?

import re


def get_abas(string):
    abas = []
    for i in range(len(string) - 2):
        if string[i] != string[i + 1] and string[i] == string[i + 2]:
            abas.append(string[i] + string[i + 1] + string[i + 2])
    return abas


def reverse_aba(string):
    return string[1] + string[0] + string[1]


count = 0

with open("input_07.txt") as f:
    for line in f:
        groups = re.split("[\[\]]", line)

        supernet_sequences = []
        hypernet_sequences = []
        aba_list = []
        bab_list = []

        is_supernet = True
        for group in groups:
            abas = get_abas(group)
            if is_supernet:
                supernet_sequences.append(group)
                aba_list.extend(abas)
            else:
                hypernet_sequences.append(group)
                bab_list.extend(abas)
            is_supernet = not is_supernet

        aba_to_bab_list = list(map(reverse_aba, aba_list))
        # print()
        # print(bab_list)
        # print(aba_to_bab_list)

        aba_bab_intersect = [val for val in aba_to_bab_list if val in bab_list]
        # print(aba_bab_intersect)

        if len(aba_bab_intersect) > 0:
            count += 1

print("Count", count)
