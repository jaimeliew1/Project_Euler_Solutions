# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 99 - Largest exponential

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

import math


def run():

    fileData = []
    with open("Data/p099_base_exp.txt") as f:
        for line in f:
            fileData.append(line)

    data = []
    for line in fileData:
        # data.append(map(lambda x: int(x),line.split(',')))
        data.append([int(x) for x in line.split(",")])

    ans = [0, 0, 0, 0]
    for i, pair in enumerate(data):
        logPair = math.log(pair[0]) * pair[1]
        if logPair > ans[0]:
            ans = [logPair, pair[0], pair[1], i]
            # print ans

    return ans[3] + 1


if __name__ == "__main__":
    print(run())
