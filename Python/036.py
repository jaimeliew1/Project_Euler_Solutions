# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import math


def isPalindrome(n):
    l = len(n)
    if n[:math.floor(l/2)] == n[l - math.floor(l/2)::][::-1]:
        return True
    else:
        return False




def run():
    limit = 1000000

    doublePal = []
    for i in range(1,limit):
        if isPalindrome(str(i)):
            if isPalindrome(bin(i)[2:]):
                doublePal.append(i)

    return sum(doublePal)



if __name__ == "__main__":
	print(run())

