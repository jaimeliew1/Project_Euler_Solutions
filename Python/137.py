# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 137

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

The infinite polynomial can be expressed as the Fibonacci generating function,
F(x) = x/(x^2 - x - 1)

For x to be rational, x = p/q where p, q are integers.

Therefore F(x) = pq/(q^2 - pq - p^2)

For F(x) to be an integer, the denominator must be 1.
 But I didnt use this fact, or the pell equation solution which is possible.
 I couldnt figure it out.

 Instead, I found that p and q are adjacent fibonacci numbers, but was unable
 to prove this.
"""


def run():
    golden_nugs = []
    i, a, b = 1, 0, 1
    while len(golden_nugs) < 15:
        A = b*a/(b**2 - b*a - a**2)
        if A > 0 and A.is_integer() and A not in golden_nugs:
            golden_nugs.append(int(A))
        i, a, b = i+1, b, a+b

    return golden_nugs[-1]


if __name__ == "__main__":
    print(run())
