# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 87 - Prime power triples

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


from itertools import product


def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


# not 1102329
def run():
    z = set()
    for a, b, c in product(rwh_primes1(7072), rwh_primes1(369), rwh_primes1(85)):
        q = a * a + b ** 3 + c ** 4
        if q < 50000000:
            z.add(q)
    return len(z)


if __name__ == "__main__":
    print(run())
