# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 112 - Bouncy numbers

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def isIncreasing(n):

    for i, digit in enumerate(str(n)):
        if i == 0:
            lastDig = digit
            continue
        if digit >= lastDig:
            lastDig = digit
        else:
            return False
    return True


def isDecreasing(n):

    for i, digit in enumerate(str(n)):
        if i == 0:
            lastDig = digit
            continue
        if digit <= lastDig:
            lastDig = digit
        else:
            return False
    return True


def isBouncy(n):
    if not isIncreasing(n) and not isDecreasing(n):
        return True
    return False


def run(N=99):
    bouncyCount = 0
    n = 100
    while bouncyCount * 100 < N * n:
        if isBouncy(n):
            bouncyCount += 1
        n += 1
    return n - 100


if __name__ == "__main__":
    print(run())
