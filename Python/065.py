# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


def genEContFrac():
    #1,2,1,1,4,1,1,6,1,1,8,1,1,10...
    yield 2
    i = 2;
    while True:
        yield 1
        yield i
        yield 1
        i += 2

def run():

    target = 100
    gen = genEContFrac()
    cur = next(gen)
    A0 = 1
    A1 = cur

    B0 = 0
    B1 = 1
    ans = 0
    for i in range(target):
        #print(A1,'/',B1,':   ',A1/B1)
        cur = next(gen)
        A1,A0 = cur*A1+A0,A1
        B1,B0 = cur*B1+B0,B1
        if i == target - 2:
            ans = sum(int(x) for x in str(A1))
    return ans


if __name__ == "__main__":
    print(run())

