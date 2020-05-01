# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 125 - Palindromic Sums

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

Watch out for duplicates. Turns out that
554455 = 9^2 + 10^2 + ... + 118^2 = 331^2 + ... + 335^2
and
9343439 = 102^2 + ... + 307^2 = 657^2 + ... + 677^2
"""

def isPalindrome(n):
    st = str(n)
    return st[::-1] == st

def run():
    palindromes = []
    S_max = 10**8
    n, d, S = 1, 1, 0 # lower number, consecutive run length, sum of squares.
    while n**2 < S_max:
        while S < S_max:
            squares = [x ** 2 for x in range(n, n + d + 1)]
            S = sum(squares)
            if isPalindrome(S) and S < S_max:
                palindromes.append(S)
            d += 1
        n += 1
        d, S = 1, 0

    return sum(set(palindromes))


if __name__ == "__main__":
    print(run())
