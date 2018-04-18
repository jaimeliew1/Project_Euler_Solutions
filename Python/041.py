# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import is_prime
import itertools


def run():
    for i in range(10, 2, -1):
        panlist = []
        digits = list(x for x in range(1, i))
        perms = list(itertools.permutations(digits))
        for p in perms:
            temp = int(''.join(map(str, p)))
            if all([temp%2, temp%3]):
                panlist.append(temp)
        panlist = list(reversed(sorted(panlist)))
        for num in panlist:
            if is_prime(num):
                return num

    return -1


if __name__ == "__main__":
    print(run())

