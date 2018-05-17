# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 389

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import numpy as np
import matplotlib.pyplot as plt

def dice_pdf(s, N):
    pdf_die = 1/s*np.ones(s)
    pdf     = pdf_die

    for i in range(N-1):

        pdf = np.convolve(pdf, pdf_die)

    x = np.arange(N,N*s+1)

    return x, pdf


def pdf_mean(X, PDF):
    return sum(x*pdf for (x, pdf) in zip(X, PDF))

def pdf_var(X, PDF):
    mean = pdf_mean(X, PDF)
    return sum(x**2*pdf for (x, pdf) in zip(X, PDF)) - mean**2

def dice_pdf_normal(s, N):
    mu = N*(s+1)/2
    var = N*(s**2 - 1)/12




def run():


    return -1


if __name__ == "__main__":
    # pdf of tetrahedral die
    T = 1/4*np.ones(4)

    # pdf of cubic die
    C = np.zeros(100)
    for i, t in enumerate(T):
        for j, x in enumerate(t*dice_pdf(6, i+1)[1]):
            C[j] += x
    C = C[C != 0] # cut of zeros at end



    # pdf of octahedral die
    O = np.zeros(200)
    for i, c in enumerate(C):
        for j, x in enumerate(c*dice_pdf(8, i+1)[1]):
            O[j] += x
    O = O[O != 0] # cut of zeros at end



    # pdf of dodecahedral die
    D = np.zeros(2000)
    for i, o in enumerate(O):
        for j, x in enumerate(o*dice_pdf(12, i+1)[1]):
            D[j] += x
    D = D[D != 0] # cut of zeros at end



#    # pdf of isocehedral die
#    I = np.zeros(50000)
#    for i, d in enumerate(D):
#        for j, x in enumerate(d*dice_pdf(20, i+1)[1]):
#            I[j] += x
#    I = I[I != 0] # cut of zeros at end
    # I takes forever to calculate and it does not generate correct answer.
    # delve into the variance of convolved distributions first.


    plt.plot(D)
    print(sum(D))
    print(run())

