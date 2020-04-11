# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 74 - Digit factorial chains

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import math


def run():
    count = 0
    everused = set()
    for i in range(1, 1000000):
        num = i
        if num in everused:
            continue
        seq = []

        while num not in seq:
            seq.append(num)
            everused.add(num)
            num = sum(math.factorial(int(x)) for x in str(num))
            if len(seq) > 60:
                break
        if len(seq) == 60:
            count += 1

    return count


if __name__ == "__main__":
    print(run())
