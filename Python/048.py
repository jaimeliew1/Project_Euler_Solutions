# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():

    return sum(x**x for x in range(1,1000))%10000000000


if __name__ == "__main__":
    print(run())

