# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 7

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def primes_sieve(n):
    # Returns boolean array indicating if each number is prime or not.
    # Sieve of Eratosthenes.
    a = [True] * int(n)
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, int(n), i):     # Mark factors non-prime
                a[n] = False
    return a

def run():
    N = 10001
    sieve = primes_sieve(1000000)
    for i in range(1, N):
        next(sieve)
    return next(sieve)


if __name__ == "__main__":
    print(run())
