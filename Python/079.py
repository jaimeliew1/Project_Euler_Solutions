# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 79 - Passcode derivation

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import itertools

def run():

    with open("Data/p079_keylog.txt") as f:
        data = f.readlines()
    data = [str(int(x)) for x in data]

    usedDigits = list(set("".join(data)))

    for perm in itertools.permutations(usedDigits):
        okay = True
        for d in data:
            i = 0
            for digit in d:
                if perm[i:].count(digit) > 0:
                    i = perm.index(digit) + 1
                else:
                    okay = False
                    continue
            if not okay:
                break
        else:
            return "".join(perm)


if __name__ == "__main__":
    print(run())
