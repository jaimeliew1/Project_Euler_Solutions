from EulerFunctions import timeit, multiplicative_partitions
import numpy as np


@timeit
def run():
    Kmax = 12000
    K = {k:1e10 for k in range(2, Kmax+1)}
    for n in range(2, Kmax + 1000): # minimal n is less than 13000
        for P in multiplicative_partitions(n):
            k = n - sum(P) + len(P)
            if 2 <= k <= Kmax:
                K[k] = min(K[k], n)
    return sum(set(K.values()))


if __name__ == '__main__':

    print(run())
