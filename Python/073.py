# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 73 - Counting fractions in a range

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from math import gcd


def run():

    N = 12000
    count = 0
    for d in range(2, N + 1):
        for n in range(d // 3 + 1, d // 2 + 1):
            if d == 2:
                continue
            if gcd(n, d) == 1:
                count += 1

    return count


if __name__ == "__main__":
    print(run())
