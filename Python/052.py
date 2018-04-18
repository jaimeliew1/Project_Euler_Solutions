# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def containSameDigits(ns):
    sortedDigits = [sorted(str(x)) for x in ns]
    return all(x == sortedDigits[0] for x in sortedDigits)




def run():
    i = 1
    while True:
        numList=[]

        for k in range(1,7):
            numList.append(i*k)
        if containSameDigits(numList):
            return i
        i += 1


if __name__ == "__main__":
    print(run())

