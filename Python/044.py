# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def PentNum(n):
    # returns the nth pentagonal number
    return n*(3*n-1)//2



def pentPairs():
    pentNums = list(PentNum(x) for x in range(1000, 3000))
    L = len(pentNums)
    for i in range(1, L):
        for j in range(i):
            yield (pentNums[i], pentNums[j])



def run():
    pentNums = list(PentNum(x) for x in range(1000, 3000))
    out = []
    for a, b in pentPairs():
        if (a + b in pentNums) and (a - b in pentNums):
            out.append(a - b)
            return out[0]
    return out[0]


if __name__ == "__main__":


   print(run())

