# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 104

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from math import log10, sqrt

golden  = (sqrt(5) + 1)/2
log_phi = log10(golden)
log_5   = log10(sqrt(5))

def Fibonacci(N):
    # returns the the first 9 digits of the Nth fibonacci number. Only works for
    # fibonacci numbers with 9 or more digits in the first place.
    return 10**(N*log_phi - log_5 - int(N*log_phi - log_5 - 8))


def pandigital_last(n):
    digits = sorted([(n//10**i)%10 for i in range(9)])
    return True if digits == [1,2,3,4,5,6,7,8,9] else False


def pandigital_first(n):
    digits = sorted([n//10**(8-i)%10 for i in range(9)])
    return True if digits == [1,2,3,4,5,6,7,8,9] else False


def run():
    i, a, b = 1, 0, 1
    while True:
        if pandigital_last(b):
            if pandigital_first(Fibonacci(i)):
                return i
        i, a, b = i+1, b, (a + b)%10**9 # generate fibonacci numbers mod 10**9


if __name__ == "__main__":
    print(run())
