# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 407 - Idempotents

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions


If we calculate a^2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a^2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a^2 ≡ a (mod n).
So M(6) = 4.

Find ∑ M(n) for 1 ≤ n ≤ 107

########################

if a^2 ≡ a (mod n), then:

a(a-1) = kn

for some integer, k.

Given a value of a, we can calculate all candidates for n by finding all factors
f of a(a-1) such that f > a.

Additional optimisations:

- Factors are generated for a and (a-1). From these two lists of factors, the
factors of a(a-1) can be found by observing the cartesian product of the two lists

- Factors are generated using a modified sieve of eratosthenes generator.

- 1 is not considered as a factor of a or (a-1) as it will never yield a
candidate for n.

- if a is prime, it will not have any candidates for n. Therefore prime a's are
ignored.

- candidates for n are only considered if n <= n_max
"""

from EulerFunctions import timeit
from itertools import product
from click import progressbar


def divisors(N):
    '''
    yields the divisors of numbers between 2 and N using a sieving method.
    '''
    divisors = [[] for i in range(N)]
    for i in range(2, N):
        for j in range(i, N, i):
            divisors[j].append(i)

            yield divisors[i]


@timeit
def run(N=int(1e7)):
    a_max = [1]*(N+1)
    fact_b = []

    div_gen = divisors(N)
    with progressbar(range(2, N)) as bar:
        for a in bar:
            fact_a = next(div_gen)

            if len(fact_a) == 1: # if a is prime
                fact_b = fact_a
                continue

            fact_ab = [_a*b for _a, b in product(fact_a, fact_b)]
            n_candid = [_n for _n in fact_ab if _n > a and _n < N+1]

            for n in n_candid:
                a_max[n] = max(a_max[n], a)
            fact_b = fact_a

    a_max[:2] = [0, 0]
    return sum(a_max)




if __name__ == "__main__":
    print(run())
