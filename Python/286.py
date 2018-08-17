# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 286

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
'''
Barbara is a mathematician and a basketball player. She has found that the probability of scoring a point when shooting from a distance x is exactly (1 - x/q), where q is a real constant greater than 50.

During each practice run, she takes shots from distances x = 1, x = 2, ..., x = 50 and, according to her records, she has precisely a 2 % chance to score a total of exactly 20 points.

Find q and give your answer rounded to 10 decimal places.


'''


def probability(q):

    cache = {(0, 1): 1/q,
             (1, 1): 1 - 1/q} # (made, distance): probability

    # recursive function
    def recurse(made, distance):
        if made < 0 or made > distance:
            return 0

        if (made, distance) not in cache:

            p_hit = 1 - distance/q
            p_miss = distance/q
            cache[(made, distance)] = p_hit*recurse(made-1, distance-1) + \
                                      p_miss*recurse(made, distance-1)

        return cache[(made, distance)]


    return recurse(20, 50)



def golden(f, x1, x4, tol=1e-11):
# Performs golden section search to minimise function f in the bounds [x1, x4]
# x1 < x2 < x3 < x4
    Gold = (1 + 5**0.5)/2 # golden_ratio

    eps = 1e10
    x2 = x4 - (x4-x1)/Gold
    x3 = x1 + (x4-x1)/Gold


    while eps > tol:
        bold = x2

        if f(x2) < f(x3): # if minimum is in left section
            x4 = x3
        else: # if the minimum is in the right section
            x1 = x2

        x2 = x4 - (x4-x1)/Gold
        x3 = x1 + (x4-x1)/Gold



        eps = abs(bold - x2)


    return(x2)


def run():
    def toOptimize(q):
        return abs(probability(q) - 0.02)

    ans = golden(toOptimize, 50, 60)
    return f'{ans:.10f}'



if __name__ == "__main__":
    print(run())

