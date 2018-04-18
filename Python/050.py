# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import primelist, is_prime


def run():
    primes = primelist(1000000)
    cumPrimes = [0]
    for p in (x for x in primes if x < 1000000):
        cumPrimes.append(p + cumPrimes[-1])

    longestPrimeChain = [0,[],0]
    for i, p in enumerate(x for x in cumPrimes[::-1] if x < 1000000):
        for k,q in enumerate(x for x in cumPrimes[::-1][longestPrimeChain[0]+1::] if x < p):

            if is_prime(p - q):
                if k+1 > longestPrimeChain[0]:
                    longestPrimeChain = [k + 1, primes[i-k-1:len(cumPrimes) - i], p - q]

    return longestPrimeChain[2]


if __name__ == "__main__":
    print(run())

