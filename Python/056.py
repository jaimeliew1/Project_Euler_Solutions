# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def digitSum(n):
    return sum(int(d) for d in str(n))


def run():


    Max = 0

    for i in range(1, 100):
        for k in range(1, 100):
            if digitSum(i**k) > Max:
                Max = digitSum(pow(i, k))

    return Max


if __name__ == "__main__":
    print(run())

