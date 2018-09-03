# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 504

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions


Let ABCD be a quadrilateral whose vertices are lattice points lying on the coordinate axes as follows:

A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a, b, c, d ≤ m and a, b, c, d, m are integers.

It can be shown that for m = 4 there are exactly 256 valid ways to construct ABCD. Of these 256 quadrilaterals, 42 of them strictly contain a square number of lattice points.

How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?





"""

from math import gcd
import itertools
from collections import Counter
def internalTriangle(a, b):
    # http://jwilson.coe.uga.edu/EMAT6680Fa05/Schultz/6690/Pick/Pick_Main.htm
    # returns the number of internal lattice points contained in the polygon T, where
    # T is defined by the vertices (0, 0), (0, a), (b, 0)

    # Calculate area:
    A = a*b/2

    # Calculate boundary lattice points
    B = a + b + gcd(a, b)

    # Calculate internal lattice points using picks theorem
    return A - B/2 + 1


def internalQuad(a, b, c, d):
    # returns the number of internal lattice points contained in the quadrilateral,
    # Q, where Q is defined by the vertices (a, 0), (0, b), (-c, 0), (0, -d)
    # where a, b, c, and d are positive integers.

    # divide Q into four triangles and calculate internal lattice points for each
    I1 = internalTriangle(a, b)
    I2 = internalTriangle(b, c)
    I3 = internalTriangle(c, d)
    I4 = internalTriangle(d, a)

    # calculate lattice points lying along x and y axes.
    I5 = (a + c - 2) + (b + d - 1)

    # sum these values to get total number of internal lattice points
    return I1 + I2 + I3 + I4 + I5




def iterpoints(m):
    # a generator returning all combinations of 1 <= a, b, c, d <= m
    gen = itertools.product(range(1, m+1), repeat=4)

    for item in gen:
        yield item

def iterpoints2(m):
    # a generator returning the combinations of 1 <= a, b, c, d <= m, and the number
    # of permutations of a,b,c,d with the same value internal lattice points.
    # for each a, b, c, d combination, there are 24 permutations. but only three
    # can have a unique number of internal lattice points


    # TODO generate unique a,b,c,d
    # generate all a,b,c and map to aabc, abbc, abcc
    # generate all a,b and map to aaab
    # generate all aaaa


    # all four values are unique (a, b, c, d)
    gen = itertools.combinations(range(1, m+1), 4)
    for item in gen:
        yield item, 8
        yield [item[i] for i in [0,1,3,2]], 8
        yield [item[i] for i in [0,2,1,3]], 8

    # three unique values and one repitition (a, a, b, c)
    gen = itertools.combinations(range(1, m+1), 3)
    for item in gen:
        yield [item[i] for i in [0,0,1,2]], 8
        yield [item[i] for i in [0,1,0,2]], 4

        yield [item[i] for i in [1,1,0,2]], 8
        yield [item[i] for i in [1,0,1,2]], 4

        yield [item[i] for i in [2,2,0,1]], 8
        yield [item[i] for i in [2,0,2,1]], 4

    # two unique values and two repititions (a, a, b, b)

    gen = itertools.combinations(range(1, m+1), 2)
    for item in gen:
        yield [item[i] for i in [0,0,1,1]], 4
        yield [item[i] for i in [0,1,0,1]], 2
        yield [item[i] for i in [0,0,0,1]], 4
        yield [item[i] for i in [1,1,1,0]], 4


    # one unique value (a, a, a, a)
    for i in range(1, m+1):
        yield [i, i, i, i], 1







def isSquare(x):
    if (int(x**0.5))**2 == x:
        return True
    else:
        return False


def run():

    m = 100

    #gen = iterpoints(m)
    gen = iterpoints2(m)
    count = 0
    for poly, n in gen:
        I = internalQuad(*poly)

        if isSquare(I):
            #count += 1
            count += n
            #print(poly, I, n)


    return count

import time
if __name__ == "__main__":
    t = time.time()
    print(run())
    print(time.time() - t)

