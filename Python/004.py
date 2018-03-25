# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 4

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def isPalindrome(x):
    # Returns true if the integer, x is palindromic
    x = str(x)
    n = len(x)
    if n%2 == 0:
        left, right = x[:n//2], x[n//2:]
    else:
        left, right = x[:(n-1)//2], x[(n+1)//2:]
    return left == right[::-1]

def run():
    palindromes = []
    for i in range(100,1000):
        for j in range(i, 1000):
            if isPalindrome(i*j):
                palindromes.append(i*j)
    return max(palindromes)


if __name__ == "__main__":
    print(run())
