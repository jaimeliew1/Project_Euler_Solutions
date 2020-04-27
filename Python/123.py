# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 123 - Prime square remainders

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

consider (p + 1)^n mod p^2
therefore (p + 1)^n = k*p^2 + r,
for some integer k and remainder r < p^2.

Expanding the LHS binomially, we find all powers of p higher than p^2 are
absorbed in the k*p^2 term. Therefore (try it by hand)

r = n*p + 1

similarly, for (p - 1)^n mod p^2,
r = n*p - 1  (when n is odd)
r = 1 - n*p  (when n is even)

Therefore (p + 1)^n + (p - 1)^n mod p^2 has a remainder of:

r = 2*n*p   (n is odd)
r = 2   (n is even)

so find first r = 2*n*p where r > 10^10
"""

from EulerFunctions import primelist


def run():
    thres = int(10 ** 10)
    for _n, p in enumerate(primelist(1000000)):
        n = _n + 1
        if n % 2 == 0:
            continue
        elif 2 * n * p > thres:
            return n


if __name__ == "__main__":
    print(run())
