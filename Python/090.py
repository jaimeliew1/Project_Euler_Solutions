# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 90

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from itertools import product, combinations




def run():
    pairs = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (6, 4), (8, 1)]
    count = 0
    for A_, B_ in product(combinations(range(0, 10), 6), repeat=2):
        A = [6 if x==9 else x for x in A_]
        B = [6 if x==9 else x for x in B_]


        if all((x in A and y in B) or (x in B and y in A) for x, y in pairs):
            count += 1

    return count//2


if __name__ == "__main__":
    print(run())
