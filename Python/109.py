# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 109 - Darts

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import numpy as np


def run():
    target = 100
    poss_d = np.concatenate([2 * np.arange(1, 21), [50]])
    poss = np.concatenate(
        [np.arange(1, 21), 2 * np.arange(1, 21), 3 * np.arange(1, 21), [25, 50]]
    )

    count = 0
    # single dart
    for d in poss_d:
        if d < target:
            count += 1
    # double darts
    for d1 in poss_d:
        for d2 in poss:
            if d1 + d2 < target:
                count += 1
    # triple darts
    for d1 in poss_d:
        for i, d2 in enumerate(poss):
            for d3 in poss[i:]:
                if d1 + d2 + d3 < target:
                    count += 1
    return count


if __name__ == "__main__":
    print(run())
