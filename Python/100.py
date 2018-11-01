# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:07:17 2018

@author: J

Solution to project euler problem 100

for a bag of N discs containing A blue discs, the probability of consequtively
drawing two blue discs is P(AA) = A(A-1)/(N(N-1)).

find the smallest A such that P(AA) == 1/2 and N > 10^12

We can see that the condition:
    2*(A^2 + A) - N^2 + N = 0       (1)
must be true.

(1) can be rearranged to:
    (2*N - 1)^2 - 2*(2*a-1)^2 = -1
or:
    x^2 - 2y^2 = -1              (2)
where:
    x = 2N -1, y = 2A - 1

(2) is a negative Pell equation. The fundamental (smallest) solution to this
equation is x, y = 1, 1.

Given the fundamental solution, a generating function can be made to generate
successive solutions to the pell equation.
In this case:
x_new = 3*x + 4*y
y_new = 2*x + 3*y

why? good question


"""



def run(verbose=False):
    x, y = 1, 1
    N, a = (x+1)//2, (y+1)//2
    while N <= 10**12:
         x, y = 3*x + 4*y, 2*x + 3*y
         N, a = (x+1)//2, (y+1)//2
         if verbose: print(a, N)
    return a

if __name__ == '__main__':
    print(run())


