# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 103 - Special subset sums: optimum

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
    #_A = [11, 17, 20, 22, 23, 24] #n=6
    _A = [20, 31, 38, 39, 40, 42, 45]
    delta_set = [-1, 0, 1]

    min_set, min_sum = None, 1e10
    for delta in product(delta_set, repeat=len(_A)):
        A = [a+d for a, d in zip(_A, delta)]
        if len(set(A)) != len(A):
            continue
        is_special = all(is_special_subset(B, C) for B, C in subset_gen(A))
        if is_special and sum(A) < min_sum:
            min_set, min_sum = sorted(set(A)), sum(A)

    #print(''.join(str(x) for x in min_set), min_sum)
    return ''.join(str(x) for x in min_set)


if __name__ == "__main__":
    print(run())
