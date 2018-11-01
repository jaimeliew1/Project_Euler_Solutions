# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 67
Date: 16 Apr 2015

This code is the same as for problem 18, with a slight difference in the way
file is read.

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""

def run():
    # Read data file
    data = []
    with open('Data/p067_triangle.txt') as f:
        for line in f:
            data.append([int(x) for x in line.split(' ')])

    #starts from the bottom of the pyramid and works upwards to create
    #a cumulitive sum pyramid, where the value at each point is the maximum
    #value of possible sums below that point
    for n in range(len(data) - 2, -1, -1):
        for i, num in enumerate(data[n]):
            data[n][i] += max(data[n+1][i], data[n+1][i+1])

    return data[0][0]

if __name__ == '__main__':
    print(run())


