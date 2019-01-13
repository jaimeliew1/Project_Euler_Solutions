# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 110

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import primelist
from collections import Counter
from math import sqrt, ceil


N_max = int(5e8)
primes = primelist(N_max)

def product(lst):
    out = 1
    for x in lst:
        out *= x
    return out


def primeFactor(n):
    primefactors = Counter()
    while n > 1:
        for p in primes:
            if n%p == 0:
                n = n//p
                primefactors[p] += 1
    return dict(primefactors)

def n_diophantine(x):
    return (product([2*a+1 for a in primeFactor(x).values()]) + 1)//2


def run():
    max_n_dio, n = 0, 0
    for i in range(0, N_max**2, product(primes[:12])):

        n_dio = n_diophantine(i)
        if n_dio > max_n_dio:
            max_n_dio, n = n_dio, i
            print(i, max_n_dio)
        if n_dio > 4e6:
            #print(i, n_dio)
            return i



if __name__ == "__main__":
    ans = run()
    print(ans, log10(ans))

