# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import itertools

def pandigitals(N):
    # a generator of 0 to N pandigital numbers
    digits = list(x for x in range(0, N + 1))
    for p in itertools.permutations(digits):
        yield ''.join(map(str, p))



def run():

    primes = [2, 3, 5, 7, 11, 13, 17]


    specials = []
    for p in pandigitals(9):
        isSpecial = True
        for i in range(1, 8):
            if int(p[i:(i + 3)]) % primes[i - 1] != 0:
                isSpecial = False
                break
        if isSpecial:
            specials.append(int(p))

    return sum(specials)




if __name__ == "__main__":
    print(run())

