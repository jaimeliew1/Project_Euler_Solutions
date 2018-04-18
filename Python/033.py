# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 33

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from math import gcd

def curious(a,b):
    aa = str(a)
    bb = str(b)
    for digit in aa:

        if (digit in bb) & (digit != '0'):
            if aa.count(digit) ==1:
                a = int(aa.replace(digit,''))
            else: #if both digits are the same, handle the situation differently
                a = int(digit)

            if bb.count(digit) ==1:
                b = int(bb.replace(digit,''))
            else:
                b = int(digit)
            return a,b
    return 0,0

def run():

    curiousList = []
    for b in range(11, 100):
        for a in range(10, b):
            x, y = curious(a, b)
            if y == 0:
                continue

            if x/y == a/b:
                curiousList.append((x, y))

    num, den = 1, 1
    for pair in curiousList:
        num *= pair[0]
        den *= pair[1]

    hcf = gcd(num, den)


    return int(den/hcf)


if __name__ == "__main__":
	print(run())

