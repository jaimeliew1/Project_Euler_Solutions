# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 139

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from math import gcd
from tqdm import trange

def run():
    N = 10000
    perim_max = int(100e6)
    ans = 0

    # Generate primitive pythagorean triples
    for n in trange(1, N):
        for m in range(n + 1, N):
            # m and n must be coprime and one of them should be even to be primitive.
            if not (gcd(m, n) == 1 and any([m % 2 == 0, n % 2 == 0])):
                continue

            # The perimeter of the triangle should be less than 100 million
            if 2 * m * (m + n) >= perim_max:
                continue
            # length of the inner square side
            s = n ** 2 + 2 * m * n - m ** 2
            # length of the long side
            c = m ** 2 + n ** 2

            # if the whole square is divisible by the small square, then this
            # pythagorean triple meets the conditions.
            if c ** 2 % s == 0:
                # also all other multiples of the triple meet the condition
                ans += int(perim_max / (2 * m * (m + n)))
                
                # print(m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2)
                # print(ans)
    return ans


if __name__ == "__main__":
    print(run())
