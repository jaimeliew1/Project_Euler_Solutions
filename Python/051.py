# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import numDigits, primelist
from collections import Counter


def exclusionList(n):
    for i in range(1,pow(2,n-1)-1):
        yield (bin(i)[2:]+'0').zfill(n)


def run():

    target = 8
    primes = primelist(1000000)
    found = False
    targetExclusionList = ''
    targetRepDigs = ''
    for n in range(2,8):
        primeSet = list((str(x))for x in primes if numDigits(x) == n)
        for ex in exclusionList(n):
            currentCount = Counter()
            for p in primeSet:
                repDigs = ''
                changeDigs = ''
                for i,k in enumerate(ex):
                    if k == '1': #exclude
                        changeDigs += p[i]
                    else:
                        repDigs += p[i]

                if changeDigs.count(changeDigs[0]) == len(changeDigs): #if all changing digits are equal
                    currentCount[repDigs] += 1
                    if currentCount[repDigs] == target:
                        found =True
                        targetExclusionList = ex
                        targetRepDigs = repDigs
                if found:
                    break
            if found:
                break
        if found: #go through array again and print answers
            ans = []

            for p in primeSet:
                repDigs = ''
                changeDigs = ''
                for i,k in enumerate(targetExclusionList):
                    if k == '1': #exclude
                        changeDigs += p[i]
                    else:
                        repDigs += p[i]

                if changeDigs.count(changeDigs[0]) == len(changeDigs): #if all changing digits are equal
                    if repDigs == targetRepDigs:
                        ans.append(p)
            break


    return min(int(x) for x in ans)


if __name__ == "__main__":
    print(run())

