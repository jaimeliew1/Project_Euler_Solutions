# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 75 - Singular integer right triangles

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions


Given a pair if integers, m and n such that m > n > 0, a pythagorian triple is:
a = m**2 - n**2, b = 2*m*n, c= m**2 + n**2
The length of the sides, L, is:
    L = a + b + c
    L = 2*m**2 + 2*m*n
    L = 2*m(m + n)

Lmax = 1,500,000
assuming m = n+1, Lmax = 2*(n+1)(2n+1) => max(n) = 611.62
"""

import numpy as np


def run():
    #%% New attempt - 9 March 2018
    makeTriple = lambda m, n: [m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2]

    Lmax = 1500000
    # Step 1: Generate triples based on above formula
    Triples = []
    for n in range(1, 611 + 1):
        m = n + 1
        while 2 * m * (m + n) < Lmax:
            Triples.append(makeTriple(m, n))
            m += 1
    Triples = np.sort(Triples)

    """
    The above algorithm does not generate all pythagorean triples. by
    multiplying the created triples by an integer, k, all triples can be found.
    """

    moreTriples = []
    for t in Triples:
        k = 2
        while sum(k * t) < Lmax:
            moreTriples.append(list(k * t))
            k += 1

    Triples = np.vstack([Triples, moreTriples])

    # eliminate repeated triples
    Triples = np.unique(Triples, axis=0)
    """
    This should be all the triples with L < Lmax. so lets find L for each triple
    and count occurennces.
    """
    L = Triples.sum(1)
    unique, counts = np.unique(L, return_counts=True)

    return sum(counts == 1)


if __name__ == "__main__":
    print(run())
