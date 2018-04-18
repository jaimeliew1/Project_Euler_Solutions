# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import primelist, is_prime, numDigits

def leftTrunc(x):
    for i in range(numDigits(x) - 1, 0, -1):
        x -= x//10**i*10**i
        yield x


def rightTrunc(x):
    for i in range(numDigits(x) - 1):
        x = (x - x%10)//10
        yield x


def run():
    primes = primelist(1000000)[4:]

    truncPrimes = []
    for p in primes:
        if all(is_prime(x) for x in leftTrunc(p)) and all(is_prime(x) for x in rightTrunc(p)):
            truncPrimes.append(p)

        if len(truncPrimes) == 11:
            break

    return sum(truncPrimes)


if __name__ == "__main__":






    print(run())

