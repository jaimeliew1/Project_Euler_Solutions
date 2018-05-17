# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 286

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
'''
let X = X1 + X2 + ... + X50 be the sum of the number of successful
basketball shots. Xi = 1 when successful and 0 when not.
P(Xi=1) = 1-i/q, where q is a constant to be found.

Find q such that P(X=20) = 0.02
Let P(n, x) be the probability of scoring n within distances 1, 2, ..., x
P(n=20, x<=50) = P(n=19, x<=19)*P(n=1, x>19) + P(n=19, x<=20)P(n=1, x>20) +
so you can calculate p(n) if you know all p(i) for i<n

P(n=1,x=i) = (1-i/q)*n!/(i*q^(n-1))
P(n=1, x<=a) = sum(i=1->a)  (1-i/q)*a!/(i*q^(a-1))

P(n=2, x<= 50) = P(n=1,x<=1)P(n=1, x>1) + .... P(n=1,x<=2)P(n=1, x>2)
            =  P(n=1,x<=1)(1 - P(n=1,x<=1)) + ... this line is wrong. not a cdf.

P(s=1, a <= x <= b) = sum(i=a to b) b!/((a-1)!*i*q^(b-a))


'''
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
def run():
    return -1

def Prange(q, a, b):
    # Returns the probability of scoring 1 point (no more or less) when
    # taking one shot from distance a to b inclusive.
    P = 0
    for i in range(a, b+1):
        print((1 - i/q)*factorial(b)/factorial(a-1) * 1/(i*q**(b-a)))
        P += (1 - i/q)*factorial(b)/factorial(a-1) * 1/(i*q**(b-a))
    return(P)

if __name__ == "__main__":
    N = 50
    q = 100

    # probability of scoring from positions 1 to x inclusive
    P1 = np.zeros(51)
    # probability of scoring from positions x (exclusive to 50 (inclusive))
    P1_ = np.zeros(51)
    for i in range(1, 51):
        P1[i] = Prange(q, 1, i)
        P1_[i] = Prange(q, i+1, 50)

    P2 = np.zeros(51)
    for i in range(1, 51):
        P2[i] = P1[i]*P1_[i] # this wont work

    print(run())

