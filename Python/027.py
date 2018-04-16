# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 27

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import primelist



limit = 100000
Range = 1000



def run():
    primes = primelist(limit)
    aMax, bMax, nMax = 0, 0, 0

    for a in range(-Range, Range):
        # b must be prime for the case n=0
        for b in (b_ for b_ in primes if b_ < Range):
            f = lambda x: x**2 + a*x + b

            n = 0
            while f(n) in primes:
                n += 1

            if n > nMax:
                aMax, bMax, nMax = a, b, n

    return aMax*bMax


if __name__ == "__main__":



    print(run())

