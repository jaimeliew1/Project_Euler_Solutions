# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 78 - Coin Partitions

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def genPentNum(n):
    return n * (3 * n - 1) // 2


def customPartitionNums():
    """
     customised version of partitionNums(n) which will keep calculating
     partition numbers until p(n) mod 1000000  = 0. returns n.
     """
    p = [1]
    i = 1
    while True:
        k = 1
        p.append(0)
        while True:
            sign = (-1) ** (k + 1)
            gp = genPentNum(k)
            if gp > i:
                break
            p[i] += sign * p[i - gp]

            gp = genPentNum(-k)
            if gp > i:
                break
            p[i] += sign * p[i - gp]
            k += 1
        if p[i] % 1000000 == 0:
            return i
        else:
            i += 1


def run():
    return customPartitionNums()


if __name__ == "__main__":
    print(run())
