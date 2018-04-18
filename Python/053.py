# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import math

def nCr(n, r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))



def run():
    count = 0
    for i in range(1,101):
        for k in range(1,i):
            if nCr(i, k) > 1000000:
                count += 1

    return count


if __name__ == "__main__":
    print(run())

