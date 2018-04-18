# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import math

def hexNumber(n):
    return int(n*(2*n-1))

def isTri(n):
    return ((math.sqrt(1+8*n)-1)/2).is_integer()

def isPent(n):
    return ((1+math.sqrt(1+24*n))/6).is_integer()



def run():

    i = 144
    while True:
        hexNum = hexNumber(i)
        if isTri(hexNum) and isPent(hexNum):
            return hexNum
        i += 1


if __name__ == "__main__":
    print(run())

