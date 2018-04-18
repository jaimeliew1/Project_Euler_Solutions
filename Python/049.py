# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from EulerFunctions import numDigits, primelist, is_prime
import itertools

def Perms(x):
    # Generator that yields the digit permutations of x.
    for perm in itertools.permutations(str(x)):
        yield int(''.join(perm))



def run():
    primes = [x for x in primelist(10000) if numDigits(x) == 4]

    for p in primes:
        primePerms = list(set(sorted(x for x in Perms(p) if is_prime(x))))

        while len(primePerms) >= 3:
            diff = primePerms[1] - primePerms[0]
            for n in primePerms[2:]:
                if (n - primePerms[0])/diff == 2:
                    out = ''.join([str(x) for x in primePerms[0:3]])
                    if len(out) == 12:
                        return int(out)
            primePerms.remove(primePerms[1])
    return -1


if __name__ == "__main__":
    print(run())

