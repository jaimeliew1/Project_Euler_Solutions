# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from EulerFunctions import primelist


primes = primelist(100000)
def npf(n): #number of prime factors
    num = 0
    for p in (x for x in primes if x <= n/2):
        if n%p == 0:
            num += 1
    if num == 0:
        return 1
    else:
        return num



def run():

    notFound = True

    i = 134000# 2*3*5*7
    while notFound:
        if i%1000 == 0:
            #print(i)
            pass
        if npf(i) == npf(i+1) == npf(i+2)==npf(i+3)== 4:
            notFound = False

        i += 1
    return i-1


if __name__ == "__main__":
    print(run())

