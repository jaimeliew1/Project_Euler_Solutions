import numpy as np
import matplotlib.pyplot as plt
import numpy as np

testgrid = np.array(   [[131,673,234,103,18],
                        [201,96,342,965,150],
                        [630,803,746,422,111],
                        [537,699,497,121,956],
                        [805,732,524,37,331]])

def dijkstra(grid, start, end, dxdy):
    '''
    Calculates least sum path over a weighted grid between a start point and
    all possible nodes. The allowable movement directions are given in dxdy.

    '''
    N = len(grid)

    pathsum = np.inf*np.ones(grid.shape)
    visited = np.zeros(grid.shape, dtype=bool)
    px, py = np.zeros(grid.shape, dtype=int), np.zeros(grid.shape, dtype=int) #pointers
    frontier = [start]
    x, y = start
    pathsum[y, x] = grid[y, x]
    # just keep going until all destinations are visited
    while not visited[end[0], end[1]]:
        for dx, dy in dxdy:
            xnew, ynew = x+dx, y+dy
            # ignore if on edge
            if any(coord < 0 for coord in [xnew, ynew]):
                continue
            if any(coord >= N for coord in [xnew, ynew]):
                continue
            # ignore if visited
            if visited[ynew, xnew]:
                continue
            # update pathsum if a better path is found
            if (pathsum[y, x] + grid[ynew, xnew]) < pathsum[ynew, xnew]:

                pathsum[ynew, xnew] = pathsum[y, x] + grid[ynew, xnew]
                px[ynew, xnew], py[ynew, xnew] = x, y
                if [xnew, ynew] not in frontier:
                    frontier.append([xnew, ynew])

        visited[y, x] = True
        frontier.remove([x, y])
        # Determine the next node to visit
        nextfrontier, nextx, nexty = np.inf, -1, -1
        for x_, y_ in frontier:
            if pathsum[y_, x_] < nextfrontier:
                nextfrontier = pathsum[y_, x_]
                nextx, nexty = x_, y_
        x, y = nextx, nexty

    path = [end]
    x, y = end
    while (x, y) != tuple(start):
        path.append([px[y, x], py[y, x]])
        x, y = path[-1]
    path.append(start)
    return pathsum[end[0], end[1]], path




cache = {}
dxdy = [[1, 0], [0, 1]]
def shortestPath(grid, xy = [0,0], prev=[]):
    ''' recursively finds the path through a grid with the lowest sum.
    Note. this method is faster than Dijkstra
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
     # use memoization
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


def run(test=False, plot=True, oldmethod=False):
    data = []
    with open('Data/p081_matrix.txt') as f:
        for line in f:
            data.append([int(x) for x in line.split(',')])
    grid = np.array(data)
    if test:
        grid = testgrid
    N = len(grid)

    if oldmethod:
        pathsum, path = shortestPath(grid, [0, 0])
    else:
        dxdy = [(1, 0),(0, 1)]
        pathsum, path = dijkstra(grid, [0,0], [N-1, N-1], dxdy)
    if plot:
        plotPath(grid, path)
    return int(pathsum)


if __name__ == '__main__':
    print(run())





