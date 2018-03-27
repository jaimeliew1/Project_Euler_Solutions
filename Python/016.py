# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 16

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def run():
    n = pow(2,1000)
    digitSum = sum(int(i) for i in str(n))

    return digitSum


if __name__ == "__main__":
	print(run())

