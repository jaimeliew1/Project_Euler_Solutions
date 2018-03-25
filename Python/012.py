# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 12

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def  triNumber(n):
    return n*(n+1)//2

def factors(n):
    # Returns factors of n in a list.
    # !!! Could be further optimised by using a list of primes.
    factors = []
    for i in range(1, int(n**0.5)):
        if n%i == 0:
            factors.append(i)
            factors.append(n//i)
    if n%n**0.5 == 0:
        factors.append(int(n**0.5))
    return factors

def run():
    nDivisors = 0
    i = 1
    while nDivisors < 500:
        nDivisors = len(factors(triNumber(i)))
        i += 1
    return triNumber(i)

if __name__ == "__main__":
    print(run())
