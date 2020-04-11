# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 76 - Counting summations

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def genPentNum(n):
    return n * (3 * n - 1) // 2


def partitionNums(n):
    """
    generates partition number p(i) for  i = 0,1,2,3....n
    note: p(0) = 1, and p(a) = 0 for a < 0 uses recurrence formula
     P(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7)
    where the subtracted numbers are from the general pentagonal number series
    the sign of p is -1^(k-1) where k is the index (kind of) of the pent num.
    """

    p = [1]
    for i in range(1, n + 1):
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
    return p


def run():
    ans = partitionNums(100)
    print(ans[100] - 1)
    return -1


if __name__ == "__main__":
    print(run())
