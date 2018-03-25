# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 2

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():
    fibMax = 4e6
    Fibs = [1, 2]
    while Fibs[-1] < fibMax:
        Fibs.append(Fibs[-2] + Fibs[-1])

    return sum(x for x in Fibs if x%2 == 0)


if __name__ == "__main__":
	print(run())
