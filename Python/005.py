# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 5

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import primelist
from collections import Counter
def primeFactors(x):
    # returns the prime factors of x.
    primes = primelist(x+1)

    factors = []
    while x > 1:
        for p in primes:
            if x%p == 0:
                factors.append(p)
                x = x//p
                break
    return factors

def run():
    factors = Counter()
    for i in range(2,21):
        factors_ = Counter(primeFactors(i))
        for key, value in factors_.items():
            factors[key] = max(factors[key], factors_[key])

    ans = 1
    for k, v in factors.items():
        ans *= k**v
    return ans



if __name__ == "__main__":

    print(run())
