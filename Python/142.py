# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 142 - Perfect Square Collection

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
from itertools import combinations
import numpy as np


def run():
    N = 1000000
    candids = {}
    # generate all pairs of squares which differ by an even number. record the
    # midpoint and the distance from the midpoint. These are the candidates for
    # squares which satisfy both (x+y) and (x-y).
    for i in range(1, int(np.sqrt(N))):
        for j in range(i + 1, int(np.sqrt(N))):
            diff_squares = j ** 2 - i ** 2
            if diff_squares % 2 == 0:
                midpoint = (j ** 2 + i ** 2) // 2
                d = diff_squares // 2
                if midpoint not in candids.keys():
                    candids[midpoint] = [d]
                else:
                    candids[midpoint].append(d)

    best_xyz = 1e20
    for x, v in candids.items():
        if len(v) == 1:
            continue
        for y, z in combinations(v, 2):
            if z > y:
                z, y = y, z
            if y in candids.keys():
                if z in candids[y]:
                    best_xyz = min(best_xyz, x + y + z)

    return best_xyz


if __name__ == "__main__":
    print(run())
