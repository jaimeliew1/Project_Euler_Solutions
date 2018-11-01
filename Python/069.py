# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 69

Author: Jaime Liew
Date: May 2016
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import primelist

def run():
    n = 1000000
    primes = primelist(n)

    i, result = 0, 1
    while result*primes[i] < n:
        result *= primes[i]
        i+=1
    return result


if __name__ == "__main__":
    print(run())

