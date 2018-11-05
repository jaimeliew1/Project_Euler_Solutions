# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 121

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

I did the n=4 case by hand and found the
probability of drawing x blues is related to the product of combinations without
repitition of integers up to n+1.

eg. probability of drawing 1 blue disk in n=4 turns:
    p(1, 4) = (24 + 12 + 8 + 6)/120
            = (1*2*3 + 1*2*4 + 1*3*4 + 2*3*4)/(1*2*3*4*5)
"""
from itertools import combinations
from math import factorial, floor

def product(X):
    product = 1
    for x in X:
        product *= x
    return product


def probability(x, n):
    # returns the probability of drawing exactly x discs when there are n draws
    thesum = sum(product(x) for x in combinations(range(1, n+1), r=n-x))
    return thesum/factorial(n + 1)


def run():
    n = 15
    prob = sum(probability(x, n) for x in range(n//2 + 1, n+1))
    return floor(1/prob)


if __name__ == '__main__':
    print(run())