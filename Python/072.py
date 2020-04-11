# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 72 - Counting fractions

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import time
from EulerFunctions import is_prime


def totient(N):
    # returns list of totient function values for n in  2 < n < N
    tots = list(range(N))
    tots[1] = 0
    for i, tot in enumerate(tots):
        if i == 0:
            continue
        if i == tot:  # if i is prime
            for n in range(i, N, i):
                tots[n] *= i - 1
                tots[n] //= i
    tots[1] = 1
    return tots[1:]


def run():
    N = 1000000
    tots = totient(N + 1)
    return sum(tots) - 1


if __name__ == "__main__":
    print(run())
