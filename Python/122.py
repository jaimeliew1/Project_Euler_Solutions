# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 122 - Efficient exponentiation

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from itertools import product

memo = {}


def depth(e):
    """
    memoizes the _depth function.
    """
    if e in memo.keys():
        return memo[e]
    else:
        memo[e] = _depth(e)
        return memo[e]


def _depth(e):
    """
    returns a list of the routes multiplication pairs to reach e in the minimum
    number of multiplications. As there can be multiple routes with the minimum
    length, all are returned.
    """
    if e == 1:
        return [()]
    elif e > 1:
        sets = []
        min_length = 10e10
        for i in range(1, e // 2 + 1):
            for a, b in product(depth(i), depth(e - i)):
                d = set().union(a, b, [(i, e - i)])
                if len(d) < min_length:
                    sets = [d]
                    min_length = len(d)
                elif len(d) == min_length:
                    sets.append(d)

        return sets


def run():
    ans = 0
    for k in range(1, 201):
        min_depth = len(depth(k)[0])
        ans += min_depth
    return ans


if __name__ == "__main__":
    print(run())
