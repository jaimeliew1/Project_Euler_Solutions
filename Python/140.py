# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 140

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

This problem is very similar to 137 with a different generating function.
A(a/b) =  (b*a + 3*a**2)/(b**2 - b*a - a**2) for integer a, b

It is possible to solve this problem by solving the pell equation x^2 - 5*y^2 = 44,
but I could not work it out.
Where this pell equation comes from:

A(x) = (x + 3*x^2)/(1 - x - x^2)
solve for x using quadratic equation, gives a determinant of:
det = (1+A)^2 + 4*A*(3+A) = n^2
This must be a perfect square (n^2) for A to be integer.
Rearranging gives (4A - 7)^2 - 5m^2 = 44
let x, y = 4A-7, m. Solve the pell equation. HOW?

My current process,
- find fundamental solution to x^2 - 5*y^2 = 1,
- find fundamental solution to x^2 - 5*y^2 = 44 (but there are multiple and I
do not know how to find them all),
- Use Brahmagupta's identity to work out generating sequence,
- generate all the solutions.

One day, please come back and solve this (and all other pell related questions)
properly. Cheers. Past Jaime. 2019-01-26

"""
from math import sqrt

phi = -(1-sqrt(5))/2



def run():
    golden_nugs = []
    b = 2
    while len(golden_nugs) < 30:
        a = int(b*phi)
        if b == 5: a = 2
        A = (b*a + 3*a**2)/(b**2 - b*a - a**2)
        if A > 0 and A.is_integer() and A not in golden_nugs:
            golden_nugs.append(int(A))
        b += 1

    return sum(golden_nugs)





if __name__ == "__main__":
    print(run())
