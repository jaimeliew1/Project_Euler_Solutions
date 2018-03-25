# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 1

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():
    N = 1000

    ans = sum(i for i in range(N) if (i%3==0) or (i%5==0))
    return ans


if __name__ == "__main__":
	print(run())

