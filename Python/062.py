# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from collections import Counter

def ordDigs(x):
    # sorts the digits of x from lowest to highest, and returns as string
    return ''.join(sorted(str(x)))



def run():
    count = Counter()
    lim = 10000

    # finds set of digits for which 5 cube numbers share
    for i in range(1, lim):
        ordered_i = ordDigs(i**3)
        count[ordered_i] += 1
        if count[ordered_i] == 5:
            magicString = ordered_i
            break

    # researches all cubes to find those cubes. This could be optimised
    cubes = []
    for i in range(1, lim):
        if ordDigs(i**3) == magicString:
            cubes.append(i**3)

    return min(cubes)


if __name__ == "__main__":
    print(run())

