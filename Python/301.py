# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 301

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

for three heaps of size a, b, c, the function, f(a, b, c)
such that f()=0 when there is no optimal nim strategy, and
f()!=0 if there is

f(a, b, c) = a XOR b XOR c

if f(n, 2*n, 3*n) = 0, then n is an integer such that its
binary representation have no consecutive 1's. See some
examples:

1, 2, 3: 001, 010, 011

?,?,?: 100101, 1001010, 1101111

The number of integers, 1<= n <=2^i with no consecutive 1's
is the (i+2)th fibonacci number.
"""

from EulerFunctions import timeit


def f(max_digits, x=''):
'''
Recursive function that returns a list of numbers which
do not have consecutive 1's in its binary representation.
'''
    if len(x) == 0:
        out = f(max_digits, '1')
    elif len(x) == max_digits:
        return [x]
    else:
        out = [x]
        if x[-1] == '0':
            out += f(max_digits, x + '0')
            out += f(max_digits, x + '1')
        else:
            out += f(max_digits, x + '0')
    return out


def nimsum(a, b, c):
    return a^b^c



@timeit
def run():
    a, b = 1, 1
    for i in range(30):
        a, b = a+b, a
    return a


if __name__ == '__main__':
        print(run())
