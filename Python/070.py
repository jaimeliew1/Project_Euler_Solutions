# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 70 - Totient permutation

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from tqdm import tqdm


def totient(N):
    # returns list of totient function values for n in  2 < n < N
    tots = list(range(N))
    tots[1] = 0
    for i, tot in enumerate(tots):
        if i == 0:
            continue
        if i == tot:  # if i is prime
            for n in range(i, N, i):
                tots[n] *= i - 1
                tots[n] //= i
    tots[1] = 1
    return tots[1:]


def isPerm(a, b):
    aa = str(a)
    bb = str(b)
    if len(aa) != len(bb):
        return False

    return sorted(aa) == sorted(bb)


def run():
    N = int(10 ** 7)
    best_cost = 999999
    best_n = -1
    tots = totient(N)

    for i, tot in enumerate(tqdm(tots)):
        if i == 0:
            continue
        if isPerm(i + 1, tot) and float(i + 1) / tot < best_cost:
            best_cost = float(i + 1) / tot
            best_n = i + 1

    return best_n


if __name__ == "__main__":
    print(run())
