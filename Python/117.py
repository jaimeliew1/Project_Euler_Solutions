# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 117 - Red, green and blue tiles

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


cache = {0: 1, 1: 1, 2: 2, 3: 4}


def N(L):
    if L in cache.keys():
        return cache[L]
    else:
        cache[L] = _N(L)
        return cache[L]


def _N(L):

    return N(L - 1) + N(L - 2) + N(L - 3) + N(L - 4)


def run():
    return N(50)


if __name__ == "__main__":
    print(run())
