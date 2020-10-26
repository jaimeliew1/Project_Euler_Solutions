# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 136 - Singleton differences

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
Numbers, n, with only one form for x^2 - y² - z^2 = n have the following
peroperties.
n is either:
- an odd prime
- 4*p where p is an odd prime.
- 16*p where p is an odd prime.
- the number 16 or 4.
"""

from EulerFunctions import primelist



def run():
    N = 50000000
    primes = primelist(N)
    count = 2
    for p in primes[1:]:
        if (p+1)%4 == 0:
            # print(p)
            count += 1
        if (2*p+2)%4 == 0 and 4*p < N:
            # print(4*p)
            count += 1
        if (4*p+4)%4 == 0 and 16*p < N:
            # print(16*p)
            count += 1
    return count

if __name__ == "__main__":
    print(run())
