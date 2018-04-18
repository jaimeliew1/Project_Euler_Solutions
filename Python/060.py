# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import is_prime, primelist

primes = primelist(10000)


def checkforAppendablePrimes(thisSet, depth, maxDepth): #recursive function checking appendable primality
    for q in (q for q in primes if q > thisSet[-1]):
        qIsCandidate = True
        for x in thisSet:
            if not(is_prime(int(str(x)+str(q))) and is_prime(int(str(q)+str(x)))):
                qIsCandidate = False

        if qIsCandidate:
            if depth == maxDepth - 1:
                return thisSet + [q]
            furtherTesting = checkforAppendablePrimes(thisSet + [q], depth+1, maxDepth)
            if furtherTesting != [0]:
                return furtherTesting
    return [0]



def run():
    for p in primes:
        primeSet = checkforAppendablePrimes([p], 1, 5)
        if primeSet != [0]:
            break

    return sum(primeSet)


if __name__ == "__main__":
    print(run())

