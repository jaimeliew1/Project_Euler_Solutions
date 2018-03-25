# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 10

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import primelist
def run():
    N = 2000000
    primes = primelist(N)
    return sum(primes)
    return -1


if __name__ == "__main__":
    print(run())
