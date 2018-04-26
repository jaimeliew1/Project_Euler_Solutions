# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
'''
Let s(n) be the smallest number m such that n divides m!


Kempner function https://en.wikipedia.org/wiki/Kempner_function

Lemma 1:
the prime decomposition of n is:
n = p1^e1*p2^e2*...pi^ei
where pi is the ith prime factor of n, and ei is the exponent of pi.
Therefore s(n) = max(s(p1^e1), s(p2^e2), ..., s(pi^ei))

Lemma 2:
if n is prime, then s(n) = n.

'''

from collections import Counter
from math import factorial






def naive(n):
    # calculates s(n) using the naive approach
    m = 2
    while factorial(m) % n != 0:
        m += 1
    return m



def run():
    N = 10**8
    # modified sieve of eratosthenes which accumulates a list of S(n).
    S = [0] * (N+1)
    for i, s in enumerate(S):
        if i < 2:
            continue
        if s == 0: # i must be prime
            exp = 1

            while i**exp < N:
                if exp == 1:
                    # lemma 2. if n is prime, s(n) = n
                    S[i] = i
                else:
                    # lemma 1. kind of. find s(p^e) manually.
                    # answer must be multiple of i
                    m = i
                    while factorial(m) % i**exp != 0:
                        m += i
                    S[i**exp] = m

                # loop over all multiples of i**exp.
                # I don't have a lemma for this.
                for k in range(i**exp*2, N+1, i**exp):
                    S[k] = max(S[k], S[i**exp])

                exp += 1

    return sum(S)




if __name__ == "__main__":
    print(run())

