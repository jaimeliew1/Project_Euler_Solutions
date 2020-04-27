# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 113 - non-bouncy numbers

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

there are (9 + k - 1) choose k ways to arrange the digits 1,2,3,4,5,6,7,8,9 with
repetition  in ascending order in a k digit number. (see 'combination with
repetitions' on wikipedia). These are increasing numbers.

There are an equal number of decreasing numbers for digits 1,2,3,4,5,6,7,8,9. If
0 is added to the digits for decreasing numbers, number of decreasing numbers
increases by a factor of (n_digits - k + 1).

"""
from scipy import special


def comb_with_replacements(n, k):
    """
    returns the number of ways to arrange k items drawn from a set of n unique
    items with replacement.
    """
    return special.comb(n + k - 1, k, exact=True)


def run():
    n_digits = 100
    n = 9 # number of available digits (1, 2, 3, 4, 5, 6, 7, 8, 9)
    N_bouncy = n
    for k in range(2, n_digits + 1):
        this_N = comb_with_replacements(n, k) * (n_digits - k + 2)
        N_bouncy += this_N
    return N_bouncy


if __name__ == "__main__":
    print(run())
