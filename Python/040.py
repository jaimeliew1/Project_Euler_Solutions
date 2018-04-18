# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import numDigits



def run():
    des = [1, 10, 100, 1000, 10000, 100000, 1000000]

    c = 0
    d = []
    currentD = 0
    for i in range(1, 1000000):

        if c < des[currentD] <= c + numDigits(i):
            d.append(int(str(i)[des[currentD] - c - 1]))
            currentD += 1
            if currentD >= 7:
                break
        c += numDigits(i)

    prod = 1
    for i in d:
        prod *= i

    return prod


if __name__ == "__main__":
    print(run())

