import time
import itertools

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

def shortestPath(grid, x, y, dir='dr'):
    pass
if __name__ == '__main__':
    start = time.time()
    fileData = []
    data = []
    with open('Data/p081_matrix.txt') as f:
        for line in f:
            fileData.append(line)
            data.append([int(x) for x in line.split(',')])

    #data = [[131,673,234,103,18],
    #        [201,96,342,965,150],
    #        [630,803,746,422,111],
    #        [537,699,497,121,956],
    #        [805,732,524,37,331]]

    data = diagonalise(data)

    sumPath = []
    for line in data:
        sumPath.append([0]*len(line))

    for layer, line in enumerate(data):
        #print('Layer {}'.format(layer))
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

    print(sumPath[-1][0])
    print("Time elapsed: ", round(time.time() - start, 7), 's')


