# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 105 - Special subset sums: testing

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from itertools import chain, combinations, product


def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3)"
    # modified to ignore empty set.
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


def subset_gen(A):
    for B in powerset(A):

        if len(B) > len(A)//2:
            break
        for C in powerset(tuple(y for y in A if y not in B)):
            yield B, C


def is_special_subset(B, C):
    # ensure the set with more elements is subset C (unless they are equal)
    if len(B) == len(C) and sum(B) != sum(C):
        return True

    elif len(B) > len(C) and sum(B) > sum(C):
        return True

    elif len(B) < len(C) and sum(B) < sum(C):
        return True

    else:
        return False



def run():
    S = 0
    with open('Data/p105_sets.txt') as f:
        for line in f.readlines():
            A = [int(x) for x in line.split(',')]
            is_special = all(is_special_subset(B, C) for B, C in subset_gen(A))
            if is_special:
                S += sum(A)
    return S


if __name__ == "__main__":

    print(run())
