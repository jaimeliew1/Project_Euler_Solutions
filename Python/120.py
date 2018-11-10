# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 120

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():

    S = 0
    for a in range(3, 1001):
        r_max = 0
        for n in range(1, a*2+2):
            r = ((a-1)**n + (a+1)**n)%a**2

            if n == 1:
                end_condition = r
            elif r == end_condition:

                break

            if r > r_max:
                r_max = r
        S += r_max


    return S


if __name__ == "__main__":
    print(run())

