import time
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
def diagonalise(d):
    n = len(d)
    a = []
    for diag in range(n):
        a.append([])
        for point in range(diag+1):
            a[-1].append(d[point][diag-point])

    for diag in range(n-1):
        a.append([])
        for point in range(n-1 - diag):
            a[-1].append(d[diag + 1 + point][n -  point - 1])
    return a

def shortestPath_old(data):
    N = len(data)
    data = diagonalise(data)
    
    sumPath = []
    for line in data:
        sumPath.append([0]*len(line))

    for layer, line in enumerate(data):
        
        if layer == 0:
            sumPath[0][0] = data[0][0]
            continue
        if layer < N:
            for j in range(len(line)):
                if j == 0:
                    sumPath[layer][0] = sumPath[layer-1][0] + data[layer][0]
                    continue
                if j == len(line)-1:
                    sumPath[layer][-1] = sumPath[layer-1][-1] + data[layer][-1]
                    continue
                sumPath[layer][j] = data[layer][j] + min(
                            sumPath[layer-1][j], sumPath[layer-1][j-1])

        if layer == len(data)-1:
            sumPath[layer][0] = data[layer][0] + min(
                            sumPath[layer-1][0], sumPath[layer-1][0 + 1])
        elif layer >= N:
            for j in range(len(line)):
                if j == len(line)-1:
                    sumPath[layer][j] = sumPath[layer-1][j] + data[layer][j]
                    continue
                sumPath[layer][j] = data[layer][j] + min(
                            sumPath[layer-1][j], sumPath[layer-1][j+1])

    return sumPath[-1][0]


cache = {}
dxdy = [[1, 0], [0, 1]]
def shortestPath(grid, xy = [0,0], prev=[]):
    ''' recursively finds the path through a grid with the lowest sum
    Parameters
    ^^^^^^^^^^
    grid:   a numpy array containing the grid of values in question
    x, y:   A list of x and y coordinates of the currently walked path. ie.
                the points to exclude in the path
            The last element (exclude[-1]) contains the latest coordinates.    
    Return
    ^^^^^^
    pathsum, path
    '''
    N = len(grid)
    
    if xy[0]*N+xy[1] in cache.keys():
        return cache[xy[0]*N+xy[1]]
    
    lowestsum, bestpath = 1e10, None

    x, y = xy
    # Condition to end recursion
    if x==N-1 and y==N-1:
        return grid[y, x], [[x, y]]

    # loop through all possible next steps    
    for dx, dy in dxdy:
        xnew, ynew = x + dx, y + dy
        # Ignore positions already in path
        if [x+dx, y+dy] in prev:
            continue
        #ignore positions outside grid
        if any(coord < 0 for coord in [xnew, ynew]):
            continue
        if any(coord >= N for coord in [xnew, ynew]):
            continue
        
        thesum, thepath = shortestPath(grid, [xnew, ynew], [xy])
        if thesum < lowestsum:
            lowestsum, bestpath = thesum, thepath
    
    cache[xy[0]*N+xy[1]] = (lowestsum + grid[y, x],bestpath + [[x, y]])
    return lowestsum + grid[y, x], bestpath + [[x, y]]
        
    



def plotPath(grid, path):
    path = np.array(path)
    x, y = path[:, 0], path[:, 1]
    plt.imshow(grid)
    plt.plot(x, y, 'r', lw=0.5)
    plt.show()
    print()
    
    
if __name__ == '__main__':    
    data = []
    with open('Data/p081_matrix.txt') as f:
        for line in f:
            data.append([int(x) for x in line.split(',')])
    data = np.array(data)    
#    data = np.array(   [[131,673,234,103,18],
#                        [201,96,342,965,150],
#                        [630,803,746,422,111],
#                        [537,699,497,121,956],
#                        [805,732,524,37,331]])
    
    start = time.time()
    thesum, thepath = shortestPath(data, [0, 0])
    print(thesum)
    print("Time elapsed: ", round(time.time() - start, 7), 's')
        
        

    plotPath(data, thepath)
    
    
    start = time.time()
    ans = shortestPath_old(list(data))
    print(ans)
    print("Time elapsed: ", round(time.time() - start, 7), 's')


