# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 116 - Red, green or blue tiles

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


cache = {}


def N(m, L):
    if (m, L) in cache.keys():
        return cache[(m, L)]
    else:
        cache[(m, L)] = _N(m, L)
        return cache[(m, L)]


def _N(m, L):
    if L < m:
        return 1
    else:
        return N(m, L - 1) + N(m, L - m)


def run():
    return N(2, 50) + N(3, 50) + N(4, 50) - 3


if __name__ == "__main__":
    print(run())
