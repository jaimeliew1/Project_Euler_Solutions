# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import numDigits

def run():

    count = 1
    for i in range(2, 10):
        p = 1

        while numDigits(i**p) == p:
            count+=1
            #print(i,p,i**p)
            p+=1


    return count


if __name__ == "__main__":
    print(run())

