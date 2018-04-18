# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 34

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from math import factorial

def digits(x):
    while x != 0:
        yield x%10
        x = x//10

def run():

    curious = []
    for x in range(3,100000):
        if x == sum(factorial(i) for i in digits(x)):
            curious.append(x)


    return sum(curious)


if __name__ == "__main__":
    print(run())

