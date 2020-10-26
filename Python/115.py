# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 115 - Counting block combinations II

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
    elif L == m:
        return 2
    else:
        return 2 * N(m, L - 1) - N(m, L - 2) + N(m, L - m - 1)


def run():
    m = 50
    L = 1
    while N(m, L) < 1000000:
        L += 1
    return L


if __name__ == "__main__":
    print(run())
