# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 35

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import is_prime, primelist, numDigits


def CircPerms(x):
    perms = [str(x)]
    for j in range(numDigits(x) - 1):
        perms.append(perms[-1][1:] + perms[-1][0])

    return [int(i) for i in perms]

def run():
    N = 1000000
    primes = primelist(N)

    circPrimes = []
    for i in primes:
        if all(is_prime(x) for x in CircPerms(i)):
            circPrimes.append(i)

    return len(circPrimes)

if __name__ == '__main__':
    print(run())


