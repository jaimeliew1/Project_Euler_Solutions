# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:40:16 2018

@author: jyli
"""

import time
import numpy as np
from numpy import nan
import matplotlib.pyplot as plt

# use dijkstras algorithm.
# Each square/node has a pathsum value, a pointer to a neighboring node, and a 
# visited/unvisited flag


cache = {}


allways = {    'e':(1, 0),
            's':(0, 1),
            'n':(0, -1),
            #'w':(-1, 0)
            }
def shortestPath2(grid, x=0, y=0, path=[[0, 0]]):
    ''' recursively finds the path through a grid with the lowest sum
    Parameters
    ^^^^^^^^^^
   
    Return
    ^^^^^^
    pathsum, path
    '''
    N = len(grid)
    
    
    # Condition to end recursion
    if x == N-1 and y==N-1:

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
        
        thesum, thepath = shortestPath2(grid, xnew, ynew, path + [(xnew, ynew)]) # ???
        if thesum < minsum:
            minsum, bestpath = thesum, thepath
    
    plotPath2(grid, bestpath + [[x, y]], path)
    cache[(x, y, valid_dirs)] = (minsum + grid[y, x],bestpath + [[x, y]])
    return minsum + grid[y, x], bestpath + [[x, y]]



def plotPath(grid, path):
    path = np.array(path)
    x, y = path[:, 0], path[:, 1]
    plt.imshow(grid)
    plt.plot(x, y, 'r', lw=0.5)
    plt.show()
    print()

    
def plotPath2(grid, path1, path2):
    path = np.array(path1)
    x, y = path[:, 0], path[:, 1]
    plt.imshow(grid)
    plt.plot(x, y, 'r', lw=0.5)
    
    path = np.array(path2)
    x, y = path[:, 0], path[:, 1]
    plt.imshow(grid)
    plt.plot(x, y, 'b', lw=0.5)
    plt.show()
    print()  
    
    
  
if __name__ == '__main__':    
    data = []
    with open('Data/p082_matrix.txt') as f:
        for line in f:
            data.append([int(x) for x in line.split(',')])
    grid = np.array(data)    
#    grid = np.array(   [[131,673,234,103,18],
#                        [201,96,342,965,150],
#                        [630,803,746,422,111],
#                        [537,699,497,121,956],
#                        [805,732,524,37,331]])
    N = len(grid)

    dxdy = [(1, 0), 
        (0, 1),
        (0, -1),
        (-1, 0)]
    pathsum = 1e10*np.ones(grid.shape)    
    visited = np.zeros(grid.shape, dtype=bool)
    px, py = nan*np.zeros(grid.shape), nan*np.zeros(grid.shape) #pointers
    frontier = [[0,0]]
    
    x, y = 0, 0
    pathsum[0, 0] = grid[0, 0]
    # just keep going until the destination is visited
    while not visited[N-1, N-1]:
        # for each neighbor of the current node
        for dx, dy in dxdy:
            xnew, ynew = x+dx, y+dy

            # ignore if on edge
            if any(coord < 0 for coord in [xnew, ynew]):
                continue
            if any(coord >= N for coord in [xnew, ynew]):
                continue
            # ignore if visited 
            if visited[xnew, ynew]:
                continue
            
            if pathsum[x, y] + grid[xnew, ynew] < pathsum[xnew, ynew]:
                pathsum[xnew, ynew] = pathsum[x, y] + grid[xnew, ynew]
                px[xnew, ynew], py[xnew, ynew] = x, y
                if [xnew, ynew] not in frontier:
                    frontier.append([xnew, ynew])
            
        visited[x, y] = True
        frontier.remove([x, y])
        
        if len(frontier) > 0:
            x, y = frontier[0]
            
    # calculate path
        
    
#    thesum, thepath = shortestPath2(data, 0, 0)
#    print(thesum)
#    plotPath(data, thepath)
    
    


