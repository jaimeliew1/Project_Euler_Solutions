# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem X

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

from collections import Counter
import math

def run():
    count = Counter()
    for a in range(1,1000):
        b = 1
        c = math.sqrt(a*a + b*b)
        while a + b + c <=1000:
            if c.is_integer():
                count[int(a + b + c)] += 1
            b += 1
            c = math.sqrt(a*a + b*b)

    return count.most_common(1)[0][0]



if __name__ == "__main__":
    print(run())

