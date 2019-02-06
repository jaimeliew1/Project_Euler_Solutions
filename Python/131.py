# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 131

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

Find all primes, p < 1000000 such that
    n^3 + n^2p = m^3 (1)
where n, m are integers.rearranging (1) gives
    n^2(n + p) = m^3        ==> n must be a cube.

let:
    n = a^3 (1.a)

rearranging (1) and (1.a) gives a difference of two cubes:
    p = m^3/a^6 - a^3 = (m/a^2 - a)(m^2/a^4 + m/a + a^2) (2)

for (2) to be prime, m/a^2 - a must be 1 (or else p is composite, which it cannot be)

Therefore,
    m/a^2 -a = 1 ==> m = a^3 + a^2 (3)

Substitute (3) into (2) gives:
    p = 3a^2 + 3a + 1.

For p < 1000000 ==> a <~ a_max = sqrt(1000000 - 1)

Therefore, find all primes of the form p = 3a^2 + 3a + 1 for integer a < a_max
"""
from EulerFunctions import primelist
from math import sqrt

def run():
    p_max  = 1000000
    a_max  = int(sqrt(p_max-1))
    primes = primelist(p_max)
    ans    = {}

    for a in range(1, a_max):
        p = 3*a**2 + 3*a + 1
        if p in primes:
            ans[p] = a

    #for k, v in ans.items(): print(f'p = {k}, n = {v}')
    return len(ans)


if __name__ == "__main__":
    print(run())
