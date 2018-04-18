# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def isPalindrome(n):
    st = str(n)
    return st[::-1] == st



def reverse(n):
    return int(str(n)[::-1])



def run():
    count = 9999

    for x in range(1,10000):

        for i in range(0, 50):
            x += reverse(x)
            if isPalindrome(x):
                count -= 1
                break

    return count


if __name__ == "__main__":
    print(run())

