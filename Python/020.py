# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 20

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from math import factorial

def run():
    #sum of digits in 100!
    Sum = sum(int(i) for i in str(factorial(100)))
    return Sum


if __name__ == "__main__":
	print(run())

