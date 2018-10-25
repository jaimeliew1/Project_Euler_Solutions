# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:50:36 2018
Solution to Project Euler problem 101

Finished on the bus from work to home in 10 minutes.

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import numpy as np

def f(n):
    return 1 -n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def run():
    order = 10 # order of polynomial, f(n)
    x = list(range(1, order+1))
    y = [f(n) for n in x]

    BOPs = []
    for k in range(1, order+1):
        coefs = np.polyfit(x[:k], y[:k], k-1)
        BOPs.append(np.polyval(coefs, k+1).round())
    return int(sum(BOPs))

if __name__ == '__main__':
    print(run())
    