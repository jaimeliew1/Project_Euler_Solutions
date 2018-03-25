# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 9

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from itertools import product

def run():
    for i, j in product(range(1,1000), range(1,1000)):
        c = 1000 - i - j
        if i**2 + j**2 == c**2:
            return(i*j*c)
    return -1


if __name__ == "__main__":
    print(run())
