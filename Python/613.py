# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 613 - Pythagorean Ant

A right triangle with side lengths 3, 4, 5 has an ant fall at a random location
on it, and walkes in a random straight direction. what is the probability the
ant walks off the long side?

The two shorter sides (labeled A and B) have length A and B.

Lemma1 : all points on a right triangle can be represented as the intersection
of two lines, where the first line passes through the vertex of line B, and a
point, a, on side A. The second line passes through the vertex of line B, and a
point, b, on side b. This is an alternative (and better) representation than
using x, and y coordinates.

lemma 2: For an ant on a point described by a and b, the probability of walking
off the hypotenuse is beta/(2*pi), where beta is the angle subtended between the
two lines described in previous lemma, and the hypotenuse.

lemma 3: beta = pi/2 + arctan(b/A) + arctan(a/B)     (proven geometrically)

lemma 4: the probability of walking off the hypotenuse for all positions is the
double integral, 1/(2*pi*A*B) /int_0^A/int_0^B beta da db

The solution to the double integral in lemma 4 was found analytically, given
that:

/int arctan(x) = x*arctan(x) * log(sqrt(x^2 + 1))

and

arctan(x) + arctan(1/x) = pi/2  if x>0


Author: Jaime Liew https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from math import log, atan, pi
def run():

    A, B, C = 3, 4, 5
    ans =  1/2 - 1/(2*pi)*A/B*log(C/A) - 1/(2*pi)*B/A*log(C/B)

    return f'{ans:1.10f}'


if __name__ == "__main__":
    print(run())
