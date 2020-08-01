# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 138 - Special isosceles triangles

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

Somehow, L(n) = Fib(6*n+3)/2 where Fib(i) is the ith fibonacci number.
So just find the sum of the first 12 L
"""


def fib_gen(N):
    a, b = 1, 1
    yield a
    yield b
    for i in range(N - 2):
        a, b = a + b, a
        yield a


def run():
    fib = list(fib_gen(75))

    ans = sum(fib[6 * i + 2] // 2 for i in range(1, 13))
    return ans


if __name__ == "__main__":
    print(run())
