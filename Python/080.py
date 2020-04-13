# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 80 - Square root digital expansion

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import decimal
import math

decimal.getcontext().prec = 102


def sumOfSqrRootDigits(n):
    a = str(decimal.Decimal(n).sqrt())
    a = a.split(".")[0] + a.split(".")[1][:99]

    return sum(int(d) for d in a)


def run():

    N = 100
    Sum = 0
    for i in range(1, N + 1):
        if int(math.floor(math.sqrt(i))) ** 2 != i:
            Sum += sumOfSqrRootDigits(i)

    return Sum


if __name__ == "__main__":
    print(run())
