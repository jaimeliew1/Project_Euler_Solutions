# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import is_prime

def run():


    cur = 1
    cornPrimes = 0
    corners = 1
    for i in range(1, 30000):
        for k in range(1, 4):
            cur += 2*i
            if is_prime(cur):
                cornPrimes += 1
            corners += 1
        cur += 2*i #Don't bother checking the last one because it isnt prime
        corners +=1

        if cornPrimes/corners < 0.1:
            return i*2 + 1



if __name__ == "__main__":
    print(run())

