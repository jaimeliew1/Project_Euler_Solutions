# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 114 - Counting block combinations I

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


cache = {}
def N(L):
    if L in cache.keys():
        return cache[L]
    else:
        cache[L] = _N(L)
        return cache[L]


def _N(L):
    if L < 3:
        return 1
    elif L == 3:
        return 2
    else:
        return 2 * N(L - 1) - N(L - 2) + N(L - 4)


def run():
    return N(50)


if __name__ == "__main__":
    print(run())
