# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 356 - Largest roots of cubic polynomials

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def root_power_sum_gen(n):
    p1, p2, p3 = 2**(2 * n), 2**n, 3
    yield p3
    yield p2
    yield p1
    while True:
        p1, p2, p3 = (2**n * p1 - n * p3) % 100000000, p1, p2
        yield p1


def run():

    return -1


if __name__ == "__main__":
    print(run())

    ans = {}
    for n in range(1, 31):
        for i, P in enumerate(root_power_sum_gen(n)):
            if i == 987654321: break

        ans[n] = P - 1
        print(n, P)

    print(sum(ans.values()) % 100000000)
