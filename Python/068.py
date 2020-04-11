# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 68 - 5-gon rings

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import itertools
import numpy as np


def run():

    n = 5

    n_min, n_max = 1, n * 2
    numSet = list(x for x in range(n_min, n_max + 1))

    # Generate all possible permutations of the middle nodes in the ring.
    totalCombSet = list(itertools.permutations(numSet, n))

    ring_vals = []
    for S in [13, 14, 15]:

        # generate Exterior and Interior values for each permutation of M
        # (E)xterior, (M)iddle, (I)nterior
        for comb in totalCombSet:
            ring = np.zeros((3, n), dtype=int)
            M = np.array(comb)
            I = np.roll(M, -1)
            E = S - (M + I)

            # Ignore repeated numbers
            if len(np.unique(E)) != n:
                continue
            # Ignore numbers out of range
            if any(E < n_min) or any(E > n_max):
                continue
            # Ignore repeated numbers between E and M
            if any(e in M for e in E):
                continue

            ring = np.vstack([E, M, I])

            # put smallest external value at front
            ind_min = np.argmin(E)
            ring = np.roll(ring, -ind_min, axis=1)

            # flatten, and convert to string value
            ring_val = int("".join([str(x) for x in ring.T.ravel()]))
            ring_vals.append(ring_val)

    return max(ring_vals)


if __name__ == "__main__":
    print(run())
