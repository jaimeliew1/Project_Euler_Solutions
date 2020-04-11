# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 71 - Ordered Fractions

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import math

def run():
    n = 1000000
    target = 3.0 / 7
    answerNum = 0
    answerDen = 1
    for den in range(1, n):  # for each possible denominator
        if den % 7 == 0:  # which isn't divisible by 7
            continue
        num = math.floor(target * den)  # numerator just below target
        if num / den > answerNum / answerDen:  # find fraction closest to target
            answerNum = num
            answerDen = den

    return answerNum


if __name__ == "__main__":
    print(run())
