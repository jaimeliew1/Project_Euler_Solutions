# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import numDigits


def seqGen():
    num = 3
    den = 2
    yield num, den
    while True:
        num, den = num + 2*den, den + num
        yield num, den


def run():
    count = 0
    for i, (num, den) in enumerate(seqGen()):
        if i == 1000:
            return count

        if numDigits(num) > numDigits(den):
            count += 1


if __name__ == "__main__":
    print(run())

