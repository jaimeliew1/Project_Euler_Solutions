# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 587

https://projecteuler.net/problem=587

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions


First the point of intersection between the circle and the line is found (x0, y0)

Next, the area under the lower circle is found up to a point, say, x.

The area below the straight line is also found up to x.

The difference of these two areas is found to give the answer. x is chosen to be y0,
which essentially flips the problem on its side to give a single integral.

The integral was solved analytically.
"""

from numpy import pi, arcsin, sqrt


def AreaUnderCurve(N, x0):
    # calculates the area under the curve from 0 to x0, where x0 is the point
    # where the line intersects the first circle. Assumes radius of 1
    r = 1
    a = 1/N # slope of the straight line

    return r*x0 - r**2/2*(arcsin((x0-r)/r) + (x0-r)*sqrt(2*x0*r - x0**2)/r**2 + pi/2)

def AreaUnderLine(N, x0):
    # actually, this is the area to the left of the line
    a = 1/N
    return 1/(a*2)*x0**2

def IntersectionPoint(N):
    a = 1/N
    r = 1
    x0 = 2*r*(a+1) - sqrt(4*r**2*(a+1)**2 - 4*r**2*(1+a**2))
    x0 = x0/(2*(1+a**2))

    y0 = x0/N

    return x0, y0


def areaPerc(N):
    r = 1

    x0, y0 = IntersectionPoint(N)
    # by passing y0 instead of x0, the problem is turned on its side.
    Ac = AreaUnderCurve(N, y0)
    Al = AreaUnderLine(N, y0)

    Atotal = r**2 - pi*r**2/4

    return (Ac-Al)/Atotal


def run():
    N = 1
    while areaPerc(N) > 0.001:
        N += 1
    return N


if __name__ == "__main__":
    print(run())

