# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:40:16 2018

@author: jyli
"""

import numpy as np
import matplotlib.pyplot as plt

testgrid = np.array(   [[131,673,234,103,18],
                        [201,96,342,965,150],
                        [630,803,746,422,111],
                        [537,699,497,121,956],
                        [805,732,524,37,331]])


cache = {}
allways = {'e':(1, 0), 's':(0, 1), 'n':(0, -1)}
def shortestPath(grid, x=0, y=0, path=[]):
    ''' recursively finds the path through a grid with the lowest sum
    Parameters
    ^^^^^^^^^^

    Return
    ^^^^^^
    pathsum, path
    '''
    N = len(grid)

    # Condition to end recursion
    if x == N-1: #and y==N-1:
        return grid[y, x], [[x, y]]

    # loop through all possible next steps to get a valid-direction string.
    valid_dirs = ''
    for way, dxdy in allways.items():
        dx, dy = dxdy
        xnew, ynew = x + dx, y + dy
        #ignore positions outside grid
        if any(coord < 0 for coord in [xnew, ynew]):
            continue
        elif any(coord >= N for coord in [xnew, ynew]):
            continue
        elif (xnew, ynew) in path:
            continue
        else:
            valid_dirs += way

    # check cache.
    if (x, y, valid_dirs) in cache.keys():
        return cache[(x, y, valid_dirs)]

    # if not in cache, calculate pathsum using recursion.
    minsum, bestpath = 1e10, []
    for way in valid_dirs:
        dx, dy = allways[way]
        xnew, ynew = x + dx, y + dy

        thesum, thepath = shortestPath(grid, xnew, ynew, path + [(xnew, ynew)])
        if thesum < minsum:
            minsum, bestpath = thesum, thepath

    cache[(x, y, valid_dirs)] = (minsum + grid[y, x],bestpath + [[x, y]])
    return minsum + grid[y, x], bestpath + [[x, y]]



def plotPath(grid, path):
    path = np.array(path)
    x, y = path[:, 0], path[:, 1]
    plt.imshow(grid)
    plt.plot(x, y, 'r', lw=0.5)
    plt.show()
    print()


def run(test=False, plot=True):
    data = []
    with open('Data/p082_matrix.txt') as f:
        for line in f:
            data.append([int(x) for x in line.split(',')])
    grid = np.array(data)
    if test:
        grid = testgrid

    minsum, bestpath = 1e10, None
    for i in range(len(data)):
        thesum, thepath = shortestPath(grid, 0, i)
        if thesum < minsum:
            minsum, bestpath = thesum, thepath
    if plot:
        plotPath(grid, bestpath)
    return int(minsum)


if __name__ == '__main__':
    print(run())





