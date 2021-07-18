# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 106 - Special subset sums: meta-testing

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from itertools import chain, combinations, product


def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3)"
    # modified to ignore empty set.
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))


def subset_gen(A):
    for B in powerset(A):

        if len(B) > len(A) // 2:
            break
        for C in powerset(tuple(y for y in A if y not in B)):

            yield B, C


def run(N=12):
    A = list(range(N))
    print("A: ", A)
    solution_set = set()

    for B, C in subset_gen(A):
        if (B, C) not in solution_set and (C, B) not in solution_set:
            solution_set.add((B, C))

    print(len(solution_set), "potential subset pairs.")

    count = 0
    # check the condition that the sum of B and C are not equal. Assume that the
    # second condition is met ie. if len(B > len(C), then sum(B) > sum(C).
    for B, C in solution_set:
        # second condition only misses subsets of EQUAL size. so ignore subsets
        # of UNEQUAL size.
        if len(B) != len(C):
            continue
        # If both subsets have 1 element, we know they can't be equal as they
        # are drawn from the same set. So we don't need to check these.
        # (although isn't this already a kind of check? whatever)
        if len(B) == 1:
            continue
        # Assuming B and C are increasing, then if every b<c where b, c are the
        # ith element of B and C, then it must be that B<C. So no need to check
        # (although, again, isn't this itself a check?)
        if all(x < y for x, y in zip(B, C)):
            continue

        # what are left are the subsets where we need to do an inequality check.
        # so lets count these.
        count += 1

    return count


if __name__ == "__main__":

    print(run())
