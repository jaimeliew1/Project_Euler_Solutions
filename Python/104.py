# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 104

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import timeit
from math import log10, sqrt

golden = (sqrt(5) + 1)/2


def Fibonacci(N):
    # returns the Nth fibonacci number, but only the first 10ish digits
    fib = 1
    for n in range(N):
        fib *= golden
        L = int(log10(fib))
        if L > 12:
            fib/=10**(L-12)
    return fib/sqrt(5)

def Fibonacci_mod():
    # generates fibonacci numbers mod 10**9
    a, b = 0, 1
    while True:
        yield b
        a, b = b, (a + b)%10**9

def pandigital_last(n):
    digits = sorted([(n//10**i)%10 for i in range(9)])
    return True if digits == [1,2,3,4,5,6,7,8,9] else False


def pandigital_first(n):
    L = int(log10(n))
    digits = sorted([n//10**(L-i)%10 for i in range(9)])
    return True if digits == [1,2,3,4,5,6,7,8,9] else False


@timeit
def run():
    for i, fibmod in enumerate(Fibonacci_mod()):
        if pandigital_last(fibmod):
            if pandigital_first(Fibonacci(i+1)):
                return i+1


if __name__ == "__main__":
    print(run())
