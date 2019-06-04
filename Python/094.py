# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 94

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
Created on Sat Nov  3 14:01:58 2018


Find almost-equilateral triangles which have integer areas. An
almost-equilateral triangle has two sides of length c and the last side almost c
(c+1 or c-1).

consider the length h which bisects the triangle through the almost-c side (with
length b) and the opposite vertex. The area, A, of the almost-equilateral
triangle is h*b/2. for A to be an integer, h must be an integer.

Therefore triangle (c, b/2, h) must be a pythagorean triple. So this code
generates pythagorean triples correspond to certain conditions to make
almost-equilateral triangles.
_________________________________________
All pythagorean triple can be generated from two integers, m, n where m > n, and c =
m**2 + n**2, and the other two sides are 2*m*n and m**2-n**2.

___________________________________

Consider the almost-equilateral triangle
where b = c+1 (1). The b/2 side corresponds to the m**2 - n**2 side.

Using (1) and the expressions using m and n, it can be shown that: 2*m**2 -
2*n**2 = m**2 + n**2 + 1 ==> m**2 - 3n**2 = 1 which is a form of Pell's equation
with a fundamental solution of m, n = 2, 1. The generator function is m, n = 2*m
+ 3*n, m + 2*n Therefore all almost equilateral triangles with b=c+1 can be
generated using this generator. Note that the perimeter (and area) of the almost
equilateral triangle is 3*(m**2 + n**2) + 1 (and (m**2 - n**2)*2*m*n)

_____________________________________

Now consider the almost-equilateral
triangle where b = c-1. The b/2 side corresponds to the 2*m*n side (as apposed
to the previous case. This was observed, but I was unable to prove this.)

In a similar method to the previous case, it can be shown that: 4mn = m**2 +
n**2 -1 ==> (m - 2n)**2 - 3n**2 = 1 which is the same Pell's equation as the
previous case with a substitution. So the solution of the previous Pell's
equation can be used to generate the almost-equilateral triangles where b = c-1.

For example, if x, y are solutions to the above pells equation, then: c = (m -
2*n)**2 + n**2 and the perimeter is 3*c - 1

Note: the first solution of pell's equation (2, 1) does not apply for the almost
equilateral triangles where b = c - 1
"""

def run():
    peri_sum = 0

    # Generate almost equilateral triangles where b = c+1
    m, n = 2, 1
    while True:
        c = m**2 + n**2
        if 3*c + 1 < 1e9:
            peri_sum += 3*c + 1
            m, n = 2*m + 3*n, m + 2*n
        else:
            break

    # Generate almost equilateral triangles where b = c-1
    m, n = 7, 4 # second iteration of pells equation
    while True:
        c = (m - 2*n)**2 + n**2
        if 3*c + 1 < 1e9:
            peri_sum += 3*c - 1
            m, n = 2*m + 3*n, m + 2*n
        else:
            break

    return peri_sum

if __name__ == '__main__':
    print(run())
