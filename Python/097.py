# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 97 - Large non-Mersenne prime

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():
    a = 2 ** 7830457
    a = a * 28433 + 1
    return a % int(1e10)


if __name__ == "__main__":
    print(run())
