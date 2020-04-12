# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 102 - Triangle containment

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions
"""
import time
import matplotlib.pyplot as plt


def pointAboveLine(p, a, b):
    # checks if point p is above the line
    try:
        slope = float(b[1] - a[1]) / (b[0] - a[0])
    except ZeroDivisionError:
        slope = 9e10
    YInt = a[1] - slope * a[0]

    if p[0] * slope + YInt < p[1]:
        return True
    else:
        return False


def surroundsOrigin(t):
    zer = (0, 0)
    if pointAboveLine(t[0], t[1], t[2]) == pointAboveLine(zer, t[1], t[2]):
        if pointAboveLine(t[1], t[0], t[2]) == pointAboveLine(zer, t[0], t[2]):
            if pointAboveLine(t[2], t[1], t[0]) == pointAboveLine(zer, t[1], t[0]):
                return True
    return False


def run():
    triangles = []
    with open("Data/p102_triangles.txt") as f:
        for line in f:
            triangles.append([int(x) for x in line.split(",")])
    triangles = [((x[0], x[1]), (x[2], x[3]), (x[4], x[5])) for x in triangles]

    count = 0
    goodTriangles = []
    for tri in triangles:
        if surroundsOrigin(tri):
            # plt.clf()
            # plt.plot(*zip(*tri))
            count += 1
            goodTriangles.append(tri)

    return count


if __name__ == "__main__":
    print(run())
