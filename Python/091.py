from EulerFunctions import timeit
def dot(l1, l2):
    return l1[0]*l2[0] + l1[1]*l2[1]

def pointgen(n):
    for x in range(0, n+1):
        for y in range(0, n+1):
            if x==0 and y==0:
                continue
            yield (x, y)

@timeit
def run():
    X = 50
    N=0

    for [x1, y1] in pointgen(X):
        for [x2, y2] in pointgen(X):
            if x1==x2 and y1==y2:
                continue
            l1 = [x1, y2]
            l2 = [x2, y2]
            l3 = [x2-x1, y2-y1]

            if dot(l1, l2) == 0 or dot(l2, l3) == 0:
                N+=1

    return N


if __name__ == '__main__':
    print(run())
