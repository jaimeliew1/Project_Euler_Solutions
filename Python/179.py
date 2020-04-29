# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 179 - Consecutive positive divisors


Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():

    N = int(1e7)
    n_factors = [1 for _ in range(N + 1)]
    # can start at 2 because 1 is a divisor for all numbers and wont change the
    # relative count.
    # Factor counting loop
    for i in range(2, N + 1):
        n = i
        while n < N:
            n_factors[n] += 1
            n += i

    # Evaluate factor count array
    count = 0
    for i in range(N):
        if n_factors[i] == n_factors[i + 1]:
            count += 1

    return count


if __name__ == "__main__":
    print(run())
