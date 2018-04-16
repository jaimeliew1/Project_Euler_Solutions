# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 1

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():
    return sum(x for x in range(1,1001) if x%3 == 0 or x%5 == 0)


if __name__ == "__main__":
	print(run())

