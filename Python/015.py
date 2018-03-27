# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 15

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

Solution is based on permutations of multisets:
    https://en.wikipedia.org/wiki/Permutation#Permutations_of_multisets
"""

from math import factorial


def run():
    N = 20
    return int(factorial(N*2)/factorial(N)**2)


if __name__ == "__main__":
	print(run())

