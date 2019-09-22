# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 347
Largest integer divisible by two primes


Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import primelist



def largest_integer_divisible_by_2_primes(p, q, N):
    '''
    finds all integers n<N divisible by only p and q. Returns the largest.
    '''
    out = []
    p_exp, q_exp = 1, 1
    while p**p_exp <= N:
        q_exp = 1
        while p**p_exp*q**q_exp <= N:
            out.append(p**p_exp*q**q_exp)
            q_exp += 1
        p_exp += 1

    if len(out) == 0:
        return 0
    else:
        return max(out)


def run(N=10000000):
    primes = primelist(N//2)

    Sum = 0
    for i, p in enumerate(primes):
        if p*primes[i+1] > N:
            break
        for q in primes[i+1:]:
            if p*q > N: break
            M = largest_integer_divisible_by_2_primes(p, q, N)
            #print(p, q, M)
            Sum += M


    return Sum


if __name__ == "__main__":
    print(run())
