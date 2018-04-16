# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

layers = 501

def run():


    x, Sum = 1, 1
    for i in range(1, layers):
        for j in range(4):
            x += 2*i
            Sum += x

    return Sum


if __name__ == "__main__":
	print(run())

