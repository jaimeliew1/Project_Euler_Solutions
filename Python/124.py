# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 124 - Ordered radicals

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
Modified sieve of Eratosthenes that records the product of prime factors. This
list is then sorted and the 10000ths entry is returned.
"""


def run():

    N = 100000
    rad = {i: 1 for i in range(N + 1)}
    rad.pop(0)
    is_prime = [True for _ in range(N + 1)]

    for i in range(2, N + 1):
        n = i
        if not is_prime[n]:
            continue

        rad[n] *= i
        n += i
        while n <= N:
            is_prime[n] = False
            rad[n] *= i
            n += i

    rad_sorted = [k for k, v in sorted(rad.items(), key=lambda item: item[1])]

    return rad_sorted[10000 - 1]


if __name__ == "__main__":
    print(run())
