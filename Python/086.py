# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 86

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import timeit
import itertools
from math import sqrt

@timeit
def run_old():
    M, count = 0, 0
    while count < 2000:
        M += 1
        a = M
        if M%100 == 0:
            print('{}...'.format(M))
        for b, c in itertools.combinations_with_replacement(range(1, M+1), 2):
            s_min = min((a + b)**2 + c**2,
                        (b + c)**2 + a**2,
                        (c + a)**2 + b**2)
            if int(sqrt(s_min))**2 == s_min:
                count += 1


    print(M, count)
    return M

@timeit
def run():
    # a <= b <= c means that min spider-fly length, smin = (a + b)**2 + c**2
    M, count = 0, 0
    while count < 1000000:
        M += 1
        c = M
        for ab in range(2, 2*M + 1):
            s_min = ab**2 + c**2

            if int(sqrt(s_min))**2 == s_min:
                count += ab//2
                if ab > M: count -= (ab - M - 1)
    return M

if __name__ == "__main__":

    print(run())
