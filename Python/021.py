# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
def factors(n):
    # Borrowed from problem 12
    # Returns factors of n in a list.
    # !!! Could be further optimised by using a list of primes.
    if n == 1:
        return [1]
    factors = [1]
    for i in range(2, int(n**0.5)):
        if n%i == 0:
            factors.append(i)
            factors.append(n//i)
    if n%n**0.5 == 0:
        factors.append(int(n**0.5))
    return factors

def amicable(a):
    return sum(factors(sum(factors(a)))) == a and sum(factors(a)) != a

def run():
    Sum = sum(x for x in range(2, 10000) if amicable(x))
    return Sum


if __name__ == "__main__":
    print(run())


