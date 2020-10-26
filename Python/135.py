# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 135 - Same differences

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import numpy as np
from tqdm import trange
from EulerFunctions import factors


def run():
    N = 1000000
    factor_list = {i: [(1, i)] for i in range(1, N)}
    for i in trange(2, int(np.sqrt(N))):
        j = i * i
        while j < N:
            factor_list[j].append((i, j // i))
            j += i

    count = {i: 0 for i in range(1, N)}
    for k, v in factor_list.items():
        for a, b in v:
            if (a + b) % 4 == 0:
                if a + b < 4 * a:
                    count[k] += 1
                if a + b < 4 * b and a != b:
                    count[k] += 1
    return sum(v == 10 for v in count.values())


if __name__ == "__main__":
    print(run())
