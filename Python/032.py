# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 32

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import numDigits
import math

def isPandigital(a, b, c):
    # Checks that each digit 1-9 appears only once in the numbers a, b and c.
    # Assumes the total number of digits of a, b and c is 9.

    st = str(a) + str(b) + str(c)
    return all(st.count(str(x)) == 1 for x in range(1, 10))


def run():
    pandigitalList = set()
    for a in range(1, 100000):
        lenBMin = 1
        while lenBMin + numDigits(a) < 9:
            b = math.ceil(pow(10, 9 - lenBMin - numDigits(a))/a) #minimum b to produce a total of 9 digits
            while numDigits(a) + numDigits(b) + numDigits(a*b) < 10:
                if isPandigital(a,b,a*b):
                    pandigitalList.add(a*b)
                b += 1 #iterates through all values of b between b min and bmax
            lenBMin += 1 # iterates through all lengths of b

    return sum(pandigitalList)



if __name__ == "__main__":
	print(run())

