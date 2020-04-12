# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 206 - Concealed Square

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import math

def run():

    nMin = int(math.sqrt(1020304050607080900)) // 10 * 10
    nMax = int(math.sqrt(1929394959697989900)) // 10 * 10

    n = nMin

    while n < nMax:
        nSqr = str(n ** 2)
        if nSqr[::2] == "1234567890":
            return n

        if n % 100 == 70:
            n += 60
        elif n % 100 == 30:
            n += 40
        else:
            n += 10



if __name__ == "__main__":
    print (run())
