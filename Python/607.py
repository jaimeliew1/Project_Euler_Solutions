# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 607

Minimise Frodo and Sam's journey across the marsh.

Use Snell's law, and a form of Newton raphson method.



Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""


from numpy import pi, sin, cos, tan, arcsin, sqrt

def run():
    W = [(50*sqrt(2)-50)/2, 10, 10, 10, 10, 10, (50*sqrt(2)-50)/2]
    V = [10, 9, 8, 7, 6, 5, 10]

    # method check:
    X = 7*[pi/4]
    assert sum(w/cos(x)/v for w, x, v in zip(W, X, V)) - 13.4738 < 1e-5


    theta, error = pi/4, 1e100
    while abs(error) > 1e-13:
        X = [arcsin(v/10*sin(theta)) for v in V]
        H = sum(w*tan(x) for w, x in zip(W, X))

        error = 50*sqrt(2) - H
        theta += error*0.001

    T = sum(w/cos(x)/v for w, x, v in zip(W, X, V))
    return '{:2.10f}'.format(T)

if __name__ == '__main__':
    print(run())
















