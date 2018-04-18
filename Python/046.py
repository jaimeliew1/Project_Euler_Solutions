# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import primelist



def run():

    primes = primelist(10000)
    squares = list(x*x for x in range(1,100))


    for i in range(7,10000,2):

        if i not in primes:
            thisNumisGood = False
            for p in (x for x in primes if x <= i-1):
                if ((i - p)/2).is_integer() and int((i - p)/2) in squares:
                        thisNumisGood = True
            if not thisNumisGood:
                return i
                break

    return -1


if __name__ == "__main__":
    print(run())

