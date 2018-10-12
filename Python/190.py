# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 19:14:18 2018

@author: J

Let Sm = (x1, x2, ... , xm) be the m-tuple of positive real numbers with
x1 + x2 + ... + xm = m for which Pm = x1 * x22 * ... * xmm is maximised.

For example, it can be verified that [P10] = 4112 ([ ] is the integer part function).

Find Σ[Pm] for 2 ≤ m ≤ 15.

MY SOLUTION
maximise:

 f(x1, x2, ..., xm) = x1^1 * x2^2 * ... * xm^m         (1)

subject to the constraint:

g(x1, x2, ..., xm) = x1 + x2 + ... + x3 - m             (2)

Using a lagrange multiplier, l, such that a lagrangian L = f - l*g, then a
maximal solution occurs with dL/dx = 0. That is:

df/dx = l*dg/dx

Substituting the derivatives of (1) and (2) for xi gives:
i/xi*f = l
which implies:
xi = i*f/l                                             (3)
and
f/l = xi/i                                              (4)

substituting (3) into the constraint, (2) gives:
f/l* (1 + 2 + ... + m) - m = 0
Using the identity for triangular numbers, this simplifies to:
f/l*(m+1)/2 = 1

Substituting (4) and rearranging gives:
xi = 2*i/(m+1)

Therefore xi can be calculated for i = 1, 2, ..., m to give the maximal solution
of f.
"""

def f(X):
    out = 1
    for i, x in enumerate(X):
        out *= x**(i+1)
    return out


def run():
    tups = []
    for m in range(2, 16):
        tup = [2*i/(m+1) for i in range(1, m+1)]
        tups.append(tup)

    return  int(sum(int(f(x)) for x in tups))

if __name__ == '__main__':
    print(run())

