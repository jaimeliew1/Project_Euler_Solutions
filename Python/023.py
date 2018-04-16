# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 23

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from itertools import product

def divisors(n):
    # returns an ordered list of divisors of n
    smalldivisors = []
    largedivisors = []
    lim = int(n**0.5)
    #print(lim)
    for i in range(1, lim+1):
        if n%i==0:
            smalldivisors.append(i)
            if i !=1:
                largedivisors.append(n//i)


    if lim**2 == n:
        smalldivisors.pop()
    largedivisors.reverse()
    return smalldivisors + largedivisors

def divisor_generator(n):
    # a generator of divisors of n (unordered)
    if n <=2:
        yield 1
    lim = int(n**0.5) + 1
    for i in range(2, lim):
        if n%i==0:
            yield i
            if i != lim:
                yield n//i



def run():
    limit = 28123
    #limit = 50
    # Find abundant numbers below limit
    abundant = []
    for i in range(1, limit):
        if i < sum(divisors(i)):
            abundant.append(i)

    #return abundant
    # find all numbers which are the sum of two abundant numbers
    abundantPairs = [False] * (limit+1)
    for a in abundant[::-1]:
        for b in abundant:
            if a + b > limit:
                break
            else:
                abundantPairs[a+b] = True

    return sum(i for (i, a) in enumerate(abundantPairs) if not a)


if __name__ == "__main__":
    print(run())

