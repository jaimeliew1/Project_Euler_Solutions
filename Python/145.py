# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 145
How many reversible numbers are there below one-billion?

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""



from EulerFunctions import timeit


def reverse(n):

    return int(str(n)[::-1])

def only_odd(n):
    while n>0:
        if n%2 == 0:
            return False
        n = n//10
    return True


@timeit
def run():
    count = 0
    for n_digits in range(1, 9):
        for n in range(10**n_digits + 1, 10**(n_digits + 1), 2):

            # if n//10**n_digits % 2 == 1: continue
            if int(str(n)[0]) % 2 ==  1: continue
            thesum = n + reverse(n)
            if only_odd(thesum):
                #print(n, thesum, n//10**(n_digits))
                count += 2


    return count


if __name__ == "__main__":
    print(run())
