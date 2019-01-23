# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import timeit, primelist
from numpy import argmin

def sequence_slow(N, primes):
    A = [1, 0]
    i_cand = [0, 1]

    for n in range(1, N):

        for i, a in enumerate(A):
            if i==0: continue
            if a < A[i-1]:
                i_cand.append(i)

        j = argmin([primes[i]**(2**A[i]) for i in i_cand])
        A[i_cand[j]] += 1
        A = A + [0]

    return A, prod([primes[i]**(2**a-1) for i, a in enumerate(A)])


def sequence_fast(N, A, primes):
    # get locations of candidates
    A += [0]*N
    i_cand = [0]
    for i, a in enumerate(A):
        if i==0: continue
        if a < A[i-1]:
            i_cand.append(i)

    # get dx of candidates
    dx_cand = [primes[i]**(2**A[i]) for i in i_cand]

    for n in range(N):
        j = argmin(dx_cand)
        A[i_cand[j]] += 1
        if j != 0:
            i_cand[j] += 1
        i = i_cand[j]
        dx_cand[j] = primes[i]**(2**A[i])

    return A

@timeit
def run():

    primes = primelist(10000000)
    Asmall, _ = sequence_slow(80, primes)
    Abig = sequence_fast(500500-80, Asmall, primes)

    out = 1
    for i, a in enumerate(Abig):
        out = (out*primes[i]**(2**a-1)) % 500500507

    return out


def prod(lst):
    out = 1
    for n in lst:
        out *= n
    return out



if __name__ == "__main__":
    print(run())
